# ADR-01 — Núcleo financiero modular

**Estado:** Propuesto. **Base documental:** 15/10/2026. **Implementación y efectividad:** sin evaluar. Este registro formaliza la decisión seleccionada en la arquitectura; no acredita aceptación institucional ni software construido.

## Contexto

El [análisis de mercado](../market_analysis.md) recomienda comenzar por préstamos o por cuentas/pagos de un perfil acotado, con localización argentina y operación demostrables. El producto necesita preservar dinero y restricciones con consistencia fuerte, mientras reportes, conciliación y comunicaciones requieren ritmos de ejecución distintos. Un proveedor nuevo debe controlar el costo de soporte y evitar desarrollar una suite universal o forks por cada cliente.

## Decisión

Mantener un núcleo financiero como **monolito modular**, con responsabilidades, interfaces y propiedad de datos explícitas. Ledger, contratos, posiciones, reservas y límites que participan del mismo invariante comparten la transacción de la celda. API y workers pueden desplegarse por separado usando los mismos comandos y reglas.

Separar primero adaptadores, procesos periféricos y componentes con necesidad real de aislamiento o escalado. Una interfaz interna no implica automáticamente un servicio remoto o una base independiente. Proyecciones, reportes y consumidores no escriben saldos directamente. El modelo de entidad/producto determina las capacidades habilitadas.

La extracción de un módulo exige justificar una necesidad medida y rediseñar explícitamente la consistencia que deja de ser local. Los contratos entre sistemas conservan estado, autoridad, idempotencia y conciliación. La baja latencia y la alta disponibilidad se evalúan junto con el costo operativo, no por el número de servicios.

## Alternativas y consecuencias

| Alternativa | Evaluación |
|---|---|
| Microservicios financieros y una base por módulo desde el inicio | Aumentan coordinación, red, despliegues y recuperación; pueden justificarse más adelante con evidencia y un diseño de los invariantes distribuidos. |
| Monolito sin fronteras | Reduce trabajo inicial de separación, pero permite dependencias y escrituras sin dueño que dificultan evolución, prueba y extracción. |
| Comprar un motor y componer alrededor | Alternativa comercial válida; requiere evaluar cobertura, integración, salida y TCO. Este ADR describe la organización del núcleo propio, no invalida comprar componentes. |

La decisión conserva transacciones locales y reutilización de producto, pero exige disciplina de dependencias y manejo de la base compartida. El escalado del núcleo tiene límites: una cuenta caliente o el writer no desaparecen por multiplicar instancias. Se presupuestan recursos separados para tareas masivas y de canal.

## Criterios de aceptación

1. Un mapa identifica módulo, datos propios, interfaz, responsable y consumidores; las escrituras monetarias atraviesan la frontera del núcleo.
2. Ningún flujo divide fondos, reservas y asiento entre commits independientes sin un protocolo financiero explícito.
3. API y workers ejecutan reglas equivalentes; las pruebas verifican autorización y contabilidad por ambos caminos.
4. Reportes y cargas masivas no degradan el servicio más allá del perfil de rendimiento aprobado; el resultado se mide con la mezcla real.
5. Una extracción presenta alternativas, consistencia, fallos, recuperación, equipo, costo y criterio de salida. La ausencia de código deja esos puntos como diseño pendiente, no como cumplimiento probado.

## Revisión y relaciones

Revisar ante contención persistente, necesidad PCI, conectividad o escalado independiente, incompatibilidad de equipos/despliegues o costo de coexistencia. Relacionado con ADR-02, ADR-03, ADR-06 y ADR-07; no prescribe su orden de aprobación. Cambiar el alcance comercial obliga a volver a evaluar las fronteras.

Fuentes: [arquitectura, estrategia y módulos](../achitecture.md#estrategia), [cumplimiento](../compliant.md) BCRA-T05, BCRA-T17 y BCRA-T25; [controles](../../.agents/skills/core-bancario-argentina/references/controles.md) CTL-01, CTL-03, CTL-04, CTL-15 y CTL-17. Estos controles contribuyen al diseño; la modularidad no certifica normas ISO.

Skill operativo: [adr-01-nucleo-modular](../../.agents/skills/adr-01-nucleo-modular/SKILL.md).

## NFR relacionados

[NFR-03](../nfr/NFR-03-latencia-capacidad.md), [NFR-09](../nfr/NFR-09-mantenibilidad-configuracion.md), [NFR-12](../nfr/NFR-12-operabilidad-costos.md). Son cualidades y restricciones a verificar; la elección de este mecanismo no demuestra por sí sola su satisfacción.
