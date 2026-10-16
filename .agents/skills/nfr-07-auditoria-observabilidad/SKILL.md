---
name: nfr-07-auditoria-observabilidad
description: "Usar al diseñar, implementar o verificar auditoría durable, correlación, métricas, alertas y evidencia de incidentes del core argentino; aplicar NFR-07 sin exponer datos personales, secretos o ROS en telemetría general."
---

# Auditoría y observabilidad verificables

## Propósito y fuentes

Aplicar [NFR-07](../../../docs/nfr/NFR-07-auditoria-observabilidad.md), [operación arquitectónica](../../../docs/achitecture.md#operacion) y [core bancario Argentina](../core-bancario-argentina/SKILL.md), con CTL-08/10/11/12/13/14/19/20. Línea base: 15/10/2026. Distinguir obligaciones aplicables de los objetivos propuestos; la meta de correlación ≥99 % aún no fue medida y no reduce la auditoría material exigida.

## Entrada mínima

Precisar acción autorizada, entidad/producto, versión, operaciones y cambios materiales, consultas sensibles, flujos críticos, arquitectura de señales, guardia y expediente de incidentes. Obtener taxonomía de acciones, denominadores, políticas de retención, relojes, accesos y obligaciones por sujeto. Trabajar con datos sintéticos y referencias internas. Si faltan inventarios o ventanas, producir un borrador explícito y mantener resultados como no evaluados; no inferir cobertura a partir de un dashboard existente.

## Procedimiento

### DISEÑAR

1. Separar auditoría de negocio durable, registro de seguridad/SIEM y logs/trazas de diagnóstico. Especificar campos reconstruibles: actor, acción, instante/canal, motivo, autorización, cambios relevantes y vínculos; excluir secretos, factores, PAN y PII innecesaria. No distribuir ROS/investigación a consumidores generales.
2. Diseñar auditoría material en el commit local y evidencia durable antes de completar entregas sensibles. La exportación a archivo protegido es asíncrona con control de antigüedad, integridad y reentrega. Kafka, SIEM y APM no son por sí solos archivo probatorio.
3. Definir catálogo de señales y escalamiento para latencia/errores, locks/pools, WAL/réplica, outbox, edad/deadline de trabajos, riel ambiguo, conciliación y recuperación. Explicitar unidad, ventana, denominador y dueño. Los relojes regulatorios parten del hecho correspondiente, no de la creación de un ticket.

### IMPLEMENTAR

Cuando se pida implementación, inspeccionar y modificar componentes autorizados: escritura de auditoría, propagación de correlación, instrumentación OpenTelemetry, validadores de payload, acceso a trazas, exportador y alertas/runbooks. Mantener el contrato transaccional y límites de cardinalidad; no muestrear registros materiales obligatorios. Implementar recuperación/reentrega con trazabilidad y control de duplicados. Para incidentes, preparar hitos, clasificación y expediente; la presentación externa corresponde al responsable autorizado. Un pedido de revisión no autoriza desplegar, notificar al regulador ni cargar datos reales al SIEM.

### VERIFICAR

Construir universo esperado desde operaciones/cambios de prueba, independiente de las trazas recibidas. Inyectar caída del exportador/SIEM, disco o cola saturados, mensaje duplicado, reloj desviado y alteración de archivo. Comprobar C01/C02 sin pérdida material, acceso segregado y recuperación por categoría. Para C03 fijar la muestra antes de conocer resultados, medir completitud sobre esa muestra y publicar tamaño/población y tasa de muestreo; comprobar sólo pasos aplicables por flujo. No confundir muestra completa con cobertura del universo ni presentar 99 % como resultado hasta ejecutar. Probar C04 mediante fallos que activen señal y ruta de atención, no sólo la presencia de una regla. Para C05 simular incidente propio y tercero, calculando hitos/notificaciones aplicables, sin enviar comunicaciones reales por simular. No inventar una retención global ni confundir plazo contractual con regulatorio.

## Evidencia y salida

Entregar criterios C01–C05 con esperado/observado, versión, ventana, fuente del denominador, pruebas sanitizadas, alertas activadas, brechas y responsable. Usar `propuesto`, `no implementado`, `no evaluado`, `falló` o `verificado en alcance`. Conservar integridad y acceso de la propia evidencia. Indicar límites del muestreo y los requisitos institucionales pendientes; un certificado del proveedor o este skill no acredita todo el servicio.
