# NFR-07 — Auditoría y observabilidad

**Estado:** Propuesto. **Base:** 15 de octubre de 2026. **Responsables propuestos:** Seguridad, Operaciones/SRE y Auditoría independiente. **Evidencia actual:** diseño documental; implementación no evaluada.

## Alcance y perfiles

Cubrir decisiones monetarias, reglas, privilegios, consultas/exportaciones sensibles, migraciones e integraciones. Distinguir auditoría durable de negocio, eventos de seguridad para SIEM y telemetría técnica muestreable. El perfil elegido conserva operaciones y obligaciones de su sujeto; ROS/investigación requieren circuito reservado. La reconstrucción exportable del saldo y del incidente aporta confianza comercial sin prometer una certificación. La correlación usa identificadores internos; secretos, factores, PAN y datos personales innecesarios no ingresan a logs/APM.

## Criterios verificables

Objetivos de diseño, no observaciones. [Arquitectura](../achitecture.md#seguridad) exige auditoría material durable; la exportación protegida puede ser asíncrona.

| ID | Métrica / unidad / ventana | Objetivo y escenario | Fuente / oráculo |
|---|---|---|---|
| NFR-07-C01 | Acciones materiales sin auditoría durable / acciones / ensayo y release | 0 al confirmar commit o completar entrega sensible; caída del exportador no elimina el registro local | CTL-12; BCRA-T22; transacción y manifiesto esperado |
| NFR-07-C02 | Registros auditables reconstruibles / registros / cada ensayo de muestra | 100 % de materiales; actor/acción/hora/canal/motivo/autorización y cambios relevantes; alteración detectada | CTL-12; evidencia original, hash/control de integridad y reloj |
| NFR-07-C03 | Operaciones críticas seleccionadas para trazado con correlación completa / operaciones críticas seleccionadas; ventana mensual | Meta nueva propuesta ≥99 % de la muestra seleccionada antes de observar su resultado; publicar también tasa de muestreo y tamaño/población total. Medir sólo pasos aplicables por flujo; auditoría material mantiene C01/C02 sobre el universo obligatorio | Propuesta adicional de medición; correlación solicitud→asiento→evento y adaptador cuando corresponda |
| NFR-07-C04 | Flujos críticos sin señal y ruta de escalamiento / flujos / release y simulacro | 0: latencia/errores, locks, réplica, outbox, edad/deadline de jobs, ambigüedad y conciliación | Arquitectura operación; CTL-14; fallos inyectados |
| NFR-07-C05 | Incidentes simulados con reloj/expediente correctos / casos / ejercicio | 100 % según obligación aplicable; origen tercero incluido; comunicación por responsable autorizado | BCRA-T20/44/45/46; hitos de ocurrido/detectado y resolución |

## Validación y evidencia

Inyectar caída de SIEM/exportador, duplicación, reloj desviado, manipulación de archivo, cola estancada y pago ambiguo. Verificar que no se confirme una operación material sin auditoría local y que una consulta sensible tenga registro antes de entregar. Recuperar muestra histórica por categoría y medir la disponibilidad exigida. El SIEM no sustituye al archivo probatorio. Guardar resultados sanitizados, reglas de alerta, inventario del denominador, brechas de correlación y expediente del simulacro. El 99 % de telemetría no tolera pérdida del 1 % de auditoría obligatoria.

## Trazabilidad y pendientes

[ADR-02](../adr/ADR-02-autoridad-sql.md), [ADR-03](../adr/ADR-03-outbox-inbox.md), [ADR-04](../adr/ADR-04-alta-disponibilidad.md); CTL-08/10/11/12/13/14/19/20. [Cumplimiento](../compliant.md): LAW-03/05/11; AML-11; DATA-01/03; BCRA-T06/13/18/20/22/23/44/45/46/47; STD01/02/09/11/12/26/29/32 según adopción. Pendientes: taxonomía de acciones, relojes, retención por clase, ventanas/carga y guardia efectiva. Son metas pendientes de prueba, no resultados certificados.

Skill operativo: [nfr-07-auditoria-observabilidad](../../.agents/skills/nfr-07-auditoria-observabilidad/SKILL.md).
