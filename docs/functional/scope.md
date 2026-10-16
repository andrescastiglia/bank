# Alcance y contrato de los requisitos funcionales

**Estado: Propuesto. Implementación, homologación y eficacia de controles: sin evaluar.** Base documental: **15/10/2026**, commit `ec0ef12a58ebc1c3e8d83334fc8fb947ab201755`. Este catálogo desarrolla la arquitectura y el alcance de negocio documentados; no convierte una propuesta en una entidad autorizada ni en un producto implementado.

## Qué significa cobertura completa

La cobertura se calcula contra un inventario explícito: los 32 módulos de esta biblioteca, los 15 módulos lógicos de la arquitectura, las 173 entradas identificadas de cumplimiento, los 71 criterios de los 13 NFR, los ocho ADR y los 21 controles de ingeniería. Las necesidades comerciales y funcionales descritas en prosa tienen una matriz adicional en [coverage.md](coverage.md). Cada relación remite a requisitos observables; la presencia de un ID no prueba por sí sola suficiencia jurídica, calidad de implementación ni funcionamiento.

El denominador es **el alcance documentado y fechado**, incluyendo los productos bancarios y extensiones condicionales especificados. No es el conjunto ilimitado de todas las actividades que cualquier entidad financiera podría realizar. Las exclusiones y pendientes de los documentos fuente siguen vigentes. Seguros como asegurador, servicios con activos virtuales, contratación pública u otra especialidad sin especificación validada quedan registrados y restringidos mediante FR-ENT-031; no se declaran cubiertos por tener una API genérica.

Se distinguen cinco evaluaciones independientes:

1. **Especificación:** existe un comportamiento, criterio de aceptación, ámbito y origen trazable.
2. **Aplicabilidad:** la entidad determinó qué obligación/producto le corresponde, con fundamento y responsable.
3. **Implementación:** existe software/configuración e integración que realizan el comportamiento.
4. **Verificación:** se obtuvo evidencia del resultado, incluidos fallos y concurrencia cuando corresponda.
5. **Aprobación/habilitación:** las funciones competentes y contrapartes emitieron las decisiones, contratos o autorizaciones necesarios.

Este entregable completa la primera evaluación para el inventario indicado. Las restantes no se infieren de que el documento esté publicado. El [catálogo JSON](catalog.json) permite incorporar después estado de implementación y evidencia en un sistema de seguimiento sin reescribir los FR.

## Perfiles y activación

| Perfil | Alcance |
|---|---|
| COMUN | Capacidades transversales del producto; no implica que toda ley citada obligue a todos sus usuarios. |
| EF | Entidad financiera autorizada, dentro de su clase, facultades y productos. |
| PSPCP | Proveedor de servicios de pago que ofrece cuentas de pago; separa fondos y resguardo de los depósitos bancarios. |
| PSP-OTRO | Otra función PSP registrada/autorizada; se aplica el régimen de la función efectivamente prestada. |
| PNFC | Proveedor no financiero de crédito alcanzado; su registro no habilita captación de depósitos. |
| PSCPP | Proveedor de servicios de créditos entre particulares a través de plataformas. No asume ni garantiza riesgo crediticio, ni promete devolver préstamos, ni compra los celebrados en su plataforma; individualiza y separa fondos según el régimen. |
| PROVEEDOR | Desarrollador u operador tecnológico, con funciones y evidencia contractuales; la tercerización no transfiere automáticamente la responsabilidad regulada. |
| Rol específico | Emisor, adquirente, administrador de transferencias, agente de valores, depositario, participante o corresponsal, sólo con habilitación y contratos correspondientes. |

Cada FR se evalúa por **sociedad + perfil/rol + producto + moneda + jurisdicción + canal + fecha**. Una sociedad del grupo no hereda licencia, datos ni fondos de otra. Una exclusión requiere fundamento y no puede derivarse de que hoy no haya tráfico. ENT registra esa decisión; IAM impone facultades y los módulos de producto verifican el perímetro antes de contratar o ejecutar.

| Etapa | Uso del catálogo |
|---|---|
| BASE | Núcleo común, gobierno, integridad, seguridad, evidencia y operación requeridos por los flujos activos. |
| CREDITO | Primera ruta comercial de crédito/cartera, con las capacidades BASE y obligaciones que le correspondan. |
| PAGOS | Primera ruta comercial alternativa de pagos/cuentas de pago o pagos bancarios según perfil. |
| BANCA | Ampliación bancaria: depósitos, crédito, servicios, prudencia, atención y localización de la EF. |
| EXT | Capacidad especializada: tarjetas, mercados, exterior, BaaS u otra extensión especificada, según perfil e integración. |

Las etapas expresan una estrategia de entrega; **no aplazan una obligación aplicable**. Un control PCI, de IA o de cambios se activa desde el primer uso en alcance, aunque la fila indique EXT. CREDITO y PAGOS son rutas iniciales alternativas, no un requisito de desarrollar simultáneamente toda la biblioteca para el primer piloto. La biblioteca completa contiene los FR de las etapas posteriores para que no queden ocultos detrás del MVP.

## FR, NFR y ADR

Un **FR** describe lo que el sistema debe hacer: por ejemplo, reservar fondos al autorizar un pago, registrar el reclamo con su reloj o rectificar un reporte conservando el anterior. Un **NFR** establece una cualidad o restricción verificable: exactitud, disponibilidad, latencia, aislamiento o accesibilidad. Un **ADR** registra una elección de arquitectura con sus razones y consecuencias.

Los FR referencian criterios NFR cuando aportan mecanismos o resultados que éstos necesitan. No sustituyen las métricas, muestras, oráculos ni escenarios de calidad del [registro NFR](../nfr/README.md). Tampoco aceptan institucionalmente los [ADR propuestos](../adr/README.md). Una obligación organizacional tiene soporte funcional —expediente, aprobación, evidencia y seguimiento— y sigue requiriendo la actuación real de Dirección, Cumplimiento, Seguridad, Auditoría u otra función competente.

## Identidad, datos y contratos de operación

- Los IDs `FR-XXX-NNN` son estables y únicos por módulo. No se reutiliza un ID retirado. Los cambios conservan historia Git, motivo e impacto en consumidores, pruebas y reglas.
- Las cinco columnas de cada tabla son el contrato de extracción: ID, comportamiento, ámbito/etapa, aceptación/excepciones y trazabilidad. El alcance y los contratos operativos posteriores forman parte del requisito; no se interpreta una fila aislada del módulo.
- Una entrada monetaria lleva entidad, identidad económica, contrato/cuenta, importe decimal exacto y moneda, fechas de evento/recepción/contable/valor pertinentes, versión de condiciones y contexto de autorización. No se usa coma flotante binaria para dinero.
- Los comandos identifican actor/servicio, finalidad, permisos, correlación y clave idempotente. La identidad económica persistente protege también después de vencer una caché de transporte. Un mismo hecho con otra clave no autoriza un segundo cargo.
- La respuesta identifica operación, estado, versión/fecha y siguiente acción permitida. Errores distinguen formato, permisos/perímetro, condición de negocio, conflicto concurrente, dependencia no disponible y resultado externo incierto. La descripción al cliente no revela ROS, secretos o criterios reservados.
- La auditoría registra el hecho durable, actor, decisión, versiones, motivo y referencias. Los eventos incluyen identidad, entidad, versión, correlación/causalidad y referencias mínimas; no distribuyen documentos, factores o datos sensibles completos por defecto.

Los nombres de comandos y estados de cada módulo son contratos conceptuales. El diseño de APIs/archivos concretará esquema, campos, límites, códigos y versionado sin cambiar su significado. Los formatos de redes y reguladores siguen su versión/homologación efectiva; este catálogo no inventa campos obligatorios de una interfaz externa aún no contratada.

## Sincronía, asincronía y autoridad

La validación de identidad, perfil, facultad, controles preventivos, restricciones, fondos, reservas y límites necesarios se completa antes del efecto financiero. Operación, posiciones, diario balanceado, auditoría y outbox se confirman en la misma transacción autorizante donde corresponda. Los guardianes estables también serializan la **creación de una nueva restricción**; no alcanza con bloquear sólo filas de restricciones existentes.

El cálculo, análisis documental, procesamiento masivo, documentos, proyecciones, notificaciones y reportes pueden ser asíncronos con recepción durable, estado, responsable, plazo y recuperación. No se mantienen locks monetarios mientras se espera a un proveedor. La finalización de un trabajo aplica su resultado mediante un comando financiero que revalida condiciones vigentes.

| Resultado | Significado común |
|---|---|
| Recibido / `202` | Solicitud aceptada durablemente con identificador y consulta; no es contrato activo, dinero disponible ni liquidación. |
| Confirmado local | Se completó el commit financiero durable bajo la política de persistencia; no prueba una liquidación externa. |
| Enviado / pendiente externo | Existe intención/evidencia de comunicación, pero falta el resultado exigido del riel. |
| Incierto | El efecto remoto pudo ocurrir. Se consulta/conciliará con la misma referencia y se conserva la restricción de fondos correspondiente. |
| Liquidado externo | Existe evidencia suficiente del riel/contraparte y registro local coherente. |
| Rechazado / cancelado | Alcance local o externo explicitado; no se afirma cancelación remota sólo por expirar un timeout. |
| Reversado / compensado | Existe una nueva operación vinculada que corrige el efecto; el hecho original y su liquidación no se borran. |

El vencimiento del lease de un worker no cerca físicamente a un emisor anterior ni prueba que no envió. Una decisión manual puede ordenar investigación o una compensación permitida, pero no reemplaza evidencia externa para afirmar no envío o liquidación. Una reserva ambigua no se libera por TTL. Los replays históricos reconstruyen proyecciones sin reenviar pagos, avisos o declaraciones por defecto.

## Tiempo, reglas y cierres

Cada obligación con plazo conserva fuente, disparador, calendario/zona, fecha efectiva y transición. Una DLQ no suspende el reloj. No hay un timeout, retención o plazo normativo único para todo el core. Las transiciones futuras identificadas en cumplimiento —incluidas las de fraude y score— se configuran con sus disparadores y no se presentan como plenamente exigibles antes de tiempo.

La configuración aprobada se activa por vigencia y conserva la versión pactada e histórica. La identidad del devengamiento base es entidad + contrato + concepto + período; **no incluye `rule_version`**. Recalcular con otra regla produce comparación y, si corresponde, ajuste vinculado autorizado; nunca otro devengamiento base del mismo hecho. Una devolución financiera no ordena automáticamente una devolución fiscal si el régimen exige otro trámite.

Los cierres y reportes requieren cortes completos, conciliación y barreras/watermarks por cada fuente pertinente; el máximo offset de un único tópico no prueba completitud global. Generación, firma, envío, recepción y aceptación regulatoria son estados distintos. La corrección conserva el reporte anterior, motivo y aceptación/rechazo de la rectificativa.

## Migración, continuidad y salida

La carga inicial bulk importa a staging con manifiestos y checkpoints, valida transacciones fuente completas y publica cohortes autorizadas. Datos `PREPARED` sólo están disponibles para validadores de migración autorizados: no integran saldos operativos, mayor corriente, reportes regulatorios, conciliación ordinaria ni eventos externos. Se elige apertura o historia financiera completa de forma excluyente para no duplicar saldos.

El baseline y sus deltas se cierran con barrera y una autoridad por contrato/cuenta. Durante coexistencia, los cupos globales se asignan por una autoridad coordinada; una vista atrasada de otro core no habilita gasto adicional. Después de actividad real, volver al legado requiere reconciliar operaciones nuevas y externas; restaurar una copia no deshace el mundo.

La recuperación restaura coherentemente SQL, documentos, jobs, identidad, claves, broker/inbox/outbox y evidencias externas antes de reabrir. La recuperación regional asíncrona mantiene un RPO dependiente del punto durable observado; no promete RPO cero regional. La salida exige datos, historia, reglas, metadatos y claves/medios acordados, exportación verificable y continuidad durante la transición.

## Límites institucionales y datos que deben completarse

El core puede preparar, validar, registrar, transmitir mediante integración autorizada y conservar constancias. No decide por sí mismo la habilitación jurídica, el criterio contable/prudencial, la sospecha AML, la presentación firmada ni la certificación de un sistema de gestión. Los documentos institucionales y decisiones efectivas conservan autor, alcance y evidencia.

Antes de activar una entidad/producto deben concretarse: licencia y roles; países y localización de originales, datos, soporte y recuperación; contratos con terceros y derechos de auditoría/salida; versiones de formatos y pruebas con redes; tasas, costos, impuestos, calendario y plan contable; plazos/obligaciones según sujeto; responsables, facultades y evidencias; objetivos NFR medidos con el volumen real. Una carencia bloquea la activación afectada y abre una brecha con responsable, no se rellena con una afirmación de cumplimiento.

ISO, NIST, COBIT, SOC, PCI, EMVCo y Swift mantienen la naturaleza y aplicabilidad del inventario fuente. Un informe SOC tiene alcance y período; las certificaciones de sistemas de gestión, como ISO/IEC 27001, cubren un alcance organizacional definido; PCI depende de función/datos/programa; ISO 20022 depende del perfil de mensajes acordado. Ninguno se declara satisfecho por seleccionar una casilla.

## Uso y mantenimiento

Seleccionar el perfil en ENT y los módulos activos; revisar FR y dependencias; derivar casos de aceptación desde cada fila y los [flujos integrados](flows.md); asociar NFR/ADR; implementar; ejecutar y guardar evidencia. Registrar cobertura, brechas y decisiones de aplicabilidad por separado. Un cambio de producto, fuente, regla, arquitectura o tercero dispara revisión de los módulos y matrices afectados. El [índice](README.md) explica cómo regenerar el catálogo y verificar su trazabilidad.
