---
name: nfr-05-seguridad-accesos
description: "Usar al diseñar, implementar o verificar autenticación, autorización por entidad/cuenta/objeto, revocación, segregación de funciones y protección de claves en el core bancario argentino; aplicar los criterios NFR-05."
---

# Seguridad y accesos verificables

## Propósito y fuentes

Convertir [NFR-05](../../../docs/nfr/NFR-05-seguridad-accesos.md) en mecanismos y pruebas trazables. Leer primero ese contrato y [seguridad arquitectónica](../../../docs/achitecture.md#seguridad). Para aplicabilidad, consultar [core bancario Argentina](../core-bancario-argentina/SKILL.md) y sus CTL-03/09/10/15/17; ampliar únicamente las referencias afectadas de cumplimiento. Línea base documental: 15/10/2026; no tratarla como investigación jurídica actualizada ni como certificado ISO/BCRA.

## Entrada mínima

Identificar acción autorizada, versión, entidad/licencia, producto, canales, usuarios y servicios, operaciones sensibles, matriz de permisos/incompatibilidades, puntos de autenticación y almacenes de claves. Determinar celda, cuentas y objetos protegidos; incluir workers, SQL, eventos, exportaciones y soporte. Si faltan datos, avanzar con identidades sintéticas y supuestos explícitos; pedir sólo lo que cambie una decisión. No inferir facultades por marca o por pertenecer a un grupo económico.

## Procedimiento

### DISEÑAR

1. Enumerar activos, actores y amenazas concretas. Para cada operación definir sujeto, entidad, cuenta, objeto, acción y autorización; denegar por defecto. Contrastar ADR-06 y ADR-02 para impedir que un topic, una consulta SQL o soporte eluda el aislamiento.
2. Especificar separación crear/aprobar/liberar para ajustes, parámetros, importaciones y reportes. Seleccionar factores según acción, riesgo, canal y disposición aplicable; distinguir una práctica adoptada de una obligación. No imponer MFA universal por interpretación del nombre del estándar.
3. Definir la efectividad de revocación/bloqueo: fuente autoritativa, transición transaccional, acuse, tratamiento de sesiones vigentes y carrera con comandos. Fijar ciclo de vida de credenciales y claves, incluidos recuperación y DR, según clasificación.

### IMPLEMENTAR

Cuando el pedido incluya implementación, inspeccionar el código y modificar los componentes autorizados: políticas, middleware, autorización de dominio, roles de base, credenciales de servicio y pruebas necesarias. Revalidar permisos y restricciones en la autoridad correspondiente; un JWT o una caché sin revocación efectiva no basta. Preservar auditoría y evitar llamadas remotas dentro del bloqueo monetario. Implementar privilegios temporales y separación real entre sujetos. Proteger claves mediante gestor soportado, sin criptografía propia ni secretos en repositorios/trazas. No desplegar ni comunicar externamente por recibir un pedido de revisión.

### VERIFICAR

Construir un oráculo independiente con matriz de permisos, pertenencia y versiones. Ejecutar casos negativos entre dos entidades, cuentas y objetos; incluir enumeración de identificadores, exportaciones, consumidores y acceso administrativo. Probar baja con sesión anterior, expiración de privilegio y comando concurrente a una revocación; comparar contra el acuse de efectividad, sin atribuir efecto a una orden aún no recibida. Ensayar bypass, replay/recuperación de autenticador y restauración/revocación de claves para el perfil elegido.

Evaluar C01–C04 por ID: accesos indebidos, restricciones omitidas y funciones incompatibles deben ser cero; los controles aplicables deben pasar en su totalidad. Registrar denominador, release y escenario. Una prueba de login o un escáner no sustituye pruebas por objeto ni una evaluación independiente exigible.

## Evidencia y salida

Entregar alcance, cambios realizados, matriz `criterio | escenario | esperado | observado | evidencia | estado | brecha/responsable`, configuración efectiva, versiones y resultados sanitizados. Usar `propuesto`, `no implementado`, `no evaluado`, `falló` o `verificado en alcance`; ausencia de código/evidencia significa no evaluado. Explicar faltantes y siguiente acción concreta. No declarar seguridad integral, homologación o cumplimiento por contar con este skill.
