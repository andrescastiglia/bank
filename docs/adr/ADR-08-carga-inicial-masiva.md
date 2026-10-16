# ADR-08: carga inicial masiva y activación controlada

**Estado:** Propuesto, pendiente de aceptación institucional y ensayos. **Línea base:** 15/10/2026. **Alcance:** diseño; no existe evidencia de un importador ejecutado. **Skill asociado:** [adr-08-carga-inicial-masiva](../../.agents/skills/adr-08-carga-inicial-masiva/SKILL.md).

## Contexto

El usuario requiere bulk insert o equivalente para la implementación. La [estrategia comercial](../market_analysis.md) prioriza préstamos/carteras acotadas, coexistencia y migración con diferencias explicables. Exigir llamadas HTTP por registro encarece la carga; insertar directamente saldos operativos omite controles y expone cohortes incompletas. La velocidad útil incluye validación, conciliación y corte, no sólo filas cargadas.

## Decisión propuesta

Adoptar [staging durable, aplicación por conjuntos y publicación controlada](../achitecture.md#carga-inicial). `COPY FROM STDIN` carga columnas explícitas en staging logged aislado por entidad/corrida, con rol mínimo, sin SQL del cliente, `COPY PROGRAM` ni acceso arbitrario al servidor. Si RLS impide COPY, usar inserciones autorizadas compatibles o staging dedicado; no desactivarla para cargar.

Cada `import_run_id` fija origen, entidad, cohorte, snapshot/watermark, modo histórico, esquema/mapeo, responsables, hashes de archivos/chunks, conteos y totales por titular/producto/moneda. Reanudar conserva manifiesto/checksum; contenido distinto genera revisión vinculada e invalida aprobación. La unicidad financiera `(entity_id, source_system, source_record_id, record_type)` rige **entre corridas**, además del checkpoint de chunk. Duplicados requieren comparación de contenido; no basta `ON CONFLICT DO NOTHING`.

El importador set-based aplica invariantes del dominio: decimal exacto, titularidad, relaciones, restricciones, reservas, límites, cronogramas y partida doble. Respeta cada transacción económica completa del origen, aunque sus filas crucen chunks. Avanza checkpoint autoritativo sólo al completarla. Usa lotes atómicos y reanudables; mantiene WAL, `fsync`, replicación síncrona, restricciones y auditoría. Throttling preserva HA y SLO de cohortes activas.

Elegir por cartera **apertura conciliada** con historia previa consultable, o **historia completa** que reconstruye la posición. Son mutuamente excluyentes para los mismos fondos: no contabilizar ambos. Finanzas define fecha, cuenta técnica y tratamiento documentado de diferencias.

La generación preparada —`PREPARED`, frontera lógica correspondiente a READY/APPLYING/RECONCILING/APPROVED, no un nuevo estado de API— queda fuera de autorizaciones, saldos operativos, mayor, RI, conciliación ordinaria y eventos corrientes. Sus totales se controlan como paquete separado; proyecciones/consumidores también respetan la frontera. La activación cambia una referencia/época de cohorte en una transacción pequeña, auditada, tras completitud, conciliación y aprobación de los responsables reales de Negocio, Operaciones, Finanzas, Seguridad y Cumplimiento según función. No exige una transacción de millones de filas.

Si el legado opera, snapshot y deltas CDC/exportación controlada tienen barrera verificable: drenar/identificar órdenes en vuelo, aplicar hasta watermark completo y transferir autoridad. Cada contrato tiene un único escritor autorizado; sin barrera se suspende la cohorte durante el corte. En coexistencia se evitan fondos duplicados también en consolidados y se concilian transferencias entre cohortes.

La importación no reenvía pagos, cobros, webhooks, avisos ni ROS históricos. No omite debida diligencia. Devengamientos futuros parten del período migrado sin repetirlo. Antes de activar puede abortarse preservando evidencia; después de admitir operaciones reales, el retorno requiere trasladar/conciliar novedades o correcciones hacia adelante. Restaurar un backup no revierte liquidaciones externas.

## Alternativas y consecuencias

| Alternativa | Ventaja | Límite |
|---|---|---|
| Staging + aplicación por conjuntos; propuesta | Rendimiento y reanudación con evidencia | Más almacenamiento temporal, mapeos y ensayos |
| API ordinaria por fila | Reutiliza contratos existentes | Sobrecosto/latencia; no resuelve corte ni completitud global |
| Inserción directa en saldos activos | Rapidez aparente | Omite invariantes y hace operable una cartera incompleta; descartada |

## Aceptación, revisión y dependencias

Exigir cero diferencias inexplicadas por titular/moneda, cuadre auxiliar–mayor–origen, apertura/historia exclusivas y frontera preparada comprobada. Ensayar duplicados entre corridas, checksum cambiado, corte por etapa, transacción fuente dividida, delta tardío, activación incompleta, réplica atrasada, cruce de cohortes y retorno antes/después de operaciones reales. Medir ventana completa, operaciones validadas/s, WAL, locks y lag con controles activos. **Pendiente de ejecución**.

Depende de ADR-01 a ADR-06 y ADR-07 para operación; revisar ante nuevo origen, perfil, volumen, modo de historia o técnica de corte. No hay capacidad o migración sin interrupción garantizadas.

## Trazabilidad

[Arquitectura](../achitecture.md), secciones 5, 10, 13, 16–18; [mercado](../market_analysis.md), secciones 6, 8, 9 y 12; [cumplimiento](../compliant.md): BCRA-T17/18/19/20/21/24/25, DATA-01–06, STD07/08/11/14/32 según alcance; [controles](../../.agents/skills/core-bancario-argentina/references/controles.md): CTL-20, CTL-01 a CTL-06, CTL-09 a CTL-13, CTL-15 a CTL-17 y CTL-19. Son mecanismos propuestos, no técnicas impuestas universalmente por esas normas.

## NFR relacionados

[NFR-01](../nfr/NFR-01-integridad-financiera.md), [NFR-02](../nfr/NFR-02-disponibilidad-recuperacion.md), [NFR-04](../nfr/NFR-04-asincronia-durable.md), [NFR-06](../nfr/NFR-06-privacidad-residencia-retencion.md), [NFR-10](../nfr/NFR-10-migracion-carga-masiva.md), [NFR-11](../nfr/NFR-11-calidad-datos-reportes.md). Son cualidades y restricciones a verificar; la elección de este mecanismo no demuestra por sí sola su satisfacción.
