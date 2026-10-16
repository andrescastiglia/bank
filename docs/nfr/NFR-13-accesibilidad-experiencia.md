# NFR-13 — Accesibilidad y comprensión de la operación

**Estado:** Propuesto. **Base:** 15/10/2026. **Medición:** sin evaluar. Sujeto y canales concretos pendientes de definir.

## Alcance

Interfaces y documentos para clientes, operadores y responsables autorizados: accesibilidad aplicable, estados comprensibles, información económica fiel y acciones críticas utilizables. El motor interno contribuye con datos y contratos correctos; las pruebas también deben cubrir canales/backoffice y terceros que producen la experiencia.

## Criterios verificables

| ID | Indicador y objetivo propuesto | Escenario y oráculo |
|---|---|---|
| NFR-13-C01 | Todos los criterios del perfil de accesibilidad normativo/contractual aplicable tienen resultado por recorrido/documento crítico | Antes de producción y ante cambios de interfaz: teclado, foco, lector de pantalla, contraste, errores y documentos según el perfil identificado; perfil no definido no permite afirmar conformidad |
| NFR-13-C02 | El 100 % de estados/comprobantes probados distingue recibido, pendiente, rechazado, confirmado y liquidado según producto | Timeout remoto y `202` no se muestran como pago exitoso; el saldo derivado informa fecha y no se presenta como autoridad para gastar |
| NFR-13-C03 | Información de tasa, cargos, CFT y condición contractual coincide con cálculo/asiento y versión aceptada en los casos materiales | Contratación, cambio, pago parcial, mora, cancelación y extracto; sólo conceptos aplicables al producto |
| NFR-13-C04 | Los recorridos aplicables de baja, revocación, reclamo y privacidad conservan acuse, seguimiento y respuesta con su plazo | Verificar canales habilitados, trazabilidad y mensajes sin revelar ROS, investigación o datos de otro cliente |
| NFR-13-C05 | Rechazos y decisiones informan lo exigible con fuente trazable cuando corresponda | Rechazo crediticio basado en información negativa: resultado/fuente conforme al régimen; no divulgar criterios reservados por analogía |

## Verificación y evidencia

Matriz de perfiles/recorridos, pruebas automáticas y evaluación manual pertinente, contratos/comprobantes versionados, casos sintéticos y conciliación con la operación. El objetivo es aprobar los criterios aplicables, no obtener un porcentaje genérico que compense un fallo crítico. Un frontend accesible no demuestra exactitud financiera ni certifica todo el servicio.

## Dependencias y revisión

Relacionar NFR-01/03/05/06/09/11 con ADR-01/03/05/06. Revisar al agregar canal, operador, producto o condición contractual. Fuentes: [arquitectura](../achitecture.md), [cumplimiento](../compliant.md) LAW-06, LAW-08, LAW-12, BCRA-F07 a BCRA-F09, DATA-02 y BCRA-T35 a BCRA-T43 según alcance; CTL-09, CTL-11 y CTL-18. No se agrega aquí una nueva edición técnica como obligación legal universal.

Skill: [nfr-13-accesibilidad-experiencia](../../.agents/skills/nfr-13-accesibilidad-experiencia/SKILL.md).
