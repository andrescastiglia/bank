# Plantilla de revisión integral

## Contexto y evidencia

Registrar commit, alcance, inventario, fecha de revisión y corte de cada fuente; materias/personas revisoras; evidencia observada, excluida y pendiente. Conservar versiones/hash cuando sean relevantes. Indicar si sólo hay diseño, prototipo o servicio real.

| Perspectiva | Preguntas materiales | Evidencia para avanzar |
|---|---|---|
| Comercial | ¿Quién compra, qué dolor paga, qué reemplaza y por qué cambiaría? | Perfil objetivo, entrevistas verificables, decisión de compra, alcance y referencia comparable |
| CEO/finanzas | ¿Cada contrato aporta margen y caja suficiente? ¿Qué financia el aprendizaje? | Modelo mensual por cohorte, costos cotizados, capacidad de entrega, escenarios y sensibilidad |
| Contabilidad/impuestos | ¿Qué política y oráculo explican cada flujo? ¿Cómo factura y tributa el proveedor? | Circuitos de asientos/cálculos, aprobación profesional y ciclo factura–cobro–retenciones |
| Legal | ¿Quién está habilitado y quién responde? ¿Qué derechos se entregan? | Perímetro, licencia/IP, contratos, datos, terceros, vigencia y conservación |
| Arquitectura/datos | ¿Quién es autoridad? ¿Cómo se resuelven concurrencia, fallo y cambio de autoridad? | Contratos, modelo de datos, protocolos, ADR, pruebas de alternativa y costos |
| QA | ¿Cuál es el oráculo independiente? ¿Qué excepciones materiales se verifican? | Casos/versiones, fixtures aprobados, fallos, conciliación y evidencias reproducibles |
| Seguridad | ¿Qué activos/fronteras/actores se atacan? ¿Cómo se recupera el control? | Modelo de amenazas, políticas efectivas, pruebas negativas y recuperación de identidad/claves |
| Operaciones | ¿Quién ejecuta el día de negocio, incidentes, cierres, migración y salida? | RACI real, runbooks, guardia/contrapartes y ensayos por roles distintos del autor |
| Producto/personas | ¿El alcance es reutilizable, comprensible, accesible y mantenible? | Ruta del usuario, límites de producto, cambios comunes, entrenamiento y sustitución de responsables |

## Ficha de hallazgo

```text
ID estable / título:
Clase: decisión pendiente, especificación, evidencia, inconsistencia u oportunidad:
Fuente: archivo + sección + IDs; hecho observado:
Activador y alcance afectados:
Efecto económico, financiero, legal u operativo:
Acciones y alternativas:
Criterio de cierre / evidencia / versión:
Responsable sugerido / dependencias / paquete del plan:
Prioridad P0-P1-P2 y justificación del hito:
Estado observado / estado de acción / próxima revisión:
```

## Consolidación

Una acción puede resolver varios hallazgos y un hallazgo puede necesitar varios paquetes. Revisar que todos tengan dueño, siguiente acción y cierre verificable. Los umbrales de negocio deben tener fuente o quedar como propuesta pendiente; una aceptación interna no exonera una obligación legal. Una fuente inaccesible se registra como limitación, no se reemplaza por certeza.
