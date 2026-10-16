---
name: core-pilot-kickoff
description: "Usar para preparar el kickoff de desarrollo o evaluar la preparación de un piloto de core bancario, con alcance, economía, RACI, dependencias, evidencias operativas y criterios de avance."
---

# Preparar kickoff y piloto

## Propósito y alcance

Preparar trabajo concreto y verificable para una ruta de producto. Distinguir kickoff de investigación/desarrollo con datos sintéticos de activación con datos/fondos/clientes reales. Leer [plan de mejoras](../../../docs/review/improvement_plan.md), revisión de [seguridad/operación](../../../docs/review/06-security-operations.md), perfiles/FR y NFR/ADR afectados. Reutilizar [el checklist](references/kickoff-checklist.md); no repetir los trece workflows NFR para cada edición.

Aplicar [el gobierno GPL](../../../GOVERNANCE.md). Para contribución al proyecto libre, adaptar G1/G4 a alcance, recursos, mantenimiento y reutilización; no imponer ventas, ARR o clientes de diseño como requisito de contribución. Para un servicio comercial, usar además su economía/contratos. Un piloto con datos/fondos reales mantiene todos los controles del sujeto. Todo cambio del agente va en rama/PR y sólo el mantenedor fusiona a `main`.

## Procedimiento

1. **Fijar el hito pedido.** G0 kickoff; G1 decisión de inversión/oferta; G2 diseño validado; G3 piloto real limitado; G4 repetibilidad/escala. Los criterios son de gestión del proyecto, no nuevos permisos legales. Registrar estado observado y evidencia, sin aprobar en nombre de responsables.
2. **Definir charter y ruta.** Identificar cliente objetivo, sociedad/rol, problema, producto incluido/excluido, flujos de fondos/datos, contraparte y autoridad. Elegir crédito o pagos por evidencia comercial, alcance jurídico, costos y capacidad; la biblioteca de 32 módulos no es un compromiso de construirlos simultáneamente.
3. **Contrastar economía y equipo.** Presupuestar por mes descubrimiento, construcción, integración, impuestos/cobros, soporte/guardia, HA/DR, actualización y salida. No prometer SLA, precio de producción o margen sin disponibilidad/cotizaciones y responsables. Mantener supuestos, financiación y contingencia diferenciados de ingresos contratados.
4. **Preparar el trabajo.** Crear backlog acotado con responsables y capacidad disponible, dependencias, hitos observables, revisión contable/legal y contratos de contraparte. Desarrollar una sección vertical con oráculos sintéticos antes de ampliar. Documentar funciones incompatibles, suplencias y accesos; dos cuentas de una persona no prueban independencia.
5. **Reunir evidencia por riesgo.** Verificar invariantes monetarias, integraciones, residencia, seguridad y reconstrucción/DR aplicables. Cubrir datos/canales/control plane y dependencias de identidad/claves. No declarar recuperabilidad de una operación local perdida sólo porque se puede consultar un riel externo.
6. **Preparar el día de negocio.** Asignar agenda de pendientes, ambigüedades, fondos/respaldo, conciliación, cierres, tributos/reportes, atención, incidentes, cambios y entrenamiento. Cada tarea tiene responsable/suplente, reloj, runbook y evidencia. Ensayar por alguien distinto del autor original con permisos mínimos.
7. **Preparar activación y retorno.** Fijar cohorte/exposición, barrera de autoridad, condiciones de suspensión, consultas y compensación permitidas, comunicación y soporte. Baseline/apertura/historia excluyentes; rollback no borra liquidaciones. Acordar quién decide y qué prueba necesita, sin ejecutar por el mero pedido de plan.
8. **Revisar preparación.** Mostrar evidencia válida, pendientes, impacto y responsable por criterio. Una obligación aplicable sin resolver no se vuelve excepción aceptable por decisión interna. Continuar análisis y tareas independientes; restringir sólo el hito afectado. Para G4 demostrar segundo cliente reutilizable y costo/margen sostenibles, sin afirmar negocio rentable a partir de ARR aislado.

## Salida y límites

Entregar charter propuesto, RACI, secuencia de trabajo, registro de dependencias, checklist del hito, evidencias/pendientes y decisión que corresponde al responsable. Señalar las tareas ya realizadas y las propuestas. El workflow no autoriza contrataciones, comunicaciones a terceros/autoridades, uso productivo, despliegues ni cambios de licencia. La autorización de esas acciones proviene de la sesión y de los responsables competentes.
