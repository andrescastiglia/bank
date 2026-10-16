# ADR-02: autoridad SQL y escritor financiero único

**Estado:** Propuesto. **Fecha y línea base:** 15/10/2026. **Implementación:** sin evaluar; no se presentan pruebas operativas ejecutadas. La aceptación por la entidad permanece pendiente.

## Contexto

La estrategia comercial propone comenzar por préstamos o una cartera acotada y demostrar confianza mediante saldos explicables, conciliación y coexistencia con sistemas existentes. La propagación eventual permite desacoplar consultas y trabajos, pero no protege por sí sola fondos, restricciones o exposición concurrente. Separar ledger, reservas y límites en autoridades independientes elevaría complejidad, latencia y costo de operación antes de validar el producto.

El núcleo necesita una frontera transaccional por entidad jurídica y celda. Las metas de rendimiento documentadas son hipótesis; ningún benchmark acredita todavía este diseño.

## Decisión

PostgreSQL será la autoridad financiera con un único writer por celda. Contrato/orden, disponibilidad, reserva, exposición, asientos, auditoría, resultado idempotente y outbox cambian en una transacción local cuando pertenecen a la misma operación. Confirmar éxito financiero sólo después del commit durable bajo la política síncrona de ADR-04. Proyecciones, cachés y bus distribuyen información; no conceden fondos.

Aplicar partida doble por entidad y moneda, importes decimales exactos, escala y redondeos explícitos. Conservar fechas de evento, recepción, valor, contabilización y período; registrar versiones de condiciones utilizadas. Correcciones mediante asientos vinculados: no editar historia ni eliminar liquidaciones mediante rollback técnico.

Usar inicialmente `READ COMMITTED`, bloqueos explícitos en orden estable y restricciones de base. Cada cuenta y grupo/línea conserva una fila guardiana: débitos, reservas, mandatos, congelamientos y cambios de límite bloquean el mismo guardián, incluso si aún no existen restricciones. La exposición agregada se mantiene mediante contador/reserva protegido; los predicados no representables requieren serializable y reintento completo acotado. No mantener locks monetarios durante llamadas remotas.

La idempotencia compara clave acotada a entidad y operación con hash canónico. Identidad económica persistente evita duplicación tras vencer una clave de transporte; para devengamientos base es `(entidad, contrato, tipo, período)`, sin versión de regla como escape. Un recálculo genera ajuste vinculado. Exposición compartida con otros cores exige autoridad coordinada o presupuestos reservados cuya suma no exceda el límite, sin conceder nuevamente hasta liberar de forma confirmada.

## Alternativas y consecuencias

- Autoridades separadas con sagas: favorecen despliegue independiente, pero requieren compensaciones y reservas distribuidas; no se eligen para esta frontera.
- Event sourcing como autoridad: facilita reconstrucción, pero añade decisiones de concurrencia, snapshots y operación; el bus actual no es el diario.
- Múltiples primarios: pueden ampliar disponibilidad geográfica, pero exigen consenso y garantías diferentes; no están demostradas.

La decisión simplifica conciliación y transacciones, a cambio de contención en cuentas calientes, dependencia SQL y una frontera de escalado por celda. Medir locks, WAL y capacidad con controles activos; extraer procesos sin fragmentar invariantes.

## Criterios de aceptación

1. Débitos, bloqueo nuevo y cambios de reservas/límite concurrentes producen un orden válido, sin sobregiro ni exposición duplicada; incluir cuenta sin restricciones iniciales y límite de grupo compartido.
2. Inyectar fallo antes/después del commit: ningún asiento parcial y un efecto ante respuesta perdida; misma clave con contenido distinto produce conflicto.
3. Diario, posiciones y reservas concilian por entidad, titular y moneda; vectores de cálculo reproducen redondeo, reglas históricas y devengamiento único ante cambio de versión.
4. Roles no autorizados no alteran diario; toda corrección conserva vínculo y auditoría. Restauración o rollback no elimina pagos liquidados.
5. Medir latencia y contención con carga normal, cuentas calientes y HA efectiva; no declarar capacidad por diseño.

## Revisión, dependencias y trazabilidad

Revisar ante exposición entre celdas, cambio de motor, saturación medida o requerimiento multirregión. Depende de ADR-01, ADR-03, ADR-04, ADR-05 y ADR-08 para fronteras, hechos, durabilidad, reglas y migración.

Fuentes: [arquitectura, §§3–8, 10–11, 16–18](../achitecture.md); [mercado, §§1, 6–9](../market_analysis.md); [cumplimiento](../compliant.md), BCRA-T18/T21/T22/T25, STD01–03/14/31–32; [CTL-01–06, CTL-12/13/15/20](../../.agents/skills/core-bancario-argentina/references/controles.md). Aplicabilidad normativa por entidad; estos mecanismos son decisiones de ingeniería. Usar el [skill ADR-02](../../.agents/skills/adr-02-autoridad-sql/SKILL.md).

## NFR relacionados

[NFR-01](../nfr/NFR-01-integridad-financiera.md), [NFR-05](../nfr/NFR-05-seguridad-accesos.md), [NFR-07](../nfr/NFR-07-auditoria-observabilidad.md), [NFR-10](../nfr/NFR-10-migracion-carga-masiva.md), [NFR-11](../nfr/NFR-11-calidad-datos-reportes.md). Son cualidades y restricciones a verificar; la elección de este mecanismo no demuestra por sí sola su satisfacción.
