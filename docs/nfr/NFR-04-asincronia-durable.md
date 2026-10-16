# NFR-04 — Asincronía durable y oportuna

**Estado:** Propuesto. **Línea base:** 15/10/2026. **Responsables por designar:** Integraciones y Operaciones. **Efectividad:** no evaluada.

El trabajo demorable debe conservarse, reanudarse y producir el efecto correcto dentro de su plazo. Abarca publicación, proyecciones, cálculos, conciliación, reportes y entregas externas. Autorización, fondos, restricciones y controles preventivos exigibles mantienen su decisión antes del efecto financiero. Una respuesta `202` sólo acredita la aceptación durable definida.

## Criterios de aceptación

| ID | Métrica, unidad y ventana | Objetivo y escenario | Fuente |
|---|---|---|---|
| NFR-04-C01 | Trabajos aceptados sin estado recuperable; cantidad por fallo y conciliación | 0 al caer proceso, publicador o consumidor en cualquier frontera de confirmación | Arquitectura §7/8 |
| NFR-04-C02 | Efectos locales/financieros duplicados o efectos externos históricos reenviados; cantidad por reentrega/replay | 0; toda intención externa ambigua conserva referencia y resolución verificable | Arquitectura §6/7; CTL-04 |
| NFR-04-C03 | Antigüedad commit–publicación y commit–proyección utilizable; segundos, p99 por ensayo normal | ≤5 s para publicación/proyección ordinaria; registrar ambos trayectos, sin sustituirlos por profundidad de cola | Arquitectura §11 |
| NFR-04-C04 | Flujos con deadline y dueño explícitos / flujos sujetos a plazo; % por inventario | 100 %; plazo legal/contractual por flujo y alerta antes del vencimiento. No existe presupuesto universal de 5 s para todos | Arquitectura §8/15 |
| NFR-04-C05 | Faltantes, duplicados y excepciones sin decisión; cantidad por cierre | 0 al declarar cierre completo; comparar universo esperado, resultados y ajustes, no sólo jobs terminados | Arquitectura §8; CTL-05/06/19 |
| NFR-04-C06 | Eventos fuera de secuencia aplicados incorrectamente y pendientes borrados para liberar capacidad; cantidad por ensayo | 0 con huecos, reordenamiento o bus caído; conservar backlog y restringir antes del agotamiento seguro | Arquitectura §7/8 |

## Validación y evidencia

Inyectar caída después de publicar y antes de marcar, commit local previo al acuse, lease vencido con worker rezagado, evento inválido y recuperación con backlog. El vencimiento de un lease local no impide llamadas externas del proceso anterior ni autoriza reenvío. Medir edad máxima, p99, tasa efectiva y margen al deadline; cuantificar recuperación bajo la capacidad acordada. DLQ conserva responsabilidad y reloj. Una restauración debe detectar divergencias entre punto financiero, broker e inbox antes de reanudar.

## Dependencias y revisión

[Arquitectura: asincronía](../achitecture.md#asincronia), [ADR-03](../adr/ADR-03-outbox-inbox.md), [ADR-04](../adr/ADR-04-alta-disponibilidad.md), CTL-04/05/13/14/19. Revisar al incorporar riel, obligación, consumidor, versión de evento o volumen. Los plazos exigibles requieren determinar sujeto/producto y fuente vigente; la durabilidad documental no acredita cumplimiento.

Skill operativo: [nfr-04-asincronia-durable](../../.agents/skills/nfr-04-asincronia-durable/SKILL.md).
