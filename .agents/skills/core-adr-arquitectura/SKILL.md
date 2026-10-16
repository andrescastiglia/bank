---
name: core-adr-arquitectura
description: "Usar para crear, mantener, relacionar o revisar Architectural Decision Records (ADR), evaluar alternativas de arquitectura y coordinar cambios que afecten varias decisiones del proyecto."
---

# Crear y mantener Architectural Decision Records

## Significado y alcance

Un **ADR — Architectural Decision Record** registra contexto, decisión arquitectónica, alternativas, razones y consecuencias. Un **NFR — Non-Functional Requirement** describe una cualidad o restricción verificable del sistema; puede motivar un ADR, pero no es la decisión. Por ejemplo, recuperarse en un tiempo acordado es NFR; adoptar una región pasiva y una política de persistencia es ADR.

Este skill gestiona el ciclo de vida de los registros y coordina los skills de las ocho decisiones de la línea base. No se limita a auditar un documento ya escrito. Para crear/medir atributos de calidad usar [core-nfr-calidad](../core-nfr-calidad/SKILL.md); para determinar obligaciones jurídicas usar las referencias pertinentes de [core-bancario-argentina](../core-bancario-argentina/SKILL.md).

## Entrada y fuentes

Identificar decisión o problema, trabajo solicitado —crear, actualizar, diseñar, implementar o revisar—, perfil/entidad, alcance, alternativas, NFR afectados y evidencia disponible. Leer el [índice ADR](../../../docs/adr/README.md), la parte pertinente de [arquitectura](../../../docs/achitecture.md), [mercado](../../../docs/market_analysis.md) y [cumplimiento](../../../docs/compliant.md). Inspeccionar código, contratos y medidas existentes antes de inferirlos.

La base del 15/10/2026 es propuesta y no acredita implementación. Si faltan datos, avanzar con supuestos y alternativas explícitas en el trabajo independiente; pedir sólo el dato que cambie una decisión. No introducir una aprobación genérica para analizar o corregir algo reversible ya autorizado.

## Procedimiento

1. **Distinguir el objeto.** Una función como importar clientes pertenece al alcance funcional; la calidad exigida de esa importación es NFR; elegir staging y publicación de cohortes es ADR. Registrar relaciones sin convertir estas tres cosas en sinónimos.
2. **Inventariar registros.** Buscar el ID y su estado actual; conservar los ocho IDs existentes. Para una decisión nueva asignar el siguiente ID libre y un nombre descriptivo. Evitar duplicados por renombrar una tecnología o un módulo.
3. **Construir el contexto.** Vincular problema comercial, perfil/licencia, restricciones, NFR, volumen y riesgos. Distinguir medición, declaración de proveedor, supuesto e inferencia. Una cifra de diseño no constituye benchmark ni mandato legal.
4. **Comparar alternativas reales.** Incluir mantener la situación si es viable. Evaluar consistencia, seguridad, fallos, latencia, recuperación, equipo, TCO, dependencia de terceros, portabilidad y migración. Explicar la razón de descarte; no fabricar una comparación para justificar una preferencia.
5. **Escribir o actualizar.** Usar [la plantilla local](references/plantilla-adr.md). Documentar decisión, alcance, consecuencias favorables y costos, límites, dependencias, criterios observables y condiciones que obligan a reconsiderar. Relacionar NFR y CTL por ID y fuente concreta.
6. **Gestionar estados e historia.** Usar `Propuesto`, `Aceptado`, `Reemplazado` o `Descartado`. Cambiar a Aceptado sólo cuando exista evidencia de una decisión real del responsable competente; no inferirlo de crear un archivo o pasar pruebas. La aceptación de diseño es distinta de implementación y verificación. Si se reemplaza una decisión aceptada, conservarla y enlazar el nuevo ADR en ambos sentidos con motivo/fecha. Una aclaración editorial puede actualizarse conservando su historial.
7. **Aplicar la acción autorizada.** Para implementación, utilizar los skills especializados, realizar cambios compatibles y verificaciones materiales; no cerrar sólo con un plan si el trabajo es realizable. Para revisión, informar desviaciones con escenario, efecto y evidencia. Para diseño, entregar decisión y backlog de validación; no desplegar por un pedido de documentación.
8. **Comprobar propagación.** Actualizar arquitectura, índice, NFR, criterios, skills y enlaces afectados. Un nuevo componente o región necesita análisis de contrato/país/perfil; el ADR por sí solo no autoriza producción ni elimina requisitos legales.

## Selección de skills especializados

| Cambio | Skill local que debe leerse |
|---|---|
| Fronteras, módulos o extracción | [adr-01-nucleo-modular](../adr-01-nucleo-modular/SKILL.md) |
| Dinero, ledger, reservas, límites y concurrencia | [adr-02-autoridad-sql](../adr-02-autoridad-sql/SKILL.md) |
| Eventos, reintentos, jobs y efectos externos | [adr-03-outbox-inbox](../adr-03-outbox-inbox/SKILL.md) |
| Topología HA, pérdida de sitio y DR | [adr-04-alta-disponibilidad](../adr-04-alta-disponibilidad/SKILL.md) |
| Parámetros, productos y temporalidad | [adr-05-configuracion-versionada](../adr-05-configuracion-versionada/SKILL.md) |
| Entidades, aislamiento y plano de control | [adr-06-aislamiento-por-celda](../adr-06-aislamiento-por-celda/SKILL.md) |
| Stack, proveedor, servicios y costos | [adr-07-stack-gestionado](../adr-07-stack-gestionado/SKILL.md) |
| Importación inicial, deltas y corte | [adr-08-carga-inicial-masiva](../adr-08-carga-inicial-masiva/SKILL.md) |

Leer los aplicables, sin ejecutar todos los workflows para una edición menor. Las relaciones son dependencias técnicas; no un orden de aprobación. No ordenar despliegues, comunicaciones externas o acciones productivas por haber abierto un skill.

## Salida

Entregar registros creados/actualizados y matriz `problema | ADR/estado | alternativas | NFR motivador | decisión | consecuencia | criterio/evidencia | dependencias | pendiente`. Indicar trabajo realizado, pruebas efectivamente ejecutadas y límites. Distinguir estado de decisión de `sin evaluar`, `diseñado`, `implementado sin evidencia` y `verificado`. No declarar aceptación, benchmark o conformidad normativa por la mera cobertura documental.
