# Revisión integral y plan de mejoras

**Conclusión:** existe una base de diseño amplia y trazable; el siguiente paso es elegir un producto comprable y demostrar su viabilidad económica, contractual, técnica y operativa. La biblioteca completa no debe convertirse en el alcance simultáneo del primer piloto.

**Fecha de revisión:** 16/10/2026 UTC. **Línea base:** `2e5d579103b94ab70c16d81debe73bf5840ba0c8`. Las fuentes de mercado/cumplimiento conservan su corte del **15/10/2026**. Los informes analizan documentos y evidencia disponible; no acreditan implementación bancaria, contratos, personal financiado, producción o certificaciones.

Empezar por el [plan integral de mejoras](improvement_plan.md): prioridades, 14 paquetes, responsables sugeridos, dependencias, criterios G0–G4 y una agenda propuesta para los primeros diez días hábiles. El [backlog estructurado](backlog.json) enlaza las acciones con **63 hallazgos**; todos permanecen abiertos hasta cumplir su criterio con evidencia.

## Perspectivas y hallazgos

| Perspectiva solicitada | Diagnóstico | Hallazgos estructurados | Cantidad |
|---|---|---|---:|
| Marketing/comercial y CEO/rentabilidad | [01 — Comercial y dirección](01-commercial-ceo.md) | [commercial.json](findings/commercial.json) | 12 |
| Contador: contabilidad/impuestos del producto y del proveedor | [02 — Contabilidad y fiscalidad](02-accounting-tax.md) | [accounting.json](findings/accounting.json) | 11 |
| Abogado: perímetro, contratos, datos, propiedad intelectual y cumplimiento | [03 — Legal y cumplimiento](03-legal-compliance.md) | [legal.json](findings/legal.json) | 10 |
| Informático: arquitectura, contratos, consistencia y datos | [04 — Arquitectura y datos](04-architecture-data.md) | [architecture.json](findings/architecture.json) | 9 |
| QA: aceptación, oráculos, evidencia y gobierno de skills | [05 — Calidad y skills](05-quality-skills.md) | [quality.json](findings/quality.json) | 9 |
| Seguridad y operaciones para kickoff/piloto | [06 — Seguridad y operación](06-security-operations.md) | [security_operations.json](findings/security_operations.json) | 12 |

Además se incorporan producto/experiencia y accesibilidad, gobierno de datos, personas/suplencia, propiedad intelectual, cadena de terceros y mantenimiento del conocimiento. Se tratan como cruces del plan y los informes, evitando multiplicar el mismo problema por cada perspectiva.

Las **37 prioridades P0** son condiciones previas al compromiso o hito indicado —por ejemplo, precio vinculante, aprobación sensible, datos reales, SLA o corte—; no representan 37 incidentes ni una prohibición de iniciar análisis/desarrollo sintético. Las **26 P1** completan entrega, mantenimiento y repetibilidad. No se inventaron fechas, personal, precios, clientes o aprobaciones para rellenar el plan.

## Alcance de la lectura y verificaciones

Se inventariaron los **125 archivos versionados de la línea base**, incluidos **96 Markdown**, **24 skills y sus metadatos**, tres JSON, el generador documental y LICENSE. [review_inventory.json](review_inventory.json) conserva rutas, tamaños, hashes originales y materias que los consultaron. Los informes indican lectura completa o por secciones pertinentes; los artefactos generados/metadatos se contrastaron estructuralmente. No se afirma que cada revisor haya leído cada artículo de todas las fuentes externas enlazadas.

Se revisaron las relaciones entre mercado, arquitectura, ocho ADR, trece NFR/71 criterios, 32 módulos/1.016 FR y 24 flujos, así como instrucciones, referencias y metadatos de los skills. La lectura por materias se contrastó entre disciplinas. El informe legal delimita un contraste oficial selectivo y sus resultados; no convierte esa muestra en actualización normativa integral.

El [informe QA](05-quality-skills.md) documenta ensayos aislados de cambios en el verificador original: retiro de IDs, pérdida de significado, reducción del denominador y enlaces/metadatos fuera de su alcance. La herramienta original puede aprobar esas últimas situaciones porque valida estructura/referencias de la biblioteca funcional. No se infiere un defecto bancario ejecutado: no hay aplicación bancaria para ensayar en esta línea base.

## Mejoras incorporadas y pendientes

Además del diagnóstico y plan se incorporan:

- Tres skills locales: [core-project-review](../../.agents/skills/core-project-review/SKILL.md), [core-fr-requisitos](../../.agents/skills/core-fr-requisitos/SKILL.md) y [core-pilot-kickoff](../../.agents/skills/core-pilot-kickoff/SKILL.md), con referencias y metadatos.
- Propagación inversa FR–casos/evidencia–ADR/NFR–skills en los coordinadores existentes. El [catálogo de skills](../skills.md) reúne ahora 27 workflows locales, sin instalar un plugin.
- Plantillas de [charter](templates/project_charter.md), [caso de negocio](templates/business_case.md) y [evidencia](templates/evidence_register.md), sin decisiones o datos reales prellenados.
- [README del proyecto](../../README.md), navegación actualizada y comprobación documental transversal con [workflow de CI](../../.github/workflows/docs.yml).

Estos cambios avanzan WP-12 y preparan el resto. **No cierran por sí solos los hallazgos.** El retiro activo/histórico de FR, la revisión de cambios semánticos, la evidencia financiera/operativa, los contratos, el caso económico y la aceptación del piloto permanecen planificados. La licencia y los estados propuestos de ADR/NFR se conservan.

## Comprobación reproducible

El [registro de verificación](validation.md) conserva resultados locales observados y ocho casos negativos del nuevo verificador; distingue esa evidencia de las pruebas documentales del diagnóstico QA y de cualquier futura prueba del producto.

Desde la raíz del repositorio, con Python 3 y [PyYAML fijado](tools/requirements.txt) disponible:

```sh
python3 docs/functional/tools/build_catalog.py --check
python3 docs/review/tools/check_review.py
```

El primer comando comprueba la biblioteca funcional y sus artefactos. El segundo valida el esquema de hallazgos/backlog, pertenencia de IDs/fuentes, dependencias y cobertura del plan, inventario/hash contra el commit histórico, enlaces locales de los Markdown del repositorio, frontmatter/metadata de todos los skills y configuración documental de CI. No valida vigencia jurídica, interpretación semántica completa, comportamiento del agente, seguridad del software ni rentabilidad.

Si cambian fuentes de las que deriva el catálogo, regenerar conscientemente con `python3 docs/functional/tools/build_catalog.py` y revisar el diff. No sustituir los estados del catálogo generado por resultados manuales de pruebas; guardar evidencia independiente y enlazar sus versiones. Si se modifica una acción del plan, mantener alineados el paquete y su criterio en backlog; el verificador detecta divergencias estructurales.

El inventario y los hallazgos conservan el diagnóstico del commit de origen aunque se incorporen mejoras posteriores. Para cerrar o reevaluar, añadir evidencia y decisión en su alcance; no reescribir la historia como si la condición original nunca hubiera existido.
