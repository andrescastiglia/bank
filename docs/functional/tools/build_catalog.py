#!/usr/bin/env python3
"""Extrae y verifica el inventario documental FR. No evalúa software ni leyes."""

import argparse
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[3]
DOCS = ROOT / "docs/functional"
EXPECTED_CODES = "ENT IAM CLI CFG CON ACC BAL LED CRE INT GAR COL PAY CHQ CRD CSH TRE FXT INV AML FRD REC RSK TAX RPT CST DAT ASY MIG OPS AIG COR".split()
SOURCE_RE = re.compile(r"\b(?:LAW-\d+|AML-\d+|DATA-\d+|TAX-\d+|BCRA-[FT]\d+|PAY-\d+|RPT-\d+|STD\d+|NFR-\d+(?:-C\d+)?|CTL-\d+|ADR-\d+)\b")
COMPLIANCE_RE = re.compile(r"(?:LAW-\d+|AML-\d+|DATA-\d+|TAX-\d+|BCRA-[FT]\d+|PAY-\d+|RPT-\d+|STD\d+)")
FR_RE = re.compile(r"FR-[A-Z]{3}-\d{3}")
ERRORS = []


def require(condition, message):
    if not condition:
        ERRORS.append(message)


def relative(path):
    return str(path.relative_to(ROOT))


def cells(line):
    return [part.strip() for part in line.strip().strip("|").split("|")]


def heading_slug(value):
    value = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"<[^>]+>", "", value).replace("`", "").replace("*", "")
    return re.sub(r"\s", "-", re.sub(r"[^\w\s-]", "", value.lower(), flags=re.UNICODE))


def anchors(path):
    text = path.read_text()
    found = set(re.findall(r'\bid=["\']([^"\']+)["\']', text))
    counts = defaultdict(int)
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, re.M):
        slug = heading_slug(heading)
        occurrence = counts[slug]
        counts[slug] += 1
        found.add(slug if occurrence == 0 else f"{slug}-{occurrence}")
    return found


def check_target(owner, target, location):
    target = unquote(target.strip("<>"))
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
        return
    filename, _, fragment = target.partition("#")
    path = (owner.parent / filename).resolve() if filename else owner
    require(path.exists(), f"{location}: enlace inexistente {target}")
    if path.exists() and path.suffix == ".md" and fragment:
        require(fragment in anchors(path), f"{location}: ancla inexistente {target}")


def extract_sources():
    sources = []
    paths = [ROOT / "docs/compliant.md"]
    paths += sorted((ROOT / "docs/nfr").glob("NFR-??-*.md"))
    paths += [ROOT / ".agents/skills/core-bancario-argentina/references/controles.md"]
    for path in paths:
        for line_number, line in enumerate(path.read_text().splitlines(), 1):
            if not line.startswith("| "):
                continue
            parts = cells(line)
            source_id = parts[0]
            kind = None
            if COMPLIANCE_RE.fullmatch(source_id):
                kind = "compliance"
            elif re.fullmatch(r"NFR-\d{2}-C\d{2}", source_id):
                kind = "nfr_criterion"
            elif re.fullmatch(r"CTL-\d{2}", source_id):
                kind = "engineering_control"
            if kind:
                sources.append({"id": source_id, "kind": kind, "file": relative(path),
                                "line": line_number, "description": parts[1], "source_row": parts})
    for path in sorted((ROOT / "docs/adr").glob("ADR-??-*.md")):
        adr_id = path.name[:6]
        title = next(line[2:] for line in path.read_text().splitlines() if line.startswith("# "))
        sources.append({"id": adr_id, "kind": "architectural_decision", "file": relative(path),
                        "line": 1, "description": title})
    ids = [source["id"] for source in sources]
    require(len(set(ids)) == len(ids), "El inventario fuente contiene IDs duplicados")
    expected = {"compliance": 173, "nfr_criterion": 71, "engineering_control": 21, "architectural_decision": 8}
    for kind, count in expected.items():
        actual = sum(source["kind"] == kind for source in sources)
        require(actual == count, f"Inventario {kind}: {actual}, esperado {count}; revisar denominador si cambió el alcance")
    return sources


def extract_modules(source_ids):
    modules, requirements = [], []
    paths = sorted(DOCS.glob("[0-9][0-9]-*.md"))
    require(len(paths) == 32, f"Hay {len(paths)} archivos de módulo; se esperan 32")
    for number, path in enumerate(paths, 1):
        require(path.name.startswith(f"{number:02d}-"), f"Orden/número incorrecto: {path.name}")
        expected_code = EXPECTED_CODES[number - 1] if number <= 32 else "INVALID"
        title = next((line[2:] for line in path.read_text().splitlines() if line.startswith("# ")), "")
        module = {"number": number, "code": expected_code, "title": title, "file": relative(path), "requirements": []}
        require(title != "", f"{path.name}: falta título")
        require("| ID | Requisito funcional | Ámbito / etapa | Criterio de aceptación y excepciones | Trazabilidad |" in path.read_text(),
                f"{path.name}: encabezado de tabla distinto del contrato de cinco columnas")
        for line_number, line in enumerate(path.read_text().splitlines(), 1):
            if not line.startswith("| FR-"):
                continue
            parts = cells(line)
            require(len(parts) == 5, f"{path.name}:{line_number}: {len(parts)} columnas, se esperan 5")
            if len(parts) != 5:
                continue
            fr_id, behavior, scope, acceptance, trace = parts
            expected_id = f"FR-{expected_code}-{len(module['requirements']) + 1:03d}"
            require(fr_id == expected_id, f"{path.name}:{line_number}: {fr_id}, se esperaba {expected_id}")
            require(all(parts), f"{fr_id}: celda vacía")
            refs = list(dict.fromkeys(SOURCE_RE.findall(trace)))
            require(bool(refs), f"{fr_id}: no tiene referencias identificadas")
            for ref in refs:
                require(ref in source_ids, f"{fr_id}: fuente desconocida {ref}")
            requirements.append({"id": fr_id, "module": expected_code, "file": relative(path), "line": line_number,
                                 "requirement": behavior, "scope_stage": scope, "acceptance_exceptions": acceptance,
                                 "source_ids": refs, "traceability_text": trace,
                                 "implementation_status": "not_evaluated", "evidence_status": "not_evaluated"})
            module["requirements"].append(fr_id)
        require(bool(module["requirements"]), f"{path.name}: sin FR")
        module["count"] = len(module["requirements"])
        modules.append(module)
    ids = [item["id"] for item in requirements]
    require(len(ids) == len(set(ids)), "IDs FR duplicados")
    return modules, requirements


def fr_links(ids, lookup, limit=None):
    shown = ids if limit is None else ids[:limit]
    links = [f"[{item}]({Path(lookup[item]['file']).name})" for item in shown]
    if limit is not None and len(ids) > limit:
        links.append(f"+{len(ids) - limit} en catálogo JSON")
    return ", ".join(links)


def source_link(source):
    path = source["file"]
    link = "../../" + path if path.startswith(".agents/") else "../" + path.removeprefix("docs/")
    return f"[{source['id']}]({link})"


def coverage_document(catalog, lookup):
    summary = catalog["summary"]
    lines = ["# Matriz de cobertura y trazabilidad", "",
             "**Generada desde los documentos de módulo. Estado: Propuesto; implementación y evidencia sin evaluar.**",
             "Base documental: 15/10/2026. Interpretar los resultados con [scope.md](scope.md).", "",
             f"El inventario contiene **{summary['functional_requirements']} FR en {summary['modules']} módulos**. Todas las entradas inventariadas tienen relaciones documentales con FR. Esto mide trazabilidad del alcance fechado; no es una certificación de cumplimiento ni demuestra que el software exista o supere pruebas.", "",
             "## Denominadores y resultado", "",
             "| Inventario | Entradas | Con relación a FR | Cobertura documental |",
             "|---|---:|---:|---:|"]
    labels = {"compliance": "Cumplimiento: leyes, BCRA, UIF, datos, fiscalidad y estándares",
              "nfr_criterion": "Criterios NFR", "engineering_control": "Controles CTL", "architectural_decision": "ADR"}
    for kind, label in labels.items():
        entries = [source for source in catalog["sources"] if source["kind"] == kind]
        covered = sum(bool(source["functional_requirements"]) for source in entries)
        lines.append(f"| {label} | {len(entries)} | {covered} | {covered / len(entries):.0%} |")
    for key, label in [("architecture_modules", "Módulos lógicos de arquitectura"), ("market_needs", "Necesidades estratégicas inventariadas"), ("prose_capabilities", "Capacidades/perímetros de prosa inventariados")]:
        count = len(catalog["manual_maps"][key])
        lines.append(f"| {label} | {count} | {count} | 100% |")
    lines += ["", "La relación de cumplimiento puede ser una función directa, un control preventivo, una integración, datos para un cálculo/reporte o soporte de evidencia institucional. Su aplicabilidad permanece en la fuente y en la columna ámbito del FR. Las funciones de apoyo a ISO/SOC/gobierno no ejecutan por sí solas la obligación organizacional. Los NFR conservan sus métricas y oráculos; los ADR conservan su estado de decisión.", "",
              "Los productos condicionales tienen comportamientos especificados, pero requieren rol/licencia, reglas, contratos e integración efectivos antes de activarse. CAP-07 registra una restricción de especialidades sin especificación suficiente; **no cuenta seguros/activos virtuales/contratación pública como plataformas funcionales especificadas**.", "",
              "## Relaciones por fuente", "",
              "Cada fila muestra hasta ocho FR para lectura; el número indica todas sus relaciones y [catalog.json](catalog.json) contiene la lista completa y la fila fuente con sus condiciones. Abrir el módulo para leer aceptación, ámbito y excepciones. No se deduce que todos los FR relacionados sean aplicables simultáneamente."]
    for kind, label in labels.items():
        lines += ["", f"### {label}", "", "| Fuente | Materia / decisión / criterio | FR relacionados | Total |", "|---|---|---|---:|"]
        for source in catalog["sources"]:
            if source["kind"] != kind:
                continue
            description = source["description"].replace("|", "&#124;")
            related = source["functional_requirements"]
            lines.append(f"| {source_link(source)} | {description} | {fr_links(related, lookup, 8)} | {len(related)} |")
    for key, title in [("architecture_modules", "Descomposición de la arquitectura"), ("market_needs", "Necesidades comerciales"), ("prose_capabilities", "Capacidades y condiciones descritas en prosa")]:
        lines += ["", f"## {title}", "", "| ID | Necesidad y fuente | FR de entrada a la capacidad |", "|---|---|---|"]
        for mapping in catalog["manual_maps"][key]:
            target = "../" + mapping["source"].removeprefix("docs/")
            lines.append(f"| {mapping['id']} | [{mapping['name']}]({target}) | {fr_links(mapping['fr'], lookup)} |")
    lines += ["", "## Revisión semántica y límites de la comprobación", "",
              "Además de comprobar IDs, se revisaron contratos entre módulos, fuentes y excepciones. La revisión incorporó sucesión/incapacidad y facultades de cotitulares; impidió sustituir evidencia del riel por una decisión manual en un pago incierto; distinguió devolución financiera y fiscal; precisó fixing/liquidación física o por diferencias de forwards; y corrigió atribuciones de fuentes de mandatos, tercerización y respaldo PSPCP.", "",
              "Se contrastaron integridad monetaria, permisos y perímetros, mecanismos de los NFR, evidencia de estándares, migración y recuperación. Los [flujos integrados](flows.md) conectan módulos y sus resultados esperados. La revisión documental no ejecuta esos escenarios ni demuestra eficacia operativa.", "",
              "Las huellas de documentos fuente y de los módulos están en el catálogo. Un cambio exige revisión de impacto y regeneración. El verificador detecta referencias ausentes, desconocidas, inventarios alterados, enlaces locales rotos o artefactos desactualizados; no detecta automáticamente toda contradicción semántica ni nuevas obligaciones posteriores al corte.", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verificar sin modificar artefactos")
    args = parser.parse_args()
    manifest = json.loads((DOCS / "coverage_map.json").read_text())
    sources = extract_sources()
    source_ids = {item["id"] for item in sources}
    modules, requirements = extract_modules(source_ids)
    lookup = {item["id"]: item for item in requirements}
    inverse = defaultdict(list)
    for item in requirements:
        for source_id in item["source_ids"]:
            inverse[source_id].append(item["id"])
    for source in sources:
        source["functional_requirements"] = inverse[source["id"]]
        require(bool(source["functional_requirements"]), f"Fuente sin relación funcional: {source['id']}")
    manual_maps = {key: manifest[key] for key in ("architecture_modules", "market_needs", "prose_capabilities")}
    require(len(manual_maps["architecture_modules"]) == 15, "Se esperan 15 módulos lógicos de arquitectura")
    architecture = (ROOT / "docs/achitecture.md").read_text()
    module_section = architecture.split("## 3. Catálogo de módulos y propiedad de datos", 1)[-1].split("## 4.", 1)[0]
    architecture_names = [cells(line)[0] for line in module_section.splitlines()
                          if line.startswith("| ") and not line.startswith("| Módulo |")]
    mapped_names = [item["name"] for item in manual_maps["architecture_modules"]]
    require(architecture_names == mapped_names,
            "El catálogo lógico de arquitectura cambió: revisar módulos y mapa de cobertura")
    map_ids = set()
    for entries in manual_maps.values():
        for mapping in entries:
            require(mapping["id"] not in map_ids, f"Relación manual duplicada {mapping['id']}")
            map_ids.add(mapping["id"])
            require(bool(mapping["fr"]), f"{mapping['id']}: sin FR")
            for fr_id in mapping["fr"]:
                require(fr_id in lookup, f"{mapping['id']}: FR desconocido {fr_id}")
            check_target(ROOT / "source-map.md", mapping["source"], mapping["id"])
    for path in sorted(DOCS.glob("*.md")):
        if path.name == "coverage.md":
            continue  # Se verifica el contenido generado más abajo.
        content = path.read_text()
        for fr_id in FR_RE.findall(content):
            require(fr_id in lookup, f"{path.name}: FR citado inexistente {fr_id}")
        for target in re.findall(r"\[[^\]]+\]\(([^\s)]+)\)", content):
            # Primera generación: los dos artefactos aún pueden no existir.
            if target in {"catalog.json", "coverage.md"}:
                continue
            check_target(path, target, path.name)
    if ERRORS:
        print("\n".join(ERRORS), file=sys.stderr)
        return 1
    source_paths = {ROOT / item["file"] for item in sources}
    source_paths.update(ROOT / name for name in ["docs/achitecture.md", "docs/market_analysis.md", "docs/skills.md"])
    source_paths.update((ROOT / ".agents/skills/core-bancario-argentina").rglob("*.md"))
    digest = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
    catalog = {"schema_version": 1, "baseline_date": manifest["baseline_date"], "baseline_commit": manifest["baseline_commit"],
               "specification_status": "proposed", "implementation_status": "not_evaluated", "evidence_status": "not_evaluated",
               "coverage_definition": "Referenced coverage of the explicitly inventoried and dated documentary scope; not legal or implementation certification.",
               "summary": {"modules": len(modules), "functional_requirements": len(requirements), "compliance_sources": 173,
                           "nfr_criteria": 71, "engineering_controls": 21, "architectural_decisions": 8},
               "source_documents_sha256": {relative(path): digest(path) for path in sorted(source_paths)},
               "fr_documents_sha256": {module["file"]: digest(ROOT / module["file"]) for module in modules},
               "fr_support_documents_sha256": {relative(DOCS / name): digest(DOCS / name) for name in ["scope.md", "flows.md"]},
               "coverage_map_sha256": digest(DOCS / "coverage_map.json"),
               "modules": modules, "requirements": requirements, "sources": sources, "manual_maps": manual_maps}
    module_lines = [f"**{len(requirements)} FR en {len(modules)} módulos.** Los conteos se extraen de las filas de requisitos.", "",
                    "| Nº | Código | Módulo | FR |", "|---:|---|---|---:|"]
    for module in modules:
        title = re.sub(r"^(?:Módulo )?\d+[. ]*\s*[—–-]?\s*", "", module["title"])
        title = re.sub(rf"\s*(?:\({module['code']}\)|[—–-]\s*{module['code']})$", "", title)
        module_lines.append(f"| {module['number']:02d} | {module['code']} | [{title}]({Path(module['file']).name}) | {module['count']} |")
    readme = (DOCS / "README.md").read_text()
    marker = "<!-- catalog:start -->\n" + "\n".join(module_lines) + "\n<!-- catalog:end -->"
    require(readme.count("<!-- catalog:start -->") == 1 and readme.count("<!-- catalog:end -->") == 1, "README: marcadores de catálogo inválidos")
    readme = re.sub(r"<!-- catalog:start -->.*?<!-- catalog:end -->", lambda _: marker, readme, flags=re.S)
    outputs = {DOCS / "catalog.json": json.dumps(catalog, ensure_ascii=False, indent=2) + "\n",
               DOCS / "coverage.md": coverage_document(catalog, lookup), DOCS / "README.md": readme}
    for path, content in outputs.items():
        if args.check:
            require(path.exists() and path.read_text() == content, f"Artefacto desactualizado: {relative(path)}")
        else:
            path.write_text(content)
    if ERRORS:
        print("\n".join(ERRORS), file=sys.stderr)
        return 1
    print(f"OK: {len(requirements)} FR; {len(modules)} módulos; 173/173 fuentes; 71/71 criterios NFR; 21/21 CTL; 8/8 ADR; 15/15 módulos lógicos. "
          + ("Artefactos reproducibles." if args.check else "Artefactos generados."))
    return 0


if __name__ == "__main__":
    sys.exit(main())
