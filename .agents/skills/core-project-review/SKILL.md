---
name: core-project-review
description: "Usar para revisar integralmente un proyecto de core bancario, contrastar negocio, contabilidad, legal, arquitectura, QA, seguridad y operaciones, y elaborar un plan de mejoras sustentado en evidencia."
---

# Revisión integral del proyecto

## Propósito y entradas

Evaluar si el alcance documentado puede convertirse en un producto vendible, operable y sostenible. No sustituir profesionales, responsables institucionales ni evidencia de implementación. Leer el [índice de revisión](../../../docs/review/README.md), el [plan](../../../docs/review/improvement_plan.md) y las fuentes del trabajo solicitado; son una referencia fechada, no una conclusión permanentemente vigente.

Identificar repositorio/commit, fecha de evaluación y fecha de las fuentes, perfil del proveedor y de sus clientes, producto/etapa, trabajo pedido y evidencia disponible. Inventariar documentos, registros, scripts, skills, licencias y anexos. No leer sólo los índices ni confundir archivos generados con fuentes independientes. Distribuir la lectura por materias cuando convenga y comprobar que ninguna fuente quede sin revisión.

Aplicar [GOVERNANCE.md](../../../GOVERNANCE.md): proyecto conforme a GPL v2 y merge exclusivo del mantenedor. Separar sostenibilidad/mantenimiento del software libre de una eventual empresa de servicios: no exigir ventas, ARR o contratos comerciales como condición general para contribuir. El agente entrega ramas/PR, sin publicar o fusionar a `main`.

## Procedimiento

1. **Separar estados.** Registrar especificación, aplicabilidad, decisión, implementación, ensayo y aprobación por separado. Un FR propuesto no es una función ejecutada; una referencia no demuestra corrección semántica. Ausencia de evidencia en el repositorio no prueba que una organización carezca de ella fuera del alcance examinado.
2. **Revisar las perspectivas.** Cubrir marketing/ventas; economía y caja del proveedor; contabilidad e impuestos del core y de la empresa; legal/contratos/IP; arquitectura y datos; QA; seguridad; kickoff y operación; producto, accesibilidad, personas y terceros. Aplicar la [matriz de preguntas](references/review-template.md). No repetir una observación como nueve hallazgos independientes.
3. **Contrastar fuentes.** Vincular cada hallazgo a archivo/sección/ID y un hecho observado. Buscar el comportamiento ya diseñado antes de afirmar que falta. Para normativa usar [core-bancario-argentina](../core-bancario-argentina/SKILL.md), sus estados y fuentes primarias; registrar alcance de la comprobación. No importar una obligación de otro sujeto o una edición contractual no verificada.
4. **Cuantificar con límites.** Distinguir precio/costo observado de supuesto. Separar ARR, ingreso devengado, facturación y caja; medir margen recurrente por cliente/celda y costo de implantación, soporte, cumplimiento y salida. No completar una planilla con clientes, tasas, aprobaciones o disponibilidades inventados. Mantener lo desconocido visible.
5. **Clasificar.** Usar brecha de especificación, decisión pendiente, falta de evidencia, inconsistencia u oportunidad. P0 significa resolver antes del hito material indicado; no significa incidente real ni impide analizar/desarrollar con datos sintéticos. P1 mejora entrega/escalabilidad; P2 se condiciona a retorno y alcance.
6. **Resolver cruces.** Examinar precio frente a aislamiento/HA/guardia; privacidad frente a archivo; latencia frente a persistencia; GPL/IP frente a modalidad de entrega; datos/fondos reales frente a permisos; y capacidad del equipo frente a compromisos. Documentar alternativas y evidencia necesaria sin aceptar decisiones en nombre del cliente.
7. **Construir el plan.** Agrupar hallazgos en paquetes con entregable concreto, responsable sugerido, dependencia, criterio de cierre, hito y estado. Mantener los IDs estables y la relación muchos-a-muchos con las acciones. Reutilizar [core-fr-requisitos](../core-fr-requisitos/SKILL.md), [ADR](../core-adr-arquitectura/SKILL.md), [NFR](../core-nfr-calidad/SKILL.md) y [kickoff](../core-pilot-kickoff/SKILL.md).
8. **Comprobar y reportar.** Validar archivos/IDs, cálculos, enlaces y artefactos generados; revisar semántica además de sintaxis. Informar qué se corrigió, qué queda planificado y qué evidencia permitiría cerrarlo. No declarar un hallazgo resuelto por añadir otro documento con el mismo control propuesto.

## Salida y autorización

Entregar diagnóstico por perspectiva, inventario revisado, hallazgos trazables, plan priorizado, decisiones pendientes y próximos pasos ejecutables. Usar [la plantilla](references/review-template.md) y la estructura de hallazgos de la revisión vigente. Preservar el diagnóstico histórico al introducir correcciones posteriores.

La creación de documentación, análisis y correcciones reversibles autorizadas puede avanzar. Un pedido de revisión no autoriza contratar, contactar terceros, usar datos productivos, presentar declaraciones, desplegar, cambiar licencias o habilitar operaciones reales. No instalar un plugin por crear estos skills locales.
