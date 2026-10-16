---
name: adr-03-outbox-inbox
description: "Usar al diseñar, implementar o revisar eventos y trabajos asíncronos del core: outbox/inbox, entrega al menos una vez, idempotencia, orden por agregado, reintentos, DLQ, replay y pagos externos ambiguos; aplica ADR-03."
---

# ADR-03: asincronía durable y efectos únicos

## Propósito y entradas

Diseñar y verificar asincronía recuperable sin perder hechos financieros ni repetir sus efectos. La línea base del **15/10/2026** es propuesta; documentación y mecanismos no prueban implementación ni cumplimiento.

Determinar modo —diseñar, implementar o revisar—, flujo/producto/entidad, origen del hecho, destinatario, necesidad de respuesta inmediata, deadline, estado duradero y consecuencias de duplicación. Obtener transacciones SQL, broker, contratos/esquemas, particionado, política de idempotencia, capacidad, referencias externas y evidencia disponible. Identificar qué soporta realmente cada tercero: deduplicación, consulta, callback autenticado y fencing. Explicitar supuestos y avanzar en trabajo reversible si falta información; solicitar sólo datos que cambian la solución.

Mantener preventivos de fondos, permisos, restricciones y riesgo exigibles antes de ejecutar. `202` comunica recepción durable con `operation_id` y consulta de estado; no declara liquidación. SQL es autoridad financiera; cola y proyección no autorizan gasto.

## Procedimiento adaptable

### Diseñar el flujo

1. Describir fronteras: comando/commit financiero, outbox, broker, inbox/efecto local y cualquier entrega externa. Enumerar puntos de caída y quién reconcilia. Persistir outbox con la operación, auditoría y resultado idempotente; nunca confirmar dinero sujeto al éxito de un segundo publish independiente.
2. Definir publicador recuperable. Reclamar mediante estado durable/compare-and-set; publicar con identificador estable y marcar después del acuse. Asumir duplicado cuando cae entre ambos pasos.
3. Por consumidor, insertar unicidad `(consumer_id, entity_id, event_id)` y efecto local en una transacción. Offset se confirma después del commit. Si necesita llamar a red, crear outbox de entrega local e intento durable; SQL y una llamada externa no comparten atomicidad.
4. Definir envelope: entidad, id estable, tipo/esquema/versión, agregado/secuencia, correlación/causalidad y tiempo; decimal como string con moneda/escala. Asignar secuencia junto a la operación y particionar por entidad/agregado. Preservar orden o detectar huecos y esperar/reconstruir; no inferir orden global.
5. Especificar jobs con estado, checkpoint, intento, deadline, próximo intento y responsable. Separar confirmaciones, AML/fraude, devengamientos, reportes y comunicaciones; dimensionar tasa/conexiones y capacidad reservada. Escalar por edad/plazo restante además de CPU/profundidad.

Comparar alternativas por disponibilidad, costo operativo, duplicados y conciliación. Las transacciones del broker no garantizan exactly-once entre PostgreSQL y un riel; no introducir coordinación distribuida sin necesidad demostrada.

### Implementar el cambio

Inspeccionar código y convenciones; extender transacciones existentes y contratos compatibles. Crear restricciones/índices, publisher, inbox, máquinas de estado y métricas dentro del alcance solicitado. No simular integración homologada ni inventar respuestas del tercero. Errores transitorios seguros usan backoff con jitter y límites de tiempo/intentos; errores de autorización o formato requieren corrección.

Para un envío externo persistir intención y referencia antes de invocar. Ante pérdida de respuesta tratar como `UNKNOWN`/`PENDING_CONFIRMATION` y consultar/conciliar antes de repetir. Callback autenticado se guarda duraderamente antes del acuse y produce comando idempotente con transición válida. Un lease/época sólo limita escrituras locales: un proceso rezagado puede seguir enviando. Si el destino no deduplica ni reconoce fencing, aislar el emisor anterior y resolver el intento potencial según el riel; vencer el lease no concede permiso de reenvío. Tampoco un TTL libera reservas de resultado ambiguo.

Mantener DLQ/cuarentena con dueño, motivo, antigüedad, datos protegidos y reejecución trazable. Un mensaje en DLQ sigue pendiente funcionalmente y no detiene reloj legal/contractual. Alertar antes del deadline y del agotamiento de disco/outbox; aplicar backpressure a operaciones afectadas sin borrar pendientes. Fallo de notificación no modifica asiento.

### Revisar o reconstruir

Seguir un hecho desde commit hasta efecto y conciliación; verificar estados reales, permisos y offsets. Buscar acuses prematuros, dobles escrituras, reintentos ciegos, huecos de secuencia, colas sin deadline y payload excesivo. En replay usar consumidor/namespace específico, checkpoints y comparación de totales; inhibir efectos históricos externos, incluidos pagos, ROS, correos y webhooks. Para restauración comparar SQL, outbox, inbox, broker, jobs e intentos/terceros; aislar eventos posteriores al punto restaurado antes de reabrir. No elegir offsets arbitrarios para aparentar avance.

## Invariantes y pruebas relevantes

Entrega al menos una vez requiere deduplicación local y unicidad financiera histórica. Bus es transporte, no ledger ni archivo legal único. Separar permisos y retención de eventos, DLQ, backups y trazas; AML obtiene hechos completos autorizados, sin ROS/legajos en topics generales. CloudEvents define formato, no autenticidad.

En cambios materiales inyectar caída entre commit/publish/marcado, entre inbox/efecto/offset y antes/después de envío externo. Probar duplicado, payload incompatible, secuencia invertida/hueco, callback tardío, worker rezagado y reserva ambigua vencida. Probar broker caído/backlog, deadline/DLQ, replay sin efectos y restauración con SQL/bus desalineados. Conciliar operaciones esperadas/aplicadas, edad y pendientes; en fase de diseño entregar casos pendientes, sin atribuirles resultados.

## Salida y trazabilidad

Entregar diseño, implementación o hallazgos según pedido, con estados/transacciones, garantías y límites; matriz `escenario → CTL → evidencia observada → estado/brecha`, métricas y siguiente acción. Registrar versiones y resultados concretos; distinguir `propuesto`, `implementado sin evidencia`, `verificado en alcance` y `brecha`. Registrar desviaciones sin bloquear tareas reversibles.

Referencias opcionales: [ADR-03](../../../docs/adr/ADR-03-outbox-inbox.md), [arquitectura §§4, 6–8, 10, 12–15](../../../docs/achitecture.md), [mercado](../../../docs/market_analysis.md) y [cumplimiento](../../../docs/compliant.md). Mapear CTL-04–06/08/10–15/19, BCRA-T06/T18/T21/T22 y STD10/14/17/27/32; usar [core-bancario-argentina](../core-bancario-argentina/SKILL.md) para aplicabilidad/actualización. No afirmar certificación por adoptar el patrón.
