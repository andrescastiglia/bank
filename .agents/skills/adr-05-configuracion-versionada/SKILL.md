---
name: adr-05-configuracion-versionada
description: "Usar al diseñar, implementar o revisar parámetros de productos, reglas fiscales/contables, vigencias, cambios y reproducción histórica del core según ADR-05."
---

# Aplicar ADR-05: configuración con historia

## Alcance

Aplicar configuración moderada sobre fórmulas/capacidades soportadas, con versiones fechadas y trazabilidad. La línea base del 15/10/2026 tiene estado **Propuesto**; comprobar su estado actual antes de cambiarla. No inventar tasas, umbrales, alícuotas ni fechas normativas reales para completar ejemplos.

Leer el [ADR-05](../../../docs/adr/ADR-05-configuracion-versionada.md) y [arquitectura](../../../docs/achitecture.md#configuracion). Usar [core-bancario-argentina](../core-bancario-argentina/SKILL.md) si el cambio requiere determinar fuente, sujeto, vigencia o requisito legal; este skill implementa el tratamiento técnico de reglas, no sustituye esa determinación.

## Entrada mínima

Identificar regla/producto, entidad, moneda/jurisdicción, objetivo del cambio, fórmula existente, momento efectivo y tratamiento contractual. Inspeccionar esquema, selector, caché, configuración instalada y consumidores disponibles. Si sólo hay documentación, proponer modelo, simulación y criterios sin afirmar resultados operativos. Avanzar con supuestos explícitos en tareas independientes de datos faltantes.

## Procedimiento

1. **Clasificar el cambio.** Distinguir parámetro de una fórmula soportada, nuevo algoritmo, mapeo contable o ampliación de licencia/producto. Un algoritmo nuevo necesita código y validación; no introducir scripting/SQL genérico para evitarlo.
2. **Modelar identidad y tiempo.** Definir regla y versión; sujeto/producto/moneda/jurisdicción; fuente; validez de negocio e historia de registro/conocimiento. Establecer política para solapamientos, fechas abiertas, calendario y resolución de versión. La versión conocida hoy no se presume conocida en un corte histórico.
3. **Definir estados y roles.** Borrador, simulación, revisión y aprobación aplicables al proceso institucional. Registrar actor, motivo y evidencia sin fabricar firmas o aceptaciones. Los requisitos de una operación productiva no impiden preparar una propuesta reversible.
4. **Distribuir y activar.** Verificar esquema/integridad del paquete; instalar localmente y cambiar una referencia en transacción, con auditoría. Validar versión y vigencia también al ejecutar. Definir tratamiento permitido ante versión faltante; nunca elegir silenciosamente la última o una tasa por defecto.
5. **Conservar resultados.** Persistir las versiones de contrato, cálculo, índice, calendario, fiscalidad y plan de cuentas usadas. El reintento de la misma operación conserva identidad económica. El devengamiento base es único por contrato/tipo/período, sin agregar versión de regla a esa identidad.
6. **Simular y aplicar la acción pedida.** Comparar antes/después en la población afectada, montos, redondeos, CFT y reportes. Para implementar, cambiar selector/esquema/código/configuración disponible y ejecutar verificaciones materiales. Para revisión, reportar hallazgos y escenarios; para diseño, dejar contratos y backlog verificables.
7. **Corregir sin reescribir.** Cambios retroactivos generan diferencias y ajustes vinculados aprobados según rol. Rollback técnico selecciona una versión válida para decisiones futuras; no revierte una liquidación, borra el cálculo original ni altera un reporte aprobado sin rectificativa.

## Invariantes y escenarios

- No permitir flags que anulen partida doble, aislamiento, permisos, auditoría o controles legales del perfil.
- No consultar el plano administrativo remoto en cada débito. Una versión local válida puede seguir operando con ese plano caído; una versión vencida no se vuelve válida por la caída.
- Activar una versión y ejecutar una operación concurrente produce una selección coherente y auditable; la caché respeta versión/ámbito.
- Probar frontera temporal anterior/igual/posterior, feriados, contrato previo, regla ausente, intervalos ambiguos, paquete alterado y activación no aprobada.
- Probar recalcular con otra regla sin duplicar devengo; comparar ajustes, asientos, extracto y reporte. Utilizar datos sintéticos y vectores monetarios revisados.

## Salida y evidencia

Entregar cambio o diseño con matriz `regla | fuente | ámbito | versión | validez/conocimiento | población | simulación | activación | evidencia | estado`. Incluir diferencias monetarias, dependencias, pruebas ejecutadas y pendientes. Usar `diseñado`, `implementado sin evidencia` o `verificado` según lo observado; no certificar cumplimiento por tener versionado.

Relacionar con CTL-02, CTL-06, CTL-12, CTL-15, CTL-18 y CTL-19 y con ADR-02/03 para efectos financieros/eventos. Registrar cualquier cambio de decisión y su impacto en los otros ADR; no introducir una excepción silenciosa a los invariantes.
