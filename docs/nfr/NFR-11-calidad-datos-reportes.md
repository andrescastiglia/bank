# NFR-11 — Calidad de datos y reportes

**Estado:** Propuesto. **Base:** 15 de octubre de 2026. **Responsables propuestos:** Finanzas, Fiscal/Cumplimiento y dueños de datos. **Evidencia actual:** diseño documental; implementación no evaluada.

## Alcance y perfiles

Cubrir datos contractuales y contables, conciliación, cierres y archivos BCRA/UIF/ARCA/COMARB efectivamente aplicables. Préstamos, PSP y banco seleccionan paquetes distintos por sujeto, producto y período. Proyecciones y reportes asíncronos no autorizan fondos. La localización argentina versionada, el saldo explicable y las presentaciones reproducibles respaldan la propuesta comercial; ofrecer un formato diseñado no acredita su aceptación ni homologación.

## Criterios verificables

Objetivos de aceptación propuestos, todavía no medidos. Base: [arquitectura, módulos y datos](../achitecture.md#modulos) y [trazabilidad](../achitecture.md#cumplimiento).

| ID | Métrica / unidad / ventana | Objetivo y escenario | Fuente / oráculo |
|---|---|---|---|
| NFR-11-C01 | Fuentes/particiones requeridas incompletas al cerrar / fuentes / cada corte | 0; snapshot consistente o barrera con watermarks por fuente, universo esperado y tardíos definidos | CTL-19; manifiesto de completitud independiente |
| NFR-11-C02 | Diferencias inexplicadas / importe exacto y registros / corte por entidad-moneda-titular | 0 entre origen, submayor, mayor y reporte; exclusiones/ajustes tienen fundamento, responsable y aprobación | CTL-01/05/19; ecuación de saldos y controles de totales |
| NFR-11-C03 | Campos/transformaciones materiales sin linaje / campos / versión de reporte | 0; reproducir resultado con datos, reglas, catálogos e índices históricos | BCRA-T06/24; manifiesto y dataset preservados |
| NFR-11-C04 | Presentaciones declaradas aceptadas sin validación completa / expedientes / cada envío | 0; estados generado/enviado/recibido/aceptado/rechazado/rectificado separados | RPT-01–08/AML-12 según perfil; acuse y validación del destinatario |
| NFR-11-C05 | Mutaciones silenciosas o intervención incompatible / casos / corrección y cambio de versión | 0; cambios tardíos producen nueva versión o rectificativa vinculada, nunca reemplazo sin historia | CTL-06/09/19; versiones aprobadas y reglas de período |

## Validación y evidencia

Probar fuente atrasada aunque otra tenga offset mayor, faltante y duplicado compensados en total global, redondeo, asiento tardío, ajuste manual, rechazo remoto y rectificativa. Repetir un corte con insumos/versiones preservados y comparar salida canónica; cualquier diferencia de empaquetado se justifica. Conservar manifiesto, conciliación por dimensión, linaje, archivo/hash, aprobación y respuesta del receptor. El término de un worker y el ticket de subida no prueban completitud ni aceptación. Los deadlines se derivan del régimen y disparador efectivos, sin SLA universal inventado.

## Trazabilidad y pendientes

[ADR-02](../adr/ADR-02-autoridad-sql.md), [ADR-03](../adr/ADR-03-outbox-inbox.md), [ADR-05](../adr/ADR-05-configuracion-versionada.md); CTL-01/02/05/06/07/08/09/18/19/20. [Cumplimiento](../compliant.md): LAW-05/06/07/08/09/16; AML-03/08/09/10/12; DATA-01/07; TAX-01/02/03/04/05/06/07/08/10/11; BCRA-F10/11/12/13/14/15/16/17/18; PAY-01/02/03/04/05/06/07/08/09/10/11; RPT-01/02/03/04/05/06/07/08; BCRA-T06/18/21/24; STD14/17/18/32 según producto. Pendientes: regímenes definitivos, formatos vigentes, calendario, fuentes y dueños. Se mapean referencias afectadas; las 173 entradas requieren aplicabilidad específica, no una declaración global.

Skill operativo: [nfr-11-calidad-datos-reportes](../../.agents/skills/nfr-11-calidad-datos-reportes/SKILL.md).
