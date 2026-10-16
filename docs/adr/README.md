# Architectural Decision Records (ADR)

Un **Architectural Decision Record** documenta una decisión arquitectónica: contexto, alternativas, elección, razones, consecuencias, alcance y condiciones de revisión. Un **Non-Functional Requirement** establece una cualidad o restricción verificable que puede motivarla. Crear el registro y aceptar la decisión son acciones distintas.

Los ocho ADR formalizan las decisiones ya enumeradas en [achitecture.md](../achitecture.md), con trazabilidad al [mercado](../market_analysis.md), [cumplimiento](../compliant.md) y sus controles. **Estado inicial: Propuesto; base 15/10/2026; implementación y efectividad sin evaluar.** No se infiere aceptación institucional del pedido de documentar o de que el archivo esté en GitHub.

## Registros y skills

| ADR | Decisión registrada | Skill operativo | NFR relacionados principales |
|---|---|---|---|
| [ADR-01](ADR-01-nucleo-modular.md) | Núcleo modular y fronteras de responsabilidad/despliegue | [adr-01-nucleo-modular](../../.agents/skills/adr-01-nucleo-modular/SKILL.md) | NFR-03, NFR-09, NFR-12 |
| [ADR-02](ADR-02-autoridad-sql.md) | Autoridad financiera SQL, escritor único y transacciones | [adr-02-autoridad-sql](../../.agents/skills/adr-02-autoridad-sql/SKILL.md) | NFR-01, NFR-05, NFR-07, NFR-10, NFR-11 |
| [ADR-03](ADR-03-outbox-inbox.md) | Outbox/inbox, reintentos y efectos externos | [adr-03-outbox-inbox](../../.agents/skills/adr-03-outbox-inbox/SKILL.md) | NFR-01, NFR-04, NFR-07, NFR-08, NFR-11, NFR-13 |
| [ADR-04](ADR-04-alta-disponibilidad.md) | HA local y recuperación regional activa/pasiva | [adr-04-alta-disponibilidad](../../.agents/skills/adr-04-alta-disponibilidad/SKILL.md) | NFR-02, NFR-03, NFR-06, NFR-12 |
| [ADR-05](ADR-05-configuracion-versionada.md) | Configuración limitada, versionada y fechada | [adr-05-configuracion-versionada](../../.agents/skills/adr-05-configuracion-versionada/SKILL.md) | NFR-01, NFR-09, NFR-11, NFR-13 |
| [ADR-06](ADR-06-aislamiento-por-celda.md) | Aislamiento por celda y entidad jurídica | [adr-06-aislamiento-por-celda](../../.agents/skills/adr-06-aislamiento-por-celda/SKILL.md) | NFR-05, NFR-06, NFR-07, NFR-12 |
| [ADR-07](ADR-07-stack-gestionado.md) | Stack acotado, servicios y mensajería gestionados | [adr-07-stack-gestionado](../../.agents/skills/adr-07-stack-gestionado/SKILL.md) | NFR-02, NFR-03, NFR-04, NFR-05, NFR-08, NFR-09, NFR-12 |
| [ADR-08](ADR-08-carga-inicial-masiva.md) | Carga inicial bulk con staging y publicación de cohortes | [adr-08-carga-inicial-masiva](../../.agents/skills/adr-08-carga-inicial-masiva/SKILL.md) | NFR-01, NFR-02, NFR-04, NFR-06, NFR-10, NFR-11 |

Los NFR y sus criterios se consultan en [el registro de requisitos no funcionales](../nfr/README.md). La tabla muestra relaciones técnicas; no prescribe un orden de aprobación ni prueba por sí sola que los requisitos se satisfagan.

## Crear, mantener y aplicar

Usar [core-adr-arquitectura](../../.agents/skills/core-adr-arquitectura/SKILL.md) para crear nuevos registros, comparar alternativas, mantener relaciones y revisar cambios transversales. Su [plantilla](../../.agents/skills/core-adr-arquitectura/references/plantilla-adr.md) incluye contexto, NFR motivadores, consecuencias y evidencia. Los skills específicos permiten aplicar cada decisión a diseño, implementación o revisión según el pedido.

Estados de decisión: **Propuesto**, **Aceptado**, **Reemplazado** o **Descartado**. Aceptado requiere una decisión real con responsable y evidencia; no equivale a software implementado, ensayos satisfactorios o cumplimiento jurídico. Registrar estos estados por separado.

Mantener IDs estables. Si una decisión aceptada se sustituye, conservar su contexto y enlazar ambos registros con motivo/fecha; no borrar la decisión previa. Cambios editoriales y aclaraciones pueden actualizarse con historial. Un pedido autorizado de análisis o corrección reversible puede avanzar sin fabricar una aceptación institucional.

Ejemplo de uso en una sesión que descubra los skills locales:

```text
$core-adr-arquitectura Creá un ADR para la alternativa propuesta,
compará sus tradeoffs y vinculalo con los NFR y decisiones afectados.

$adr-03-outbox-inbox Revisá el envío externo ante caída del worker,
identificá sus estados ambiguos y verificá el efecto financiero único.
```

El [índice general de skills](../skills.md) relaciona workflows de registros, requisitos y cumplimiento.
