# Revisión de calidad y gobierno de skills

**Revisión:** 16/10/2026. **Commit analizado:** `2e5d579103b94ab70c16d81debe73bf5840ba0c8`. **Base de las fuentes del proyecto:** 15/10/2026. No se actualizaron normas ni se ejecutó una aplicación bancaria. Los ensayos descritos abajo verifican el generador documental en copias aisladas del commit; no son pruebas del producto.

## Alcance y fortalezas comprobadas

Se analizaron los 32 documentos de módulo y su extracción de **1.016 FR**, los 24 flujos, catálogo, mapas, generador, 13 NFR/71 criterios, ocho ADR y los 24 skills existentes con sus metadatos y referencias. El inventario exacto de archivos y los campos completos de cada hallazgo están en [quality.json](findings/quality.json). Se contrastaron la arquitectura, cumplimiento, mercado, índices y contratos de mantenimiento. La revisión combina inspección de textos, inventario de relaciones y mutaciones del verificador; no presenta esa inspección como ejecución de los FR.

La base tiene fortalezas concretas:

- [scope.md](../functional/scope.md) separa especificación, aplicabilidad, implementación, verificación y habilitación. También impide reutilizar IDs retirados y conserva la distinción entre `202`, commit local y liquidación externa.
- [FL-04, FL-07, FL-08, FL-20 y FL-21](../functional/flows.md) incluyen concurrencia, incertidumbre, dos recaudos reales, preparación aislada y recuperación. [NFR-01](../nfr/NFR-01-integridad-financiera.md), [NFR-04](../nfr/NFR-04-asincronia-durable.md) y [NFR-10](../nfr/NFR-10-migracion-carga-masiva.md) preservan las invariantes difíciles, sin confundir broker con autoridad financiera.
- [NFR-02](../nfr/NFR-02-disponibilidad-recuperacion.md) y [NFR-03](../nfr/NFR-03-latencia-capacidad.md) distinguen SLO mensual, ensayo breve, carga ofrecida, RPO observado y objetivos propuestos. No encontré una promesa documental de RPO regional cero sobre replicación asíncrona.
- Los 24 `SKILL.md` son sustantivos: distinguen diseñar, implementar y verificar, contienen fallos/oráculos y no atribuyen cumplimiento o despliegue a la existencia del texto. Los nombres coinciden con sus directorios; los 24 metadatos tienen los campos de interfaz requeridos y sus enlaces locales de archivo resuelven. Esto valida su estructura actual, no su comportamiento en sesiones futuras.
- `python docs/functional/tools/build_catalog.py --check` pasa en el commit analizado. Los denominadores 173/71/21/8 son controles explícitos de esa base fechada; no son un universo jurídico ilimitado ni deben cambiarse silenciosamente al agregar alcance.

## Diagnóstico por perspectiva

**QA funcional:** hay buenos contratos de aceptación en prosa. Falta convertir la selección de piloto en casos identificables, datos esperados independientes y un criterio de salida material. Los 24 flujos citan 219 FR diferentes; son escenarios integrados deliberadamente selectivos, no una suite que permita deducir cobertura de ejecución sobre los 1.016 FR.

**Trazabilidad y herramienta:** el verificador demuestra existencia, forma, relación y reproducibilidad de artefactos. No certifica significado. Las mutaciones muestran dos problemas de mantenimiento adicionales: el retiro de un FR intermedio contradice su política de identidad, y retirar una necesidad del propio denominador manual puede mantener el 100 % publicado sin una decisión de cambio visible.

**Gobierno de skills:** la separación coordinadores/especialistas evita un checklist universal. Sin embargo, los coordinadores fueron escritos sin incorporar todavía la biblioteca FR como entrada de análisis de impacto. Tampoco hay una comprobación conjunta de cambios en los 24 workflows/metadatos ni un registro común que conecte ejecución del workflow, criterio y evidencia.

## Hallazgos y criterios de cierre

### REV-QA-01 — P1: retirar un FR obliga a renumerar los siguientes

**Evidencia:** [scope, identidad](../functional/scope.md) exige IDs estables y no reutilizables. `extract_modules()` en [build_catalog.py](../functional/tools/build_catalog.py) exige `FR-código-(cantidad ya extraída + 1)`. Al retirar sólo la fila FR-CFG-007 de una copia, FR-CFG-008 y todas las siguientes pasan a ser rechazadas por secuencia, aun conservando sus identidades.

**Acción:** conservar un registro de IDs activos/retirados y vínculos de sustitución; validar unicidad y pertenencia sin exigir contigüidad. No reciclar el número ni renumerar las pruebas/consumidores para satisfacer el parser.

**Cierre:** una fixture retira un ID intermedio y mantiene todos los demás; el catálogo distingue retirado/activo, detecta reutilización y exige resolver referencias activas al retirado. Resolver antes del primer retiro/división sustancial de requisitos.

### REV-QA-02 — P1: la cobertura conserva 100 % después de perder significado o retirar una necesidad del denominador

**Evidencia:** en copia aislada, sustituir conducta/aceptación de FR-COR-032 por una consulta de hora, conservando IDs de fuente, permite regenerar y pasar `--check`. También quitar MKT-06 —profundidad financiera y aceptación del piloto— de [coverage_map.json](../functional/coverage_map.json) reduce el inventario comercial de seis a cinco y genera 5/5, 100 %. La advertencia semántica de [coverage.md](../functional/coverage.md) es correcta; falta un contrato de cambio que haga visible esa pérdida.

**Acción:** versionar el inventario manual con altas, retiros y motivo/decisor; producir diff de comportamiento, aceptación y relaciones antes de regenerar. Revisar semánticamente las funciones materiales afectadas; no intentar resolver suficiencia con conteo de palabras o un LLM que autoapruebe cambios.

**Cierre:** eliminar MKT-06 exige decisión explícita y comparación contra la versión anterior; cambiar la prohibición PSCPP de FR-COR-032 aparece como cambio material pendiente de revisión. La comprobación sigue informando por separado consistencia estructural y aprobación semántica.

### REV-QA-03 — P1: el control reproducible no alcanza a los skills que guían los cambios

**Evidencia:** `main()` comprueba enlaces de `docs/functional/*.md` y huellas de fuentes seleccionadas; los skills especializados y `agents/openai.yaml` no integran ese alcance. En copias aisladas, romper el enlace del skill ADR-08 a su ADR y eliminar un campo/cambiar el prompt del metadato NFR-01 mantiene `--check` exitoso incluso antes de regenerar. En la base real esos archivos están correctos.

**Acción:** agregar una validación de skills separada o extendida: frontmatter/nombre, metadatos, referencias, pares registro–skill y manifiesto de versiones. Probar selección de workflow con unos pocos pedidos positivos/negativos materiales; un validador de YAML no demuestra que el agente elija o ejecute bien el workflow.

**Cierre:** ambas mutaciones fallan la verificación correspondiente; los 24 skills originales la pasan. Un cambio editorial menor no dispara ensayos bancarios, y un cambio de instrucción financiera sí exige regresión del escenario afectado.

### REV-QA-04 — P0 antes de aceptar el piloto: falta un denominador de aceptación elegido por perfil y materialidad

**Evidencia:** [mercado §§6 y 12](../market_analysis.md) pide escoger una ruta inicial; [scope, perfiles y activación](../functional/scope.md) permite CREDITO o PAGOS sin desarrollar todo a la vez. FR-ENT-030 y FR-OPS-025 prevén preparación/release, pero el catálogo no contiene aún una selección concreta de perfil, casos obligatorios, responsables, criticidad y excepciones del piloto.

**Acción:** elegir la primera ruta y construir una matriz de aceptación de esa entrega: FR/criterio NFR aplicable, caso, riesgo de fondos/datos/plazo, oráculo, entorno, dueño y evidencia exigible. Definir impedimentos materiales y ampliaciones pospuestas sin aplazar obligaciones del producto activo.

**Cierre:** ninguna ruta financiera activa queda sin prueba de integridad, autorización, respuesta incierta, conciliación y recuperación; un defecto material no se compensa con promedio/porcentaje de pruebas aprobadas. La selección permite empezar desarrollo independiente; no implica probar los 1.016 FR antes del primer piloto.

### REV-QA-05 — P0 antes de aceptar cálculos: faltan vectores monetarios y temporales con valores esperados independientes

**Evidencia:** FR-CFG-008, FR-INT-002, FR-INT-009, FR-INT-012 y FR-INT-014 exigen vectores, precisión, CFT, identidad y ajuste. [NFR-01-C04](../nfr/NFR-01-integridad-financiera.md) y [ADR-05](../adr/ADR-05-configuracion-versionada.md) remiten a resultados históricos aprobados. No hay todavía fixtures de entrada/salida revisadas; no se afirma un defecto de cálculo en software inexistente.

**Acción:** preparar un conjunto sintético con principal/interés/comisión/impuesto separados, redondeo intermedio/final, pago parcial, reverso y cambio de regla sin segundo devengo. Incorporar `America/Argentina/Buenos_Aires`, fin de día/período, feriados/bisiesto, vigencia frente a fecha conocida e índice ausente/corregido; UVA/UVI y forward por diferencia sólo si se activan esas variantes.

**Cierre:** cada fixture tiene versión, fuente de regla, resultado exacto y revisión independiente de quien implemente el cálculo; la misma muestra verifica cotización, contrato, asiento y reporte. No se usa como único oráculo el mismo algoritmo bajo prueba.

### REV-QA-06 — P0 antes de mover fondos en piloto: falta un modelo de prueba reproducible para carreras y efectos externos

**Evidencia:** [ADR-02](../adr/ADR-02-autoridad-sql.md), [ADR-03](../adr/ADR-03-outbox-inbox.md), FR-BAL-014, FR-RSK-006 y FR-ASY-011 a FR-ASY-014 describen las fronteras correctas. [FL-04, FL-07 y FL-08](../functional/flows.md) nombran fallos, pero no enumeran aún intercalados controlados y resultados permitidos/prohibidos como casos independientes.

**Acción:** diseñar fixture de estado inicial, pasos/fallos y oráculo por frontera: crear bloqueo donde no había fila, dos disposiciones de grupo, commit con respuesta perdida, envío antes de caída, worker antiguo tras lease y callback tardío. Separar duplicado de transporte de dos recaudos reales. Incluir pruebas de segregación con dos credenciales de la misma persona/controlador; distintos `principal` no bastan para inferir independencia de funciones.

**Cierre:** cada historia produce un orden válido, un efecto por hecho y un estado ambiguo protegido cuando corresponde; queda verificable que ninguna decisión manual reemplaza evidencia externa. La falta de deduplicación/consulta/fencing del riel tiene resultado de contingencia explícito, no éxito supuesto. El ensayo técnico se ejecutará al existir componentes autorizados.

### REV-QA-07 — P0 antes de comprometer capacidad o corte: faltan una campaña y datasets representativos que combinen carga, bulk y recuperación

**Evidencia:** [NFR-03-C05](../nfr/NFR-03-latencia-capacidad.md) deja presupuestos degradados pendientes; [NFR-10-C01/C07/C08](../nfr/NFR-10-migracion-carga-masiva.md) exige ventana completa, coexistencia y retorno; [NFR-02-C04/C05/C06](../nfr/NFR-02-disponibilidad-recuperacion.md) condiciona restauración a volumen/dependencias. FR-MIG-027 y FR-OPS-013 especifican funciones, sin campaña ejecutada.

**Acción:** fijar población/historial/distribución de cuentas calientes, escenarios normal/pico y backlog, ambiente/topología/recursos, copia limpia/claves y evidencia externa sintética. Componer ensayos: carga con batch, pérdida de zona, bulk con cartera activa, corte con deltas y retorno tras actividad, restauración SQL/broker desalineados y salida independiente.

**Cierre:** informe por escenario conserva carga ofrecida/completada, histogramas/errores, conciliación y costo; bulk mide extracción, transferencia, carga, validación, aplicación, conciliación, corte y margen. Recuperación mide punto durable y pérdida regional real. No inferir SLO mensual de una muestra breve ni fijar throughput comercial antes de medir.

### REV-QA-08 — P1: falta un contrato de evidencia que conecte caso, corrida y aprobación sin editar el catálogo generado

**Evidencia:** [flows, condiciones de aceptación](../functional/flows.md) pide conservar versiones y resultados; FR-OPS-025 exige expediente de release. Los campos actuales de [catalog.json](../functional/catalog.json) son requisitos/relaciones/estados sin evaluar; las salidas de [core-nfr-calidad](../../.agents/skills/core-nfr-calidad/SKILL.md) y los especialistas son tablas útiles, pero no asignan identidad común a caso, corrida, artefacto, revisión y vencimiento de evidencia.

**Acción:** definir registro externo o separado del artefacto generado: `case_id`, FR/criterios y versión, fixture/oráculo, `run_id`, entorno/digests, esperado/observado, artefactos/hash/clasificación, revisor, decisión y evento que exige revalidar. Conservar resultados fallidos/previos; actualizar un documento no convierte en verificado su nuevo significado.

**Cierre:** otra persona reconstruye qué fue probado y qué cambió; regenerar catálogo preserva el registro de pruebas y no reutiliza evidencia de una versión incompatible. Evidencia sensible se exporta minimizada y con permisos/retención por categoría.

### REV-QA-09 — P1: los coordinadores no propagan todavía impacto hacia los FR ni tienen regresión por tipo de cambio

**Evidencia:** [core-adr-arquitectura, propagación](../../.agents/skills/core-adr-arquitectura/SKILL.md) manda actualizar arquitectura/NFR/skills; [core-nfr-calidad, historia](../../.agents/skills/core-nfr-calidad/SKILL.md) hace algo equivalente. Ninguno enlaza la biblioteca funcional incorporada después. [adr-08](../../.agents/skills/adr-08-carga-inicial-masiva/SKILL.md) enumera medición desde extracción a corte omitiendo explícitamente transferencia/margen de NFR-10-C01, ejemplo de por qué coordinar fuentes y evitar listas copiadas.

**Acción:** incorporar análisis inverso `cambio → FR/aceptación → NFR/ADR → casos/evidencia → skills` en coordinadores reutilizables. Son suficientes tres workflows: revisión integral/evidencia, ciclo de vida FR y kickoff/readiness del piloto, que deleguen en los especialistas existentes. No crear skills por rol, por FR o 24 checklists adicionales.

**Cierre:** una regla modificada señala FR/casos afectados, una modificación financiera selecciona concurrencia/duplicados, y bulk/DR selecciona frontera PREPARED, efectos externos y conciliación; edición editorial sólo valida estructura/enlaces. Pedidos de documentación no ejecutan carga ni fondos; pedidos implementables no terminan sólo con recomendaciones. Actualizar enumeraciones de fases desde la fuente NFR, sin rebajar su objetivo.

## Ensayos documentales realizados

Se extrajo el commit con `git archive` a seis carpetas temporales independientes y se ejecutaron comprobación, regeneración y nueva comprobación. El repositorio fuente no se modificó.

| Caso aislado | Cambio | Resultado observado |
|---|---|---|
| Base | Ninguno | `--check`, regeneración y `--check` pasan; 1.016 FR. |
| Retiro | Eliminar fila FR-CFG-007 sin renumerar las siguientes | Falla por secuencia; exige FR-CFG-007 al encontrar FR-CFG-008. |
| Significado | Conservar ID/fuentes de FR-COR-032 y sustituir conducta/aceptación por consulta de hora | Primera comprobación detecta artefacto viejo; regeneración y nueva comprobación pasan. |
| Denominador | Eliminar MKT-06 del mapa comercial | Regenera cinco necesidades y publica 5/5, 100 %, sin decisión de retiro. |
| Skill | Enlace ADR-08 a un archivo inexistente | La comprobación funcional sigue pasando antes y después de regenerar. |
| Metadato | Quitar `short_description` y usar skill inexistente en prompt NFR-01 | La comprobación funcional sigue pasando antes y después de regenerar. |

Estos resultados no significan que las prohibiciones o el contenido de la base real estén erróneos. Delimitan qué detecta el chequeo automatizado y qué control de mantenimiento adicional hace falta. No se propone automatizar una declaración jurídica de conformidad.

## Próximas decisiones y secuencia de QA

Elegir perfil/producto/cliente de diseño y sus responsables institucionales permite fijar la aceptación inicial; mientras tanto pueden prepararse inventarios, fixtures sintéticas y diseño de ensayos. Priorizar exactitud, unicidad, autorización/restricciones, ambigüedad, conciliación y restauración sobre amplitud de productos. Concretar formatos/contratos de riel, vectores aprobados, presupuesto degradado, ventana de migración, BIA y perfil de accesibilidad antes de aceptar las partes que dependen de ellos.

La secuencia sugerida es: arreglar contrato de mantenimiento y revisión de cambios; seleccionar alcance material; preparar fixtures/oráculos y registros de evidencia; implementar una ruta; ejecutar sus pruebas financieras/negativas y de contrato; medir carga/recuperación/bulk pertinentes; revisar hallazgos y habilitaciones reales. Los gates P0 corresponden al compromiso o activación indicado, sin paralizar análisis/desarrollo independiente ya autorizado.
