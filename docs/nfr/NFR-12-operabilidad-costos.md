# NFR-12 — Operabilidad y costos de servicio

**Estado:** Propuesto. **Base:** 15/10/2026. **Medición:** sin evaluar; no hay servicio operativo acreditado.

## Alcance

Capacidad de operar el perfil contratado, detectar y resolver problemas y sostener su costo con responsables y evidencia. El [mercado](../market_analysis.md) exige repetibilidad, soporte y salida, además de tecnología. Este NFR evalúa resultados de operación; ADR-01/07 eligen la organización y plataforma que contribuyen a ellos.

## Criterios verificables

| ID | Indicador, ventana y objetivo propuesto | Escenario y oráculo |
|---|---|---|
| NFR-12-C01 | Cobertura del 100 % de flujos críticos habilitados por dueño, guardia/escalamiento y runbook vigente; evaluar antes del piloto y ante cambio material | Inventario de BIA/producto confrontado con responsables y ejercicio; un nombre sin disponibilidad ni procedimiento no basta |
| NFR-12-C02 | Todos los incidentes materiales de la muestra conservan detección, clasificación, responsable, acciones, comunicaciones y resolución; relojes según perfil/contrato | Simular caída propia/tercero y comprobar expediente y deadlines aplicables; no imponer un MTTR legal universal |
| NFR-12-C03 | Costo mensual por celda, contrato/cuenta operada y unidad técnica calculable, con moneda y supuestos explícitos | Conciliar base/réplicas, bus, almacenamiento/WAL, egreso, claves, observabilidad, entornos, guardia, licencias, localización y salida con la fuente de costos |
| NFR-12-C04 | Presupuesto y capacidad remanente contrastados con el escenario aprobado, antes de ampliar exposición | Medir costo y recursos con carga, fallos y retención activos; límite económico lo fija el caso de negocio, no este documento |
| NFR-12-C05 | Prueba de operación y salida ejecutable por roles distintos del autor original | Runbook con evidencia reproducible, acceso mínimo y recuperación/escalamiento; registrar dependencias personales sin afirmar que desaparecieron |

## Verificación y evidencia

Inventario de servicios críticos, RACI, cobertura de soporte, expediente del ejercicio, métricas, costos/desglose, supuestos y resultado. Medir tiempos observados y compararlos con objetivos del perfil; pendientes o umbrales económicos no definidos permanecen explícitos. La aceptación institucional y los avisos regulatorios los realizan sus responsables; un tablero no los sustituye.

## Dependencias y revisión

Depende de NFR-02/03/04/07 y ADR-01/04/07. Revaluar al agregar cliente, producto, tercero, retención o región, y cuando un incidente o costo contradiga el modelo. Fuentes: [arquitectura, operación](../achitecture.md#operacion), [cumplimiento](../compliant.md) BCRA-T02, BCRA-T04, BCRA-T15 a BCRA-T20, BCRA-T26 a BCRA-T33; CTL-13 a CTL-16. El costo es un objetivo de negocio, no una dispensa de controles.

Skill: [nfr-12-operabilidad-costos](../../.agents/skills/nfr-12-operabilidad-costos/SKILL.md).
