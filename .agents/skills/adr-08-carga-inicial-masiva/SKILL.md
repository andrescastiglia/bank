---
name: adr-08-carga-inicial-masiva
description: "Usar al diseñar, implementar o revisar carga inicial bulk del core: COPY, staging durable, mapeos, deduplicación entre corridas, conciliación, CDC, activación de cohortes y retorno conforme ADR-08."
---

# ADR-08: importación masiva y transición de autoridad

## Propósito y referencias

Convertir datos del legado en una cartera completa, conciliada y operable, usando bulk sin omitir reglas financieras. Aplicar ante onboarding, importadores, migraciones por cohorte, cambios de mapeo o revisión de corte/retorno. Leer [ADR-08](../../../docs/adr/ADR-08-carga-inicial-masiva.md), [arquitectura](../../../docs/achitecture.md#carga-inicial), secciones 5, 10, 13 y 16–18, [skill regulatorio](../core-bancario-argentina/SKILL.md) y [controles](../core-bancario-argentina/references/controles.md): CTL-20 y controles financieros, privacidad, continuidad y reportes relacionados. Consultar [mercado](../../../docs/market_analysis.md), secciones 8–9 y 12: el valor incluye coexistencia, riesgo y salida. Base documental **15/10/2026**, sin importador ni ensayos acreditados; revalidar obligaciones aplicables al corte real.

## Entrada mínima

Determinar modo `DISEÑAR`, `IMPLEMENTAR` o `REVISAR`; entidad/perfil/producto; origen, población y volumen; ventana disponible; operación concurrente; esquema y calidad; historia requerida; custodios; responsables y contratos. Localizar código/configuración existentes. Expresar supuestos y pendientes que condicionen el corte, avanzando con análisis, artefactos y cambios reversibles autorizados. No solicitar datos personales reales si bastan fixtures sintéticos ni inventar aprobación institucional.

## Procedimiento adaptable

1. **Definir manifiesto y autoridad.** Establecer `import_run_id`, origen, entidad, cohorte, snapshot/watermark, versión de esquema/mapeo, modo de historia, hashes por archivo/chunk, conteos y sumas por titular/producto/moneda. Enumerar población esperada, responsables y criterios de rechazo. Elegir apertura conciliada con historia previa consultable **o** historia completa que reconstruye saldos; no sumar ambos. Definir autoridad actual, destino y barrera de transferencia.
2. **Preparar transporte y staging.** Validar formato, encoding, fechas/calendarios, escala decimal y archivos cifrados en destinos autorizados. Usar `COPY FROM STDIN` con columnas explícitas a staging logged, dedicado por entidad/corrida y credenciales mínimas; nunca SQL del cliente, `COPY PROGRAM` ni filesystem arbitrario. Si RLS bloquea COPY, usar una ruta de inserción autorizada compatible o staging dedicado; no desactivar políticas. Restringir PII/rechazos, retención y acceso de soporte.
3. **Aplicar con identidad estable.** Validar claves, relaciones, titularidad/facultades, KYC, reservas/bloqueos, garantías, cronogramas, principal/devengados/mora y monedas. Importar por conjuntos mediante procedimientos/comandos bulk controlados que respeten invariantes del dominio. Ordenar dependencias y preservar la transacción económica completa del origen aun cuando cruce chunks; el checkpoint autoritativo sólo avanza tras completarla. Imponer unicidad `(entity_id, source_system, source_record_id, record_type)` entre corridas y comparar payload/checksum. Un archivo corregido crea revisión vinculada y vuelve a validar; no reutilizar aprobación ni checkpoint de contenido diferente.
4. **Separar preparación de operación.** Lotes atómicos y reanudables cargan generación no operable. Excluirla de autorizaciones, saldos/mayor operativos, RI, conciliación ordinaria, proyecciones y eventos corrientes; verificar también consolidaciones con legado. Conciliar origen–auxiliares–mayor por titular/moneda, reservas y restricciones. No compensar errores individuales con totales globales o cuentas técnicas inexplicadas. No publicar cartera parcialmente preparada.
5. **Planificar/ejecutar el corte autorizado.** Si el origen sigue activo, aplicar snapshot y deltas CDC/exportación controlada con watermark, transacciones completas y barrera comprobable. Drenar o identificar operaciones en vuelo; sin barrera, suspender esa cohorte durante el corte. Activar mediante un cambio pequeño y auditado de generación/routing/época, con un único escritor por contrato y aprobaciones de los roles reales competentes. La aprobación institucional rige la activación productiva; no impide preparar diseño, código, conciliaciones o ensayos autorizados. No requerir una transacción masiva final.
6. **Trabajar según modalidad.** En `DISEÑAR`, producir contratos, estados, mapeos, plan de corte/retorno y ensayos. En `IMPLEMENTAR`, modificar importador/configuración autorizados y verificar invariantes/reanudación con datos sintéticos. En `REVISAR`, contrastar rutas efectivas, SQL, permisos, manifiestos y evidencia con el ADR; describir brechas reproducibles. Completar la tarea solicitada, sin reemplazar implementación por recomendaciones.

## Invariantes y aceptación

- Mantener decimal exacto, partida doble y unicidad financiera. Repetir chunks/corridas no duplica efecto; `ON CONFLICT DO NOTHING` no explica conflictos.
- No desactivar WAL, `fsync`, persistencia síncrona, auditoría, restricciones o seguridad para mejorar velocidad. Medir extracción→carga→validación→aplicación→conciliación→corte, operaciones validadas/s, WAL, replica lag, locks e impacto en cohortes activas; aplicar throttling.
- No reemitir pagos, cobros, webhooks, avisos ni ROS históricos. Preparar proyecciones y próximos devengamientos sin repetir períodos; conservar debida diligencia requerida.
- Ensayar duplicado entre corridas, checksum cambiado, caída por etapa, registro inválido, transacción fuente dividida/delta tardío, apertura versus historia, activación incompleta denegada y exclusión de generación preparada. Incluir réplica atrasada y transferencias entre cohortes migradas/legadas.
- Antes de activar puede abortarse conservando evidencia y retención debida. Tras admitir operaciones reales, retorno requiere conciliar/trasladar novedades o corregir hacia adelante; borrar lotes o restaurar backup no revierte fondos liquidados. Ensayar ambos escenarios.

## Salida y evidencia

Entregar artefactos/cambios, manifiesto de ejemplo sintético, decisiones pendientes, métricas y matriz `etapa/invariante | prueba | esperado | observado | evidencia/versiones | estado | responsable/acción`. Estados: `propuesto`, `sin evaluar`, `parcial`, `implementado sin evidencia` o `verificado`. Para diseño, marcar ensayos no ejecutados; para implementación/revisión, enlazar resultados reproducibles y diferencias concretas. No afirmar migración completada, cumplimiento o capacidad garantizada por haber terminado COPY. Actualizar ADR ante cambios materiales conservando trazabilidad y justificación.
