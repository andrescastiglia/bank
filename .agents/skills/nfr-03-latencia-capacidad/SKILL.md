---
name: nfr-03-latencia-capacidad
description: "Usar al diseñar, implementar o verificar presupuestos de latencia, percentiles, capacidad, contención y aislamiento bajo carga del core bancario argentino conforme a NFR-03."
---

# NFR-03: latencia y capacidad

## Resultado y entrada mínima

Aplicar [NFR-03](../../../docs/nfr/NFR-03-latencia-capacidad.md) con controles financieros activos. Sus números son metas propuestas al 15/10/2026, sin benchmark ejecutado ni capacidad comercial demostrada. Distinguir diseño, implementación y medición según el pedido. No generar carga en producción ni redimensionar servicios por una solicitud de análisis.

Recoger endpoints, mezcla, volumen/cardinalidad, retención, cuentas concentradoras, tasa y duración de pico, batch simultáneo, regiones/RTT, dependencias, cuotas, recursos y costo. Identificar punto inicial/final de cada trayecto y estado realmente confirmado. Usar [cumplimiento](../core-bancario-argentina/SKILL.md) cuando un plazo venga de riel o normativa; no atribuirle automáticamente los presupuestos locales del proyecto.

## Procedimiento por acción

1. **Diseñar:** mapear NFR-03-C01 a C05 a instrumentos y escenarios. Separar saldo autoritativo, transferencia interna, aceptación durable y resolución externa. Definir dataset, calentamiento, ventana, errores admisibles y condiciones de saturación antes de medir. Si falta una tolerancia o presupuesto degradado, registrarlo pendiente, sin inventar un compromiso.
2. **Implementar:** para el cambio autorizado inspeccionar esperas de locks, llamadas remotas, contención, pools, N+1, índices y operaciones masivas. Mantener autorización, integridad y persistencia. Relacionar ajustes con ADR-02/04/07, sin reabrir decisiones por una optimización especulativa. Si cambia la autoridad o durabilidad, requiere evaluación arquitectónica explícita.
3. **Verificar:** usar carga ofrecida controlada y registrar solicitudes programadas, iniciadas, completadas, rechazadas y expiradas. Contabilizar espera para no ocultar lentitud al saturarse el generador. Ejecutar sólo mediciones proporcionales en el entorno autorizado; para documentos producir el plan y dejar resultados sin evaluar. Conciliar operaciones al terminar, porque un error financiero invalida una mejora de tiempo.

## Metas y oráculos

Medir gateway–respuesta: saldo consistente p95/p99 ≤50/100 ms; transferencia interna ≤100/200 ms incluyendo commit durable; aceptación demorable ≤75/150 ms incluyendo registro durable. No sumarlos entre componentes. Medir adicionalmente red pública y operación externa completa con su propio deadline.

El perfil hipotético contiene 250.000 cuentas/contratos, 100 comandos/s durante 60 min y pico de 500/s durante 10 min, simultáneos con hasta 1.000 lecturas/s. Mezcla monetaria: mitad transferencias internas y mitad aceptación externa; lecturas: mitad consistentes y mitad proyecciones. No derivar capacidad de promedios nacionales ni confundir comando con asiento o transacción facturable.

Buscar colas crecientes, hot accounts, CPU aparentemente baja con locks saturados, falta de conexiones, exclusión de errores del informe y desactivación de controles. Medir año de crecimiento, batch y pérdida de zona; informar que sus presupuestos degradados siguen pendientes si no fueron acordados.

## Evidencia y salida

Conservar dataset sintético, semilla, generador, versiones, recursos/costo, histograma completo, error/timeout, tasa efectiva, saturación, backlog, trazas y conciliación. Entregar `criterio | trayecto | escenario/ventana | carga ofrecida/completada | p95/p99 | objetivo | evidencia | estado/brecha`.

Usar `no evaluado` sin ejecución reproducible; acotar todo resultado al perfil probado. Proponer optimizaciones por evidencia y revisar al cambiar mezcla, volumen, retención, infraestructura o contrato. No prometer capacidad productiva ni cumplimiento jurídico a partir de una estimación o prueba parcial.
