# ADR-03: outbox, inbox y procesamiento asíncrono durable

**Estado:** Propuesto. **Fecha y línea base:** 15/10/2026. **Implementación:** sin evaluar; las verificaciones siguientes son criterios pendientes, no resultados operativos. Aceptación institucional pendiente.

## Contexto

La arquitectura prioriza trabajo asíncrono cuando su semántica lo permite: proyecciones, conciliación, reportes, devengamientos y comunicaciones. La estrategia comercial requiere integración y coexistencia confiables a costo operable; reemplazar atomicidad local por dobles escrituras SQL/bus generaría pérdida de hechos o duplicación difícil de explicar. Una cola durable tampoco garantiza cumplir deadlines ni conocer el resultado de un pago cuyo acuse se perdió.

Controles preventivos, restricciones y fondos permanecen en el camino autorizado. Un acuse `202` acredita recepción durable, sin afirmar ejecución o liquidación.

## Decisión

Persistir eventos en outbox dentro de la transacción financiera de ADR-02. Publicadores redundantes reclaman trabajo recuperable, publican y marcan entrega después del acuse del bus. Asumir entrega **al menos una vez**: la caída entre publicación y marcado produce duplicados válidos.

Cada consumidor registra `(consumer_id, entity_id, event_id)` en inbox y su efecto SQL local en la misma transacción; confirma offset sólo después del commit. Si invoca correo, webhook o tercero, persiste una outbox de entrega e intentos durables. No atribuir atomicidad SQL/red ni prometer exactly-once por usar transacciones Kafka.

El envelope incluye entidad, identificador estable, tipo/versión, agregado, secuencia, correlación, causalidad y tiempos; importes decimales como strings. Validar esquemas y compatibilidad. Particionar por entidad/agregado; asignar secuencia con la operación. Preservar orden o detectar huecos antes de aplicar efectos dependientes. No existe orden global entre particiones.

Workers mantienen estado, intentos, checkpoint, deadline, dueño y próxima ejecución. Un lease/token condiciona cambios locales, pero no detiene físicamente un envío remoto de un proceso rezagado. Registrar intención antes del envío y considerar ambiguo cualquier intento potencialmente ejecutado sin respuesta. Usar referencia idempotente homologada, consulta y conciliación; sin deduplicación/fencing remoto, aislar el worker anterior y resolver el intento antes de reenviar. No liberar reservas ambiguas por TTL.

Separar pools y prioridades; medir edad, plazo restante, espacio y tasa efectiva. DLQ exige responsable y resolución: no suspende obligaciones. Replay usa namespace independiente y suprime efectos externos históricos. Minimizar datos; segregar AML/ROS, PII, DLQ y archivo según permisos/retención. El bus no sustituye ledger ni archivo legal.

## Alternativas y consecuencias

- Publicación síncrona doble SQL/bus: menor infraestructura inicial, pero ventana de inconsistencia; descartada.
- Transacción distribuida: agrega coordinación y acopla disponibilidad; no cubre universalmente terceros.
- Garantías exclusivas del broker: útiles dentro de su alcance, insuficientes para SQL y rieles.

La decisión desacopla latencia y permite recuperación, a cambio de duplicados esperados, almacenamiento adicional, reconciliación y operación de backlog. La outbox permite continuidad acotada ante caída del bus, hasta capacidad segura o deadline/control dependiente; no justifica acumulación ilimitada ni descarte.

## Criterios de aceptación

1. Caídas entre commit, publicación, marcado, inbox y offset no pierden hechos ni duplican efectos financieros; payload/evento inválido queda visible, sin falso éxito funcional.
2. Eventos duplicados/desordenados detectan secuencias y huecos; proyección reconstruida concilia con la autoridad y replay no dispara desembolsos, ROS ni notificaciones históricos.
3. Timeout, callback tardío, lease vencido y worker rezagado no causan reenvío ciego ni liberación indebida; registrar resolución externa y conciliación.
4. Backlog bajo carga y caída del broker produce alarmas antes de agotar capacidad/plazo; DLQ conserva dueño, antigüedad y reejecución trazable.
5. Restauración conjunta SQL/bus/inbox compara watermarks y referencias externas antes de reabrir; ningún offset arbitrario elimina pendientes.

## Revisión, dependencias y trazabilidad

Revisar ante nuevo riel, semántica de entrega distinta, crecimiento del backlog, cambio de particionado o motor de workflows. Depende de ADR-02, ADR-04, ADR-06 y ADR-07.

Fuentes: [arquitectura §§4, 6–8, 10, 12–15](../achitecture.md); [mercado §§1, 6, 9](../market_analysis.md); [cumplimiento](../compliant.md), BCRA-T06/T18/T21/T22, PAY aplicable, STD10/14/17/27/32; [CTL-04–06/08/10–15/19](../../.agents/skills/core-bancario-argentina/references/controles.md). Usar el [skill ADR-03](../../.agents/skills/adr-03-outbox-inbox/SKILL.md); verificar alcance normativo por entidad y riel.

## NFR relacionados

[NFR-01](../nfr/NFR-01-integridad-financiera.md), [NFR-04](../nfr/NFR-04-asincronia-durable.md), [NFR-07](../nfr/NFR-07-auditoria-observabilidad.md), [NFR-08](../nfr/NFR-08-interoperabilidad-portabilidad.md), [NFR-11](../nfr/NFR-11-calidad-datos-reportes.md), [NFR-13](../nfr/NFR-13-accesibilidad-experiencia.md). Son cualidades y restricciones a verificar; la elección de este mecanismo no demuestra por sí sola su satisfacción.
