#!/usr/bin/env python3
"""Verifica documentación, trazabilidad de la revisión y estructura de skills.

No evalúa leyes, comportamiento del agente, producto bancario ni rentabilidad.
"""

import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.dont_write_bytecode = True

try:
    import yaml
except ImportError:
    sys.exit("Falta PyYAML. Instalar las dependencias de docs/review/tools/requirements.txt.")


ROOT = Path(__file__).resolve().parents[3]
REVIEW = ROOT / "docs/review"
ERRORS = []
AREAS = {"commercial": "COM", "accounting": "ACC", "legal": "LEG", "architecture": "ARC", "quality": "QA", "security_operations": "SEC"}
FINDING_KEYS = {"id", "title", "kind", "priority", "trigger", "statement", "evidence", "impact", "actions", "acceptance", "owner_role", "dependencies", "suggested_deliverables", "skill_impact"}


def require(condition, message):
    if not condition:
        ERRORS.append(message)


def read_json(path):
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError) as exc:
        ERRORS.append(f"{path.relative_to(ROOT)}: {exc}")
        return {}


def check_path(name, context):
    path = (ROOT / name).resolve()
    require(path.is_relative_to(ROOT) and path.is_file(), f"{context}: archivo inexistente o fuera del repositorio: {name}")


def check_closure_evidence(value, closed, context):
    require(isinstance(value, list), f"{context}: closure_evidence debe ser una lista")
    if not isinstance(value, list):
        return
    if closed:
        require(bool(value), f"{context}: cerrado sin referencia de evidencia")
    for reference in value:
        valid = isinstance(reference, str) and bool(reference.strip())
        if isinstance(reference, dict):
            valid = isinstance(reference.get("reference"), str) and bool(reference["reference"].strip())
        require(valid, f"{context}: referencia de evidencia vacía o inválida")


def check_findings(catalog):
    known_ids = {item["id"] for item in catalog.get("requirements", []) + catalog.get("sources", [])}
    known_ids.update(item.split("-C")[0] for item in known_ids.copy() if item.startswith("NFR-"))
    findings, documents, areas = {}, {}, set()
    for path in sorted((REVIEW / "findings").glob("*.json")):
        data = read_json(path)
        require(set(data) == {"area", "baseline_commit", "review_date", "lenses", "documents_reviewed", "findings"}, f"{path.name}: esquema raíz incorrecto")
        area = data.get("area")
        require(area in AREAS and area not in areas, f"{path.name}: área inválida/duplicada")
        areas.add(area)
        require(bool(data.get("lenses")), f"{path.name}: faltan perspectivas")
        documents[area] = set(data.get("documents_reviewed", []))
        for name in documents[area]:
            check_path(name, path.name)
        for number, finding in enumerate(data.get("findings", []), 1):
            fr_id = finding.get("id")
            require(set(finding) == FINDING_KEYS, f"{fr_id}: esquema incorrecto")
            require(fr_id == f"REV-{AREAS.get(area, 'INVALID')}-{number:02d}", f"{path.name}: ID de hallazgo inválido/no consecutivo: {fr_id}")
            require(fr_id not in findings, f"Hallazgo duplicado: {fr_id}")
            require(finding.get("priority") in {"P0", "P1", "P2"}, f"{fr_id}: prioridad inválida")
            require(finding.get("kind") in {"missing_decision", "specification_gap", "evidence_gap", "inconsistency", "opportunity"}, f"{fr_id}: clase inválida")
            for key in ["title", "trigger", "statement", "impact", "owner_role"]:
                require(isinstance(finding.get(key), str) and bool(finding[key].strip()), f"{fr_id}: {key} vacío")
            for key in ["actions", "acceptance", "evidence"]:
                require(isinstance(finding.get(key), list) and bool(finding[key]), f"{fr_id}: {key} sin elementos")
            for evidence in finding.get("evidence", []):
                require(set(evidence) == {"path", "section", "detail", "ids"}, f"{fr_id}: esquema de evidencia incorrecto")
                check_path(evidence["path"], fr_id)
                require(evidence["path"] in documents[area], f"{fr_id}: evidencia fuera del inventario declarado")
                for source_id in evidence["ids"]:
                    require(source_id in known_ids, f"{fr_id}: ID fuente desconocido {source_id}")
            findings[fr_id] = {"source": str(path.relative_to(ROOT)), "area": area, "baseline_commit": data.get("baseline_commit"), "review_date": data.get("review_date"), **finding}
    require(areas == set(AREAS), "El inventario de perspectivas está incompleto")
    return findings, documents


def check_backlog(backlog, findings):
    items = {item["id"]: item for item in backlog.get("findings", [])}
    packages = {item["id"]: item for item in backlog.get("work_packages", [])}
    require(len(items) == len(backlog.get("findings", [])) and len(packages) == len(backlog.get("work_packages", [])), "Backlog: IDs duplicados")
    require(set(items) == set(findings), "Backlog: inventario de hallazgos divergente")
    summary = backlog.get("summary", {})
    require(summary.get("findings") == len(findings), "Backlog: conteo de hallazgos divergente")
    require(summary.get("work_packages") == len(packages), "Backlog: conteo de paquetes divergente")
    require(summary.get("by_priority") == dict(Counter(item["priority"] for item in findings.values())), "Backlog: prioridades divergentes")
    require(summary.get("closed_findings") == sum(item.get("state") == "closed" for item in items.values()), "Backlog: conteo de cierre divergente")
    plan = (REVIEW / "improvement_plan.md").read_text()
    for wp_id, package in packages.items():
        require(package.get("state") in {"planned", "in_progress", "blocked", "closed"}, f"{wp_id}: estado inválido")
        check_closure_evidence(package.get("closure_evidence"), package.get("state") == "closed", wp_id)
        require(bool(package.get("finding_ids")), f"{wp_id}: sin hallazgos")
        for dep in package.get("dependencies", []):
            require(dep in packages and dep != wp_id, f"{wp_id}: dependencia inválida {dep}")
        for fid in package.get("finding_ids", []):
            require(fid in items and wp_id in items[fid]["work_packages"], f"{wp_id}: relación no recíproca con {fid}")
        for gate in package.get("gates", []):
            require(gate in {"G0", "G1", "G2", "G3", "G4"}, f"{wp_id}: hito inválido")
        rows = [line for line in plan.splitlines() if line.startswith("| **" + wp_id + " ")]
        require(len(rows) == 1, f"{wp_id}: fila ausente o duplicada en plan")
        if len(rows) == 1:
            parts = [cell.strip() for cell in rows[0].strip("|").split("|")]
            require(len(parts) == 4 and parts[2] == package.get("actions_deliverables") and parts[3] == package.get("acceptance"), f"{wp_id}: plan y backlog tienen acciones/criterios distintos")
    for fid, item in items.items():
        require(item.get("state") in {"open", "in_progress", "closed", "not_applicable_with_basis"}, f"{fid}: estado inválido")
        require(bool(item.get("work_packages")), f"{fid}: no tiene acción en el plan")
        for wp_id in item.get("work_packages", []):
            require(wp_id in packages and fid in packages[wp_id]["finding_ids"], f"{fid}: paquete no recíproco {wp_id}")
        check_path(item["report"], fid)
        source = findings.get(fid, {})
        for key in ["source", "area", "title", "priority", "kind", "trigger"]:
            require(item.get(key) == source.get(key), f"{fid}: {key} difiere de su diagnóstico")
        require(source.get("baseline_commit") == backlog.get("baseline_commit") and source.get("review_date") == backlog.get("review_date"), f"{fid}: línea base/fecha incoherentes")
        check_closure_evidence(item.get("closure_evidence"), item.get("state") == "closed", fid)
    visited, visiting = set(), set()
    def visit(wp_id):
        if wp_id in visiting:
            ERRORS.append(f"Dependencia circular de paquetes: {wp_id}")
            return
        if wp_id in visited or wp_id not in packages:
            return
        visiting.add(wp_id)
        for dep in packages[wp_id].get("dependencies", []):
            visit(dep)
        visiting.remove(wp_id)
        visited.add(wp_id)
    for wp_id in packages:
        visit(wp_id)


def check_inventory(inventory, backlog, documents):
    baseline = inventory.get("baseline_commit", "")
    require(baseline == backlog.get("baseline_commit"), "Inventario: commit distinto al backlog")
    require(bool(re.fullmatch(r"[0-9a-f]{40}", baseline)), "Inventario: commit no válido")
    if not re.fullmatch(r"[0-9a-f]{40}", baseline):
        return
    try:
        tracked = set(subprocess.check_output(["git", "ls-tree", "-r", "--name-only", baseline], cwd=ROOT, text=True).splitlines())
    except subprocess.CalledProcessError:
        ERRORS.append("No se encontró el commit histórico del inventario; obtener el historial Git")
        return
    entries = inventory.get("files", [])
    paths = [item["path"] for item in entries]
    require(len(paths) == len(set(paths)) and set(paths) == tracked, "Inventario: no coincide con todos los archivos del commit fuente")
    for item in entries:
        path = item["path"]
        original = subprocess.check_output(["git", "show", f"{baseline}:{path}"], cwd=ROOT)
        require(hashlib.sha256(original).hexdigest() == item.get("sha256") and len(original) == item.get("bytes"), f"Inventario: hash/tamaño histórico incorrecto de {path}")
        actual = {area for area, names in documents.items() if path in names}
        require(bool(actual) and actual == set(item.get("reviewed_by", [])), f"Inventario: revisión no declarada/incorrecta de {path}")
    summary = inventory.get("summary", {})
    require(summary.get("files") == len(entries), "Inventario: total incorrecto")
    require(summary.get("markdown") == sum(path.endswith(".md") for path in paths), "Inventario: Markdown incorrecto")
    require(summary.get("skills") == sum(path.endswith("/SKILL.md") for path in paths), "Inventario: skills incorrectos")


def check_skills_and_links():
    spec = importlib.util.spec_from_file_location("fr_document_links", ROOT / "docs/functional/tools/build_catalog.py")
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    names = set()
    for path in sorted((ROOT / ".agents/skills").glob("*/SKILL.md")):
        text = path.read_text()
        require(text.startswith("---\n"), f"{path.parent.name}: falta frontmatter YAML")
        try:
            data = yaml.safe_load(text.split("---", 2)[1])
            require(isinstance(data, dict), f"{path.parent.name}: frontmatter no es objeto")
            if not isinstance(data, dict):
                continue
            require(data.get("name") == path.parent.name and data.get("name") not in names, f"{path.parent.name}: nombre inválido/duplicado")
            names.add(data.get("name"))
            require(isinstance(data.get("description"), str) and bool(data["description"].strip()), f"{path.parent.name}: descripción vacía")
            metadata = yaml.safe_load((path.parent / "agents/openai.yaml").read_text())
            require(isinstance(metadata, dict), f"{path.parent.name}: metadata no es objeto")
            if not isinstance(metadata, dict):
                continue
            interface = metadata.get("interface", {})
            for key in ["display_name", "short_description", "default_prompt"]:
                require(isinstance(interface.get(key), str) and bool(interface[key].strip()), f"{path.parent.name}: interface.{key} inválido")
            policy = metadata.get("policy", {})
            require(isinstance(policy, dict) and set(policy).issubset({"allow_implicit_invocation", "products"}), f"{path.parent.name}: policy inválida")
            if isinstance(policy, dict) and "allow_implicit_invocation" in policy:
                require(isinstance(policy["allow_implicit_invocation"], bool) or policy["allow_implicit_invocation"] is None, f"{path.parent.name}: invocación implícita no booleana")
        except (OSError, IndexError, yaml.YAMLError) as exc:
            ERRORS.append(f"{path.parent.name}: YAML/metadata inválidos: {exc}")
    markdowns = sorted((ROOT / "docs").rglob("*.md")) + sorted((ROOT / ".agents").rglob("*.md"))
    if (ROOT / "README.md").exists():
        markdowns.append(ROOT / "README.md")
    for path in markdowns:
        text = path.read_text()
        # Las plantillas pueden mostrar Markdown como datos dentro de bloques de código.
        text = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", text, flags=re.M | re.S)
        for target in re.findall(r"\[[^\]]+\]\(([^\s)]+)\)", text):
            helper.check_target(path, target, str(path.relative_to(ROOT)))
    ERRORS.extend(helper.ERRORS)
    workflow = yaml.safe_load((ROOT / ".github/workflows/docs.yml").read_text())
    require(workflow.get("permissions", {}).get("contents") == "read", "CI: permisos de contenido deben ser read")
    runs = [step.get("run", "") for job in workflow.get("jobs", {}).values() for step in job.get("steps", [])]
    require(any("build_catalog.py --check" in run for run in runs) and any("check_review.py" in run for run in runs), "CI: faltan verificaciones documentales")
    return len(names), len(markdowns)


def main():
    catalog = read_json(ROOT / "docs/functional/catalog.json")
    findings, documents = check_findings(catalog)
    backlog = read_json(REVIEW / "backlog.json")
    inventory = read_json(REVIEW / "review_inventory.json")
    check_backlog(backlog, findings)
    check_inventory(inventory, backlog, documents)
    skill_count, markdown_count = check_skills_and_links()
    if ERRORS:
        print("\n".join(ERRORS), file=sys.stderr)
        return 1
    print(f"OK: {len(findings)} hallazgos; {len(backlog['work_packages'])} paquetes; {len(inventory['files'])} archivos de línea base; {skill_count} skills; enlaces de {markdown_count} Markdown y estructura documental válidos. No es validación semántica ni de producto.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
