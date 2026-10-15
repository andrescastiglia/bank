# Documentación del core bancario argentino

Investigación en español basada en el análisis aportado por el usuario, ampliada con fuentes primarias. Fecha de corte: **15 de octubre de 2026**.

| Entregable | Contenido |
|---|---|
| [market_analysis.md](market_analysis.md) | Demanda, segmentos, proveedores, evidencia de casos locales, escenarios de mercado y TCO, alternativas de construcción/compra y estrategia de entrada. |
| [compliant.md](compliant.md) | Leyes, BCRA, UIF, AAIP, fiscalidad, ISO y estándares de industria, con aplicabilidad, vigencias, controles y evidencias. |
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
