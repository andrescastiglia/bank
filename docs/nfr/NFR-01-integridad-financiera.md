# NFR-01 — Integridad financiera

**Estado:** Propuesto. **Línea base:** 15/10/2026. **Responsables por designar:** Finanzas y líder del núcleo. **Efectividad:** no evaluada; no existe evidencia de implementación.

Este requisito exige exactitud, unicidad y consistencia de los efectos monetarios, independientemente del motor, lenguaje o patrón elegido. Abarca comandos, reservas, restricciones, límites, devengamientos, ajustes, integraciones y carga inicial. El perfil comercial acotado facilita demostrar estas propiedades antes de ampliar el catálogo.

## Criterios de aceptación

La ventana es cada ejecución y cada corte conciliado; la tolerancia propuesta es cero para errores monetarios materiales. Los vectores de cálculo deben tener resultados aprobados por responsables financieros.

| ID | Métrica y unidad | Objetivo y escenario | Fuente |
|---|---|---|---|
| NFR-01-C01 | Operaciones desbalanceadas por entidad/moneda; cantidad | 0 tras contabilización, reverso, importación o recuperación; no compensar monedas ni titulares | Arquitectura §5; CTL-01/05 |
| NFR-01-C02 | Efectos económicos adicionales por identidad; cantidad | 0 ante reintentos, callback duplicado, replay y pérdida de respuesta; devengamiento único por entidad/contrato/tipo/período, sin incluir versión de regla en su identidad | Arquitectura §5/8; CTL-04 |
| NFR-01-C03 | Sobregiros no autorizados o restricciones/límites omitidos; cantidad | 0 con dos débitos, alta concurrente de embargo/reserva o consumos de línea/grupo | Arquitectura §5; CTL-03 |
| NFR-01-C04 | Diferencia respecto de vector histórico aprobado; unidad monetaria exacta | 0 en interés, comisión, impuesto y redondeo por regla/moneda/fecha; reversos preservan originales | Arquitectura §5/9; CTL-02/06 |
| NFR-01-C05 | Éxitos financieros sin commit durable y confirmaciones finales externas sin evidencia del riel; cantidad por clase | 0 ante fallo de commit, timeout y confirmación tardía; sólo exigir evidencia externa cuando interviene un riel. `202`/acuse acredita recepción durable, no confirmación financiera final; ambigüedad conserva estado/reserva y caso | Arquitectura §§5–6; CTL-04/05 |

## Validación y evidencia

Construir muestras sintéticas con saldos insuficientes, cuentas concentradoras, dos monedas, bisiesto, fin de período y cambios de regla. Comparar comandos aceptados, diario, posiciones, reservas, exposición, custodia y manifiesto esperado por titular. Inyectar fallos antes/después del commit y del envío externo. Conservar semilla, versión, intercalado concurrente, resultado esperado/observado y conciliación; un saldo global correcto no prueba todos los criterios.

## Dependencias y revisión

[Arquitectura: consistencia](../achitecture.md#consistencia), [ADR-02](../adr/ADR-02-autoridad-sql.md), [ADR-03](../adr/ADR-03-outbox-inbox.md), [CTL-01 a CTL-06](../../.agents/skills/core-bancario-argentina/references/controles.md). Revisar al cambiar producto, fórmula, concurrencia, identidad económica o migración. BCRA-T21 fundamenta el riesgo de integridad; estos mecanismos y objetivos no equivalen a una certificación normativa.

Skill operativo: [nfr-01-integridad-financiera](../../.agents/skills/nfr-01-integridad-financiera/SKILL.md).
