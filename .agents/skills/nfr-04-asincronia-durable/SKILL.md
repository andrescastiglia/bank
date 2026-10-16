---
name: nfr-04-asincronia-durable
description: "Usar al diseñar, implementar o verificar durabilidad, unicidad de efectos, frescura, deadlines, reintentos y recuperación de trabajos asíncronos del core bancario argentino conforme a NFR-04."
---

# NFR-04: asincronía durable

## Resultado y entrada mínima

Aplicar [NFR-04](../../../docs/nfr/NFR-04-asincronia-durable.md), línea base propuesta del 15/10/2026, para evaluar calidad del procesamiento independientemente del broker elegido. Identificar si se solicita diseñar, implementar o verificar; no ejecutar replay, reenvío externo ni cambios productivos por una petición documental.

Recoger inventario de trabajos, productor/consumidor, identidad, estado durable, deadline, dueño, autoridad financiera, contrato externo y capacidad de consulta/deduplicación. Determinar volumen normal/pico, retención, backlog tolerable y punto de restauración. Consultar [cumplimiento](../core-bancario-argentina/SKILL.md) para plazos exigibles por sujeto/producto; una DLQ no pausa una obligación y cinco segundos no es un plazo legal universal.

## Procedimiento por acción

1. **Diseñar:** mapear NFR-04-C01 a C06 y distinguir recepción, aceptación durable, publicación, aplicación y finalización externa. Mantener controles preventivos, fondos y restricciones antes del efecto financiero. Especificar estados ambiguos, reloj inicial, recuperación, identidad económica, orden por agregado y evidencia de completitud. Registrar fuente y margen de cada deadline.
2. **Implementar:** dentro del cambio autorizado revisar fronteras de commit/acuse, recuperación del trabajo reclamado, deduplicación durable y entrega externa según ADR-03. Preservar referencias a través de reintentos y no asumir atomicidad con una llamada de red. Separar recursos por criticidad; limitar concurrencia para sostener plazos. Instrumentar edad, tasa efectiva, espacio y margen antes del vencimiento, sin borrar pendientes para mejorar métricas.
3. **Verificar:** seleccionar caídas antes/después del commit local y del acuse, publicación repetida, hueco/reordenamiento, evento inválido, worker rezagado y bus caído. Comprobar estado esperado tras recuperar y conciliar contra un manifiesto del universo. Ejecutar ensayos proporcionados sólo con implementación y entorno autorizados; para análisis entregar diseño de prueba, no mediciones ficticias.

## Oráculos y fallos

Exigir cero trabajos aceptados sin recuperación, efectos financieros duplicados, reenvíos externos históricos y cierres declarados con faltantes sin resolver. La unicidad de devengamiento se define por entidad/contrato/tipo/período: otra versión de regla no crea un nuevo hecho base. El replay de proyecciones inhibe por defecto pagos, correos y presentaciones externas.

Un lease vencido protege transiciones locales sólo si se verifica su token; no impide que el worker anterior llame al tercero. Ante envío potencial, conservar estado ambiguo y resolver por consulta/conciliación e aislamiento cuando corresponda, sin reenvío ni liberación automática de reserva. Reproducir también restauración donde broker, inbox y estado financiero representan puntos diferentes.

Para flujo ordinario, medir p99 ≤5 s desde commit hasta publicación y hasta proyección utilizable en carga normal. Informar ambas ventanas y la edad más antigua; tareas con deadline distinto requieren presupuesto propio. El p99 puede ocultar excepciones: escalarlas con dueño y reloj, no declararlas procesadas por estar en cuarentena.

## Evidencia y salida

Conservar versiones, configuración, identificadores sintéticos, cronología, offsets/checkpoints, manifiestos, conteos de efectos, antigüedad y conciliación. Entregar `criterio | flujo | deadline/fuente | escenario | objetivo | observado | evidencia | estado/brecha` y procedimiento de resolución de ambiguos.

Usar `no evaluado` sin ejecución o contrato necesario; acotar toda conformidad técnica al escenario probado. No afirmar cumplimiento normativo ni homologación del riel. Revisar ante nuevos consumidores, esquemas, obligaciones, integraciones, capacidad o cambios de recuperación.
