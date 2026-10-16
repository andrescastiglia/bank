# Skills de arquitectura, decisiones y requisitos

Los skills locales están versionados bajo `.agents/skills/`. Una sesión de Codex que los descubra puede invocarlos con `$nombre`; la lectura de los archivos permite revisar sus instrucciones sin afirmar que ya estén cargados en todas las sesiones.

## Workflows generales

| Necesidad | Skill | Resultado |
|---|---|---|
| Crear, mantener o revisar **Architectural Decision Records** | [core-adr-arquitectura](../.agents/skills/core-adr-arquitectura/SKILL.md) | Contexto, alternativas, decisión, consecuencias, estado, dependencias y evidencia |
| Crear, mantener o verificar **Non-Functional Requirements** | [core-nfr-calidad](../.agents/skills/core-nfr-calidad/SKILL.md) | Atributo/restricción, escenario, métrica, unidad, ventana, objetivo con fuente, oráculo y resultado |
| Determinar requisitos legales/regulatorios/estándares por perfil | [core-bancario-argentina](../.agents/skills/core-bancario-argentina/SKILL.md) | Aplicabilidad, fuente vigente, control técnico/institucional y evidencia; sin certificación automática |

Los dos nuevos workflows generales cubren el ciclo de vida de ADR y NFR. Se acompañan de **ocho skills específicos de ADR** y **trece de NFR**, enlazados junto con sus registros en [el catálogo ADR](adr/README.md) y [el catálogo NFR](nfr/README.md).

## Cómo trabajar con ellos

1. Identificar si el pedido trata de una función, una decisión de arquitectura o una cualidad exigida. Una función puede involucrar múltiples ADR y NFR.
2. Leer el coordinador correspondiente y sólo los skills específicos afectados. Usar el workflow regulatorio cuando cambien alcance, sujeto, obligación o estándar aplicable.
3. Adaptar el trabajo a **diseñar**, **implementar** o **revisar/verificar**. Los skills contienen entradas mínimas, pasos, invariantes, escenarios de fallo y salida; no son sólo resúmenes de documentos.
4. Mantener `función → NFR/criterio → ADR → componente/cambio → CTL/fuente → prueba/evidencia`. Aceptación de una decisión, implementación y verificación son estados diferentes.
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
```

La línea base es del 15/10/2026. Registros ADR y NFR se crean como **Propuestos**, con implementación/efectividad sin evaluar salvo evidencia real registrada. Este trabajo agrega documentación y workflows; no afirma infraestructura desplegada, ensayos operativos, homologaciones o certificaciones obtenidas.
