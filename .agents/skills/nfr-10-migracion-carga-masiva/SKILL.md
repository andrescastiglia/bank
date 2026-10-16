---
name: nfr-10-migracion-carga-masiva
description: "Usar al diseñar, implementar o verificar carga inicial bulk, migración por cohortes, snapshot/deltas, conciliación, activación y retorno del core argentino, midiendo ventana completa y ausencia de diferencias financieras inexplicadas."
---

# NFR-10: migración y carga masiva

## Aplicación y entradas mínimas

Leer [NFR-10](../../../docs/nfr/NFR-10-migracion-carga-masiva.md), arquitectura/ADR-08 enlazados y [core bancario argentino](../core-bancario-argentina/SKILL.md). Usar los criterios de calidad sin duplicar la decisión del mecanismo bulk. Adaptar el trabajo a diseño, implementación o verificación solicitados; no presentar un plan como una migración ejecutada.

Identificar entidad, cartera/cohorte, origen/destino, población, modo de historia, corte, operación concurrente, ventana aprobada, responsables y datos de prueba disponibles. Obtener mapeos, totales financieros, restricciones/KYC, documentos, esquema y versiones. Pedir sólo faltantes que cambien el resultado. Sin snapshot consistente o ventana, preparar validadores/ensayo con supuestos explícitos y registrar la dependencia antes de declarar aceptación.

## Flujo operativo

1. **Fijar criterios y oráculos.** Mapear NFR-10-C01 a C08 al ensayo. Usar inventario esperado y conciliación por titular, contrato, producto, entidad, moneda y mayor. Exigir cero diferencias inexplicadas; documentar redondeos y ajustes justificados/aprobados. Definir apertura conciliada o historia completa: nunca recontabilizar historia además de la misma apertura. Preservar búsqueda documental e histórica autorizada.
2. **Preparar o implementar.** Construir manifiestos con identificadores, hashes, versiones de mapeo, conteos y totales. Si se pide código, inspeccionar la implementación y modificar la ruta de importación real, sus validaciones y pruebas; no entregar únicamente una lista. Usar staging aislado y carga bulk controlada; rechazos trazables sin descarte silencioso. No aceptar SQL ejecutable del cliente ni desactivar durabilidad, índices únicos, auditoría o controles críticos para mejorar la tasa.
3. **Verificar aplicación/reanudación.** Inyectar chunk duplicado, checksum cambiado, proceso interrumpido y nueva corrida. El checkpoint debe reflejar confirmación durable de la transacción económica fuente completa, aunque sus filas atraviesen chunks. Probar unicidad económica entre corridas/revisiones, no sólo dentro de un `run_id`; un delta incompleto no se publica. Cambiar archivo/mapeo invalida la aprobación previa.
4. **Medir ventana completa.** Registrar extracción + transferencia + carga + validación + aplicación + conciliación + corte + margen. Medir registros válidos/s y operaciones financieras validadas/s, horas, WAL, lag, locks y recursos. Comparar con ventana aprobada, preservando SLO de carteras activas mediante throttle. Evaluar cada SLO con su ventana, denominador y presupuesto; una muestra corta no demuestra el SLO mensual ni la meta 99,95 % exige cero errores individuales. Mantener separado el objetivo de cero controles críticos desactivados. No inventar mínimos de filas/s ni comparar sólo el tiempo de `COPY` con toda la ventana.
5. **Ensayar corte y aislamiento.** Si hay origen activo, validar snapshot/deltas, watermark final, operaciones en vuelo y barrera de autoridad; sin barrera verificable, exigir suspensión acotada de cohorte. Probar que cada contrato tenga una sola autoridad y que activación incompleta falle. Antes de activar, consultas de negocio, trabajadores corrientes, mayor operativo, RI, conciliación ordinaria y eventos corrientes excluyen la preparación; permitir validación y conciliación autorizadas del paquete de migración aislado. No emitir pagos, cobros, notificaciones ni ROS históricos como operaciones nuevas. Probar también interacción entre cohortes migradas y legadas.
6. **Ensayar retorno.** Antes de activar puede abortarse la generación manteniendo evidencia. Después de operar, conciliar y trasladar operaciones nuevas mediante retorno controlado o correcciones hacia adelante. No borrar lotes activos ni restaurar una base anterior para deshacer egresos liquidados. Probar el escenario con actividad realista posterior al corte.

## Salida y estado

Entregar alcance/volumen, manifiesto, mapeos, rechazos, checkpoints, mediciones por etapa, conciliación, resultado de corte/retorno y brechas con responsables. Asociar evidencia a cada criterio y versión. Si no se ejecutó el ensayo, usar `sin evaluar`; si existe código sin prueba, `implementado sin evidencia`. Marcar verificado sólo el escenario medido. La aprobación institucional de salida requiere evidencia concreta; no inventar aprobaciones ni afirmar cumplimiento integral por terminar la carga.
