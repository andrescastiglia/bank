#!/usr/bin/env python3
"""Verifica la migración de endpoints y transición de la repetición BO; sin red."""
import hashlib
import importlib.util
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WATCH = ROOT / '.regulatory-watch'
RUN_ID = 'RUN-20261016T023356Z'
spec = importlib.util.spec_from_file_location('check_watch', ROOT / 'docs/regulatory-watch/tools/check_watch.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
v = module.Validator()
migration = v.read(WATCH / 'migrations/2026-10-16.1-to-2026-10-16.2.json')
previous_path = ROOT / migration['previous_state']
previous_registry_path = ROOT / migration['previous_registry']
for name, path in [('state.json', previous_path), ('sources.json', previous_registry_path)]:
    v.require(hashlib.sha256(path.read_bytes()).hexdigest() == migration['snapshot_sha256'][name], 'Snapshot previo alterado: ' + name)
previous = v.read(previous_path)
old_registry = v.read(previous_registry_path)
registry = v.read(WATCH / 'sources.json')
v.require(old_registry.get('inventory_version') == migration['from_inventory_version'] == '2026-10-16.1', 'Inventario previo inesperado')
v.require(registry.get('inventory_version') == migration['to_inventory_version'] == '2026-10-16.2', 'Inventario nuevo inesperado')
expected_registry = deepcopy(old_registry)
expected_registry['inventory_version'] = registry['inventory_version']
bo = next(source for source in expected_registry['sources'] if source['source_id'] == 'WATCH-BO')
bo['entrypoints'] = ['https://www.boletinoficial.gov.ar/seccion/primera', 'https://www.boletinoficial.gob.ar/seccion/primera']
v.require(registry == expected_registry, 'La migración debe cambiar sólo la versión y los dos endpoints oficiales BO')
v.require(v.read(ROOT / 'docs/regulatory-watch/sources.json') == registry, 'Registro documental y operativo distintos')
old_sources = v.registry(old_registry)
sources = v.registry(registry)
old_checkpoints = v.state(previous, old_registry, old_sources, 'previous-state')
state = v.read(WATCH / 'snapshots' / RUN_ID / 'state.json')
checkpoints = v.state(state, registry, sources, 'state')
run = v.read(WATCH / 'runs' / (RUN_ID + '.json'))
results = v.run(run, registry, sources)
v.transition(previous, state, run, registry, old_checkpoints, checkpoints, results)
v.require(results['WATCH-BO']['status'] == 'PARTIAL', 'BO recuperado debe reflejar cobertura parcial')
v.require(checkpoints['WATCH-BO']['covered_through'] == old_checkpoints['WATCH-BO']['covered_through'] is None, 'BO parcial no adelanta checkpoint')
v.require(run['status'] == 'PARTIAL', 'El resultado global permanece parcial')
v.require(len(state['run_index']) == len(previous['run_index']) + 1, 'Debe añadirse una única corrida')
manifest = v.read(WATCH / 'evidence' / (RUN_ID + '.json'))
v.require(any(item.get('url', '').startswith('https://www.boletinoficial.gov.ar/') and item.get('status') == 200 for item in manifest['fetches']), 'Falta evidencia de consulta al host gov')
if v.errors:
    raise SystemExit('\n'.join(v.errors))
print('OK: migración limitada a endpoints; dos inventarios validados; historia conservada; repetición PARTIAL y checkpoint BO sin avance. No prueba cobertura jurídica completa.')
