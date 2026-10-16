# Verificación de los entregables de revisión

**Fecha:** 16/10/2026 UTC. **Diagnóstico de origen:** commit `2e5d579103b94ab70c16d81debe73bf5840ba0c8`. Este registro describe comprobaciones efectivamente realizadas sobre los artefactos de la revisión antes de publicarlos. No registra pruebas de una aplicación bancaria ni certifica obligaciones institucionales.

## Resultados observados

| Comprobación | Resultado local |
|---|---|
| Generador funcional en modo `--check` | Catálogo reproducible: 1.016 FR, 32 módulos, 173 fuentes, 71 criterios NFR, 21 CTL, ocho ADR y 15 módulos lógicos |
| Verificador integral de la revisión | 63 hallazgos asociados a 14 paquetes; inventario histórico de 125 archivos coherente con Git; fuentes, IDs, relaciones y dependencias consistentes |
| Skills | Frontmatter/metadatos YAML de los 27 skills válidos; enlaces locales de documentación/skills comprobados |
| Artefactos | JSON y sintaxis Python válidos; bloques Markdown cerrados; comprobación de whitespace Git sin errores |
| Revisión cruzada | Corregidas precisiones de recuperación regional, devengo/facturación/cobro, payback y cobertura activa de FR retirados; se conserva el diagnóstico original |

La validación utiliza Python 3 y PyYAML 6.0.3, fijado en [requirements.txt](tools/requirements.txt). La configuración de [CI](../../.github/workflows/docs.yml) ejecuta los dos verificadores con permisos de lectura e historial disponible para contrastar hashes. La ejecución local no constituye evidencia de una corrida remota; su estado se consulta en las acciones del commit publicado.

## Casos negativos del nuevo verificador

Se reprodujeron en copias temporales, sin modificar el repositorio de trabajo ni servicios productivos. Cada variante inválida fue rechazada y la copia íntegra volvió a pasar:

| Mutación | Resultado esperado y observado |
|---|---|
| `allow_implicit_invocation` como cadena en vez de booleano | Rechazo de metadata inválida |
| Enlace local roto en ADR-08 | Rechazo, aunque esté fuera del alcance del generador funcional original |
| Hallazgo sin paquete/acción | Rechazo de relación incompleta |
| Dependencia circular entre WP-01 y WP-02 | Rechazo del ciclo |
| Hash del inventario histórico alterado | Rechazo contra el contenido del commit original |
| Criterio del plan distinto del backlog | Rechazo de divergencia entre entregables |
| Hallazgo cerrado con `closure_evidence: true` | Rechazo del tipo incorrecto; se requiere lista de referencias |
| Paquete cerrado con lista de evidencia vacía | Rechazo del cierre sin referencia |

El [informe QA](05-quality-skills.md) registra por separado sus seis ensayos aislados sobre el verificador original y límites de cobertura/semántica. Los nuevos controles estructurales no arreglan automáticamente todos esos límites: retiro histórico/activo, revisión de significado, denominadores versionados y regresión del comportamiento de skills continúan en WP-12.

## Límites y reproducción

```sh
python3 docs/functional/tools/build_catalog.py --check
python3 docs/review/tools/check_review.py
git diff --check
```

Una referencia de evidencia puede ser sintácticamente válida sin demostrar el control; la revisión competente debe examinar contenido, alcance, versión y resultado. Los checks no interpretan leyes, no prueban rentabilidad, no ejecutan escenarios de dinero/seguridad/carga/DR ni demuestran que el agente siga correctamente cada skill. Los 63 hallazgos permanecen abiertos: añadir documentación, YAML y CI no satisface por sí solo sus criterios de negocio o producto.
