---
name: nfr-13-accesibilidad-experiencia
description: "Usar al diseñar, implementar o revisar accesibilidad de canales/documentos, comprensión de estados de pagos e información contractual de clientes u operadores según NFR-13."
---

# Evaluar accesibilidad y comprensión

## Entrada y alcance

Identificar usuario, canal/documento, entidad/producto, recorrido, perfil de accesibilidad aplicable y condiciones económicas. Leer [NFR-13](../../../docs/nfr/NFR-13-accesibilidad-experiencia.md), los contratos/estados de [arquitectura](../../../docs/achitecture.md) y la evidencia disponible. El requisito es propuesto en la línea base; no hay conformidad ni mediciones acreditadas por el documento.

Para determinar obligación jurídica o perfil técnico incorporado, usar [core-bancario-argentina](../core-bancario-argentina/SKILL.md). No imponer una versión de un estándar web como si fuera una ley universal ni considerar que todo motor sin UI está fuera de su contribución a canales y documentos.

## Procedimiento

1. Delimitar recorridos materiales: alta/contratación, consulta de saldo, orden/confirmación, operación incierta, cambio de condición, baja, reclamo y solicitud de datos. Identificar actores y requisitos realmente aplicables; no crear pantallas o trámites que no fueron pedidos.
2. Construir una matriz de criterios del perfil de accesibilidad acordado, con oráculo por criterio. Incorporar navegación por teclado, foco, lector de pantalla, contraste, mensajes de error y documentos cuando correspondan. Sin perfil definido, avanzar con hallazgos evidentes y dejar la conformidad pendiente de esa definición.
3. Conectar los textos al estado financiero real. `202` es aceptación durable de trabajo, no liquidación; timeout no es rechazo inequívoco. Una proyección incluye su frescura y los comprobantes reflejan lo efectivamente confirmado. Evitar inducción a repetir un pago con nueva identidad.
4. Contrastar oferta, simulación, contrato aceptado, cargos, CFT y extracto con versiones/cálculo/asiento. Verificar idioma, unidades, moneda, fecha y diferencias entre principal, interés e impuesto. No introducir tasas o importes normativos ficticios.
5. Revisar controles y salida de recorridos. Consentimiento y revocación deben producir efecto verificable; reclamos/bajas/derechos tienen acuse y seguimiento. Mensajes de error no exponen ROS, investigaciones, secretos ni datos de terceros. En rechazo crediticio, conservar y comunicar resultado/fuente exigibles según alcance.
6. Ejecutar según el encargo: corregir UI/API/plantillas disponibles si se pidió implementar; proponer contratos y estados si se pidió diseñar; revisar y reportar evidencia si se pidió evaluar. Comprobar con casos sintéticos, evaluación manual y herramientas automáticas pertinentes. No declarar accesibilidad por una captura o una sola herramienta.
7. Relacionar las mejoras con ADR-03/05/06 y NFR de integridad, seguridad, privacidad y datos. Documentar los criterios que el core satisface y las dependencias del canal/tercero; no transferirlas implícitamente.

## Aceptación y salida

Aplicar NFR-13-C01 a C05 por recorrido. Registrar `criterio | perfil/fuente | usuario/canal | escenario | resultado esperado | observado | evidencia | brecha/acción`. El resultado no se resume en una puntuación que compense fallos de una acción crítica.

Separar diseñado, implementado sin evidencia y verificado. Informar lo cambiado, los casos comprobados y los límites pendientes, incluyendo interfaz, documento o tercero no evaluado. La experiencia debe ayudar a operar correctamente; una explicación clara no vuelve válido un cargo incorrecto, y una UI accesible no certifica todo el cumplimiento del core.
