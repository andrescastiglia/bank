"""Regresión documental con fixtures sintéticas en directorio temporal; sin consultas externas."""

from copy import deepcopy
from pathlib import Path
import json
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[3]
TEMPORARY = tempfile.TemporaryDirectory(prefix='bank-regwatch-check-')
OUT = Path(TEMPORARY.name)
TOOL = ROOT / 'docs/regulatory-watch/tools/check_watch.py'
REG = json.loads((ROOT / 'docs/regulatory-watch/sources.json').read_text())
SEED = json.loads((ROOT / 'docs/regulatory-watch/state.initial.json').read_text())
REQUIRED = [s['source_id'] for s in REG['sources'] if s['required_for_detection']]
RESULTS = []


def save(name, data):
    p = OUT / (name + '.json')
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
    return p


def window(start, end):
    return {'from_inclusive': start, 'to_exclusive': end}


def full_run(name='RUN-20261016', start='2026-10-15T00:00:00-03:00', end='2026-10-16T00:00:00-03:00', day='2026-10-16'):
    w = window(start, end)
    return {
        'schema_version': 1, 'run_id': name,
        'started_at': day + 'T08:00:00-03:00', 'finished_at': day + 'T08:05:00-03:00',
        'requested_window': w, 'inventory_version': REG['inventory_version'],
        'status': 'COMPLETE_NO_CHANGES', 'change_ids': [], 'errors': [],
        'source_results': [{
            'source_id': sid, 'status': 'COMPLETE', 'requested_window': deepcopy(w), 'covered_window': deepcopy(w),
            'coverage_basis': {'all_pages_processed': True, 'all_annexes_processed': True, 'pages_expected': 1, 'pages_processed': 1, 'annexes_expected': 0, 'annexes_processed': 0, 'outstanding_cursor': None},
            'evidence_refs': [{'url': 'https://example.org/synthetic-fixture', 'sha256': '0' * 64, 'fetched_at': day + 'T08:02:00-03:00'}],
            'gaps': [], 'not_applicable_basis': None,
        } for sid in REQUIRED],
    }


def apply(previous, run):
    state = deepcopy(previous)
    state['last_run_id'] = run['run_id']
    state['run_index'].append({'run_id': run['run_id'], 'status': run['status']})
    for result in run['source_results']:
        cp = next(x for x in state['source_checkpoints'] if x['source_id'] == result['source_id'])
        cp['status'] = result['status']
        cp['last_attempt_at'] = run['finished_at']
        cp['open_gaps'] = deepcopy(result['gaps'])
        if result['status'] == 'COMPLETE':
            cp['covered_through'] = result['requested_window']['to_exclusive']
        if result['status'] == 'NOT_APPLICABLE_WITH_BASIS':
            cp['not_applicable_basis'] = result['not_applicable_basis']
    return state


def unavailable(result):
    result['status'] = 'UNAVAILABLE'
    result['covered_window'] = None
    result['coverage_basis'] = {'all_pages_processed': False, 'all_annexes_processed': False, 'pages_expected': None, 'pages_processed': 0, 'annexes_expected': 0, 'annexes_processed': 0, 'outstanding_cursor': None}
    result['evidence_refs'] = []
    result['gaps'] = [{'cause': 'HTTP403', 'retry_required': True}]


def check(name, expected, run=None, state=None, previous=None):
    args = [sys.executable, str(TOOL)]
    if state is not None:
        args += ['--state', str(save(name + '.state', state))]
    if run is not None:
        args += ['--run', str(save(name + '.run', run))]
    if previous is not None:
        args += ['--previous-state', str(save(name + '.previous', previous))]
    result = subprocess.run(args, cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == expected, (name, result.returncode, expected, result.stdout, result.stderr)
    assert 'Traceback' not in result.stderr, (name, result.stderr)
    RESULTS.append({'case': name, 'exit_code': result.returncode, 'expected': expected, 'output': (result.stdout or result.stderr).splitlines()[:3]})


check('default_seed', 0)
r = full_run()
check('complete_zero_changes', 0, r)
state1 = apply(SEED, r)
check('first_run_checkpoint', 0, r, state1, SEED)
r2 = deepcopy(r)
r2['status'] = 'COMPLETE_WITH_CHANGES'
r2['change_ids'] = ['CHANGE-20261016-BCRA-001']
check('complete_with_change', 0, r2)
for name, field, value in [
    ('page2_missing', 'pages_expected', 2),
    ('annex_missing', 'annexes_expected', 1),
    ('cursor_pending', 'outstanding_cursor', 'page-2'),
    ('false_all_pages', 'all_pages_processed', False),
    ('boolean_count', 'pages_processed', True),
]:
    bad = deepcopy(r)
    bad['source_results'][0]['coverage_basis'][field] = value
    check(name, 1, bad)
bad = deepcopy(r)
bad['source_results'][0]['evidence_refs'] = []
check('complete_without_evidence', 1, bad)
bad = deepcopy(r)
bad['source_results'].pop()
check('required_source_omitted', 1, bad)
bad = deepcopy(r)
bad['source_results'].append(deepcopy(bad['source_results'][0]))
check('duplicated_source_id', 1, bad)
bad = deepcopy(r)
bad['source_results'][0]['status'] = 'NOT_APPLICABLE_WITH_BASIS'
bad['source_results'][0]['not_applicable_basis'] = 'No acceso no justifica excluir una fuente requerida.'
bad['source_results'][0]['covered_window'] = None
check('required_excluded', 1, bad)
optional = deepcopy(r)
result = deepcopy(r['source_results'][0])
result['source_id'] = 'WATCH-STANDARDS'
unavailable(result)
result['status'] = 'NOT_APPLICABLE_WITH_BASIS'
result['gaps'] = []
result['not_applicable_basis'] = 'Fixture sintética sin estándares contractuales activados.'
optional['source_results'].append(result)
check('optional_na_with_basis', 0, optional)
optional['source_results'][-1]['not_applicable_basis'] = None
check('optional_na_without_basis', 1, optional)
partial = deepcopy(r)
unavailable(partial['source_results'][0])
partial['status'] = 'PARTIAL'
check('http403_partial', 0, partial, apply(SEED, partial), SEED)
partial['status'] = 'COMPLETE_NO_CHANGES'
check('http403_not_no_changes', 1, partial)
failed = deepcopy(r)
for result in failed['source_results']:
    unavailable(result)
failed['status'] = 'FAILED'
check('all_unavailable_failed', 0, failed, apply(SEED, failed), SEED)
failed['status'] = 'PARTIAL'
check('all_unavailable_not_partial', 1, failed)
next_run = full_run('RUN-20261017', '2026-10-16T00:00:00-03:00', '2026-10-17T00:00:00-03:00', '2026-10-17')
unavailable(next_run['source_results'][0])
next_run['status'] = 'PARTIAL'
state2 = apply(state1, next_run)
check('failed_source_keeps_checkpoint', 0, next_run, state2, state1)
bad_state = deepcopy(state2)
bad_state['source_checkpoints'][0]['covered_through'] = '2026-10-17T00:00:00-03:00'
check('failed_source_checkpoint_advance', 1, next_run, bad_state, state1)
bad_state = deepcopy(state2)
bad_state['source_checkpoints'][0]['status'] = 'COMPLETE'
bad_state['source_checkpoints'][0]['open_gaps'] = []
check('failed_source_status_hidden', 1, next_run, bad_state, state1)
backfill = full_run('RUN-20261019', '2026-10-16T00:00:00-03:00', '2026-10-19T00:00:00-03:00', '2026-10-19')
check('missed_runs_backfill', 0, backfill, apply(state1, backfill), state1)
gap = full_run('RUN-20261019-GAP', '2026-10-18T00:00:00-03:00', '2026-10-19T00:00:00-03:00', '2026-10-19')
check('checkpoint_jumps_gap', 1, gap, apply(state1, gap), state1)
overlap = full_run('RUN-20261017-OVERLAP', '2026-10-15T00:00:00-03:00', '2026-10-17T00:00:00-03:00', '2026-10-17')
check('overlap_contiguous', 0, overlap, apply(state1, overlap), state1)
bad_state = apply(state1, overlap)
bad_state['source_checkpoints'][0]['covered_through'] = '2026-10-15T00:00:00-03:00'
check('checkpoint_regression', 1, overlap, bad_state, state1)
bad = deepcopy(r)
bad['finished_at'] = '2026-02-31T08:05:00-03:00'
check('invalid_calendar_date', 1, bad)
bad = deepcopy(r)
bad['finished_at'] = '2026-10-16T08:05:00'
check('timezone_missing', 1, bad)
bad = deepcopy(r)
bad['source_results'][0]['evidence_refs'][0]['url'] = 'http://example.org/synthetic-fixture'
check('http_evidence_url', 1, bad)
bad = deepcopy(r)
bad['status'] = []
check('status_wrong_type', 1, bad)
bad_state = deepcopy(SEED)
bad_state['source_checkpoints'][0]['status'] = []
check('state_status_wrong_type', 1, state=bad_state)
bad = deepcopy(r)
del bad['source_results'][0]['coverage_basis']['outstanding_cursor']
check('coverage_field_omitted', 1, bad)
bad = deepcopy(r)
bad['change_ids'] = ['CHANGE-1', 'CHANGE-1']
bad['status'] = 'COMPLETE_WITH_CHANGES'
check('change_id_duplicate', 1, bad)

# Per-source windows may differ; COMPLETE is local, global target can remain pending.
previous_mixed = deepcopy(state1)
previous_mixed['last_run_id'] = 'RUN-20261018'
previous_mixed['source_checkpoints'][0]['covered_through'] = '2026-10-18T00:00:00-03:00'
previous_mixed['source_checkpoints'][0]['last_attempt_at'] = '2026-10-18T08:05:00-03:00'
mixed = full_run('RUN-MIXED-20261019', '2026-10-16T00:00:00-03:00', '2026-10-19T00:00:00-03:00', '2026-10-19')
mixed['source_results'][0]['requested_window']['from_inclusive'] = '2026-10-18T00:00:00-03:00'
mixed['source_results'][0]['covered_window'] = deepcopy(mixed['source_results'][0]['requested_window'])
check('different_source_checkpoints_full_backfill', 0, mixed, apply(previous_mixed, mixed), previous_mixed)
chunked = deepcopy(mixed)
chunked['run_id'] = 'RUN-CHUNKED-20261019'
chunked['status'] = 'PARTIAL'
chunked['source_results'][1]['requested_window']['to_exclusive'] = '2026-10-17T00:00:00-03:00'
chunked['source_results'][1]['covered_window'] = deepcopy(chunked['source_results'][1]['requested_window'])
chunked_state = apply(previous_mixed, chunked)
check('source_complete_but_global_tail_pending', 0, chunked, chunked_state, previous_mixed)
assert chunked_state['source_checkpoints'][1]['status'] == 'COMPLETE'
assert chunked_state['source_checkpoints'][1]['covered_through'] == '2026-10-17T00:00:00-03:00'
assert chunked_state['source_checkpoints'][1]['open_gaps'] == []
premature = deepcopy(chunked)
premature['status'] = 'COMPLETE_NO_CHANGES'
check('global_complete_with_source_target_pending', 1, premature)
resume = full_run('RUN-RESUME-20261019', '2026-10-17T00:00:00-03:00', '2026-10-19T00:00:00-03:00', '2026-10-19')
for result in resume['source_results']:
    if result['source_id'] != REQUIRED[1]:
        result['requested_window']['from_inclusive'] = '2026-10-18T00:00:00-03:00'
        result['covered_window'] = deepcopy(result['requested_window'])
check('resume_remaining_source_tail', 0, resume, apply(chunked_state, resume), chunked_state)
source_gap = deepcopy(mixed)
source_gap['source_results'][1]['requested_window']['from_inclusive'] = '2026-10-18T00:00:00-03:00'
source_gap['source_results'][1]['covered_window'] = deepcopy(source_gap['source_results'][1]['requested_window'])
check('source_window_skips_its_checkpoint', 1, source_gap, apply(previous_mixed, source_gap), previous_mixed)
outside = deepcopy(mixed)
outside['source_results'][0]['requested_window']['from_inclusive'] = '2026-10-15T00:00:00-03:00'
check('source_window_outside_envelope', 1, outside)
covered_outside = deepcopy(mixed)
covered_outside['source_results'][0]['covered_window']['from_inclusive'] = '2026-10-16T00:00:00-03:00'
check('coverage_outside_source_window', 1, covered_outside)

(OUT / 'results.json').write_text(json.dumps(RESULTS, indent=2, ensure_ascii=False) + '\n')
print('PASS', len(RESULTS), 'documentary fixtures; no Internet, product execution, or repository mutations.')

TEMPORARY.cleanup()
