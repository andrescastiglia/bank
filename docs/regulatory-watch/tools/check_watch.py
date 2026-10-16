#!/usr/bin/env python3
"""Valida bitácoras y continuidad declaradas; no consulta ni interpreta normas."""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


ROOT = Path(__file__).resolve().parents[3]
WATCH = ROOT / "docs/regulatory-watch"
SOURCE_STATUSES = {"NOT_STARTED", "COMPLETE", "PARTIAL", "UNAVAILABLE", "NOT_APPLICABLE_WITH_BASIS"}
RUN_STATUSES = {"COMPLETE_WITH_CHANGES", "COMPLETE_NO_CHANGES", "PARTIAL", "FAILED"}
COMPLETE_RUNS = {"COMPLETE_WITH_CHANGES", "COMPLETE_NO_CHANGES"}
IDENTIFIER = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]*")
SHA256 = re.compile(r"[0-9a-fA-F]{64}")


class Validator:
    def __init__(self):
        self.errors = []

    def require(self, condition, message):
        if not condition:
            self.errors.append(message)
        return bool(condition)

    def read(self, path):
        def unique_pairs(pairs):
            value = {}
            for key, item in pairs:
                self.require(key not in value, f"{path}: clave JSON duplicada: {key}")
                value[key] = item
            return value

        try:
            value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_pairs)
        except (OSError, ValueError) as exc:
            self.errors.append(f"{path}: no se pudo leer JSON: {exc}")
            return {}
        return self.object(value, str(path))

    def object(self, value, context):
        if not self.require(isinstance(value, dict), f"{context}: debe ser un objeto"):
            return {}
        return value

    def fields(self, value, required, context):
        self.require(required.issubset(value), f"{context}: faltan campos: " + ", ".join(sorted(required - set(value))))

    def enum(self, value, choices, context):
        if not self.require(isinstance(value, str) and value in choices, f"{context}: valor inválido"):
            return None
        return value

    def array(self, value, context):
        if not self.require(isinstance(value, list), f"{context}: debe ser una lista"):
            return []
        return value

    def string(self, value, context):
        return self.require(isinstance(value, str) and bool(value.strip()), f"{context}: texto vacío o inválido")

    def identifier(self, value, context):
        return self.require(isinstance(value, str) and bool(IDENTIFIER.fullmatch(value)), f"{context}: ID vacío o inválido")

    def integer(self, value, context, nullable=False):
        if nullable and value is None:
            return True
        return self.require(type(value) is int and value >= 0, f"{context}: debe ser entero no negativo" + (" o null" if nullable else ""))

    def timestamp(self, value, context, nullable=False):
        if nullable and value is None:
            return None
        if not isinstance(value, str) or not re.match(r"^\d{4}-\d{2}-\d{2}T", value):
            self.errors.append(f"{context}: se requiere fecha ISO8601 con hora y zona")
            return None
        try:
            result = datetime.fromisoformat(value.replace("Z", "+00:00"))
            if result.tzinfo is None or result.utcoffset() is None:
                raise ValueError("falta zona horaria")
            return result
        except ValueError as exc:
            self.errors.append(f"{context}: fecha ISO8601 inválida: {exc}")
            return None

    def timezone(self, value, context):
        if not self.string(value, context):
            return
        try:
            ZoneInfo(value)
        except (ValueError, ZoneInfoNotFoundError):
            self.errors.append(f"{context}: zona IANA desconocida")

    def https(self, value, context):
        try:
            parsed = urlsplit(value) if isinstance(value, str) else None
            valid = parsed and parsed.scheme == "https" and parsed.hostname and not parsed.username and not parsed.password
        except ValueError:
            valid = False
        self.require(valid, f"{context}: se requiere URL HTTPS absoluta sin credenciales")

    def window(self, value, context, nullable=False):
        if nullable and value is None:
            return None
        window = self.object(value, context)
        start = self.timestamp(window.get("from_inclusive"), context + ".from_inclusive")
        end = self.timestamp(window.get("to_exclusive"), context + ".to_exclusive")
        if start is not None and end is not None:
            self.require(start < end, f"{context}: intervalo vacío o invertido")
            return start, end
        return None

    def id_list(self, value, context):
        values = self.array(value, context)
        seen = set()
        for item in values:
            if self.identifier(item, context):
                self.require(item not in seen, f"{context}: ID duplicado {item}")
                seen.add(item)
        return values

    def registry(self, data):
        self.require(type(data.get("schema_version")) is int and data["schema_version"] == 1, "sources: schema_version debe ser 1")
        self.string(data.get("inventory_version"), "sources.inventory_version")
        self.timezone(data.get("reporting_timezone"), "sources.reporting_timezone")
        self.timestamp(data.get("initial_backfill_from"), "sources.initial_backfill_from")
        self.integer(data.get("overlap_days"), "sources.overlap_days")
        self.string(data.get("scope"), "sources.scope")
        sources = {}
        rows = self.array(data.get("sources"), "sources.sources")
        self.require(bool(rows), "sources: inventario vacío")
        for row in rows:
            row = self.object(row, "sources.source")
            source_id = row.get("source_id")
            if not self.identifier(source_id, "sources.source_id"):
                continue
            self.require(source_id not in sources, f"sources: source_id duplicado {source_id}")
            self.enum(row.get("category"), {"regulation", "conditional", "standard"}, source_id + ".category")
            self.require(type(row.get("required_for_detection")) is bool, f"{source_id}: required_for_detection debe ser booleano")
            self.string(row.get("authority"), source_id + ".authority")
            self.string(row.get("coverage_scope"), source_id + ".coverage_scope")
            entrypoints = self.array(row.get("entrypoints"), source_id + ".entrypoints")
            self.require(bool(entrypoints), f"{source_id}: faltan entrypoints")
            for url in entrypoints:
                self.https(url, source_id + ".entrypoints")
            sources[source_id] = row
        self.require(any(row.get("required_for_detection") is True for row in sources.values()), "sources: falta al menos una fuente requerida")
        return sources

    def state(self, data, registry, sources, label):
        self.fields(data, {"schema_version", "repository", "state_branch", "reporting_timezone", "initial_backfill_from", "inventory_version", "last_run_id", "source_checkpoints", "agenda", "changes", "run_index"}, label)
        self.require(type(data.get("schema_version")) is int and data["schema_version"] == 1, f"{label}: schema_version debe ser 1")
        self.string(data.get("repository"), label + ".repository")
        self.require(data.get("state_branch") == "automation/regulatory-state", f"{label}: state_branch debe ser automation/regulatory-state, nunca main")
        self.require(data.get("reporting_timezone") == registry.get("reporting_timezone"), f"{label}: reporting_timezone distinto del registro")
        self.require(data.get("inventory_version") == registry.get("inventory_version"), f"{label}: inventory_version distinto del registro; migrar inventario explícitamente")
        initial = self.timestamp(data.get("initial_backfill_from"), label + ".initial_backfill_from")
        registered_initial = self.timestamp(registry.get("initial_backfill_from"), "sources.initial_backfill_from")
        self.require(initial == registered_initial, f"{label}: initial_backfill_from distinto del registro")
        if data.get("last_run_id") is not None:
            self.identifier(data.get("last_run_id"), label + ".last_run_id")
        for field in ("agenda", "changes", "run_index"):
            self.array(data.get(field), label + "." + field)
        checkpoints = {}
        for item in self.array(data.get("source_checkpoints"), label + ".source_checkpoints"):
            item = self.object(item, label + ".checkpoint")
            self.fields(item, {"source_id", "covered_through", "last_attempt_at", "status", "open_gaps"}, label + ".checkpoint")
            source_id = item.get("source_id")
            if not self.identifier(source_id, label + ".source_id"):
                continue
            self.require(source_id in sources, f"{label}: fuente desconocida {source_id}")
            self.require(source_id not in checkpoints, f"{label}: checkpoint duplicado {source_id}")
            status = self.enum(item.get("status"), SOURCE_STATUSES, f"{label}/{source_id}.status")
            covered = self.timestamp(item.get("covered_through"), f"{label}/{source_id}.covered_through", nullable=True)
            attempted = self.timestamp(item.get("last_attempt_at"), f"{label}/{source_id}.last_attempt_at", nullable=True)
            gaps = self.array(item.get("open_gaps"), f"{label}/{source_id}.open_gaps")
            if covered is not None and initial is not None:
                self.require(covered >= initial, f"{label}/{source_id}: checkpoint anterior al backfill inicial")
            if covered is not None and attempted is not None:
                self.require(covered <= attempted, f"{label}/{source_id}: checkpoint posterior al último intento")
            if status == "NOT_STARTED":
                self.require(item.get("covered_through") is None and item.get("last_attempt_at") is None, f"{label}/{source_id}: NOT_STARTED debe tener corte/intento null")
            elif status is not None:
                self.require(attempted is not None, f"{label}/{source_id}: estado iniciado requiere last_attempt_at")
            if status == "COMPLETE":
                self.require(covered is not None and attempted is not None, f"{label}/{source_id}: COMPLETE requiere corte e intento")
                self.require(not gaps, f"{label}/{source_id}: COMPLETE no admite gaps abiertos")
            if status == "NOT_APPLICABLE_WITH_BASIS":
                self.require(sources.get(source_id, {}).get("required_for_detection") is False, f"{label}/{source_id}: no se puede excluir una fuente requerida")
                self.string(item.get("not_applicable_basis"), f"{label}/{source_id}.not_applicable_basis")
            checkpoints[source_id] = item
        self.require(set(checkpoints) == set(sources), f"{label}: checkpoints deben enumerar todas las fuentes del registro sin omisiones")
        if any(item.get("status") != "NOT_STARTED" for item in checkpoints.values()):
            self.require(data.get("last_run_id") is not None, f"{label}: estado iniciado requiere last_run_id")
        return checkpoints

    def run(self, data, registry, sources):
        minimum = {"schema_version", "run_id", "started_at", "finished_at", "requested_window", "inventory_version", "status", "source_results", "change_ids", "errors"}
        self.require(minimum.issubset(data), "run: faltan campos mínimos: " + ", ".join(sorted(minimum - set(data))))
        self.require(type(data.get("schema_version")) is int and data["schema_version"] == 1, "run: schema_version debe ser 1")
        self.identifier(data.get("run_id"), "run.run_id")
        self.require(data.get("inventory_version") == registry.get("inventory_version"), "run: inventory_version distinto del registro")
        started = self.timestamp(data.get("started_at"), "run.started_at")
        finished = self.timestamp(data.get("finished_at"), "run.finished_at")
        window = self.window(data.get("requested_window"), "run.requested_window")
        if started is not None and finished is not None:
            self.require(started <= finished, "run: finished_at anterior a started_at")
        if window is not None and finished is not None:
            self.require(window[1] <= finished, "run: no se puede declarar cubierta una ventana futura al cierre de la corrida")
        status = self.enum(data.get("status"), RUN_STATUSES, "run.status")
        changes = self.id_list(data.get("change_ids"), "run.change_ids")
        self.array(data.get("errors"), "run.errors")
        if status == "COMPLETE_NO_CHANGES":
            self.require(not changes, "run: COMPLETE_NO_CHANGES requiere change_ids vacío")
        if status == "COMPLETE_WITH_CHANGES":
            self.require(bool(changes), "run: COMPLETE_WITH_CHANGES requiere change_ids no vacío")
        results, source_windows = {}, {}
        progress = False
        for result in self.array(data.get("source_results"), "run.source_results"):
            result = self.object(result, "run.source_result")
            self.fields(result, {"source_id", "status", "requested_window", "covered_window", "coverage_basis", "evidence_refs", "gaps", "not_applicable_basis"}, "run.source_result")
            source_id = result.get("source_id")
            if not self.identifier(source_id, "run.source_id"):
                continue
            self.require(source_id in sources, f"run: fuente desconocida {source_id}")
            self.require(source_id not in results, f"run: resultado duplicado {source_id}")
            context = "run/" + source_id
            source_status = self.enum(result.get("status"), SOURCE_STATUSES, context + ".status")
            requested = self.window(result.get("requested_window"), context + ".requested_window")
            source_windows[source_id] = requested
            if requested is not None and window is not None:
                self.require(window[0] <= requested[0] < requested[1] <= window[1], f"{context}: requested_window debe estar contenido en la envolvente de corrida")
            covered = self.window(result.get("covered_window"), context + ".covered_window", nullable=True)
            if covered is not None and requested is not None:
                self.require(requested[0] <= covered[0] < covered[1] <= requested[1], f"{context}: covered_window fuera del intervalo solicitado a la fuente")
            basis = self.object(result.get("coverage_basis"), context + ".coverage_basis")
            self.fields(basis, {"all_pages_processed", "all_annexes_processed", "pages_expected", "pages_processed", "annexes_expected", "annexes_processed", "outstanding_cursor"}, context + ".coverage_basis")
            for field in ("all_pages_processed", "all_annexes_processed"):
                self.require(type(basis.get(field)) is bool, f"{context}: {field} debe ser booleano")
            count_valid = {}
            for field in ("pages_expected", "pages_processed", "annexes_expected", "annexes_processed"):
                count_valid[field] = self.integer(basis.get(field), context + "." + field, nullable=field == "pages_expected")
            for expected, processed in (("pages_expected", "pages_processed"), ("annexes_expected", "annexes_processed")):
                if count_valid.get(expected) and count_valid.get(processed) and basis.get(expected) is not None:
                    self.require(basis[processed] <= basis[expected], f"{context}: {processed} supera {expected}")
            cursor = basis.get("outstanding_cursor")
            self.require(cursor is None or isinstance(cursor, str) and bool(cursor.strip()), f"{context}: outstanding_cursor debe ser texto no vacío o null")
            evidence = self.array(result.get("evidence_refs"), context + ".evidence_refs")
            for reference in evidence:
                reference = self.object(reference, context + ".evidence_ref")
                self.https(reference.get("url"), context + ".evidence.url")
                self.require(isinstance(reference.get("sha256"), str) and bool(SHA256.fullmatch(reference["sha256"])), f"{context}: sha256 de evidencia inválido")
                fetched = self.timestamp(reference.get("fetched_at"), context + ".evidence.fetched_at")
                if fetched is not None and finished is not None:
                    self.require(fetched <= finished, f"{context}: evidencia consultada después de finalizar la corrida")
            gaps = self.array(result.get("gaps"), context + ".gaps")
            if source_status == "COMPLETE":
                self.require(covered is not None and covered == requested, f"{context}: COMPLETE requiere covered_window igual a requested_window")
                self.require(basis.get("all_pages_processed") is True and basis.get("all_annexes_processed") is True, f"{context}: COMPLETE requiere todas las páginas y anexos")
                self.require(cursor is None, f"{context}: COMPLETE tiene cursor pendiente")
                self.require(bool(evidence), f"{context}: COMPLETE requiere evidencia no vacía")
                self.require(not gaps, f"{context}: COMPLETE no admite gaps")
                if count_valid.get("pages_expected") and count_valid.get("pages_processed") and basis.get("pages_expected") is not None:
                    self.require(basis["pages_expected"] == basis["pages_processed"], f"{context}: faltan o sobran páginas declaradas")
                if count_valid.get("annexes_expected") and count_valid.get("annexes_processed"):
                    self.require(basis["annexes_expected"] == basis["annexes_processed"], f"{context}: faltan o sobran anexos declarados")
            if source_status in {"NOT_STARTED", "UNAVAILABLE"}:
                self.require(covered is None, f"{context}: {source_status} no puede declarar cobertura")
                self.require(basis.get("pages_processed") == 0 and basis.get("annexes_processed") == 0, f"{context}: {source_status} no puede declarar páginas/anexos procesados; usar PARTIAL si hubo cobertura")
            if source_status == "NOT_APPLICABLE_WITH_BASIS":
                self.require(sources.get(source_id, {}).get("required_for_detection") is False, f"{context}: no se puede excluir una fuente requerida")
                self.string(result.get("not_applicable_basis"), context + ".not_applicable_basis")
                self.require(covered is None, f"{context}: no aplicabilidad no declara cobertura")
            elif result.get("not_applicable_basis") is not None:
                self.string(result.get("not_applicable_basis"), context + ".not_applicable_basis")
            if source_status in {"PARTIAL", "UNAVAILABLE"}:
                self.require(bool(gaps), f"{context}: {source_status} requiere gaps/causa explícitos")
            if source_status == "COMPLETE" or covered is not None or source_status == "PARTIAL" and any(type(basis.get(field)) is int and basis[field] > 0 for field in ("pages_processed", "annexes_processed")):
                progress = True
            results[source_id] = result
        required = {source_id for source_id, source in sources.items() if source.get("required_for_detection") is True}
        self.require(required.issubset(results), "run: faltan resultados de fuentes requeridas: " + ", ".join(sorted(required - set(results))))
        all_required_complete = bool(window) and all(
            results.get(source_id, {}).get("status") == "COMPLETE"
            and source_windows.get(source_id) is not None
            and source_windows[source_id][1] == window[1]
            for source_id in required
        )
        if status in COMPLETE_RUNS:
            self.require(all_required_complete, "run: COMPLETE_* exige todas las fuentes requeridas COMPLETE hasta to_exclusive global; queda cobertura objetivo pendiente")
        if status == "PARTIAL":
            self.require(not all_required_complete and progress, "run: PARTIAL requiere fuentes requeridas incompletas y cobertura parcial alcanzada")
        if status == "FAILED":
            self.require(not progress, "run: FAILED exige que no se haya alcanzado cobertura")
        return results

    def transition(self, previous, state, run, registry, old, new, results):
        self.require(state.get("last_run_id") == run.get("run_id"), "transición: last_run_id debe identificar la corrida aplicada")
        self.require(previous.get("repository") == state.get("repository"), "transición: repository cambió")
        initial = self.timestamp(registry.get("initial_backfill_from"), "transición.initial_backfill_from")
        started = self.timestamp(run.get("started_at"), "transición.started_at")
        finished = self.timestamp(run.get("finished_at"), "transición.finished_at")
        for source_id in set(old) & set(new):
            before, after = old[source_id], new[source_id]
            context = "transición/" + source_id
            old_cut = self.timestamp(before.get("covered_through"), context + ".previous.covered_through", nullable=True)
            new_cut = self.timestamp(after.get("covered_through"), context + ".covered_through", nullable=True)
            old_attempt = self.timestamp(before.get("last_attempt_at"), context + ".previous.last_attempt_at", nullable=True)
            new_attempt = self.timestamp(after.get("last_attempt_at"), context + ".last_attempt_at", nullable=True)
            if old_cut is not None:
                self.require(new_cut is not None and new_cut >= old_cut, f"{context}: checkpoint retrocede o se elimina")
            if old_attempt is not None:
                self.require(new_attempt is not None and new_attempt >= old_attempt, f"{context}: last_attempt_at retrocede o se elimina")
            result = results.get(source_id)
            if result is None:
                self.require(after == before, f"{context}: fuente omitida cambió sin resultado de corrida")
                continue
            window = self.window(result.get("requested_window"), context + ".requested_window")
            if new_attempt is not None and started is not None and finished is not None:
                self.require(started <= new_attempt <= finished, f"{context}: último intento fuera de la corrida aplicada")
            baseline = old_cut if old_cut is not None else initial
            advances = new_cut is not None and (old_cut is None or new_cut > old_cut)
            if advances:
                self.require(result.get("status") == "COMPLETE" and after.get("status") == "COMPLETE", f"{context}: sólo COMPLETE puede adelantar covered_through")
                if window is not None and baseline is not None:
                    self.require(window[0] <= baseline < window[1], f"{context}: avance sin cobertura contigua; falta backfill desde checkpoint previo")
                    self.require(new_cut == window[1], f"{context}: nuevo checkpoint debe ser to_exclusive de la corrida completa")
            if result.get("status") != "COMPLETE":
                self.require(new_cut == old_cut, f"{context}: una fuente no COMPLETE debe conservar su checkpoint anterior")
                self.require(after.get("status") == result.get("status"), f"{context}: estado debe reflejar el resultado no completo de la corrida")
                if result.get("status") in ("PARTIAL", "UNAVAILABLE"):
                    self.require(bool(after.get("open_gaps")), f"{context}: fallo/cobertura parcial deben conservar gaps abiertos")
            if isinstance(after.get("status"), str) and after["status"] in {"PARTIAL", "UNAVAILABLE", "NOT_STARTED", "NOT_APPLICABLE_WITH_BASIS"}:
                self.require(new_cut == old_cut, f"{context}: estado no COMPLETE no puede adelantar checkpoint")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, default=WATCH / "state.initial.json", help="Estado a validar; por defecto, seed sin ejecución")
    parser.add_argument("--run", type=Path, help="Corrida documental a validar")
    parser.add_argument("--previous-state", type=Path, help="Estado anterior; exige --run y verifica continuidad del estado seleccionado")
    args = parser.parse_args(argv)
    if args.previous_state is not None and args.run is None:
        print("--previous-state requiere --run", file=sys.stderr)
        return 1
    validator = Validator()
    registry = validator.read(WATCH / "sources.json")
    sources = validator.registry(registry)
    state = validator.read(args.state)
    checkpoints = validator.state(state, registry, sources, "state")
    if args.state.resolve() == (WATCH / "state.initial.json").resolve():
        validator.require(state.get("last_run_id") is None, "seed: last_run_id debe ser null; no es una corrida ejecutada")
        for source_id, checkpoint in checkpoints.items():
            validator.require(checkpoint.get("status") == "NOT_STARTED" and checkpoint.get("covered_through") is None and checkpoint.get("last_attempt_at") is None, f"seed/{source_id}: el estado inicial no debe declarar consultas ni cobertura")
    run = validator.read(args.run) if args.run is not None else None
    results = validator.run(run, registry, sources) if run is not None else {}
    if args.previous_state is not None:
        previous = validator.read(args.previous_state)
        old = validator.state(previous, registry, sources, "previous-state")
        validator.transition(previous, state, run, registry, old, checkpoints, results)
    if validator.errors:
        print("\n".join(validator.errors), file=sys.stderr)
        return 1
    required = sum(source.get("required_for_detection") is True for source in sources.values())
    detail = "transición declarada verificada" if args.previous_state is not None else "sin verificar transición histórica"
    print(f"OK: {len(sources)} fuentes ({required} requeridas); estado válido" + (f"; corrida {run['run_id']} válida" if run is not None else "; sin ejecutar consultas") + f"; {detail}. No prueba cobertura real, interpretación jurídica ni implementación normativa.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
