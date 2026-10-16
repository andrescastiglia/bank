---
name: nfr-08-interoperabilidad-portabilidad
description: "Usar al diseñar, implementar o verificar contratos de API/eventos, adaptadores de rieles y salida de proveedor del core argentino, con criterios medibles de compatibilidad, semántica, seguridad y restauración independiente."
---

# NFR-08: interoperabilidad y portabilidad

## Aplicación y entradas mínimas

Aplicar al trabajo solicitado: diseño, implementación, selección de proveedor o verificación. Leer [NFR-08](../../../docs/nfr/NFR-08-interoperabilidad-portabilidad.md) y las secciones enlazadas; consultar [core bancario argentino](../core-bancario-argentina/SKILL.md) para encuadre y controles aplicables. El NFR contiene atributos verificables; los ADR documentan mecanismos y alternativas. No convertir un ensayo en una afirmación de homologación o certificación.

Obtener del contexto entidad/producto, interfaz o conjunto de datos afectado, versiones soportadas, rol de contraparte, finalidad/destino y alcance de la tarea. Para integraciones identificar contrato, perfil de red y deadlines; para salida, inventario, volumen, retención, ventana/presupuesto, destino independiente y custodia de claves. Pedir sólo faltantes que cambien la decisión; avanzar con supuestos explícitos sobre aspectos reversibles. Una ventana desconocida impide declarar aceptación temporal, pero permite preparar pruebas y medir.

## Flujo operativo

1. **Delimitar.** Seleccionar NFR-08-C01 a C06 pertinentes y CTL asociados. Enumerar API, eventos, archivos, documentos, historial y metadatos necesarios. Determinar qué datos requieren canal o permisos separados. La salida completa respeta finalidad, secreto y minimización: no distribuir PAN completo innecesario, secretos o ROS a cualquier destinatario.
2. **Diseñar.** Formular contratos con versión, semántica financiera, autenticación/autorización, errores, correlación, duplicados, orden, cancelación y vencimiento. Definir combinaciones productor/consumidor soportadas y transición; no asumir compatibilidad por compartir JSON o un esquema ISO 20022. Para salida, documentar formato, diccionario, versiones, referencias y recuperación protegida de claves, incluyendo claves envueltas cuando corresponda.
3. **Implementar cuando se solicite.** Inspeccionar contratos, adaptadores, controles de exportación y herramientas existentes; modificar la superficie mínima. Añadir validación de esquema y semántica, autorización por entidad, manifiestos y procedimientos reproducibles según alcance. No sustituir la tarea de código por una matriz documental. Mantener simuladores sin capacidad de emitir fondos reales.
4. **Verificar.** Usar pruebas contractuales y resultados financieros como oráculo: el mismo comando soportado conserva efecto, estado y autorización a través de la evolución. Inyectar duplicados, timeout después del envío, respuesta perdida, reverso y consumidor anterior. Contrastar deadlines con el contrato concreto del riel; ningún valor interno reemplaza el plazo externo. Distinguir pruebas locales, sandbox y resultados formales de contraparte.
5. **Ensayar salida.** Exportar a un destino autorizado y restaurar fuera de la cuenta/servicio administrado por el proveedor saliente, sin depender de sus herramientas privadas inaccesibles. Validar inventario, hashes, relaciones y conciliación por titular/contrato/moneda; reconstruir historial y demostrar uso autorizado de claves. Incluir una prueba negativa de acceso cruzado. Medir horas, bytes, costos de egreso, archivo y coexistencia; un archivo descargable aislado no demuestra portabilidad.

## Evidencia y salida

Entregar resultados por criterio: alcance/versión, objetivo, métrica/unidad, ventana/escenario, observado, evidencia, brecha y siguiente acción. Adjuntar matriz de compatibilidad, resultados de contrato/contraparte, manifiestos, conciliación y procedimiento de restauración según corresponda; evitar datos sensibles en ejemplos o logs.

Usar `sin evaluar`, `implementado sin evidencia`, `verificado` o brecha documentada según lo observado. Si sólo se diseñó, declarar explícitamente que no hay implementación ni mediciones. Si falta una red, clave o destino independiente, conservar la prueba pendiente y su dependencia concreta. No equiparar compatibilidad técnica, participación autorizada y cumplimiento integral.
