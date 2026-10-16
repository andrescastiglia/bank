# NFR-02 — Disponibilidad y recuperación coherente

**Estado:** Propuesto. **Línea base:** 15/10/2026. **Responsables por designar:** Operaciones, negocio y continuidad. **Efectividad:** no evaluada.

El servicio debe permanecer utilizable y recuperar su estado financiero coherente ante fallos declarados. Incluye identidad, claves, red, documentos, jobs, base, mensajería y rieles. Los objetivos siguientes son hipótesis para el piloto; el BIA y el perfil contratado deben validarlos. No son cifras impuestas universalmente por BCRA.

## Criterios de aceptación

| ID | Métrica, unidad y ventana | Objetivo y escenario | Fuente |
|---|---|---|---|
| NFR-02-C01 | Solicitudes válidas atendidas correctamente / total válido; % mensual por entidad/endpoint | ≥99,95 % API monetaria local; mantenimiento obstructivo consume presupuesto; rechazo de negocio correcto es respuesta válida | Arquitectura §11 |
| NFR-02-C02 | Tiempo hasta redistribución; segundos por ensayo | ≤30 s al caer un proceso, sin perder trabajo aceptado, con dependencias operativas | Arquitectura §10 |
| NFR-02-C03 | RTO y commits reconocidos perdidos; segundos y cantidad por ensayo | ≤120 s y 0 ante pérdida de writer/zona, sólo con persistencia síncrona remota efectiva, réplica elegible, aislamiento del primario anterior y capacidad probados | Arquitectura §10 |
| NFR-02-C04 | RTO; minutos por ensayo regional; retraso durable; segundos observados | ≤60 min en piloto; lag operativo objetivo ≤60 s. RPO regional real se mide sobre el último estado recuperado, sin garantía de 60 s | Arquitectura §10 |
| NFR-02-C05 | RTO; horas por restauración | ≤4 h preliminares para corrupción/ransomware y volumen piloto, condicionado a copia limpia, llaves y conciliación | Arquitectura §10 |
| NFR-02-C06 | Efectos duplicados, saldos incoherentes o hechos huérfanos aplicados; cantidad por reapertura | 0; reconciliar punto financiero, mensajes y riel antes de habilitar operación | Arquitectura §10; CTL-13 |

El indicador temporal por canarios se informa separado: 99,95 % equivale a **21 min 36 s** de indisponibilidad en 30 días. No convertir esa equivalencia en medición por solicitudes. El RTO comprende restablecimiento validado del servicio, no sólo promoción de una base.

## Validación y evidencia

Ensayar proceso, partición, zona, región y copia limpia con carga representativa. Registrar hitos, commits reconocidos, último punto durable, operaciones externas y pérdida observada. Aislar eventos del broker posteriores a una restauración SQL; reconciliar inbox/offsets sin replay de efectos históricos. Un backup existente o un failover rápido no demuestran continuidad integral.

## Dependencias y revisión

[Arquitectura](../achitecture.md#disponibilidad), [ADR-04](../adr/ADR-04-alta-disponibilidad.md), [ADR-03](../adr/ADR-03-outbox-inbox.md), [ADR-07](../adr/ADR-07-stack-gestionado.md), CTL-13/14/16. Revisar BIA, dependencia, región, volumen y compromiso comercial antes de producción y después de incidentes o cambios materiales.

Skill operativo: [nfr-02-disponibilidad-recuperacion](../../.agents/skills/nfr-02-disponibilidad-recuperacion/SKILL.md).
