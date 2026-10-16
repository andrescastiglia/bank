# NFR-10 — Migración y carga masiva verificables

**Estado:** Propuesto. **Línea base:** 15 de octubre de 2026. **Responsables propuestos:** Migración, Finanzas, Operaciones y Seguridad. Objetivos pendientes de ensayo y alcance aprobado.

## Alcance y motivación

Carga inicial y coexistencia por cohorte: extracción, transferencia, staging, validación, aplicación, conciliación, corte y retorno. Su demostración reduce riesgo comercial y permite estimar TCO. Este NFR especifica calidad/desempeño; ADR-08 define el mecanismo bulk.

## Criterios medibles

| ID | Métrica y unidad | Ventana/escenario | Objetivo propuesto | Fuente |
|---|---|---|---|---|
| NFR-10-C01 | Duración, horas; registros válidos y operaciones financieras validadas/s | Ensayo completo con población y carga coexistente representativas | Total ≤ ventana aprobada: extracción + transferencia + carga + validación + aplicación + conciliación + corte + margen; tasas medidas, sin mínimo inventado | Arquitectura §16.2; mercado §§8–9 |
| NFR-10-C02 | Diferencias inexplicadas, cantidad/importe por moneda | Cada corrida antes de activar; titular, contrato, producto, entidad y mayor | Cero; conteos, saldos, intereses, mora, reservas, restricciones y documentos conciliados; redondeos explicados/aprobados | CTL-01–06, CTL-20 |
| NFR-10-C03 | Objetos/asientos duplicados o transacciones fuente incompletas aplicadas, cantidad | Reinicio, chunk repetido y nueva corrida/revisión | Cero; checkpoints verificables y unicidad económica entre corridas; aplicación sólo de transacciones fuente completas | Arquitectura §16.2; CTL-04, CTL-20 |
| NFR-10-C04 | Posiciones contabilizadas dos veces, cantidad | Apertura versus historia completa | Cero; elegir un modo por cartera, reconstruir corte y conservar consulta histórica | Arquitectura §16.3; CTL-01, CTL-19–20 |
| NFR-10-C05 | Datos preparados expuestos a operación ordinaria y efectos históricos emitidos, cantidad | Antes de activar: consultas de negocio, mayor/RI y conciliación operativos, consumidores corrientes | Cero; permitir validación y conciliación autorizadas del paquete de migración aislado, sin pagos, cobros, avisos o ROS históricos como nuevos | Arquitectura §§16.4–16.5; CTL-08, CTL-19–20 |
| NFR-10-C06 | Contratos con doble autoridad o deltas faltantes, cantidad | Corte con operaciones en vuelo, watermark y barrera verificables | Cero; sin barrera, ventana de suspensión explícita; activación incompleta denegada | Arquitectura §16.4; CTL-03–05, CTL-20 |
| NFR-10-C07 | Resultado de cada SLO según métrica/ventana/denominador; controles críticos desactivados, cantidad | Ensayo de carga coexistente y réplica atrasada; separar período de ensayo y ventana del SLO | Cumplir objetivo y presupuesto del perfil con evidencia del período medido, sin inferir SLO mensual de una muestra corta; 0 controles críticos desactivados. No convertir disponibilidad 99,95 % en tolerancia cero a cualquier error individual | Arquitectura §§11, 16.2; CTL-12–13 |
| NFR-10-C08 | Operaciones posteriores al corte sin conciliar/trasladar, cantidad | Ensayo de retorno después de activar y operar | Cero; preservar liquidaciones reales y recuperar mediante retorno conciliado/correcciones, sin borrar lotes activos | Arquitectura §16.5; CTL-05, CTL-13, CTL-20 |

## Aceptación, dependencias y evidencia

Conservar manifiesto/hash, población esperada, mapeos/versiones, rechazos, checkpoints, mediciones, conciliaciones y ensayo de retorno. Ninguna carga terminada equivale a aceptación financiera. Sin ventana o snapshot consistente, registrar dependencia pendiente.

[Carga inicial](../achitecture.md#carga-inicial), [ADR-08](../adr/ADR-08-carga-inicial-masiva.md), [mercado/TCO](../market_analysis.md), [cumplimiento](../compliant.md#bcra-tecnologia). Aplican CTL-01–06, CTL-08, CTL-11–13, CTL-19–20 y STD14; vincular cada obligación según entidad/producto.

Skill operativo: [nfr-10-migracion-carga-masiva](../../.agents/skills/nfr-10-migracion-carga-masiva/SKILL.md).
