# NFR-06 — Privacidad, residencia y retención

**Estado:** Propuesto. **Base:** 15 de octubre de 2026. **Responsables propuestos:** responsable de datos, Legal/Cumplimiento y Seguridad. **Evidencia actual:** diseño documental; implementación no evaluada.

## Alcance y perfiles

Incluir datos personales, contratos, legajos, investigación AML, diario, eventos, DLQ, archivos, respaldos, telemetría y soporte remoto. Distinguir responsable, encargado y subencargados por entidad y finalidad. Cada perfil de préstamo, PSP o entidad financiera activa su propio régimen; la nube exterior requiere análisis concreto y, para EF, preservar originales/documentación exigidos en Argentina. Una región primaria local no acredita todos los tratamientos. La portabilidad documentada y la minimización reducen riesgo de implementación y costos de salida para el comprador.

## Criterios verificables

Objetivos de aceptación propuestos, todavía no medidos; base en [seguridad y trazabilidad](../achitecture.md#seguridad).

| ID | Métrica / unidad / ventana | Objetivo y escenario | Fuente / oráculo |
|---|---|---|---|
| NFR-06-C01 | Flujos sin finalidad, rol, país y destinatario / flujos / cambio de despliegue | 0 en inventario contrastado con tráfico, servicios y soporte; incluye DR/KMS/subencargados | DATA-01/04/05/06; inventario y contratos efectivos |
| NFR-06-C02 | Categorías sin política completa / categorías / incorporación o cambio | 0: autoridad, disparador, duración fundada, hold, disposición y nivel de acceso; obligaciones concurrentes evaluadas | CTL-11; matriz de conservación de compliant |
| NFR-06-C03 | Supresiones indebidas o reintroducciones / casos / ensayo de vencimiento/restauración | 0: preservar evidencia obligatoria, retirar difusión vencida y reaplicar disposiciones al restaurar | LAW-05; DATA-02/07; reglas por registro |
| NFR-06-C04 | Solicitudes resueltas en plazo aplicable / solicitudes / cada expediente | 100 % de casos probados: reloj desde recepción, identidad verificada y respuesta fundada; excepciones de conservación explícitas | DATA-02; plazo y calendario del expediente |
| NFR-06-C05 | Exposiciones ROS o cambios de país no habilitados / casos / release y cambio de proveedor | 0 en canales, analítica, soporte y exportaciones generales; activación de DR condicionada al expediente aplicable | AML-11; DATA-05/06; BCRA-T29/34 |

## Validación y evidencia

Ensayar categorías con disparadores distintos, obligaciones concurrentes, hold vigente/levantado, fin de encargo y rectificación. Revisar bases, índices, colas, cachés y ciclo de backups; una marca de borrado no prueba disposición. Conservar inventario, decisiones de aplicabilidad, contratos, prueba de recuperación y certificado técnico de eliminación cuando proceda. Diferenciar eliminación del dato innecesario de preservación restringida del asiento y su soporte. No asignar TTL global, archivo perpetuo ni retenciones numéricas nuevas.

## Trazabilidad y pendientes

[ADR-06](../adr/ADR-06-aislamiento-por-celda.md), [ADR-04](../adr/ADR-04-alta-disponibilidad.md), [ADR-05](../adr/ADR-05-configuracion-versionada.md); CTL-08/10/11/12/16/17. [Cumplimiento](../compliant.md): LAW-03/05; AML-01/02/05/11; DATA-01/02/03/04/05/06/07/08; TAX-09; BCRA-T02/06/13/19/23/26/27/28/29/30/31/32/33/34/40; STD01/04/05/06/10/11/19 según alcance. Pendientes: entidad, categorías efectivas, países, fundamento de transferencias, responsables y política de cada plazo. El inventario de referencias no equivale a cumplimiento demostrado.

Skill operativo: [nfr-06-privacidad-residencia-retencion](../../.agents/skills/nfr-06-privacidad-residencia-retencion/SKILL.md).
