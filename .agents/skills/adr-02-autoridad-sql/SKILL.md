---
name: adr-02-autoridad-sql
description: "Usar al diseñar, implementar o revisar la autoridad SQL del core: transacciones monetarias, partida doble, saldos, reservas, restricciones, límites compartidos, idempotencia y concurrencia; aplica ADR-02 sin atribuir al bus ni a una caché autoridad sobre fondos."
---

# ADR-02: autoridad SQL del núcleo financiero

## Propósito, alcance y entradas

Preservar una autoridad financiera por entidad y celda, con writer SQL único y transacciones locales que mantienen las invariantes económicas. La línea base del **15/10/2026** es un diseño propuesto; no acredita aceptación institucional, implementación, rendimiento ni cumplimiento demostrado.

Identificar modo solicitado —diseñar, implementar o revisar—, producto, entidad, moneda, semántica de saldo utilizable, cuentas puente, límites, restricciones y autoridad actual. Obtener operación/cambio concreto, esquema y código disponibles, política de aislamiento/durabilidad, idempotencia, versiones y evidencia. Si faltan datos, explicitar supuestos y avanzar con modelos o cambios reversibles; consultar sólo información que cambie materialmente la solución.

La autoridad incluye contrato/orden, posición, reserva y exposición que comparten una operación. Una transferencia entre entidades/celdas requiere operaciones vinculadas y liquidación explícita; no prometer atomicidad entre sus bases. Un saldo de proyección se presenta con fecha y retraso y no autoriza gasto.

## Procedimiento según el pedido

### Diseñar

1. Dibujar flujo de fondos y frontera: qué filas protegen cada invariante y qué núcleo decide. Definir partida doble por entidad/moneda, cuentas transitorias y semántica de autorización, reserva, contabilización y liquidación.
2. Definir transacción: verificar identidad/entidad y autorización; reclamar clave idempotente y comparar hash canónico; bloquear guardianes en orden determinista; revalidar restricciones, fondos, vigencia y límites; modificar estado; insertar asientos, auditoría y outbox; guardar resultado; commit durable; responder estado alcanzado.
3. Asignar guardián estable por cuenta y grupo/línea. Toda creación/modificación de reserva, mandato, bloqueo o límite toma ese mismo lock, aunque no haya una restricción previa. Proteger contadores de exposición en la misma transacción. Si un predicado no puede representarse así, proponer serializable con reintentos acotados.
4. Para exposición distribuida entre cores, definir una autoridad común o presupuestos previamente reservados, de suma acotada al límite. Documentar reserva, vencimiento, conciliación y liberación confirmada; una agregación eventual no concede capacidad.
5. Definir exactitud, temporalidad, identidades económicas y roles SQL. Contrastar alternativas con latencia, contención, costo y dificultad de conciliación; entregar diseño verificable y decisiones pendientes.

### Implementar

Inspeccionar primero convenciones y dependencias del repositorio. Adaptar el cambio al esquema existente; no crear un ledger paralelo. Mantener las modificaciones monetarias dentro del comando transaccional común, incluidas importaciones autorizadas. Usar migraciones versionadas, restricciones únicas y procedimientos/roles que impidan escritura arbitraria del diario. No llamar a rieles o motores remotos dentro de la transacción con locks; obtener decisiones antes y revalidar localmente referencia, vencimiento y estado.

Conservar clave, hash, identificador de operación y resultado estable. Un reintento con contenido distinto se rechaza como conflicto; una respuesta perdida se resuelve consultando la operación. La caducidad de la clave de transporte no elimina la unicidad económica histórica. Para devengamiento base usar `(entity_id, contract_id, accrual_type, business_period)`; versión de regla es atributo. Un recálculo compara y genera ajuste vinculado, sin repetir el devengamiento original.

Aplicar decimal exacto/enteros escalados, moneda y escala declaradas; precisión intermedia y redondeo aprobados. Separar instantes UTC de fecha de negocio/calendario, conservar versiones de contrato y cálculo. Resolver deadlocks o abortos con reintento completo acotado y misma identidad; nunca convertirlos en otro envío externo.

### Revisar

Seguir una operación de extremo a extremo: autorización, commit, reserva/asiento, outbox y conciliación. Identificar lecturas atrasadas, locks incompletos, claves débiles y caminos alternativos de escritura. Evaluar configuración efectiva, código y evidencia según estén disponibles. Entregar hallazgos con escenario reproducible, efecto financiero, archivo/ubicación, control y corrección concreta; distinguir ausencia de evidencia de defecto demostrado. Corregir dentro del alcance autorizado cuando se solicite, registrando desviaciones sin paralizar análisis reversible.

## Invariantes y verificación material

- Débitos y créditos cuadran por entidad/moneda; no compensar ARS con USD. Reservas y restricciones prevalecen según semántica aprobada, sin gasto ni exposición duplicados.
- Asientos contabilizados no se editan/borran por negocio. Corrección exige nuevo asiento, motivo, vínculo y facultad; rollback técnico no deshace liquidación externa.
- Operación, cambios de posición/reserva/límite, auditoría, outbox y resultado idempotente son atómicos cuando pertenecen a la misma frontera.
- Confirmar éxito después de durabilidad efectiva del writer y réplica síncrona según perfil; detener escritura afectada si esa política no puede sostenerse. Failover/fencing corresponde también a ADR-04.

En implementación material probar débitos simultáneos, inserción concurrente de bloqueo inicialmente inexistente, reserva contra pago, límite de grupo y cuentas calientes. Inyectar caída antes/después del commit y pérdida de respuesta; repetir payload igual/distinto y reintento tardío. Probar redondeos, período cerrado, cambio de regla sin duplicar devengo, reversos, acceso SQL denegado y conciliación. Medir contención con controles activos. En diseño entregar estos casos como plan, sin afirmar ejecución.

## Salida y fuentes

Entregar artefacto pedido, frontera/invariantes, alternativas o cambios, matriz `escenario → CTL → evidencia → resultado/brecha`, riesgos y próxima acción. Registrar versión, configuración, datos sintéticos y resultado observado; usar estados `propuesto`, `implementado sin evidencia`, `verificado en alcance` o `brecha` según corresponda.

Referencias opcionales: [ADR-02](../../../docs/adr/ADR-02-autoridad-sql.md), [arquitectura §§3–8, 10, 16–18](../../../docs/achitecture.md), [mercado](../../../docs/market_analysis.md) y [cumplimiento](../../../docs/compliant.md). Trazar CTL-01–06/12/13/15/20, BCRA-T18/T21/T22/T25 y STD01–03/14/31–32 según aplicabilidad; usar [core-bancario-argentina](../core-bancario-argentina/SKILL.md) para fuente vigente y jerarquía. Este mapeo no certifica conformidad.
