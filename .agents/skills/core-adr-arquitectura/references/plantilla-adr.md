# Plantilla de Architectural Decision Record

Usar como guía y completar con hechos y fuentes. Las expresiones entre `<...>` son campos de autoría; no deben quedar como hechos en un ADR terminado. No cambiar registros aceptados para ocultar una decisión anterior.

```markdown
# ADR-XX — Título de la decisión

Estado: Propuesto / Aceptado / Reemplazado / Descartado
Fecha y versión de fuentes: <fecha>
Responsable de decisión: <rol o persona real; pendiente si no existe>
Implementación/verificación: <estado separado de aceptación>
Reemplaza / reemplazado por: <ID y vínculo si corresponde>

## Contexto

<Problema concreto, perfil/producto, negocio, restricciones y evidencia.>
<NFR que motivan la decisión, con ID/criterios y escenario.>

## Decisión

<Qué se elige, dónde aplica y quién tiene autoridad sobre datos/acciones.>
<Garantías, límites y tratamiento de fallos.>

## Alternativas y razones

<Alternativas viables, tradeoffs y motivo de selección o descarte.>
<Distinguir mediciones, supuestos y presupuesto.>

## Consecuencias

<Beneficios, costos, nuevas dependencias, riesgos y trabajo de transición.>

## Criterios de aceptación y evidencia

<Escenario, resultado observable, NFR/CTL, evidencia y estado actual.>
<La prueba pendiente sigue pendiente; no fabricar resultados.>

## Revisión y relaciones

<Cuándo reconsiderar, dependencias y repercusión en otros ADR/NFR.>
<Fuentes locales/oficiales revisadas y su alcance.>
```

Separar aceptación de la decisión, preparación para producción, prueba operativa y conformidad jurídica. Documentar la evidencia correspondiente a cada una sin exigir una nueva confirmación para todo trabajo reversible.
