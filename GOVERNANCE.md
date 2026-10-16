# Gobierno del proyecto

**Decisión del mantenedor, 16/10/2026:** desarrollar el proyecto conforme a la licencia GNU GPL v2 existente y reservar los merges a `main` exclusivamente a **[@andrescastiglia](https://github.com/andrescastiglia)**.

## Licencia y contribuciones

[LICENSE](LICENSE) conserva su texto. Las contribuciones deben ser compatibles con la licencia del proyecto, mantener atribución/procedencia e identificar dependencias y materiales de terceros. No se introduce doble licenciamiento, cesión exclusiva ni excepción propietaria por esta decisión. El carácter libre permite usos comerciales compatibles; no significa ausencia de costos, mantenimiento o responsabilidad operativa.

La revisión comercial anterior sigue siendo una referencia de costos, opciones y riesgos. La venta de una suite, el ARR o los clientes de diseño dejan de ser condiciones generales para contribuir al proyecto libre. Quien decida ofrecer servicios comerciales deberá evaluar sus contratos, impuestos y viabilidad; esto no modifica las exigencias del sujeto que opere servicios financieros reales.

La decisión resuelve la orientación del proyecto. Quedan por verificar la procedencia de cada aporte, la compatibilidad de componentes concretos y cualquier obligación de entrega aplicable. Los hallazgos históricos de la revisión no se cierran retroactivamente ni se reescriben como si esa decisión hubiese existido antes.

## Roles y flujo de cambios

| Rol | Facultad |
|---|---|
| Mantenedor `@andrescastiglia` | Prioriza, acepta/rechaza y realiza los merges a `main` |
| Personas contribuyentes | Proponen cambios en ramas/forks, aportan evidencia y responden revisión |
| Agentes de IA | Investigan, preparan propuestas y pruebas, publican ramas/PR dentro del alcance autorizado |
| CI | Verifica y reporta resultados; carece de autorización para aprobar o fusionar |
| Revisión especializada | Aporta criterio legal, contable, de seguridad o producto; no representa al operador ni sustituye su habilitación |

Una PR puede estar técnicamente lista y seguir pendiente de la decisión del mantenedor. Nadie debe usar auto-merge, una API o credenciales del dueño para atribuir a la persona un merge ejecutado por un agente. No se bloquea la investigación o el desarrollo independiente por esperar esa decisión sobre otra PR.

## Aplicación técnica en GitHub

[CODEOWNERS](.github/CODEOWNERS) asigna la revisión al mantenedor; no limita por sí solo quién puede fusionar. La automatización de CI mantiene permisos de lectura y no contiene pasos de merge.

Comprobación de esta sesión: repositorio público, dueño `andrescastiglia`, auto-merge desactivado, consulta de rulesets sin reglas listadas y consulta de protección de `main` rechazada por la integración con **HTTP 403**. También se intentó crear, por la API oficial, un ruleset que restringiera actualizaciones de `main` a PR con bypass del administrador del repositorio; esa operación fue rechazada con **HTTP 403**. Por ello, **la protección efectiva de `main` no está acreditada ni se declara configurada**. No se intentó eludir esa limitación.

Para imponer la política desde GitHub, el mantenedor debe configurar reglas/permisos de `main` que exijan PR, bloqueen actualización directa, borrado y force-push, y reserven la actualización mediante PR al dueño. Configurar checks según el alcance, revisión y conversaciones resueltas sin crear un requisito de autoaprobación imposible. Verificar los actores de bypass y que ninguna app/bot tenga bypass de merge. Un solo aprobador requerido no equivale a un único actor habilitado para fusionar.

Se deja una [plantilla de ruleset](.github/main-ruleset.example.json) revisable para aplicar desde Settings → Rules → Rulesets con una sesión autorizada. Restringe actualizaciones, borrado y force-push de `main`, exige PR y concede bypass sólo mediante PR al rol administrador. Antes de aplicarla, verificar que ese rol sólo corresponda al mantenedor y que la identidad de agentes/apps sea distinta; si cambia la propiedad o existen otros administradores, adaptar actores/permisos. **La plantilla no se aplica automáticamente y no prueba exclusividad por persona.** No exige otra aprobación numérica para evitar que el único mantenedor deba aprobar su propia PR.

Las credenciales de un agente deben corresponder a una identidad separada, con mínimos permisos sobre ramas/PR y sin administración/bypass de `main`. Si usa credenciales indistinguibles de las del dueño, las reglas basadas en identidad no pueden distinguir al humano del agente; la política documentada sigue aplicándose, pero no constituye una barrera técnica suficiente.

### Bloqueo de force-push/borrado y check obligatorio

Por pedido explícito del mantenedor se intentó configurar estas tres protecciones. La API volvió a rechazar la creación del ruleset con **HTTP 403 — Resource not accessible by integration**; la lectura de protección también devolvió 403 y la lista de rulesets estaba vacía. Por tanto, **estas protecciones no quedaron aplicadas ni verificadas** desde esta integración.

La [configuración lista para importar](.github/main-protection.ruleset.json) apunta sólo a `refs/heads/main`, bloquea borrado y actualizaciones no fast-forward y exige el check **`documentation`**, emitido por **GitHub Actions (app 15368)**. Exige que la rama esté actualizada con su base y no incluye actores de bypass. Es adicional a la plantilla de gobierno anterior: no concede permisos de merge ni reemplaza restricciones de identidad/PR existentes. El nombre del check y su app se verificaron contra una ejecución real aprobada en `main`.

El [workflow](.github/workflows/docs.yml) ejecuta ese check en todas las PR, sin filtros de archivos en `pull_request`, para que una PR de código o estado no quede esperando un check omitido. Esto valida documentación; no sustituye pruebas de producto futuras. Antes de activar la exigencia, integrar este cambio de workflow mediante el merge del mantenedor.

Para aplicar la configuración con una sesión administrativa autorizada: abrir **Settings → Rules → Rulesets → New ruleset → Import a ruleset**, seleccionar el JSON y comprobar `Active`, destino `main`, ausencia de bypass y los tres controles. Después verificar desde GitHub que un fallo o check pendiente impide el merge y que borrado/force-push están restringidos; no intentar borrar ni forzar `main` para probarlo. Importar el archivo o fusionar el workflow no se considera evidencia de protección hasta observar la regla activa.

## Vigilancia y decisiones regulatorias

Se establece [vigilancia normativa diaria](docs/regulatory-watch/README.md), con fuentes oficiales, cobertura por fuente, agenda de vigencias, deduplicación e impacto trazable. El agente prepara propuestas y deja la integración al mantenedor.

Fusionar una mejora no certifica cumplimiento de una entidad. La aplicación efectiva depende del perfil, producto, fecha, implementación, prueba y decisiones institucionales correspondientes. Un cambio normativo puede necesitar una modificación de código, parámetros, documentos, operación o contrato, y no siempre obliga al núcleo o a todos sus usuarios.
