# NFR-03 — Latencia y capacidad con controles activos

**Estado:** Propuesto. **Línea base:** 15/10/2026. **Responsables por designar:** Ingeniería y Operaciones con cliente de diseño. **Efectividad:** no evaluada; no son benchmarks.

El núcleo debe responder dentro del presupuesto correspondiente bajo un perfil reproducible, manteniendo integridad, autorización, persistencia y aislamiento. El universo hipotético es de 250.000 cuentas/contratos; las cifras nacionales de pagos y el promedio del modelo comercial no determinan TPS del cliente.

## Criterios de aceptación

Medir desde ingreso al gateway hasta respuesta completa. Calcular percentiles sobre observaciones del trayecto, sin sumarlos entre componentes; documentar calentamiento, errores, cardinalidad y tamaño de muestra. La red pública y las dependencias externas llevan medición adicional.

| ID | Métrica, unidad y ventana | Objetivo y escenario | Fuente |
|---|---|---|---|
| NFR-03-C01 | Latencia p95/p99; ms en cada ensayo | Saldo consistente ≤50/100, autorización incluida | Arquitectura §11 |
| NFR-03-C02 | Latencia p95/p99; ms en cada ensayo | Transferencia interna ≤100/200, con contención y commit durable | Arquitectura §11 |
| NFR-03-C03 | Latencia p95/p99; ms en cada ensayo | Aceptación de trabajo demorable ≤75/150, solicitud durable; no implica finalización | Arquitectura §11 |
| NFR-03-C04 | Carga ofrecida/completada; comandos/s y lecturas/s durante 60/10 min | Sostener 100 comandos/s por 60 min y pico de 500/s por 10 min, junto con hasta 1.000 lecturas/s; 50 % transferencias internas/50 % aceptación externa y 50 % lecturas consistentes/50 % proyecciones | Arquitectura §11 |
| NFR-03-C05 | Percentiles, errores, saturación y backlog; ms, %, recursos y edad por ensayo adverso | Informar resultados con cuenta caliente, un año de crecimiento, batch y pérdida de zona; presupuestos degradados pendientes de validación, sin ocultar incumplimientos | Arquitectura §10/11 |

Para decisiones con tercero, fijar el plazo por riel/servicio y medir extremo a extremo; no aplicar el objetivo local a toda la transferencia externa. Los errores y timeouts permanecen visibles: una respuesta rápida incorrecta no satisface el requisito.

## Validación y evidencia

Usar generador de carga con tasa ofrecida controlada y latencias que incluyan espera; evitar omitir solicitudes durante saturación. Conservar dataset sintético, distribución de saldos, historial, configuración, recursos/costo, trazas, histogramas y conciliación antes/después. Reportar filas calientes, esperas, pools, persistencia y amplificación de asientos/eventos; no desactivar controles para mejorar resultados.

## Dependencias y revisión

[Arquitectura: rendimiento](../achitecture.md#rendimiento), [ADR-02](../adr/ADR-02-autoridad-sql.md), [ADR-04](../adr/ADR-04-alta-disponibilidad.md), [ADR-07](../adr/ADR-07-stack-gestionado.md), CTL-03/13/17 y STD14. Revisar al contratar volumen, cambiar mezcla, retención, infraestructura o perfil. Capacidad prometida y costo comercial requieren evidencia del escenario contratado.

Skill operativo: [nfr-03-latencia-capacidad](../../.agents/skills/nfr-03-latencia-capacidad/SKILL.md).
