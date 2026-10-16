# Plantilla de Non-Functional Requirement

Completar los campos con hechos y fuentes. Identificar la función relacionada sin confundirla con la cualidad exigida. Los campos entre `<...>` son instrucciones de autoría, no contenido final.

```markdown
# NFR-XX — Atributo de calidad o restricción

Estado del requisito: Propuesto / Aceptado / Reemplazado / Descartado
Base y versión: <fecha/fuentes>
Responsable: <rol real o pendiente>
Estado de evaluación: <no evaluado/diseñado/verificado/brecha...>

## Alcance

<Perfil, producto/función, usuarios y componentes afectados.>
<Por qué necesita esta cualidad; exclusiones justificadas.>

## Criterios verificables

ID: NFR-XX-C01
Estímulo y origen: <carga, usuario, fallo o cambio>
Objeto/servicio: <qué se evalúa>
Entorno y población: <normal/degradado, datos y volumen>
Respuesta esperada: <efecto observable>
Métrica y unidad: <definición operacional, numerador/denominador>
Ventana y muestreo: <período y cobertura>
Objetivo y fuente: <valor o condición; ley/contrato/meta/supuesto>
Oráculo: <cómo se decide correcto/incorrecto>

## Verificación y evidencia

<Diseño de ensayo, datos sintéticos, instrumentación y fallos.>
<Resultado esperado; observación y evidencia cuando existan.>
<Dependencias que impiden afirmar aceptación.>

## Relaciones y revisión

<Funciones, ADR, CTL y obligaciones aplicables por ID/fuente.>
<Conflictos/tradeoffs, responsable, cambios que exigen revalidar.>
```

Ejemplo de separación: el NFR exige un efecto económico único ante reintento; ADR-02/03 eligen transacción, identidad y outbox/inbox para contribuir a conseguirlo. La palabra «exactly once» de un producto no es el oráculo.
