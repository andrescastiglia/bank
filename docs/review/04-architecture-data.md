# Revisión 04 — Arquitectura y datos

**Fecha de revisión:** 16/10/2026. **Commit examinado:** `2e5d579103b94ab70c16d81debe73bf5840ba0c8`. **Línea base de fuentes:** 15/10/2026. **Alcance:** revisión documental de ingeniería; implementación, verificaciones operativas y aprobación institucional siguen separadas y sin acreditar.

La base sostiene una arquitectura coherente para iniciar un producto acotado. Sus principales riesgos actuales son **decisiones de diseño que deben concretarse para el flujo y entorno elegidos**, antes de repartir implementación o comprometer un servicio. Se registran **nueve hallazgos**, sin atribuir defectos de ejecución a software inexistente. La revisión no pide multiplicar servicios ni imponer Kubernetes, un nuevo motor o toda la banca universal al primer piloto.

## Fortalezas comprobadas en la documentación

- **Autoridad monetaria y consistencia local explícitas:** ADR-01/02 y BAL/LED conservan fondos, reservas, límites, asientos, auditoría y outbox en una frontera transaccional; contemplan guardianes incluso para la primera restricción.
- **Asincronía con semántica financiera:** ADR-03 y ASY mantienen entrega al menos una vez, inbox/efecto local atómicos, offset posterior al commit y separación entre lease local y fencing remoto. `202`, confirmación local y liquidación externa están diferenciados.
- **HA con límites honestos:** ADR-04 distingue durabilidad síncrona local, pérdida regional posible y recuperación integral. No presenta lag objetivo como RPO garantizado ni réplica como backup.
- **Reglas e historia conservadas:** ADR-05 y CFG/INT separan vigencia y conocimiento, preservan versiones y evitan duplicar devengamientos por cambiar la regla.
- **Bulk y coexistencia financieramente controlados:** ADR-08 y MIG preservan transacción fuente completa, identidad entre corridas, frontera PREPARED y exclusión mutua entre apertura e historia; retorno no borra operaciones reales.
- **Trazabilidad documental reproducible:** `python3 docs/functional/tools/build_catalog.py --check` terminó correctamente sobre la baseline: 1016 FR, 32 módulos, 173 fuentes, 71 criterios NFR, 21 CTL, ocho ADR y 15 módulos lógicos. Se leyó el generador y los mapas: el resultado verifica extracción, referencias y huellas; **no verifica suficiencia semántica ni comportamiento bancario**, límite que los documentos ya explican.
- **Skills ajustados a la acción solicitada:** los ocho especializados y sus coordinadores contemplan diseñar, implementar o revisar, distinguen propuesta de evidencia y no fabrican permisos institucionales para tareas reversibles.

## Diagnóstico por perspectiva

| Perspectiva | Estado documental observado | Próximo resultado revisable |
|---|---|---|
| Arquitectura y APIs | Fronteras/semántica propuestas coherentes; comandos conceptuales | Contrato normativo del primer circuito y responsables de transición |
| Modelo SQL | Invariantes y estrategia de bloqueo definidos; modelo lógico aún no fijado | Claves/cardinalidades y receta de transacción por comando |
| Eventos y trabajos | Outbox/inbox, reintento, DLQ y replay especificados por resultado | Cursores, continuidad de feeds autorizados y horizontes de reconstrucción |
| Migración | Bulk, PREPARED, barrera y autoridad única definidos | Protocolo de acuerdo con legado y callbacks que cruzan el corte |
| Datos y reportes | Manifiestos/linaje/completitud exigidos | Barrera concreta por régimen y consistencia SQL–objetos |
| Continuidad y costos | Metas hipotéticas y restricciones declaradas | Fuentes sobrevivientes, oferta/sitios reales y presupuesto durable |

## Prioridades y hallazgos

P0 significa resolver antes del **hito afectado** indicado; no denuncia un incidente ni detiene prototipos independientes. P1 completa la entrega controlada. Los criterios siguientes cierran la brecha **de diseño**; no sustituyen las pruebas futuras de implementación ni la decisión institucional.

| Hallazgo | Prioridad | Naturaleza | Hito afectado |
|---|---|---|---|
| REV-ARC-01 — Fijar el contrato de comandos y estados del primer flujo | P0 | Especificación por concretar | Antes de dividir entre equipos la implementación del primer comando monetario y de integrar su primer canal o riel. |
| REV-ARC-02 — Concretar el modelo lógico y el protocolo de guardianes SQL | P0 | Especificación por concretar | Antes de implementar el esquema financiero y los comandos concurrentes del primer producto. |
| REV-ARC-03 — Definir el corte entre cores y el destino de callbacks en vuelo | P0 | Especificación por concretar | Antes de un ensayo de corte de cohorte que incluya operación concurrente o instrucciones externas pendientes. |
| REV-ARC-04 — Resolver secuencias filtradas, cursores y horizonte de replay | P1 | Especificación por concretar | Antes de implementar publicadores redundantes, consumidores con orden o la política de purga/reconstrucción. |
| REV-ARC-05 — Seleccionar una barrera de corte que vincule SQL y fuentes externas | P0 | Decisión pendiente | Antes de implementar el primer cierre o dataset regulatorio que combine más de una fuente. |
| REV-ARC-06 — Demostrar qué hechos locales son reconstruibles tras perder la región | P0 | Especificación por concretar | Antes de aceptar el perfil de DR regional o comprometer su RTO/RPO con un cliente. |
| REV-ARC-07 — Contrastar topología, garantías gestionadas y costo con una oferta real | P0 | Decisión pendiente | Antes de seleccionar proveedor, fijar presupuesto de infraestructura o vender el perfil de disponibilidad/latencia. |
| REV-ARC-08 — Dimensionar backlog durable, WAL y recuperación con ingreso continuo | P1 | Especificación por concretar | Antes de dimensionar almacenamiento/pools y aceptar el ensayo conjunto de carga, caída de broker e importación. |
| REV-ARC-09 — Definir consistencia entre referencias SQL y objetos probatorios | P1 | Especificación por concretar | Antes de formalizar contratos o cierres que dependan de documentos almacenados fuera de PostgreSQL. |

## REV-ARC-01 — Fijar el contrato de comandos y estados del primer flujo

**P0 · Especificación por concretar.** Antes de dividir entre equipos la implementación del primer comando monetario y de integrar su primer canal o riel.

Los FR definen conductas y nombres de comandos/estados conceptuales, y la arquitectura propone HTTP/JSON/OpenAPI. Falta un contrato normativo de mensajes y transiciones para el flujo seleccionado: campos, precondiciones, autoridad de cada estado, versión esperada, canonicalización idempotente, resultados recuperables y errores. Es una capa de diseño pendiente reconocida en scope.md, no una interfaz ya implementada que haya fallado.

**Evidencia.**

- [docs/functional/scope.md](../functional/scope.md), Identidad, datos y contratos de operación: Declara expresamente conceptuales los nombres de comandos y estados y difiere esquema, campos, límites, códigos y versionado al diseño de APIs/archivos.
- [docs/achitecture.md](../achitecture.md), §§4–6 y 14: Distingue 202, commit local y evidencia externa; define hash canónico y propone HTTP/JSON/OpenAPI, sin un esquema normativo por comando. Referencias: `ADR-02`, `ADR-03`, `ADR-07`.
- [docs/functional/28-integraciones-eventos-trabajos.md](../functional/28-integraciones-eventos-trabajos.md), FR-ASY-001, FR-ASY-003 y FR-ASY-008: Exige aceptación durable, comparación canónica y compatibilidad de contratos, que necesitan una especificación común verificable. Referencias: `FR-ASY-001`, `FR-ASY-003`, `FR-ASY-008`, `NFR-08-C01`, `NFR-13-C02`.

**Impacto:** Canal, núcleo, worker y adaptador pueden implementar significados incompatibles para la misma solicitud, especialmente después de perder una respuesta o cambiar de principal autorizado.

**Mejora concreta.**

- Especificar para un flujo inicial la API/comandos/eventos y una tabla completa estado origen → condición → actor → efecto SQL → resultado visible, con ejemplos permitidos y denegados.
- Definir qué campos forman la identidad económica y el hash canónico, el ámbito de la clave de transporte, versionado, consultas autorizadas, conflictos y recuperación de resultados; mapear cada estado externo por perfil de riel.
- Vincular estos contratos a los FR/NFR/ADR y a sus productores/consumidores; conservar el resto de la biblioteca como alcance condicionado.

**Criterios de cierre.**

- Existe un contrato versionado del flujo inicial que permite a canal, núcleo y adaptador obtener la misma respuesta para éxito, rechazo, contenido conflictivo, 202, timeout y confirmación tardía.
- Una revisión de escritorio recorre esos casos con datos sintéticos y no deja transiciones o significados financieros ambiguos; las futuras pruebas de implementación quedan identificadas sin declararse ejecutadas.

**Responsable sugerido:** Arquitectura de dominio e Integraciones, con Producto y responsables del riel. **Dependencias:** Selección del primer producto y entidad; Perfil técnico efectivo de la contraparte; Definición financiera de autorización, contabilización y liquidación.

**Artefactos propuestos, aún no creados:** `docs/design/command-contracts.md`, `docs/design/api-contracts.yaml`.

**Skills afectados:** [adr-01-nucleo-modular](../../.agents/skills/adr-01-nucleo-modular/SKILL.md), [adr-02-autoridad-sql](../../.agents/skills/adr-02-autoridad-sql/SKILL.md), [adr-03-outbox-inbox](../../.agents/skills/adr-03-outbox-inbox/SKILL.md). Deben pedir/consumir el contrato concreto y conservar su estado; esta revisión no los modifica.

## REV-ARC-02 — Concretar el modelo lógico y el protocolo de guardianes SQL

**P0 · Especificación por concretar.** Antes de implementar el esquema financiero y los comandos concurrentes del primer producto.

La autoridad SQL, las transacciones y los guardianes estables están bien seleccionados. Los documentos aún no fijan un modelo lógico común con claves, cardinalidades, propiedad de cada dato, restricciones y conjunto/orden de locks por comando. En particular, falta concretar cómo se sincronizan pertenencia a grupo, traslado entre grupos, límites y guardianes al cambiar relaciones concurrentemente.

**Evidencia.**

- [docs/achitecture.md](../achitecture.md), §§3 y 5 — Transacción de referencia: Exige propiedad de tablas, READ COMMITTED con locks ordenados, guardianes de cuenta/grupo y serializable para predicados no representables. Referencias: `ADR-01`, `ADR-02`.
- [docs/functional/07-saldos-reservas-restricciones.md](../functional/07-saldos-reservas-restricciones.md), FR-BAL-004, FR-BAL-005, FR-BAL-020 y FR-BAL-030: Define resultados de serialización y caminos autorizados, pero no el esquema y las recetas de lock que los materializan. Referencias: `FR-BAL-004`, `FR-BAL-005`, `FR-BAL-020`, `FR-BAL-030`, `NFR-01-C03`.
- [docs/functional/23-riesgos-prudencia-exposiciones.md](../functional/23-riesgos-prudencia-exposiciones.md), FR-RSK-005 y FR-RSK-006: Los cambios de límite/grupo deben ser coherentes con autorizaciones en vuelo y revalidar versiones bajo bloqueo estable. Referencias: `FR-RSK-005`, `FR-RSK-006`, `NFR-05-C02`.
- [docs/functional/08-ledger-contabilidad-cierres.md](../functional/08-ledger-contabilidad-cierres.md), FR-LED-004, FR-LED-005 y FR-LED-008: Partida doble, atomicidad e identidad económica necesitan restricciones persistentes compatibles entre operación normal y carga. Referencias: `FR-LED-004`, `FR-LED-005`, `FR-LED-008`, `NFR-01-C01`, `NFR-01-C02`.

**Impacto:** Un desarrollador puede bloquear correctamente las filas existentes y aun omitir una relación o un guardián que otro comando cambia, permitiendo autorizar con un grupo o límite anterior.

**Mejora concreta.**

- Crear ERD/diccionario del primer producto con claves por entidad, moneda, identidad económica y generación, escalas exactas y relaciones entre contrato, posición, reserva, restricción, límite, diario, auditoría y outbox.
- Documentar por comando lectura autoritativa, filas guardianas, estabilidad/no eliminación, orden total de locks, revalidación de membresía/versiones y política de reintento completo.
- Precisar qué invariantes se comprueban mediante restricciones/procedimientos de la base y cuáles requieren serializable; incluir importador bulk y ajustes dentro de la misma frontera lógica.

**Criterios de cierre.**

- El modelo permite derivar claves y relaciones sin que cada módulo invente su propia identidad de cuenta, operación, grupo o generación.
- Una revisión de intercalados cubre dos débitos, alta de la primera restricción, cambio de grupo durante un desembolso, reducción de límite, reintento y carga bulk; cada caso identifica el punto de serialización y ningún camino carece de guardián.

**Responsable sugerido:** Arquitectura de datos y líder del núcleo, con Riesgos y Finanzas. **Dependencias:** Modelo de disponibilidad y catálogo de asientos; Semántica de grupo/contraparte; Contratos de comandos iniciales.

**Artefactos propuestos, aún no creados:** `docs/design/financial-data-model.md`, `docs/design/transaction-locking-protocol.md`.

**Skills afectados:** [adr-02-autoridad-sql](../../.agents/skills/adr-02-autoridad-sql/SKILL.md), [adr-05-configuracion-versionada](../../.agents/skills/adr-05-configuracion-versionada/SKILL.md), [adr-08-carga-inicial-masiva](../../.agents/skills/adr-08-carga-inicial-masiva/SKILL.md). Deben pedir/consumir el contrato concreto y conservar su estado; esta revisión no los modifica.

## REV-ARC-03 — Definir el corte entre cores y el destino de callbacks en vuelo

**P0 · Especificación por concretar.** Antes de un ensayo de corte de cohorte que incluya operación concurrente o instrucciones externas pendientes.

La migración exige barrera, una autoridad por contrato y activación pequeña. No se concreta todavía el protocolo entre el legado y el nuevo núcleo: quién confirma que el origen quedó inhibido, cómo rechaza un worker con época antigua y qué autoridad recibe/aplica un callback referido a una orden enviada antes del corte. Cambiar routing local no constituye por sí solo fencing del otro sistema.

**Evidencia.**

- [docs/achitecture.md](../achitecture.md), §§6 y 16.4–16.5: Advierte que un lease no impide envíos remotos y exige drenar/identificar operaciones, barrera y una autoridad por contrato. Referencias: `ADR-03`, `ADR-08`.
- [docs/functional/01-entidades-perimetro.md](../functional/01-entidades-perimetro.md), FR-ENT-022: El cambio de época debe rechazar escritores anteriores; el mecanismo de acuerdo con el origen no se especifica. Referencias: `FR-ENT-022`.
- [docs/functional/29-carga-inicial-migracion-salida.md](../functional/29-carga-inicial-migracion-salida.md), FR-MIG-020, FR-MIG-021, FR-MIG-022, FR-MIG-023 y FR-MIG-029: Define deltas, barrera, activación, transferencias entre cohortes y retorno sin una máquina común de transición de autoridad entre sistemas. Referencias: `FR-MIG-020`, `FR-MIG-021`, `FR-MIG-022`, `FR-MIG-023`, `FR-MIG-029`, `NFR-10-C06`.
- [docs/functional/28-integraciones-eventos-trabajos.md](../functional/28-integraciones-eventos-trabajos.md), FR-ASY-014 y FR-ASY-031: Callbacks idempotentes y segregación de generación necesitan conocer la autoridad correcta durante la transición. Referencias: `FR-ASY-014`, `FR-ASY-031`.

**Impacto:** Una orden del origen puede confirmarse después de activar la cohorte; descartarla pierde el efecto, aplicarla por ambos lados duplica dinero y reenviarla puede duplicar un pago.

**Mejora concreta.**

- Especificar estados y acuses del protocolo de corte, incluyendo congelamiento del origen, watermark final, inhibición efectiva, activación y recuperación si se pierde cada acuse.
- Asignar dueño y ruta de resolución a cada intención externa pendiente, preservando referencia e identidad económica; definir recepción/forward de callbacks y conciliación entre autoridades.
- Exigir un mecanismo comprobable de inhibición en el origen; si no está disponible, documentar la ventana de suspensión y las operaciones que deben resolverse antes de activar.

**Criterios de cierre.**

- Una tabla de fallos define acción segura antes/después de cada acuse y separa época SQL/routing de la capacidad de envío remoto.
- El ensayo diseñado incluye comando con época obsoleta, callback anterior al corte recibido después, transferencia entre cohortes y retorno con novedades; cada efecto conserva un único responsable y una identidad económica.

**Responsable sugerido:** Líder de migración y Arquitectura de integraciones, con custodio del legado. **Dependencias:** Capacidad real del sistema origen para inhibir operaciones; Contrato del riel/callbacks; Mapa de operaciones en vuelo y barrera final.

**Artefactos propuestos, aún no creados:** `docs/design/cohort-cutover-protocol.md`.

**Skills afectados:** [adr-03-outbox-inbox](../../.agents/skills/adr-03-outbox-inbox/SKILL.md), [adr-08-carga-inicial-masiva](../../.agents/skills/adr-08-carga-inicial-masiva/SKILL.md). Deben pedir/consumir el contrato concreto y conservar su estado; esta revisión no los modifica.

## REV-ARC-04 — Resolver secuencias filtradas, cursores y horizonte de replay

**P1 · Especificación por concretar.** Antes de implementar publicadores redundantes, consumidores con orden o la política de purga/reconstrucción.

El diseño ofrece preservar orden o detectar huecos, y exige retención suficiente, pero no selecciona el protocolo de secuencia/cursor. Una versión de agregado puede avanzar por hechos que un consumidor no recibe legítimamente por tipo o permisos. Sin distinguir secuencia del feed autorizado y versión del agregado, un filtro puede parecer pérdida y bloquear la proyección o inducir solicitudes de contenido reservado.

**Evidencia.**

- [docs/achitecture.md](../achitecture.md), §7 — Orden, privacidad y replay: Propone secuencia monotónica por agregado, publicadores redundantes y feeds minimizados con AML restringido; no define la continuidad visible para cada consumidor. Referencias: `ADR-03`.
- [docs/functional/28-integraciones-eventos-trabajos.md](../functional/28-integraciones-eventos-trabajos.md), FR-ASY-005, FR-ASY-006, FR-ASY-009, FR-ASY-023 y FR-ASY-028: Exige publicación recuperable, inbox, huecos, replay y conservación; faltan política concreta de cursores y compatibilidad entre purga y reconstrucción. Referencias: `FR-ASY-005`, `FR-ASY-006`, `FR-ASY-009`, `FR-ASY-023`, `FR-ASY-028`, `NFR-04-C06`, `NFR-06-C05`.
- [docs/adr/ADR-03-outbox-inbox.md](../adr/ADR-03-outbox-inbox.md), Decisión y criterios de aceptación: El bus no es archivo legal y un replay no debe producir efectos externos; el origen canónico y los límites del replay deben quedar identificados por feed. Referencias: `ADR-03`, `NFR-04-C02`.

**Impacto:** Consumidores pueden esperar indefinidamente un evento no autorizado, omitir un evento realmente faltante o repetir un efecto después de purgar su inbox.

**Mejora concreta.**

- Definir por feed qué representa su secuencia, continuidad visible, orden de publicación, posición del consumidor y reparación autorizada de huecos, sin filtrar datos reservados.
- Elegir serialización del publicador por agregado o buffer/reordenamiento con cursor durable; especificar cambio de particionado, versión y generación durante replay.
- Fijar horizontes relacionados de broker, outbox, inbox, snapshots y archivo canónico; indicar cómo reconstruir si el checkpoint es anterior al evento más antiguo disponible y qué identidades nunca se liberan por purga técnica.

**Criterios de cierre.**

- El contrato distingue hueco real, evento filtrado, duplicado y cambio de versión sin exponer contenidos restringidos.
- Un recorrido de escritorio con dos publicadores, dos tipos de evento, consumidor restringido, purga y replay muestra convergencia o excepción explícita y cero efectos externos históricos nuevos.

**Responsable sugerido:** Arquitectura de eventos y responsables de consumidores/datos. **Dependencias:** Contratos de eventos y permisos por feed; Políticas de retención y archivo por categoría; Diseño de snapshots y reconstrucción.

**Artefactos propuestos, aún no creados:** `docs/design/event-stream-recovery-contract.md`.

**Skills afectados:** [adr-03-outbox-inbox](../../.agents/skills/adr-03-outbox-inbox/SKILL.md), [adr-06-aislamiento-por-celda](../../.agents/skills/adr-06-aislamiento-por-celda/SKILL.md). Deben pedir/consumir el contrato concreto y conservar su estado; esta revisión no los modifica.

## REV-ARC-05 — Seleccionar una barrera de corte que vincule SQL y fuentes externas

**P0 · Decisión pendiente.** Antes de implementar el primer cierre o dataset regulatorio que combine más de una fuente.

Los documentos rechazan correctamente usar un offset máximo como corte global y requieren snapshot/barrera por fuente. Falta elegir, para un reporte inicial, cómo se forma ese corte y cómo se relacionan snapshot SQL, secuencias de eventos, versiones de archivos externos, fechas de negocio y revisiones tardías. Un manifiesto con campos no demuestra por sí solo consistencia entre ellos.

**Evidencia.**

- [docs/achitecture.md](../achitecture.md), §13 — Datos, cierres y reportes asíncronos: Enumera manifiesto, watermarks y snapshot o barrera, sin elegir algoritmo por régimen/flujo. Referencias: `ADR-02`, `ADR-03`, `ADR-05`.
- [docs/functional/08-ledger-contabilidad-cierres.md](../functional/08-ledger-contabilidad-cierres.md), FR-LED-017, FR-LED-018 y FR-LED-020: El cierre exige universo, completitud y linaje antes de balance/paquete. Referencias: `FR-LED-017`, `FR-LED-018`, `FR-LED-020`.
- [docs/functional/25-reportes-localizacion.md](../functional/25-reportes-localizacion.md), FR-RPT-004, FR-RPT-007 y FR-RPT-036: Requiere corte completo, reglas históricas y reproducción, que necesitan la relación entre puntos de captura de cada fuente. Referencias: `FR-RPT-004`, `FR-RPT-007`, `FR-RPT-036`, `NFR-11-C01`, `NFR-11-C03`.
- [docs/functional/22-conciliacion-excepciones.md](../functional/22-conciliacion-excepciones.md), FR-REC-006 y FR-REC-025: Define corte y revisión por tardíos; no resuelve cuál revisión de cada fuente integra un cierre concreto. Referencias: `FR-REC-006`, `FR-REC-025`, `NFR-11-C05`.

**Impacto:** Dos módulos pueden declarar completas sus fuentes y producir saldos diferentes para la misma fecha, especialmente con asientos tardíos, recálculos de interés o un extracto rectificado.

**Mejora concreta.**

- Elegir para un cierre inicial captura directa desde snapshot SQL o una barrera de materialización, documentando qué datos externos y revisiones deben estar completos.
- Definir un contrato de cut_id con población, snapshot/punto SQL, watermarks por feed, archivos y hashes, versiones de reglas/índices y criterio de fechas/tardíos.
- Preservar el dataset/corte anterior y generar nueva revisión o rectificativa cuando aparece un hecho posterior conocido, sin recomponer silenciosamente el original.

**Criterios de cierre.**

- Finanzas, REC y RPT pueden derivar el mismo universo y totales desde el cut_id y explicar cada exclusión.
- Casos documentados con fuente atrasada, evento fuera de orden, interés recalculado y archivo corregido conservan el corte original y determinan exactamente cuándo se permite cerrar o rectificar.

**Responsable sugerido:** Arquitectura de datos y responsables de Finanzas, conciliación y reportes. **Dependencias:** Régimen/paquete inicial seleccionado; Fuentes externas y sus reglas de completitud; Política de fecha contable, conocimiento y rectificativas.

**Artefactos propuestos, aún no creados:** `docs/design/consistent-close-report-cut.md`.

**Skills afectados:** [adr-02-autoridad-sql](../../.agents/skills/adr-02-autoridad-sql/SKILL.md), [adr-03-outbox-inbox](../../.agents/skills/adr-03-outbox-inbox/SKILL.md), [adr-05-configuracion-versionada](../../.agents/skills/adr-05-configuracion-versionada/SKILL.md). Deben pedir/consumir el contrato concreto y conservar su estado; esta revisión no los modifica.

## REV-ARC-06 — Demostrar qué hechos locales son reconstruibles tras perder la región

**P0 · Especificación por concretar.** Antes de aceptar el perfil de DR regional o comprometer su RTO/RPO con un cliente.

El riesgo de pérdida regional con réplica asíncrona está correctamente declarado. No se identifica todavía una fuente sobreviviente por clase de hecho reconocido. Consultar rieles sirve para efectos externos, pero no recupera necesariamente una transferencia interna, un bloqueo, una revocación o una rectificación de datos que sólo existían en el WAL/outbox y archivo aún no exportado de la región perdida.

**Evidencia.**

- [docs/achitecture.md](../achitecture.md), §10 — Objetivos de recuperación y copias: Admite commits informados ausentes en DR y exige definir reconstrucción desde evidencia independiente antes de contratar. Referencias: `ADR-04`, `NFR-02-C04`.
- [docs/functional/30-operacion-continuidad-terceros.md](../functional/30-operacion-continuidad-terceros.md), FR-OPS-008, FR-OPS-010, FR-OPS-011 y FR-OPS-012: Exige punto durable y reconciliación integral antes de reabrir, pero no presenta matriz de fuentes sobrevivientes por tipo de operación. Referencias: `FR-OPS-008`, `FR-OPS-010`, `FR-OPS-011`, `FR-OPS-012`, `NFR-02-C06`.
- [docs/functional/27-auditoria-privacidad-archivo.md](../functional/27-auditoria-privacidad-archivo.md), FR-DAT-014: Reaplicar disposiciones al restaurar requiere que el registro de esas disposiciones sobreviva también al escenario de pérdida. Referencias: `FR-DAT-014`, `NFR-06-C03`.
- [docs/functional/08-ledger-contabilidad-cierres.md](../functional/08-ledger-contabilidad-cierres.md), FR-LED-009 y FR-LED-029: La transferencia local no tiene un riel externo que actúe como oráculo independiente de recuperación. Referencias: `FR-LED-009`, `FR-LED-029`.

**Impacto:** Una base restaurada puede cuadrar y aun omitir derechos u órdenes ya reconocidos; reconstrucción y reapertura podrían extenderse más allá del RTO hipotético o ser incompletas.

**Mejora concreta.**

- Inventariar por clase de hecho el acuse que se da al cliente, el punto de durabilidad, la evidencia que sobrevive fuera del fallo y cómo detectar/reparar ausencias.
- Incluir dinero local, mandatos/restricciones, configuración, privilegios, disposiciones de privacidad, documentos e identidades económicas; no limitarse a pagos con tercero.
- Acordar en BIA las clases y pérdidas potenciales admitidas o ajustar persistencia/ubicación de evidencia cuando no resulten reconstruibles; no prometer RPO cero ni introducir sincronía interregional indiscriminada.

**Criterios de cierre.**

- La matriz distingue reconstruible, parcialmente reconstruible y no reconstruible con fundamento y decisión del responsable para el perfil concreto.
- Un caso diseñado de pérdida regional identifica el último hecho reconocido ausente, la fuente independiente o límite asumido y las condiciones de reapertura afectadas; el RTO incluye esa conciliación.

**Responsable sugerido:** Continuidad/SRE y Arquitectura de datos, con entidad, Riesgos y Seguridad. **Dependencias:** BIA del perfil contratado; Geometría de sitios, copias y evidencia; Decisiones de pérdida potencial aceptables por clase de dato.

**Artefactos propuestos, aún no creados:** `docs/design/regional-data-recoverability.md`.

**Skills afectados:** [adr-04-alta-disponibilidad](../../.agents/skills/adr-04-alta-disponibilidad/SKILL.md), [adr-03-outbox-inbox](../../.agents/skills/adr-03-outbox-inbox/SKILL.md), [adr-06-aislamiento-por-celda](../../.agents/skills/adr-06-aislamiento-por-celda/SKILL.md). Deben pedir/consumir el contrato concreto y conservar su estado; esta revisión no los modifica.

## REV-ARC-07 — Contrastar topología, garantías gestionadas y costo con una oferta real

**P0 · Decisión pendiente.** Antes de seleccionar proveedor, fijar presupuesto de infraestructura o vender el perfil de disponibilidad/latencia.

Tres dominios independientes, PostgreSQL 18 soportado con commit síncrono, Kafka multizona y DR son propuestas coherentes, condicionadas a disponibilidad real. No hay selección contrastada de región/sitios, tier de servicio, garantías de promoción, ubicaciones de soporte/KMS, conectividad con rieles y costo conjunto. La arquitectura ya registra este pendiente; corresponde resolverlo como paquete verificable de selección, sin asumir que cualquier oferta gestionada cumple el esquema.

**Evidencia.**

- [docs/achitecture.md](../achitecture.md), §§10, 14, 15 y 19: Advierte que no toda región tiene tres zonas y deja sitios, residencia, terceros, RTO/RPO y costos pendientes. Referencias: `ADR-04`, `ADR-07`.
- [docs/adr/ADR-07-stack-gestionado.md](../adr/ADR-07-stack-gestionado.md), Decisión propuesta y alternativas: PostgreSQL 18 debe estar soportado por el proveedor elegido y los gestionados dependen de jurisdicción/contrato y garantías verificables. Referencias: `ADR-07`.
- [docs/nfr/NFR-12-operabilidad-costos.md](../nfr/NFR-12-operabilidad-costos.md), NFR-12-C03 y NFR-12-C04: Costo y capacidad deben contrastarse con consumo/escenario y presupuesto aprobados, aún inexistentes para un perfil concreto. Referencias: `NFR-12-C03`, `NFR-12-C04`.
- [docs/market_analysis.md](../market_analysis.md), §§8 y 12: El TCO incluye operación, integración, migración y salida; los valores del modelo son ilustrativos y no cotizaciones.

**Impacto:** Un servicio puede no ofrecer la versión, independencia de sitios o política de standby elegible necesarias, o hacerlo a un piso de costo incompatible con el primer cliente.

**Mejora concreta.**

- Comparar ofertas viables por región/sitio y tier con evidencias fechadas de independencia, durabilidad/promoción, versiones, límites, soporte, KMS, copias, supervisión y salida.
- Mapear procesamiento, originales/documentos, telemetría, soporte y DR según su flujo; validar custodia local cuando proceda sin convertirla en una obligación universal de alojar todo en Argentina.
- Estimar RTT hacia sitios/rieles y TCO del mismo perfil completo, incluyendo capacidad al perder una zona, DR, Kafka, guardia, datos, claves, egreso e implementación; registrar qué sigue siendo supuesto hasta medir.

**Criterios de cierre.**

- Una matriz de selección distingue garantía contractual, capacidad técnica, supuesto y resultado pendiente; toda carencia tiene alternativa o condición de no selección.
- La entidad y el proveedor disponen de un presupuesto por celda y una topología realizable del perfil elegido, con revisión de países/contratos y sin anunciar aún benchmarks.

**Responsable sugerido:** Arquitectura de plataforma y Compras/Finanzas, con Legal, Seguridad y Operaciones. **Dependencias:** Primer producto, volumen y entidad; Ofertas y contratos efectivos; Ubicaciones de procesamiento, custodia y contrapartes.

**Artefactos propuestos, aún no creados:** `docs/design/platform-site-selection.md`, `docs/design/platform-tco-assumptions.md`.

**Skills afectados:** [adr-04-alta-disponibilidad](../../.agents/skills/adr-04-alta-disponibilidad/SKILL.md), [adr-06-aislamiento-por-celda](../../.agents/skills/adr-06-aislamiento-por-celda/SKILL.md), [adr-07-stack-gestionado](../../.agents/skills/adr-07-stack-gestionado/SKILL.md). Deben pedir/consumir el contrato concreto y conservar su estado; esta revisión no los modifica.

## REV-ARC-08 — Dimensionar backlog durable, WAL y recuperación con ingreso continuo

**P1 · Especificación por concretar.** Antes de dimensionar almacenamiento/pools y aceptar el ensayo conjunto de carga, caída de broker e importación.

Se especifican tasas de carga hipotéticas, backpressure, cuotas y alertas por edad, pero no un presupuesto de capacidad durable por flujo ni el tiempo de vaciado con ingreso continuo. Una tasa de comandos no determina por sí sola bytes de WAL, outbox/inbox, retención, conexiones o capacidad de catch-up, especialmente durante bulk o pérdida de zona.

**Evidencia.**

- [docs/achitecture.md](../achitecture.md), §§8, 11 y 16.2: Requiere limitar antes del agotamiento, medir amplificación y throttle de migración; no contiene un modelo de headroom o catch-up por flujo. Referencias: `ADR-03`, `ADR-07`, `ADR-08`.
- [docs/functional/28-integraciones-eventos-trabajos.md](../functional/28-integraciones-eventos-trabajos.md), FR-ASY-019, FR-ASY-025, FR-ASY-026 y FR-ASY-028: Los plazos, frescura, conservación y admisión necesitan presupuestos relacionados, no sólo alarmas independientes. Referencias: `FR-ASY-019`, `FR-ASY-025`, `FR-ASY-026`, `FR-ASY-028`, `NFR-04-C04`, `NFR-04-C06`.
- [docs/functional/29-carga-inicial-migracion-salida.md](../functional/29-carga-inicial-migracion-salida.md), FR-MIG-026 y FR-MIG-027: Bulk debe preservar recursos/SLO de cohortes activas con WAL y réplica medidos. Referencias: `FR-MIG-026`, `FR-MIG-027`, `NFR-10-C07`, `NFR-03-C05`.
- [docs/functional/30-operacion-continuidad-terceros.md](../functional/30-operacion-continuidad-terceros.md), FR-OPS-005 y FR-OPS-015: Pide capacidad reservada y señales, sin cantidades derivadas del perfil contratado. Referencias: `FR-OPS-005`, `FR-OPS-015`.

**Impacto:** El sistema puede sobrevivir la caída inicial y después agotar disco o no reducir backlog, incumpliendo deadlines al recuperar pese a tener workers escalados.

**Mejora concreta.**

- Modelar por flujo tasa de ingreso y amplificación de filas/eventos/bytes, horizonte de conservación, tamaño máximo de atraso y margen antes de agotar disco/conexiones.
- Estimar recuperación con ingreso sostenido: si tasa de servicio es μ e ingreso λ, el backlog sólo drena cuando μ es mayor que λ; relacionar el tiempo de drenaje con deadlines y capacidad remanente.
- Definir umbrales y acciones de admisión por producto/riel, incluyendo recepción que no admite rechazo genérico, y presupuesto específico de bulk/WAL/replicación.

**Criterios de cierre.**

- Una hoja de capacidad reproduce los recursos requeridos y el margen/tiempo de recuperación para carga normal, pico, broker caído, pérdida de zona y bulk coexistente.
- Las acciones por umbral conservan pendientes y durabilidad y tienen dueño; los valores están marcados como estimados o medidos y se enlazan a los escenarios NFR pertinentes.

**Responsable sugerido:** Ingeniería de plataforma/SRE y Arquitectura de datos, con dueños de flujos. **Dependencias:** Distribución y tamaño reales de operaciones/eventos; Horizontes de retención y deadlines; Oferta de infraestructura y presupuesto de costo.

**Artefactos propuestos, aún no creados:** `docs/design/durable-capacity-and-catchup.md`.

**Skills afectados:** [adr-03-outbox-inbox](../../.agents/skills/adr-03-outbox-inbox/SKILL.md), [adr-07-stack-gestionado](../../.agents/skills/adr-07-stack-gestionado/SKILL.md), [adr-08-carga-inicial-masiva](../../.agents/skills/adr-08-carga-inicial-masiva/SKILL.md). Deben pedir/consumir el contrato concreto y conservar su estado; esta revisión no los modifica.

## REV-ARC-09 — Definir consistencia entre referencias SQL y objetos probatorios

**P1 · Especificación por concretar.** Antes de formalizar contratos o cierres que dependan de documentos almacenados fuera de PostgreSQL.

Se prevén documentos/archivo en objetos y metadatos/operaciones en SQL, con hashes, retención y recuperación. Falta concretar el protocolo que asegura que una referencia confirmada apunta a una versión íntegra y recuperable del objeto, y cómo se tratan uploads huérfanos, borrado/hold y restauraciones SQL/objetos de puntos distintos. La transacción SQL no hace atómica una carga o eliminación en el almacén de objetos.

**Evidencia.**

- [docs/achitecture.md](../achitecture.md), §§12–14 y 16.1: Separa PII/documentos/archivo de SQL y exige contenido/versiones recuperables, sin definir transacción de metadatos y ciclo del objeto. Referencias: `ADR-06`, `ADR-07`.
- [docs/functional/05-contratos-documentos.md](../functional/05-contratos-documentos.md), FR-CON-008, FR-CON-010 y FR-CON-020: Formalización, entrega y paquete probatorio dependen de firmas/anexos completos y contenido exacto conservado. Referencias: `FR-CON-008`, `FR-CON-010`, `FR-CON-020`.
- [docs/functional/27-auditoria-privacidad-archivo.md](../functional/27-auditoria-privacidad-archivo.md), FR-DAT-005, FR-DAT-010, FR-DAT-011, FR-DAT-013 y FR-DAT-024: Integridad, hold, disposición y manifiesto deben mantener referencia estable y evitar borrar objetos aún exigibles. Referencias: `FR-DAT-005`, `FR-DAT-010`, `FR-DAT-011`, `FR-DAT-013`, `FR-DAT-024`, `NFR-06-C02`, `NFR-07-C02`.
- [docs/functional/30-operacion-continuidad-terceros.md](../functional/30-operacion-continuidad-terceros.md), FR-OPS-010: Restaurar datos y documentos como conjunto exige detectar referencias sin versión del objeto disponible. Referencias: `FR-OPS-010`, `NFR-08-C04`.

**Impacto:** Un contrato puede quedar formalizado con un anexo faltante, o una copia restaurada referenciar un objeto eliminado o una versión equivocada, afectando prueba contractual y reproducción histórica.

**Mejora concreta.**

- Especificar estados de objeto y metadatos: carga/verificación de hash/versión, referencia confirmada, disposición pendiente y disposición efectiva; decidir qué evidencia durable precede a formalizar/entregar.
- Usar referencias de versión inmutables con entidad, clasificación, política/hold y dueño; resolver uploads no referenciados sin borrar evidencia vinculada ni retener todo indefinidamente.
- Definir manifiesto de backup/restore/salida que relacione punto SQL con versiones exactas de objetos y claves recuperables; bloquear únicamente el paso afectado ante referencia incompleta.

**Criterios de cierre.**

- Los recorridos documentados de fallo después del upload, después del commit de referencia y durante disposición/hold tienen resolución idempotente y responsable.
- Una revisión del manifiesto puede localizar cada objeto requerido y detectar faltantes o versiones incompatibles antes de declarar formalizado, entregado o restaurado el expediente.

**Responsable sugerido:** Arquitectura de datos/documentos y Seguridad, con Legal y responsables de archivo. **Dependencias:** Modelo de objetos, claves y metadatos; Políticas de retención/hold por categoría; Garantías del servicio de almacenamiento y recuperación.

**Artefactos propuestos, aún no creados:** `docs/design/evidence-object-consistency.md`.

**Skills afectados:** [adr-06-aislamiento-por-celda](../../.agents/skills/adr-06-aislamiento-por-celda/SKILL.md), [adr-07-stack-gestionado](../../.agents/skills/adr-07-stack-gestionado/SKILL.md), [adr-04-alta-disponibilidad](../../.agents/skills/adr-04-alta-disponibilidad/SKILL.md). Deben pedir/consumir el contrato concreto y conservar su estado; esta revisión no los modifica.

## Decisiones institucionales que siguen pendientes

Seleccionar cliente/perfil y primer producto; aprobar semántica de saldo, asientos, grupos y calendarios; establecer BIA y pérdida potencial aceptable; confirmar capacidad del legado y contratos de riel; determinar sitios/países/custodia y derechos de terceros; asignar responsables y presupuesto. La arquitectura ya reconoce esos pendientes. Resolverlos requiere evidencia y actuación de la entidad, sin convertir una propuesta técnica en licencia, política contable o aceptación de riesgo.

Los nueve artefactos de diseño pueden prepararse de manera gradual para un mismo circuito inicial; no se exige resolver todo EXT antes de construir BASE. Cuando cambie una decisión, aplicar el coordinador ADR para mantener arquitectura, FR, NFR, skills y mapas consistentes.

## Fuentes leídas y límites de la revisión

Se revisaron **la arquitectura completa**, los **ocho ADR**, las **trece familias NFR con sus 71 criterios**, los **ocho SKILL.md especializados de ADR**, los coordinadores ADR/NFR y el skill regulatorio con su catálogo CTL. Se leyeron el alcance, índice, cobertura, mapas, flujos, catálogo estructurado y generador FR; se contrastaron los textos de ENT/IAM/CLI/CFG/CON, ACC/BAL/LED/CRE/INT/GAR/COL, PAY/CHQ/CRD/CSH/TRE/FXT/INV, REC/RSK/TAX/RPT/DAT, ASY/MIG/OPS/COR. Las secciones comerciales consultadas fueron decisión/estrategia, diferenciación, TCO, migración y ejecución; el relevamiento regulatorio se usó como fuente local fechada y para comprobar la trazabilidad técnica, sin nueva verificación de vigencia oficial.

El inventario de rutas exactas y los campos completos de los nueve hallazgos están en [findings/architecture.json](findings/architecture.json). No se ejecutaron pruebas de producto, consultas a proveedores, benchmarks ni simulacros de HA/migración. El único chequeo ejecutado fue el verificador documental existente; su resultado no acredita implementación o certificación. No se modificó la baseline ni se crearon los artefactos propuestos.
