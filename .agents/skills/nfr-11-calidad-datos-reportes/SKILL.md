---
name: nfr-11-calidad-datos-reportes
description: "Usar al diseñar, implementar o verificar calidad, cortes consistentes, linaje, conciliación, reproducibilidad y aceptación de reportes del core argentino; aplicar NFR-11 a cierres y regímenes efectivos por entidad y período."
---

# Calidad y reportes reproducibles

## Propósito y fuentes

Convertir [NFR-11](../../../docs/nfr/NFR-11-calidad-datos-reportes.md) en reglas, manifiestos y evidencia. Leer [arquitectura y trazabilidad](../../../docs/achitecture.md#cumplimiento) y [core bancario Argentina](../core-bancario-argentina/SKILL.md), especialmente CTL-01/02/05/06/07/08/09/18/19/20. Base documental: 15/10/2026; las versiones y cambios posteriores requieren verificación. No tratar el inventario de 173 entradas como aplicabilidad universal ni como homologación de formatos.

## Entrada mínima

Determinar acción autorizada, entidad/licencia, producto, destinatario y régimen, período/corte, fuentes, volúmenes, plan de cuentas, formatos efectivos, reglas de agregación y calendario. Obtener responsables de datos, aprobadores, controles de totales y evidencia de aceptación disponible. Identificar datos manuales, exclusiones, tardíos y dependencias externas. Si no existe sujeto o formato definido, diseñar con dataset sintético y marcar pendiente la aplicabilidad; no inventar endpoints, diseños de registro ni fechas legales.

## Procedimiento

### DISEÑAR

1. Seleccionar paquetes por entidad/producto/período, separando banco, PSP y prestamista. Trazar cada campo o importe material hacia contrato, operación, asiento y transformación. Las políticas contables, fiscales y de riesgo las define su responsable; una proyección técnica no las sustituye.
2. Definir manifiesto del corte: snapshot transaccional o barrera de completitud, watermarks por fuente/partición, universo esperado, versiones de reglas/catálogos/índices, totales, excepciones y aprobadores. Un offset máximo de Kafka o el término de un worker no prueba un corte consistente.
3. Separar estados preparado, validado, aprobado, enviado, recibido, aceptado, rechazado y rectificado. Definir tratamiento de tardíos y ajustes manuales con segregación, motivo y nueva versión vinculada. El ticket de subida no equivale a aceptación del receptor.

### IMPLEMENTAR

Si el usuario pide implementar, inspeccionar y modificar el alcance autorizado: ingesta/validación, contratos de datos, snapshots/barreras, reglas versionadas, manifiestos, conciliación, workflow y pruebas necesarias. Ejecutar procesos pesados de modo asíncrono fuera del writer monetario; conservar deadlines y capacidad por flujo. No habilitar una proyección para autorizar fondos ni corregir saldos por escritura directa. Preservar fuentes y versión utilizadas para regenerar períodos anteriores; impedir reemplazos silenciosos de archivos aprobados. Una revisión no autoriza presentar un reporte real ni modificar la contabilidad institucional.

### VERIFICAR

Usar controles independientes por entidad, moneda, titular, fecha y régimen. Probar faltante/duplicado que se compensan en un total global, fuente atrasada con otras avanzadas, redondeo, cierre, asiento tardío, intervención incompatible, rechazo y rectificativa. Reproducir el corte con los insumos/versiones preservados; comparar salida canónica y justificar diferencias de empaquetado. Conciliar saldo inicial más movimientos con saldo final y totales del reporte. Medir C01–C05 con denominadores declarados: cero fuentes incompletas, diferencias inexplicadas, campos materiales sin linaje, aceptaciones sin validación y cambios sin historia. Verificar tanto el contenido como el estado del receptor, sin enviar archivos reales durante una simulación.

## Evidencia y salida

Entregar cambios realizados y matriz `criterio | corte/versión | escenario | esperado | observado | evidencia | estado | responsable`. Adjuntar manifiesto sanitizado, linaje, conciliación, archivo/hash y acuse/validación cuando existan. Distinguir `propuesto`, `no implementado`, `no evaluado`, `falló` y `verificado en alcance`. Una norma futura requiere su versión y fecha efectiva, sin alterar salidas históricas. Informar los regímenes pendientes y dependencias concretas; no declarar cumplimiento global por generar un archivo.
