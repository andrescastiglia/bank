# ADR-05 — Configuración limitada, versionada y fechada

**Estado:** Propuesto. **Base documental:** 15/10/2026. **Implementación y efectividad:** sin evaluar. Formaliza la línea base de arquitectura; no acredita aprobación institucional ni parámetros financieros reales.

## Contexto

Tasas, comisiones, calendarios, impuestos, planes contables y requisitos locales cambian con distintas vigencias. El mercado requiere adaptación sin convertir cada cliente en un fork. Al mismo tiempo, un núcleo debe reconstruir qué regla se aplicó a cada contrato, operación, devengamiento y reporte. Una tabla mutable de parámetros o un motor de scripts irrestricto no ofrece esa garantía.

## Decisión

Configurar capacidades soportadas por plataforma, entidad, producto, contrato e integración. Nuevos algoritmos, invariantes o relaciones contables requieren código, revisión y pruebas. No ejecutar SQL o scripts arbitrarios desde parámetros de negocio.

Cada regla tiene identificador, entidad/producto/moneda/jurisdicción, versión, fuente, vigencia de negocio, fecha de registro, estado, responsables, motivo y referencias de fórmulas/mapeos. Versiones aprobadas se distribuyen y activan localmente de forma atómica y auditable. El camino transaccional no depende del plano administrativo remoto.

Los contratos y operaciones conservan las versiones utilizadas. Se impiden solapamientos ambiguos, activación anticipada y fallback silencioso. Caer el scheduler o el plano de administración no habilita usar una versión vencida o no aprobada. Correcciones retroactivas conservan el original y generan ajustes explícitos, no una segunda operación económica por cambiar el número de versión.

No se desactivan mediante flags la partida doble, separación de entidades, autorización, auditoría o controles legales aplicables. Una capacidad habilitada continúa sujeta al perfil y licencia.

## Alternativas y consecuencias

| Alternativa | Evaluación |
|---|---|
| Parámetros mutables sin historia | Operación inicial sencilla, pero impide explicar decisiones históricas y distinguir fecha conocida de fecha efectiva. |
| Todo en código/forks por cliente | Puede servir para cambios de algoritmo; como regla general encarece la localización común y multiplica releases. |
| Motor genérico de reglas/scripts | Extensibilidad mayor, con superficie de ejecución y riesgo de semántica no controlada; requiere otro ADR y pruebas si se incorpora. |

La decisión favorece reutilización y reproducción, a cambio de un modelo temporal, simulador, validación, permisos y migración de reglas más exigentes. Configurar no evita revisión profesional: Finanzas, Fiscal y Cumplimiento definen aplicabilidad y parámetros reales dentro de sus funciones.

## Criterios de aceptación

1. Un corte histórico reproduce el resultado con fórmula, índice, calendario, tasa, comisión, impuesto y mapeo realmente aplicados.
2. Probar bordes anterior/igual/posterior a vigencia, feriados, cambios de zona y ausencia de versión; no existe selección ambigua.
3. La activación es atómica; concurrencia entre cambio y operación conserva una única versión coherente por operación.
4. Probar caída del plano/scheduler, paquete alterado y versión no aprobada. Las operaciones usan versiones locales válidas o un error/estado permitido y explícito.
5. Recalcular un devengamiento base no crea otro por cambiar `rule_version`; las diferencias se ajustan y concilian con el original.
6. Rollback de configuración no borra contratos, asientos, reportes ni efectos externos ejecutados.

## Revisión y relaciones

Revisar al incorporar fórmulas nuevas, otra jurisdicción, actualización que cambie el significado de datos o una necesidad comprobada de reglas ejecutables. Relacionado con ADR-01, ADR-02, ADR-03, ADR-06 y ADR-08. Una nueva edición normativa necesita análisis de alcance y vigencia; este ADR no congela el derecho aplicable.

Fuentes: [arquitectura, configuración](../achitecture.md#configuracion), [mercado](../market_analysis.md), [cumplimiento](../compliant.md) LAW-06, TAX-01 a TAX-11 según producto, BCRA-T06, BCRA-T17, BCRA-T22 y RPT-08; [controles](../../.agents/skills/core-bancario-argentina/references/controles.md) CTL-02, CTL-06, CTL-12, CTL-15, CTL-18 y CTL-19.

Skill operativo: [adr-05-configuracion-versionada](../../.agents/skills/adr-05-configuracion-versionada/SKILL.md).

## NFR relacionados

[NFR-01](../nfr/NFR-01-integridad-financiera.md), [NFR-09](../nfr/NFR-09-mantenibilidad-configuracion.md), [NFR-11](../nfr/NFR-11-calidad-datos-reportes.md), [NFR-13](../nfr/NFR-13-accesibilidad-experiencia.md). Son cualidades y restricciones a verificar; la elección de este mecanismo no demuestra por sí sola su satisfacción.
