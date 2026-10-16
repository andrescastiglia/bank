# Non-Functional Requirements (NFR)

Un **Non-Functional Requirement** define cómo debe comportarse una función o servicio en términos de calidad o restricciones verificables. Incluye alcance, estímulo/fallo, entorno, respuesta, métrica/unidad, población/ventana, objetivo con fuente y oráculo. El **Architectural Decision Record** documenta la alternativa elegida para contribuir a cumplirlo.

| Objeto | Ejemplo del proyecto |
|---|---|
| Funcionalidad | Importar una cartera y permitir consultar sus contratos |
| NFR | Completar la carga dentro de la ventana aprobada, sin duplicados ni diferencias financieras inexplicadas y preservando el servicio activo |
| ADR | Usar staging durable, aplicación por conjuntos y activación controlada de una cohorte |

Se formalizan **13 familias de NFR** derivadas del conjunto documentado, con criterios `NFR-XX-CYY`. **Estado inicial: Propuesto; base 15/10/2026; evaluación sin evidencia operativa.** Las metas de arquitectura son propuestas, no benchmarks ni obligaciones universales. Criterios adicionales binarios/de cobertura se identifican como diseño propuesto; toda aceptación exige resolver el perfil y su evidencia.

## Catálogo, criterios y skills

| NFR | Cualidad o restricción | Indicador/oráculo principal | Skill |
|---|---|---|---|
| [NFR-01](NFR-01-integridad-financiera.md) | Integridad financiera | Cero efectos económicos extra, desbalances y omisiones de restricciones en escenarios definidos | [nfr-01-integridad-financiera](../../.agents/skills/nfr-01-integridad-financiera/SKILL.md) |
| [NFR-02](NFR-02-disponibilidad-recuperacion.md) | Disponibilidad y recuperación | SLO mensual propuesto, RTO por fallo y RPO con condiciones explícitas | [nfr-02-disponibilidad-recuperacion](../../.agents/skills/nfr-02-disponibilidad-recuperacion/SKILL.md) |
| [NFR-03](NFR-03-latencia-capacidad.md) | Latencia y capacidad | Percentiles extremo a extremo y carga ofrecida/completada con controles activos | [nfr-03-latencia-capacidad](../../.agents/skills/nfr-03-latencia-capacidad/SKILL.md) |
| [NFR-04](NFR-04-asincronia-durable.md) | Durabilidad y oportunidad de procesos demorables | Pérdidas/duplicados, antigüedad, deadlines y completitud | [nfr-04-asincronia-durable](../../.agents/skills/nfr-04-asincronia-durable/SKILL.md) |
| [NFR-05](NFR-05-seguridad-accesos.md) | Seguridad y acceso autorizado | Acceso indebido denegado y permisos/revocaciones verificables por acción/objeto | [nfr-05-seguridad-accesos](../../.agents/skills/nfr-05-seguridad-accesos/SKILL.md) |
| [NFR-06](NFR-06-privacidad-residencia-retencion.md) | Privacidad, residencia y conservación | Finalidad/retención por categoría y flujos/custodia permitidos | [nfr-06-privacidad-residencia-retencion](../../.agents/skills/nfr-06-privacidad-residencia-retencion/SKILL.md) |
| [NFR-07](NFR-07-auditoria-observabilidad.md) | Auditabilidad y observabilidad | Auditoría material completa y durable; correlación técnica y alertas medidas por separado | [nfr-07-auditoria-observabilidad](../../.agents/skills/nfr-07-auditoria-observabilidad/SKILL.md) |
| [NFR-08](NFR-08-interoperabilidad-portabilidad.md) | Interoperabilidad y portabilidad | Contratos compatibles y exportación/reconstrucción utilizable fuera del proveedor | [nfr-08-interoperabilidad-portabilidad](../../.agents/skills/nfr-08-interoperabilidad-portabilidad/SKILL.md) |
| [NFR-09](NFR-09-mantenibilidad-configuracion.md) | Mantenibilidad y configuración | Cambio/reproducción trazables sin perder invariantes ni historia | [nfr-09-mantenibilidad-configuracion](../../.agents/skills/nfr-09-mantenibilidad-configuracion/SKILL.md) |
| [NFR-10](NFR-10-migracion-carga-masiva.md) | Calidad y desempeño de migración | Ventana completa, conciliación, reanudación, aislamiento previo y retorno | [nfr-10-migracion-carga-masiva](../../.agents/skills/nfr-10-migracion-carga-masiva/SKILL.md) |
| [NFR-11](NFR-11-calidad-datos-reportes.md) | Calidad y reproducibilidad de datos/reportes | Corte completo, linaje, exactitud y evidencia de validación/aceptación | [nfr-11-calidad-datos-reportes](../../.agents/skills/nfr-11-calidad-datos-reportes/SKILL.md) |
| [NFR-12](NFR-12-operabilidad-costos.md) | Operabilidad y restricciones económicas | Cobertura de soporte/runbooks y costo de servicio reproducible bajo el perfil | [nfr-12-operabilidad-costos](../../.agents/skills/nfr-12-operabilidad-costos/SKILL.md) |
| [NFR-13](NFR-13-accesibilidad-experiencia.md) | Accesibilidad y comprensión de estados/documentos | Criterios del perfil por recorrido y mensajes fieles a operación/contrato | [nfr-13-accesibilidad-experiencia](../../.agents/skills/nfr-13-accesibilidad-experiencia/SKILL.md) |

## Relación con decisiones y controles

Los [ocho ADR](../adr/README.md) son mecanismos seleccionados; los NFR son condiciones a verificar. Un mismo NFR puede satisfacerse mediante otra decisión técnicamente viable si se preservan sus condiciones y obligaciones; cambiar el mecanismo requiere analizar y registrar consecuencias, no cambiar el objetivo para esconder una brecha.

Cada registro enlaza sus ADR/CTL y fuentes pertinentes. La [matriz de arquitectura](../achitecture.md#cumplimiento) conserva la cobertura del inventario legal/regulatorio y estándares; el catálogo de NFR no sustituye el encuadre de la entidad ni inventa una certificación.

Conservar por criterio: perfil y fuente; métrica/unidad y población; ventana; entorno/carga/fallo; resultado esperado; método/oráculo; evidencia; versión; responsable y brecha. Separar **estado del requisito** de **resultado de evaluación**. Un ensayo satisfactorio acredita el escenario probado, no todas las cargas futuras.

Ejemplos que requieren precisión:

- El 99,95 % mensual no implica cero errores individuales ni se prueba con un ensayo breve. Tiempo y solicitudes tienen denominadores diferentes.
- Un lag objetivo de 60 segundos no garantiza RPO regional de 60 segundos con réplica asíncrona.
- `202` y acuses prueban recepción durable; una confirmación financiera final exige el estado y persistencia correspondientes.
- Auditoría material no se muestrea para cumplir una meta de trazas. NFR-07-C03 añade una meta propuesta de completitud ≥99 % **de operaciones previamente seleccionadas para trazado**, publicando además la cobertura de muestreo; no es un valor original de la arquitectura ni un permiso de perder evidencia material.
- La preparación de una migración puede ser visible para validadores autorizados y queda excluida de operación, mayor/RI y conciliación ordinarios hasta la activación.

## Crear, mantener y verificar

Usar [core-nfr-calidad](../../.agents/skills/core-nfr-calidad/SKILL.md) y su [plantilla de requisitos](../../.agents/skills/core-nfr-calidad/references/plantilla-nfr.md) para especificar nuevas cualidades, resolver conflictos y mantener la trazabilidad. Los skills especializados aplican criterios a diseño, implementación o verificación según el trabajo pedido. No se ejecutan ensayos productivos por una petición documental.

```text
$core-nfr-calidad Especificá los NFR del nuevo flujo con escenarios,
métricas, ventanas, fuente de objetivos y evidencia de aceptación.

$nfr-03-latencia-capacidad Prepará o ejecutá el ensayo autorizado,
separá carga ofrecida/completada y reportá percentiles y errores.
```

Para perfiles nuevos, IA o funciones especializadas, ampliar las cualidades y controles pertinentes; no considerar el catálogo inicial una cobertura automática de todo producto futuro. El [índice de skills](../skills.md) integra requisitos, decisiones y cumplimiento.
