# Skills del proyecto de core bancario

Los skills locales están versionados bajo `.agents/skills/`. Una sesión de Codex que los descubra puede invocarlos con `$nombre`; la lectura de los archivos permite revisar sus instrucciones sin afirmar que ya estén cargados en todas las sesiones.

## Workflows generales

| Necesidad | Skill | Resultado |
|---|---|---|
| Crear, mantener o revisar **Architectural Decision Records** | [core-adr-arquitectura](../.agents/skills/core-adr-arquitectura/SKILL.md) | Contexto, alternativas, decisión, consecuencias, estado, dependencias y evidencia |
| Crear, mantener o verificar **Non-Functional Requirements** | [core-nfr-calidad](../.agents/skills/core-nfr-calidad/SKILL.md) | Atributo/restricción, escenario, métrica, unidad, ventana, objetivo con fuente, oráculo y resultado |
| Determinar requisitos legales/regulatorios/estándares por perfil | [core-bancario-argentina](../.agents/skills/core-bancario-argentina/SKILL.md) | Aplicabilidad, fuente vigente, control técnico/institucional y evidencia; sin certificación automática |
| Revisar el proyecto desde negocio, controles y operación | [core-project-review](../.agents/skills/core-project-review/SKILL.md) | Diagnóstico por perspectiva, hallazgos sustentados y plan con dependencias y cierre verificable |
| Crear, mantener o retirar **Functional Requirements** | [core-fr-requisitos](../.agents/skills/core-fr-requisitos/SKILL.md) | FR observables, IDs estables, aplicabilidad, aceptación, diferencias semánticas y relación con casos/evidencia |
| Preparar kickoff o evaluar preparación de piloto | [core-pilot-kickoff](../.agents/skills/core-pilot-kickoff/SKILL.md) | Charter, economía, responsables, dependencias, agenda operativa y criterios G0–G4 |
| Ejecutar vigilancia normativa y preparar propuestas | [core-regulatory-watch](../.agents/skills/core-regulatory-watch/SKILL.md) | Cobertura por fuente, novedades verificadas, agenda/checkpoints y PR; únicamente el mantenedor realiza el merge |

El repositorio incluye **28 skills: siete workflows generales, ocho específicos de ADR y trece de NFR**, enlazados junto con sus registros en [el catálogo ADR](adr/README.md) y [el catálogo NFR](nfr/README.md). Los workflows de revisión, FR y kickoff se incorporan con la [revisión integral](review/README.md); vigilancia normativa se incorpora con el [gobierno GPL](../GOVERNANCE.md). Reutilizan arquitectura/calidad/cumplimiento y evitan un skill por rol o por cada FR.

## Cómo trabajar con ellos

1. Identificar si el pedido trata de una función, una decisión de arquitectura o una cualidad exigida. Una función puede involucrar múltiples ADR y NFR.
2. Leer el coordinador correspondiente y sólo los skills específicos afectados. Usar el workflow regulatorio cuando cambien alcance, sujeto, obligación o estándar aplicable.
3. Adaptar el trabajo a **diseñar**, **implementar** o **revisar/verificar**. Los skills contienen entradas mínimas, pasos, invariantes, escenarios de fallo y salida; no son sólo resúmenes de documentos.
4. Mantener `cambio ↔ FR ↔ NFR/criterio ↔ ADR ↔ componente ↔ CTL/fuente ↔ caso/oráculo/evidencia ↔ skill`. Revisar el impacto en ambas direcciones. Aceptación de una decisión, implementación y verificación son estados diferentes.
5. Conservar fuentes/versiones y actualizar registros e índices ante cambios. Una meta propuesta no es una medición, una elección tecnológica no es un NFR y un ADR no sustituye una autorización o licencia.

Ejemplos:

```text
$core-adr-arquitectura Compará alternativas de persistencia para este cambio,
creá o actualizá el Architectural Decision Record y vinculá los NFR afectados.

$core-nfr-calidad Definí los requisitos no funcionales de recuperación,
con fallos, escenarios, RTO/RPO y evidencia necesaria sin inventar resultados.

$adr-08-carga-inicial-masiva Diseñá o implementá la ruta bulk autorizada
con checkpoints, conciliación y activación de cohorte según la arquitectura.

$nfr-10-migracion-carga-masiva Verificá ventana completa, diferencias,
unicidad, aislamiento de preparación y retorno de la carga inicial.

$core-project-review Contrastá este proyecto desde negocio, contabilidad,
legal, arquitectura, QA, seguridad y operaciones y priorizá sus mejoras.

$core-fr-requisitos Revisá este cambio de comportamiento, conservá IDs
y propagá aceptación, fuentes, casos, NFR, ADR y evidencia afectados.

$core-pilot-kickoff Prepará el kickoff de una ruta de producto con equipo,
dependencias y criterios de avance; distinguí desarrollo de piloto real.

$core-regulatory-watch Revisá novedades oficiales, recuperá gaps de cobertura,
verificá fechas y aplicabilidad y prepará una PR sin fusionarla.
```

La línea base es del 15/10/2026. Registros ADR y NFR se crean como **Propuestos**, con implementación/efectividad sin evaluar salvo evidencia real registrada. Este trabajo agrega documentación y workflows; no afirma infraestructura desplegada, ensayos operativos, homologaciones o certificaciones obtenidas.

Los workflows agregados el 16/10/2026 no revalidan por sí solos las fuentes regulatorias del día anterior. El [plan de mejoras](review/improvement_plan.md) conserva pendientes de retiro de FR, deriva semántica y regresión de comportamiento. La comprobación YAML/enlaces valida estructura y no demuestra que el agente aplique correctamente cada escenario.

Todos los workflows están sujetos a [AGENTS.md](../AGENTS.md): ramas y propuestas; ningún agente hace push directo, merge o auto-merge a `main`. La programación de vigilancia se gestiona por separado; un archivo SKILL no es un proceso activo ni prueba cobertura.
