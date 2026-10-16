---
name: nfr-06-privacidad-residencia-retencion
description: "Usar al diseñar, implementar o verificar inventario de tratamientos, residencia, transferencias, derechos, secreto ROS y retención por categoría del core argentino; aplicar NFR-06 a datos, eventos, backups y soporte."
---

# Privacidad y ciclo de vida de datos

## Propósito y fuentes

Aplicar [NFR-06](../../../docs/nfr/NFR-06-privacidad-residencia-retencion.md), [arquitectura](../../../docs/achitecture.md#cumplimiento) y [skill regulatorio](../core-bancario-argentina/SKILL.md), especialmente CTL-08/10/11/12/16/17. La base es 15/10/2026. Leer DATA, AML, conservación y tercerización de cumplimiento sólo para las referencias afectadas; verificar vigencia antes de decidir producción. Una política de diseño no acredita efectividad ni certificación.

## Entrada mínima

Determinar acción autorizada, entidad y rol responsable/encargado, producto/licencia, categorías de datos, finalidad/fundamento, países, proveedores/subencargados y soporte remoto. Incluir bus, DLQ, copias, KMS, telemetría, índices y región de DR. Solicitar reglas aprobadas de conservación, disparadores, contratos, holds y solicitudes de titulares disponibles; usar ejemplos sintéticos. Si falta un fundamento, registrarlo `por determinar` y continuar el inventario sin inventar una duración o destino habilitado.

## Procedimiento

### DISEÑAR

1. Mapear cada flujo y copia a entidad, finalidad, propietario, destinatario, ubicación, acceso y mecanismo de transferencia. Distinguir domicilio del proveedor de ubicación de tratamiento/control. Para EF identificar originales/documentación exigidos en Argentina y funciones locales; no extrapolar ese régimen a todo PSP ni concluir que nube exterior está prohibida o habilitada sin condiciones.
2. Definir política por `record_class`, autoridad, disparador, duración fundada, hold, fecha de disposición y nivel de acceso. Evaluar obligaciones concurrentes; separar difusión crediticia, archivo contable y conservación AML. No usar TTL único ni WORM perpetuo sobre todo dato personal.
3. Modelar recepción y reloj de derechos, verificación de identidad, respuesta, propagación y preservación restringida cuando corresponda. Mantener ROS e investigación fuera de CRM, canales, analítica general y soporte. Las referencias pseudónimas no prueban anonimización.

### IMPLEMENTAR

Si se autoriza implementar, inspeccionar esquemas, contratos y procesos disponibles; modificar inventarios ejecutables, clasificación, minimización de payloads, políticas de archivo, gestión de holds y disposición dentro del alcance. Hacer visibles retención y procedencia de cada objeto. Implementar barreras a exportación y activación de destinos pendientes, sin introducir aprobaciones ficticias. La configuración de DR debe reflejar las condiciones reales de transferencia, custodia y contrato. Conservar asientos y soportes que sigan obligados; corregir datos mediante sus flujos autorizados. Preparar la reaplicación de supresiones/restricciones al restaurar copias. Un pedido de análisis no autoriza borrar datos reales ni cambiar proveedores.

### VERIFICAR

Contrastar inventario con servicios, tráfico y acceso de soporte. Probar vencimiento sin obligación, obligación concurrente, hold vigente/levantado, fin de encargo, difusión vencida y rectificación. Restaurar copia sintética y verificar que no reintroduce datos dispuestos ni reactiva su difusión. Medir C01–C05 por categoría, flujo, expediente y release: cero flujos/políticas sin definir, cero supresiones indebidas/exposiciones y resolución dentro del plazo aplicable. Calcular relojes desde el disparador efectivo con calendario correcto. No importar un plazo AAIP de 72 horas desde GDPR ni copiar retenciones bancarias a otro sujeto.

## Evidencia y salida

Entregar inventario/matriz por criterio, cambios autorizados, pruebas sanitizadas, política versionada, evidencia contractual y decisiones pendientes con responsable. Distinguir diseño, implementación y resultado observado: `no implementado` o `no evaluado` cuando corresponda. Documentar excepciones fundadas sin afirmar que una aceptación interna elimina obligaciones. Exportar evidencia mínima, preservando secreto; no publicar datos personales ni enviar comunicaciones externas sin autorización.
