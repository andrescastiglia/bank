# Catálogo técnico de controles y pruebas

Los controles **CTL** son propuestas de ingeniería. Vincular cada uno con los artículos o secciones efectivamente aplicables; no presentarlos como transcripción literal de una norma. La prioridad depende del producto y su materialidad. Usar datos sintéticos para los ejemplos y pruebas.

## Integridad financiera

| ID | Diseño y riesgo cubierto | Criterio de aceptación y evidencia |
|---|---|---|
| CTL-01 | Libro de partida doble por entidad y moneda; diario como registro financiero de referencia, correcciones mediante contrapartida y vínculo al original. | Cada transacción contabilizada balancea por moneda. Intentos de asientos incompletos y fallos de persistencia se rechazan o quedan íntegramente recuperables. Conciliar diario, auxiliares y mayor; documentar diferencias y ajustes aprobados. |
| CTL-02 | Exactitud monetaria: decimal o enteros escalados; moneda, escala, redondeo, bases de cálculo, calendario e impuestos versionados. | Vectores aprobados por producto verifican interés simple/compuesto, año bisiesto, días hábiles, CFT, cancelación anticipada y redondeos. La reproducción del cálculo usa la regla histórica y coincide con el extracto/contrato. |
| CTL-03 | Concurrencia y disponibilidad de fondos: límites, reservas, embargos y bloqueos con semántica consistente. | Dos débitos concurrentes no gastan el mismo saldo ni omiten una restricción vigente. Validar sobregiro autorizado por separado. Registrar autorizaciones, retenciones y vencimientos. |
| CTL-04 | Pagos y comandos idempotentes: identificadores únicos, máquina de estados, vencimiento, consultas de estado y recuperación. | Un reintento o evento duplicado no produce doble débito/crédito. Si la respuesta remota se pierde, consultar/reconciliar antes de repetir. Diferenciar autorizado, contabilizado, liquidado, rechazado, pendiente y reversado. |
| CTL-05 | Conciliación con riel, corresponsal, cuenta custodia, procesador y mayor. | Por fecha/moneda/entidad, reconciliar saldo inicial, movimientos y saldo final; mostrar faltantes, duplicados, pendientes y antigüedad. Un saldo global correcto no compensa una diferencia por titular. Cada ajuste conserva origen y aprobación. |
| CTL-06 | Temporalidad: fecha/hora del evento, recepción, contabilización, valor y período de negocio, zona horaria y calendario explícitos. | Eventos tardíos, fin de mes/año, feriados y cambios normativos respetan reglas fechadas. Fechas valor y contables no se confunden. Cierres y reaperturas quedan autorizados y auditados. |

## Identidad, datos y delito financiero

| ID | Diseño y riesgo cubierto | Criterio de aceptación y evidencia |
|---|---|---|
| CTL-07 | Registro de cliente/persona, representación y beneficiarios finales; integración con identificación y KYC. | Mantener múltiples roles sin duplicar identidad; almacenar procedencia, vigencia y resultado de la verificación. El alta/cambio de riesgo activa la debida diligencia correspondiente. La decisión final del sujeto obligado permanece identificada. |
| CTL-08 | Integración AML/FT/FP y antifraude con datos de calidad y acceso restringido. | Probar transferencia de eventos completos, listas versionadas, trazabilidad de alertas, investigación, congelamientos y decisiones. No exponer la existencia de ROS al cliente. No sustituir el motor AML por un umbral único de monto. Distinguir monitoreo posterior de controles preventivos. |
| CTL-09 | Autorización de mínimo privilegio, identidad de servicios, autenticación reforzada según riesgo y doble intervención en tareas sensibles. | Denegar por defecto; probar acceso cruzado entre entidades/clientes, cambios de rol, baja y privilegios temporales. Separar crear/aprobar/liberar ajustes, cambios de parámetros y reportes. Evidenciar revisiones de acceso y sesiones privilegiadas. |
| CTL-10 | Clasificación, minimización, cifrado y gestión del ciclo de vida de claves. | Inventariar datos y flujos; verificar cifrado en tránsito/reposo según alcance, rotación, revocación y recuperación de claves con segregación. No incluir secretos, PAN completo ni datos personales innecesarios en logs o entornos de prueba. |
| CTL-11 | Secreto financiero, privacidad, derechos de titulares y retención por categoría. | Cada acceso/cesión/exportación tiene finalidad y autoridad. Implementar búsqueda, acceso, rectificación, restricción y supresión cuando legalmente proceda. Preservar evidencia por obligación de conservación o retención judicial; no borrar asientos para ejecutar una solicitud de supresión. Probar vencimientos y disposición documentada. |
| CTL-12 | Auditoría con integridad, tiempo sincronizado y acceso separado de administración operativa. | Reconstruir quién, qué, cuándo, desde dónde, motivo, autorización y valores relevantes anteriores/posteriores. Detectar alteraciones; mantener correlación entre canal, core y terceros. Registrar acceso/exportación de trazas y retención justificada. |

## Operación y desarrollo

| ID | Diseño y riesgo cubierto | Criterio de aceptación y evidencia |
|---|---|---|
| CTL-13 | Continuidad basada en análisis de impacto, objetivos de recuperación por servicio y dependencia, y respaldos recuperables. | Ensayar restauración y recuperación ante pérdida de zona/región o cifrado malicioso según escenario. Medir RTO/RPO observados y reconciliar operaciones antes de reabrir. Los valores obligatorios se toman de la norma aplicable; las metas adicionales se aprueban con negocio. |
| CTL-14 | Observabilidad y respuesta a incidentes con responsables y comunicaciones obligatorias. | Simular detección, clasificación, escalamiento, contención y recuperación; medir tiempos y conservar evidencia. Distinguir los plazos BCRA de plazos de contrato y recomendaciones. Incluir incidentes originados en terceros y acceso al portal regulatorio por responsable autorizado. |
| CTL-15 | Desarrollo seguro y cambios: revisión de código, dependencias, separación de entornos, validación y reversión. | Evidenciar trazabilidad requisito-cambio-aprobación-despliegue. Revisar vulnerabilidades y dependencias, probar cambios materiales y procedimientos de emergencia; firmar/verificar artefactos cuando corresponda. Un rollback técnico no revierte automáticamente una operación financiera ya liquidada. |
| CTL-16 | Gestión de terceros y salida: inventario de servicios, datos, países, criticidad y subcontratistas. | Verificar contrato, acceso de auditoría/supervisor, incidentes, continuidad, devolución y borrado de datos. Ejecutar exportación y restauración de prueba con formato legible, claves, historial y metadatos; evaluar continuidad durante transición y costos de salida. |
| CTL-17 | Segregación multientidad y multicliente en datos, contabilidad, recursos y claves. | Pruebas de autorización negativa por API, consultas, eventos, soporte y exportaciones demuestran aislamiento. Identificar razón social responsable y cuenta de custodia sin mezclar fondos propios/clientes. Aislar recursos para evitar que la carga de un cliente bloquee a otros. |

## Consumidor, supervisión y migración

| ID | Diseño y riesgo cubierto | Criterio de aceptación y evidencia |
|---|---|---|
| CTL-18 | Condiciones comerciales, consentimiento/aceptación, comprobantes y reclamos versionados. | Reproducir términos vigentes al contratar, tasas/cargos/costos y avisos; conciliar importe informado y debitado. Registrar entrega y canal; probar baja, reverso y reclamo en los casos aplicables. No denominar firma digital a un mecanismo que sólo acredita firma electrónica. |
| CTL-19 | Fábrica de reportes y prudencia: linaje, reglas y validaciones con revisión institucional. | Reproducir un reporte para un corte, reconciliarlo contra mayor/submayores y documentar transformaciones, catálogos y exclusiones. Mantener acuses, rechazos, rectificativas y responsable; validar reglas regulatorias y técnicas por versión. |
| CTL-20 | Migración por producto/cohorte: origen, mapeos, controles de totales, trazabilidad histórica y retorno. | Ensayo y aprobación con saldos, intereses devengados, mora, garantías, bloqueos, KYC y reportes reconciliados. Comparar resultados en paralelo según criticidad. Demostrar recuperación y reconciliación si se revierte; controlar eventos durante corte. No exigir una técnica comercial específica como si fuera obligación normativa universal. |
| CTL-21 | IA o modelos usados en decisiones: inventario, datos, finalidad, validación y supervisión humana proporcional. | Mantener versión, aprobación y explicación rastreable de decisiones; probar sesgo, deriva, manipulación de entradas, divulgación de datos y dependencia del proveedor. La autorización contable y el control transaccional deben seguir reglas verificables. Vincular con BCRA y privacidad según uso. |

## Plantilla de caso de prueba

```text
ID de prueba / requisito / CTL:
Sujeto, producto, moneda y versión normativa:
Escenario y datos sintéticos:
Precondiciones:
Acción y fallo o concurrencia inyectados:
Resultado financiero y operativo esperado:
Evidencia obtenida y ubicación:
Resultado observado / brecha / responsable:
Fecha de ejecución, versión de software y aprobación:
```

Un certificado, una prueba unitaria o una captura aislada no demuestra por sí sola el funcionamiento de extremo a extremo. Elegir evidencia proporcional al control: contrato firmado, configuración efectiva, revisión de accesos, conciliación, acuse regulatorio, ejecución de recuperación o prueba técnica.
