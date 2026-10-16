# Documentación del core bancario argentino

Investigación en español basada en el análisis aportado por el usuario, ampliada con fuentes primarias. Fecha de corte: **15 de octubre de 2026**.

| Entregable | Contenido |
|---|---|
| [market_analysis.md](market_analysis.md) | Demanda, segmentos, proveedores, evidencia de casos locales, escenarios de mercado y TCO, alternativas de construcción/compra y estrategia de entrada. |
| [compliant.md](compliant.md) | Leyes, BCRA, UIF, AAIP, fiscalidad, ISO y estándares de industria, con aplicabilidad, vigencias, controles y evidencias. |
| [achitecture.md](achitecture.md) | Arquitectura modular, configuración versionada, consistencia financiera, asincronía, HA, baja latencia y carga inicial masiva con trazabilidad a requisitos. |
| [ADR: Architectural Decision Records](adr/README.md) | Ocho registros de decisiones: contexto, alternativas, elección, consecuencias y criterios de revisión, con sus skills. |
| [NFR: Non-Functional Requirements](nfr/README.md) | Trece familias de requisitos de calidad y restricciones verificables, con escenarios, métricas, objetivos, oráculos y skills. |
| [FR: Functional Requirements por módulo](functional/README.md) | 1.016 requisitos funcionales en 32 módulos, con aceptación, excepciones, perfiles, 24 flujos integrados y cobertura trazable del inventario documental. |
| [Skills de ADR y NFR](skills.md) | Workflows para crear, mantener, aplicar y verificar registros y requisitos; selección e invocación de skills específicos. |
| [Skill: core-bancario-argentina](../.agents/skills/core-bancario-argentina/SKILL.md) | Procedimiento reutilizable para verificar fuentes y convertir requisitos en controles, pruebas y backlog. |
| [Registro de fuentes BCRA](research/bcra_sources.json) | Metadatos y huellas SHA-256 de los documentos descargados; las URLs de textos ordenados pueden actualizar su contenido. |

El skill se encuentra en la ruta local `.agents/skills/core-bancario-argentina/`. Está preparado para que Codex lo descubra al cargar los skills del repositorio; no se publicó ni instaló un plugin en una cuenta externa. Una sesión que lo tenga disponible puede invocarlo con `$core-bancario-argentina`.

Sus referencias están separadas por materia:

- [Leyes y autoridades transversales](../.agents/skills/core-bancario-argentina/references/leyes.md).
- [Regulaciones BCRA](../.agents/skills/core-bancario-argentina/references/regulaciones-bcra.md).
- [ISO](../.agents/skills/core-bancario-argentina/references/iso.md).
- [Normas y estándares de industria](../.agents/skills/core-bancario-argentina/references/estandares-industria.md).
- [Controles técnicos y criterios de aceptación](../.agents/skills/core-bancario-argentina/references/controles.md).
- [Método de verificación y mantenimiento](../.agents/skills/core-bancario-argentina/references/metodologia.md).

La investigación distingue datos comprobados, declaraciones de proveedores, estimaciones ilustrativas y requisitos condicionados. Para aplicar la matriz normativa a una operación real, completar entidad jurídica, licencia/registro, productos, monedas, jurisdicciones, terceros y fecha de puesta en producción. Revisar cambios posteriores al corte y las transiciones futuras ya identificadas.

La [matriz de cobertura funcional](functional/coverage.md) relaciona las 173 entradas de cumplimiento, los 71 criterios NFR, ocho ADR, 21 controles y 15 módulos lógicos de arquitectura con FR concretos. El 100% indica relaciones dentro de ese inventario fechado; implementación, evidencia y habilitación institucional permanecen sin evaluar. El [alcance funcional](functional/scope.md) conserva condiciones por licencia, producto y especialidades que requieren investigación adicional.
