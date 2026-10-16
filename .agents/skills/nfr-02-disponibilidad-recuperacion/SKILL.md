---
name: nfr-02-disponibilidad-recuperacion
description: "Usar al diseñar, implementar o verificar SLO de disponibilidad, tolerancia a fallos, RTO/RPO y recuperación financiera coherente del core bancario argentino conforme a NFR-02."
---

# NFR-02: disponibilidad y recuperación

## Resultado y entrada mínima

Aplicar [NFR-02](../../../docs/nfr/NFR-02-disponibilidad-recuperacion.md) sin convertir metas propuestas en compromisos demostrados. Línea base: 15/10/2026. Identificar si se solicita diseño, implementación o verificación, y avanzar dentro de esa autorización; documentar un simulacro no autoriza ejecutarlo en producción.

Determinar entidad, servicio crítico, BIA disponible, volumen, topología/dominios reales, dependencia de identidad, llaves, red, rieles y documentos, ventanas de operación y puntos de persistencia. Obtener políticas efectivas de confirmación, promoción, aislamiento del primario y restauración. Para normativa y responsabilidad compartida consultar [cumplimiento](../core-bancario-argentina/SKILL.md). Un SLA de nube o réplica existente no demuestra recuperación del servicio completo.

## Procedimiento por acción

1. **Diseñar:** definir fallos cubiertos, comienzo/fin de interrupción, criterios de reapertura, RTO y pérdida tolerable por servicio. Trazar NFR-02-C01 a C06 con ADR-04 y dependencias. No confundir tres procesos o máquinas dentro del mismo sitio con independencia geográfica. Si falta BIA, mantener las cifras como hipótesis por validar.
2. **Implementar:** revisar dentro del cambio autorizado el comportamiento cuando falta réplica elegible, aislamiento del primario anterior, capacidad remanente, rutas a llaves e identidad y manifestación de dependencias degradadas. No introducir degradación silenciosa de durabilidad para recuperar disponibilidad. Conservar backups protegidos e independientes de fallos administrativos, y runbooks con conciliación integral.
3. **Verificar:** seleccionar caída de proceso, writer/zona, partición, región y copia limpia según cambio y entorno. Medir desde disrupción hasta servicio utilizable y validado, además de hitos de promoción. Comparar commits reconocidos y operaciones externas con el punto restaurado. Ejecutar sólo ensayos autorizados y acotados; para un pedido documental producir escenarios, instrumentos y oráculos.

## Metas y oráculos

La disponibilidad propuesta de API monetaria local es ≥99,95 % mensual por solicitudes válidas, desglosada por entidad/endpoint. Mantenimiento obstructivo cuenta; rechazo correcto de negocio es válido. Timeouts técnicos y aceptación no durable son fallos. Reportar canarios temporales por separado: 21 min 36 s en 30 días es equivalencia temporal, no evidencia del indicador por solicitudes.

Las metas de recuperación son proceso ≤30 s; writer/zona ≤120 s y cero commits reconocidos perdidos únicamente bajo persistencia síncrona remota efectiva y aislamiento probados; región ≤60 min en ensayo piloto; copia limpia ≤4 h preliminares para su volumen. Lag regional objetivo ≤60 s no garantiza ese RPO: medir pérdida real y declarar operaciones reconocidas que faltan.

Buscar dos primarios, pérdida oculta, broker posterior al punto financiero restaurado, inbox anterior a offsets, claves irrecuperables y replay que repite envíos externos. Reabrir requiere reconciliar estados y rieles; una base promovida no basta.

## Evidencia y salida

Entregar `criterio | servicio/escenario | objetivo | RTO/RPO observado | punto durable | evidencia | estado | brecha`. Conservar cronología, versiones, configuración efectiva, carga, commits de referencia, conciliaciones y dependencias. Explicitar condiciones y pérdida potencial regional.

Usar `no evaluado` sin infraestructura o ejecución; `satisface en escenario probado` sólo con resultados completos. No declarar cumplimiento normativo ni aceptación del riesgo por negocio. Registrar responsable pendiente y revisar al cambiar BIA, topología, volumen, proveedor o contrato, y tras incidentes materiales.
