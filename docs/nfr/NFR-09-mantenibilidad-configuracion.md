# NFR-09 — Mantenibilidad y configuración controlada

**Estado:** Propuesto. **Línea base:** 15 de octubre de 2026. **Responsables propuestos:** Arquitectura, Producto y Entrega; Finanzas/Cumplimiento según el cambio. Metas pendientes de implementación y pruebas.

## Alcance y motivación

Evolución de módulos, reglas, configuración por entidad/contrato, esquemas y despliegues. Un producto compartido y actualizable, con parámetros acotados y evidencia histórica, reduce personalizaciones y costo de actualización según el posicionamiento y TCO documentados. Un algoritmo financiero nuevo requiere código revisado, sin convertir cualquier comportamiento en configuración ejecutable.

## Criterios medibles

| ID | Métrica y unidad | Ventana/escenario | Objetivo propuesto | Fuente |
|---|---|---|---|---|
| NFR-09-C01 | Cambios con trazabilidad completa, % | Cada cambio material de código, esquema o parámetro | 100% vincula requisito, versión, pruebas, revisión/aprobación aplicable, artefacto y despliegue; cero forks permanentes por cliente | Arquitectura §§3, 15; CTL-15 |
| NFR-09-C02 | Operaciones históricas reproducibles, % | Cada cambio de reglas; casos anteriores, futuros y retroactivos | 100% usa versión exacta; conserva vigencia de negocio y fecha de registro/aprobación; cero intervalos ambiguos aceptados | Arquitectura §9; CTL-02, CTL-06, CTL-18 |
| NFR-09-C03 | Activaciones inválidas o parcialmente visibles, cantidad | Activación concurrente; scheduler/plano de configuración caído | Cero reglas futuras, vencidas, ausentes o no aprobadas utilizadas; referencia activa atómica y sin fallback silencioso | Arquitectura §9; CTL-09, CTL-12 |
| NFR-09-C04 | Bypass de controles mediante configuración, cantidad | Cada flag/perfil y prueba negativa de permisos | Cero omisiones de partida doble, aislamiento, autorización, auditoría o control legal aplicable; cero SQL/scripts arbitrarios en reglas de negocio | Arquitectura §§5, 9; CTL-01, CTL-09, CTL-17 |
| NFR-09-C05 | Casos de actualización/reversión compatibles, % | Cada release; versiones coexistentes soportadas y cambio de esquema | 100% de casos aprobados preserva contratos y operaciones; cero borrados/reversiones de dinero ya ejecutado por rollback técnico | Arquitectura §15; CTL-04, CTL-15 |
| NFR-09-C06 | Tiempo de cambio, horas; costo, moneda/base; trabajo específico, horas/cliente | Por cambio y revisión de release | Medir desde solicitud hasta activación; comparar con objetivo aprobado para ese tipo de cambio y registrar regresiones; sin promesa universal | Mercado §§6, 8, 12; arquitectura §15 |

## Aceptación y evidencia

Entregar historial de cambios, configuración efectiva, simulaciones financieras, pruebas de límites temporales y permisos, matriz de versiones y ensayo de despliegue/reversión. La reversión debe preservar el original y registrar ajustes autorizados cuando corresponda. Medir mantenibilidad mediante cambios representativos, incluyendo una nueva fórmula que requiera código; contar módulos o cobertura aislada no demuestra facilidad de cambio. Si falta un objetivo temporal/económico, registrar la medición y su aprobación pendiente.

## Dependencias y trazabilidad

[Configuración](../achitecture.md#configuracion), [módulos](../achitecture.md#modulos), [operación](../achitecture.md#operacion); [ADR-01](../adr/ADR-01-nucleo-modular.md), [ADR-05](../adr/ADR-05-configuracion-versionada.md); [mercado/TCO](../market_analysis.md); [cumplimiento](../compliant.md#bcra-tecnologia), BCRA-T17, STD13–14. CTL-01–02, CTL-04, CTL-06, CTL-09, CTL-12, CTL-15, CTL-17–18 sustentan los escenarios.

Skill operativo: [nfr-09-mantenibilidad-configuracion](../../.agents/skills/nfr-09-mantenibilidad-configuracion/SKILL.md).
