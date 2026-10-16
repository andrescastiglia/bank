# Registro de evidencia y cierre de mejoras

**Plantilla sin ejecuciones registradas.** Mantener hallazgo, acción, decisión, implementación y evidencia como objetos relacionados, con sus propios estados.

| Campo | Contenido requerido |
|---|---|
| Identidad | ID de hallazgo REV, paquete WP, FR/NFR/ADR/CTL/fuente y caso de aceptación |
| Alcance | Sociedad/rol, producto, monedas, jurisdicción, entorno, población y versión |
| Tipo | Diseño, decisión, contrato, configuración, código, prueba, acuse o ejercicio operativo |
| Oráculo | Fuente independiente, cálculo esperado, contraparte, conciliación o criterio observado |
| Ejecución | Actor/rol, instante, entradas/fixture, pasos, fallos, resultado esperado/observado |
| Evidencia | Ubicación protegida, hash/manifiesto, acceso, retención, fecha y limitaciones |
| Revisión | Revisor competente, independencia exigida, resultado, excepción y decisión vinculada |
| Estado | No evaluado, preparado, ejecutado con brecha, verificado en alcance, no aplica con fundamento |
| Reapertura | Cambio de fuente/código/configuración/tercero/fecha, vencimiento de evidencia o nuevo incidente |

Los documentos públicos del repositorio guardan referencias y resultados sanitizados; contratos, datos personales, secretos y ROS se conservan sólo en el destino autorizado. Verificar la evidencia antes de declarar cierre. Un resultado válido para una versión/cohorte no se extiende automáticamente a todas las entidades/productos.

## Prueba de cierre

```text
Hallazgo y criterio original:
Acción implementada / versión / responsable:
Caso, población y oráculo independiente:
Resultado observado y enlace protegido:
Qué prueba y qué no prueba:
Revisión/decisión real y remanentes:
Fecha o disparador de reevaluación:
```

Conservar el hallazgo de la línea base. Una mejora de workflow puede prepararlo para ejecución sin cerrar el riesgo de negocio. No cambiar el umbral después de observar el ensayo para ocultar una brecha, ni marcar una obligación legal como dispensada mediante una excepción interna.
