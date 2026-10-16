# NFR-05 — Seguridad y accesos

**Estado:** Propuesto. **Base:** 15 de octubre de 2026. **Responsables propuestos:** Seguridad e identidad; dueño de cada operación. **Evidencia actual:** diseño documental; implementación no evaluada.

## Alcance y perfiles

Aplicar al núcleo, backoffice, APIs, workers, soporte, bus, archivo y accesos administrativos de cada celda. Préstamos, cuentas de pago y entidades financieras comparten denegación por defecto y aislamiento; las obligaciones por canal, autenticador, tarjetas o licencia se seleccionan expresamente. La ventaja comercial es ofrecer un producto reutilizable con permisos y evidencia explicables, sin bifurcar código por cliente. MFA se determina por acción, riesgo y obligación aplicable; no se afirma un mandato universal para todo inicio de sesión.

## Criterios verificables

Todos son objetivos de aceptación propuestos, todavía no medidos. Fuente de diseño: [arquitectura, seguridad](../achitecture.md#seguridad).

| ID | Métrica / unidad / ventana | Objetivo y escenario | Fuente / oráculo |
|---|---|---|---|
| NFR-05-C01 | Accesos indebidos exitosos / casos / release material | 0 en pruebas negativas por entidad, cuenta, objeto y acción, incluyendo SQL, eventos, soporte y exportación | CTL-09/17; matriz de permisos y pertenencia |
| NFR-05-C02 | Restricciones o revocaciones omitidas / operaciones / ensayo concurrente | 0 después del acuse de efectividad; comandos en carrera respetan el punto transaccional definido | Arquitectura; CTL-03/09; secuencia y versión autoritativas |
| NFR-05-C03 | Combinaciones incompatibles habilitadas / casos / cambio de roles | 0 para crear/aprobar/liberar ajustes, reglas, cargas y reportes; privilegios temporales expiran | CTL-09; matriz institucional de incompatibilidades |
| NFR-05-C04 | Controles criptográficos/autenticadores aplicables aprobados / controles / release | 100 % del alcance elegido: bypass, recuperación, revocación, rotación y restauración de claves; sin secretos en trazas | CTL-10; BCRA-T12/13 y reglas del canal |

## Validación y evidencia

Usar identidades y cuentas sintéticas de dos entidades, sesiones previas a una baja, trabajadores con mensajes demorados y un cambio concurrente de mandato. Registrar solicitud, resultado, versión de autorización y momento de efectividad; recibir una orden no demuestra su aplicación. Inspeccionar permisos efectivos y credenciales de servicio, no sólo pantallas de roles. Probar separación con usuarios distintos y restaurar claves en entorno aislado. Conservar resultados sanitizados, configuración efectiva, versión de software y brechas; un escáner aislado no acredita estos criterios.

## Trazabilidad y pendientes

[ADR-06](../adr/ADR-06-aislamiento-por-celda.md), [ADR-02](../adr/ADR-02-autoridad-sql.md), [ADR-05](../adr/ADR-05-configuracion-versionada.md); CTL-03/09/10/15/17. [Cumplimiento](../compliant.md): LAW-03/11; DATA-03; AML-11; BCRA-T03/09/11/12/13/14/25/36/37/38/39/40/41/42; STD01/02/03/04/19/20/21/22/23/24/25/26/27/28/29 según activación. Quedan pendientes perfil/licencia, canales, matriz aprobada, política de privilegios, algoritmo/gestor de claves y evidencia ejecutada. El mapeo identifica referencias afectadas, sin acreditar conformidad integral ni certificación ISO.

Skill operativo: [nfr-05-seguridad-accesos](../../.agents/skills/nfr-05-seguridad-accesos/SKILL.md).
