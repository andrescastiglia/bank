# Revisión de seguridad informática y operaciones

**Fecha de revisión:** 16/10/2026. **Commit revisado:** `2e5d579103b94ab70c16d81debe73bf5840ba0c8`. **Base regulatoria/documental:** 15/10/2026. **Método:** revisión documental, sin escaneo de producción, prueba de intrusión, contratación, comunicación externa ni modificación del producto.

La documentación permite iniciar un desarrollo acotado con datos sintéticos y una agenda concreta de decisiones. Todavía no aporta evidencia para afirmar aislamiento efectivo, operación con guardia, recuperación medida o aptitud de un piloto con dinero real. Los P0 siguientes se resuelven antes del hito indicado: no constituyen una prohibición general para investigar, diseñar o desarrollar. No se halló evidencia de explotación ni se evaluó una implementación bancaria desplegada.

## Fortalezas específicas

- IAM, ADR-06 y NFR-05 extienden autorización a cuenta/objeto/acción, respuestas idempotentes, SQL, eventos, soporte, exportación y KMS. El aislamiento no se reduce a un filtro de aplicación.
- AML/FRD distinguen controles preventivos y monitoreo posterior; una indisponibilidad interna no inventa causas de rechazo para todos los fondos entrantes. ROS conserva circuito reservado.
- ASY y ADR-04 reconocen incertidumbre remota: timeout y lease vencido no prueban no envío, y restaurar SQL no revierte pagos. Outbox/inbox y conciliación mantienen la autoridad monetaria.
- DAT considera categorías, holds, países auxiliares y derechos; no promete borrado universal ni retención eterna. MIG incluye transacción fuente completa, unicidad entre corridas y PREPARED fuera del mayor/RI/eventos operativos.
- OPS distingue servicio recuperado técnicamente de reapertura conciliada, y SOC/ISO de licencia o certificación del producto. Estas fortalezas son decisiones y requisitos diseñados, con implementación/verificación todavía sin evaluar.

## Modelo de amenazas usado

| Activo/frontera | Actor o fallo plausible | Camino de abuso/impacto revisado | Controles diseñados y evidencia faltante |
|---|---|---|---|
| Dinero y autorización | Operador con dos identidades o servicio delegado | Crea y aprueba ajuste/cambio de destino, reusa decisión preventiva o reserva ambigua | IAM, REC, AML y FRD tienen reglas; faltan vínculo por persona, matriz efectiva y casos concurrentes. |
| Entidad y datos | Cliente/API/worker con referencia ajena | Cambia objeto/campo/entidad; recupera resultado idempotente o exportación de otra celda | ADR-06 y NFR-05 exigen aislamiento; falta materializar rutas, campos, permisos y casos negativos. |
| ROS, legajos y archivo | Soporte, analítica o restauración | Divulga investigación o reintroduce dato vencido desde DLQ/backup | DAT/AML delimitan accesos/ciclo de vida; faltan inventario, políticas efectivas y ensayo de derechos/restore. |
| IAM/KMS/control plane | Administrador comprometido, identidad caída o clave perdida | Abarca varias celdas o impide recuperar copias y evidencia | ADR-04/ADR-06 reconocen dependencia común; faltan dominios de administración y recuperación de raíces de confianza. |
| Build y entrega | Dependencia/artefacto o credencial CI comprometidos | Sustituye release o cambia reglas e infraestructura con permisos productivos | OPS prescribe SDLC/SBOM/revisión; aún no acredita pipeline/artefacto de producto ni validación independiente aplicable. |
| Riel, colas y día de negocio | Proveedor caído, callback falsificado, fuente tardía | Doble envío, backlog sin reloj, cierre incompleto o reapertura incoherente | ASY/REC/OPS conservan intención/cortes/plazos; faltan políticas por riel y ejercicios con personas/contrapartes. |

No se introducen requisitos universales de MFA, HSM, PCI o aviso AAIP de 72 horas. Se aplican perfil, canal, función, fuente y contrato de la línea base, cuya vigencia debe revalidarse antes de la decisión productiva.

## Diagnóstico por etapa de arranque

| Etapa | Qué puede avanzar | Evidencia/decisión necesaria para cerrar esa etapa |
|---|---|---|
| Kickoff de desarrollo | Elegir ruta inicial de crédito o pagos, asignar dueños de implementación y comenzar núcleo/pruebas sintéticas | Alcance y exclusiones, modelo de amenazas, política de identidades/SoD, backlog de seguridad/operación y responsable de CI/CD; no exige montar una guardia de producción para redactar o programar. |
| Integración y preparación | Construir APIs, IAM, adaptadores, entorno aislado y runbooks; ensayar fallos con contrapartes de prueba | Contratos de interfaces y contingencia, permisos efectivos, pipeline, inventario de datos, oráculos financieros, ensayos de recuperación/corte y revisión independiente exigible según sujeto. |
| Piloto con clientes/datos/fondos reales | Activar únicamente el perfil y cohorte aceptados | RACI y disponibilidad reales de proveedor/entidad, países/contratos/avisos aplicables, BIA/SLO probados, conciliación y atención operables, decisión de activación por funciones competentes. |
| Escalado y salida | Ampliar cohortes por capacidad/exposición y retirarse ordenadamente | Costo/guardia sostenibles, cambios revisados y salida reconstruida fuera del proveedor sin perder historia, claves o pendientes. |

No hay un headcount legal universal propuesto. Deben cubrirse funciones de producto/dominio contable, ingeniería, plataforma, seguridad y QA durante desarrollo; el piloto agrega cobertura efectiva de operación, conciliación, atención y funciones reguladas aplicables del cliente. La acumulación de roles se evalúa frente a incompatibilidades, carga y suplencia, no por contar títulos en un organigrama.

## Hallazgos y acciones

### REV-SEC-01 — Falta concretar amenazas y contratos de autorización por ruta

**P1 · Brecha de especificación · Responsable sugerido:** Seguridad de producto y Arquitectura.

**Hito afectado:** Antes de congelar APIs, interfaces de administración e integraciones del primer producto; el modelado puede comenzar durante el kickoff con datos sintéticos.

El catálogo exige autorización por entidad, objeto y acción y prevé pruebas negativas, pero sigue siendo conceptual: no contiene matriz de rutas/campos, principales, relaciones de confianza y permisos efectivos. Falta un artefacto que permita revisar cómo se deriva entidad/objeto en API, callback, exportación, job e importador, y qué atributos no puede cambiar el solicitante. Esto es una brecha de especificación verificable, no una vulnerabilidad ejecutada.

**Impacto:** Una implementación puede proteger el endpoint y permitir lectura o modificación de un atributo, cuenta o trabajo de otra entidad; exportación e idempotencia amplifican la fuga.

**Evidencia documental:**

- [FR-IAM-004, FR-IAM-023, FR-IAM-027](../../docs/functional/02-identidad-accesos.md): El requisito define autorización y matriz de pruebas, sin una matriz instanciada de endpoints/campos y permisos.
- [Identidad, datos y contratos de operación](../../docs/functional/scope.md): Declara conceptuales los comandos y deja esquema, campos y límites para diseño de APIs.
- [NFR-05-C01 y pendientes](../../docs/nfr/NFR-05-seguridad-accesos.md): El oráculo requiere matriz de pertenencia/permisos y evidencia negativa todavía pendiente.

**Acciones:**

- Crear diagrama de flujos y fronteras de confianza del perfil inicial, con activos dinero, identidad, PII, ROS y claves.
- Definir por ruta mensaje/campos admitidos, principal, derivación de entidad/objeto, autorización y límites de abuso; incluir mass assignment, referencias cruzadas, callback falsificado, archivo malicioso y agotamiento de recursos.
- Derivar casos positivos/negativos de cada frontera y asignarlos a FR/NFR existentes.

**Criterio de cierre:**

- Matriz revisada por Arquitectura y Seguridad cubre cada ruta habilitada y recurso SQL/evento/objeto asociado.
- Casos sintéticos de dos entidades prueban denegación de lectura, escritura, respuesta idempotente y exportación cruzadas; las rutas aún no implementadas se marcan sin evaluar.

### REV-SEC-02 — La independencia de aprobaciones debe vincularse a persona y delegación

**P0 · Brecha de especificación · Responsable sugerido:** Seguridad IAM y dueño institucional de cada aprobación.

**Hito afectado:** Antes de habilitar aprobación/liberación de ajustes, parámetros, importaciones o reportes con efectos reales.

FR-IAM-007 compara un mismo principal e impide evasión por cuenta técnica o canal, y REC exige aprobador independiente. No se especifica de forma comprobable cómo se reconoce a una misma persona con dos cuentas administrativas, identidades federadas o un servicio delegado, ni quién puede modificar ese vínculo. La intención de separación existe; falta precisar el sujeto de incompatibilidad para poder probarla.

**Impacto:** Una misma persona podría ejercer maker y checker mediante identidades distintas si se implementa literalmente sólo la comparación de principal; una cuenta técnica podría ocultar al iniciador.

**Evidencia documental:**

- [FR-IAM-001, FR-IAM-007 y FR-IAM-008](../../docs/functional/02-identidad-accesos.md): Vincula identidad/principal y formula incompatibilidad por principal; no define identidad canónica del empleado ni delegación de servicios para aprobaciones.
- [FR-REC-022 y FR-REC-023](../../docs/functional/22-conciliacion-excepciones.md): El preparador no aprueba/libera y una aprobación debe acompañar el ajuste al núcleo.
- [NFR-05-C03](../../docs/nfr/NFR-05-seguridad-accesos.md): La aceptación exige cero combinaciones incompatibles habilitadas.

**Acciones:**

- Definir identidad canónica del operador humano y procedencia de acciones delegadas, sin confundirla con deduplicación de clientes.
- Evaluar incompatibilidad por persona/control efectivo y por cadena de delegación; proteger cambios del vínculo y de la matriz.
- Definir tratamiento de emergencia limitado, con motivo, alcance, expiración y revisión independiente aplicables; no habilitar excepciones que eliminen una obligación.

**Criterio de cierre:**

- Dos credenciales de la misma persona no pueden crear y aprobar/liberar el mismo ajuste ni aprobar su propia asignación sensible.
- Servicio delegado conserva iniciador y aprobador identificables; cambiar importe/destino/invariante invalida aprobación anterior.
- Auditor reconstruye quién hizo cada etapa y cómo se comprobó independencia.

### REV-SEC-03 — Bootstrap y recuperación de IAM/KMS no tienen diseño operativo concreto

**P0 · Brecha de especificación · Responsable sugerido:** Seguridad de plataforma y Operaciones/SRE.

**Hito afectado:** Antes de elegir definitivamente la organización de cuentas/administradores cloud y antes de confiar datos o backups reales a ese plano de control.

ADR-04 y ADR-06 identifican IAM/KMS y administración compartidos como dependencias comunes y exigen recuperación. No hay aún un diseño instanciado de raíces de confianza, custodios, acceso de emergencia, separación de administración de copias/claves y restauración cuando el proveedor de identidad o el administrador productivo están comprometidos. El control está diseñado en intención, no demostrado en su implementación.

**Impacto:** Comprometer una administración común puede vencer el aislamiento entre celdas o impedir recuperar copias aparentemente íntegras; una dependencia circular de credenciales puede bloquear el DR.

**Evidencia documental:**

- [Decisión propuesta y Aceptación](../../docs/adr/ADR-06-aislamiento-por-celda.md): Separa claves por celda y reconoce IAM/KMS/red/plano operativo como dependencias comunes.
- [FR-IAM-008 y FR-IAM-022](../../docs/functional/02-identidad-accesos.md): Exige acceso temporal y recuperación/rotación de credenciales, sin un bootstrap específico.
- [FR-OPS-009 y FR-OPS-010](../../docs/functional/30-operacion-continuidad-terceros.md): Copias protegidas frente al administrador productivo y recuperación integral quedan propuestas.

**Acciones:**

- Diseñar dominios de administración y raíces de confianza para producción, copias, claves, auditoría y CI/CD, con responsabilidades y dependencias explícitas.
- Crear procedimiento de recuperación de identidad/claves con custodios, acceso de emergencia limitado, evidencias y ubicación autorizada.
- Ensayar pérdida de IAM, revocación de claves y compromiso de un administrador en entorno aislado, preservando separación entre entidades.

**Criterio de cierre:**

- Administrador productivo comprometido no puede eliminar/modificar simultáneamente todas las copias y el material necesario para restaurarlas.
- Otro rol autorizado recupera identidad, claves y auditoría siguiendo el procedimiento sin depender del componente perdido.
- Ensayo conserva configuración efectiva, accesos usados, punto recuperado y límites residuales del modelo de amenazas.

### REV-SEC-04 — Las contingencias preventivas todavía no están instanciadas por operación y riel

**P0 · Decisión pendiente · Responsable sugerido:** Cumplimiento/AML, Fraude, Pagos y Seguridad.

**Hito afectado:** Antes de autorizar dinero real en un producto/canal o conectar un riel de producción.

AML y FRD separan controles preventivos de monitoreo posterior y prohíben rechazos entrantes genéricos, y ASY preserva estados ambiguos. Faltan las decisiones específicas del primer producto para lista vencida, proveedor sin respuesta, score no disponible, mandato revocado y callback pendiente: quién decide, qué estado financiero se conserva y qué permite cada contraparte. No falta el requisito; falta su política operable.

**Impacto:** Una política global de continuar o bloquear puede permitir fraude o incumplir el tratamiento de recepción del esquema; liberar/reintentar ante incertidumbre puede duplicar dinero.

**Evidencia documental:**

- [FR-AML-005, FR-AML-009 y FR-AML-011](../../docs/functional/20-prevencion-la-ft-fp.md): Exige resultado vigente/contingencia permitida, congelamiento autoritativo y causas admisibles de recepción.
- [FR-FRD-004 y FR-FRD-005](../../docs/functional/21-prevencion-fraude.md): Exige decisión preventiva vigente y contingencia diferenciada por riel/sentido.
- [FR-ASY-012 y FR-ASY-013](../../docs/functional/28-integraciones-eventos-trabajos.md): Timeout/lease no autorizan reenvío ni liberación de reserva ambigua.

**Acciones:**

- Crear tabla por operación, sentido, perfil, dependencia y estado de frescura con conducta permitida, dueño y escalamiento.
- Acordar contrato técnico/operativo con rieles y proveedores preventivos, incluyendo consultas de estado y autenticidad de callback.
- Probar concurrencia entre restricción/revocación y autorización y caída entre intención externa y confirmación.

**Criterio de cierre:**

- Cada combinación habilitada tiene un resultado explícito y fundado: rechazo permitido, pendiente, derivación o ejecución con controles exigibles.
- Fallos sintéticos no liberan reservas ambiguas, no reenvían a ciegas ni convierten indisponibilidad interna en rechazo entrante universal.

### REV-SEC-05 — Retención, residencia y derechos necesitan una matriz poblada y ensayo de restauración

**P0 · Brecha de evidencia · Responsable sugerido:** Responsable de datos de la entidad, Legal y Seguridad.

**Hito afectado:** Antes de recibir legajos, cartera importada, soporte o telemetría con datos personales reales.

DAT/NFR-06 ya requieren mapa de tratamientos, retención por categoría, holds y reaplicación de disposiciones al restaurar. No constan inventario poblado, políticas efectivas por almacén ni prueba de que el dato retirado de difusión no reaparezca desde backups, DLQ o proyecciones. Las referencias legales y los FR son diseño; no son evidencia de tratamiento aplicado.

**Impacto:** Una supresión indiscriminada puede destruir soporte exigible; una restauración o soporte exterior puede reintroducir difusión vencida o una transferencia no evaluada.

**Evidencia documental:**

- [FR-DAT-007, FR-DAT-010, FR-DAT-014 y FR-DAT-021](../../docs/functional/27-auditoria-privacidad-archivo.md): Cubre países, retención, restauración y reserva ROS pero su estado es sin evaluar.
- [NFR-06-C01, NFR-06-C02, NFR-06-C03 y NFR-06-C04](../../docs/nfr/NFR-06-privacidad-residencia-retencion.md): Requiere cero flujos/categorías sin política y resolver derechos en plazo; pendientes incluyen países y fundamentos.
- [DATA-02, DATA-04, DATA-05, DATA-06 y TAX-09](../../docs/compliant.md): La conservación y transferencia dependen de categoría, sujeto, finalidad y deber concurrente.

**Acciones:**

- Poblar categorías de identidad/legajo, contratos, diario, ROS, logs, colas, backups y soporte con fundamento, disparador, duración, acceso, país y disposición.
- Resolver mecanismos de transferencia, originales locales cuando corresponda y responsabilidad de subencargados.
- Ensayar derechos, hold/levantamiento y restauración con datos sintéticos, preservando registros legales y exclusión de ROS.

**Criterio de cierre:**

- Inventario se contrasta con servicios y destinos reales del perfil, incluidos KMS/DR/APM/soporte.
- Caso de acceso/corrección conserva reloj desde recepción; restaurar no repone datos a difusión vencida ni borra evidencia bajo hold.
- Resultado explica remanentes, plazos concurrentes y disposición por almacén, sin declarar borrado completo sólo por un flag.

### REV-SEC-06 — SDLC y cadena de suministro carecen todavía de evidencia de ejecución

**P1 · Brecha de evidencia · Responsable sugerido:** Ingeniería, Plataforma, Seguridad y QA independiente.

**Hito afectado:** Al iniciar el repositorio de producto y antes de promover un release candidato con acceso a un entorno sensible.

La arquitectura y OPS prescriben revisión, separación, SBOM, artefactos verificables, pruebas y QA independiente; no se acreditan pipeline de producto, configuración de repositorio, credenciales de build ni release reproducible. La cobertura documental del catálogo no valida un binario o despliegue. Es una tarea de construcción del proyecto, no un fallo de una aplicación existente.

**Impacto:** Un cambio no revisado, dependencia comprometida o credencial de CI excesiva puede modificar la autoridad financiera y eludir controles del runtime.

**Evidencia documental:**

- [15. Operación, entrega segura y costos](../../docs/achitecture.md): CI/CD y migración de esquemas se describen como diseño, no como ejecuciones.
- [FR-OPS-022, FR-OPS-025 y FR-OPS-026](../../docs/functional/30-operacion-continuidad-terceros.md): Vincula cambio, QA/tercero independiente aplicable y versiones/SBOM.
- [Decisión propuesta](../../docs/adr/ADR-07-stack-gestionado.md): Cada dependencia debe tener versión, licencia, SBOM, responsable y parcheo; la elección sigue propuesta.

**Acciones:**

- Definir repositorio protegido, revisores/entornos, credenciales de CI de mínimo alcance y proceso de promoción con procedencia verificable.
- Implementar build/versionado y verificaciones de secretos, dependencias, código e infraestructura proporcionales al alcance, vinculadas a casos financieros y permisos negativos.
- Planificar QA y pruebas externas independientes cuando el sujeto/contrato lo exija; mantenerlas separadas de escáneres propios.

**Criterio de cierre:**

- Release de prueba enlaza requisito, revisión, fuentes/dependencias, pruebas, artefacto identificado y despliegue; secretos no aparecen en repositorio/logs.
- Autor no puede sustituir por sí solo artefacto/promoción aprobada y una dependencia vulnerable conserva tratamiento/retest.
- Pruebas independientes aplicables tienen alcance y evidencia propia antes de la activación afectada, sin exigirlas para escribir documentación.

### REV-SEC-07 — No hay modelo operativo dotado para asumir guardia y responsabilidades de cliente

**P0 · Decisión pendiente · Responsable sugerido:** Dirección del proveedor y responsable operativo de la entidad.

**Hito afectado:** Antes de prometer cobertura de soporte/SLA o habilitar un piloto con clientes y fondos; en kickoff basta designar responsables de trabajo y plan de dotación.

Arquitectura sección 19 deja RACI, guardia, formación y presupuesto como decisiones pendientes, y OPS/NFR-12 proponen responsables y suplencias. No constan personas/servicios contratados, horario de cobertura, financiación recurrente o prueba de que una ausencia no deja sin conciliación, aprobación o atención a la entidad. Un organigrama de roles propuestos no constituye un equipo disponible.

**Impacto:** Se puede tener software correcto y no responder un incidente, cerrar la cartera o atender al usuario dentro del plazo; concentrar todo en el fundador impide independencia y continuidad.

**Evidencia documental:**

- [19. Decisiones pendientes para convertir el diseño en implementación](../../docs/achitecture.md): Capacidad de operación incluye RACI, guardia, soporte, formación y presupuesto por resolver.
- [FR-OPS-003 y FR-OPS-037](../../docs/functional/30-operacion-continuidad-terceros.md): Pide dueño/guardia/runbook y designaciones; no acredita designaciones reales.
- [NFR-12-C01, NFR-12-C03 y NFR-12-C05](../../docs/nfr/NFR-12-operabilidad-costos.md): Exige cobertura del inventario crítico, costo reproducible y ejecución por roles distintos del autor.

**Acciones:**

- Separar RACI de desarrollo, operación técnica del proveedor y funciones institucionales del cliente.
- Asignar dueño, suplente, horario/escalamiento y autoridad por operación crítica, incluida conciliación, ajustes, reclamos, AML/fraude y presentación de reportes.
- Presupuestar dotación y soporte de terceros con el servicio efectivamente ofrecido; resolver ubicación de funciones TI/SI cuando aplique al sujeto.

**Criterio de cierre:**

- Matriz poblada y compromisos de disponibilidad cubren todos los flujos activos y las incompatibilidades de funciones.
- Simulacro con ausencia del titular llega a un suplente con acceso mínimo y potestad real; costos de guardia/localización/QA quedan en el TCO.
- El kickoff identifica responsables de implementación sin anunciar que esa dotación ya presta servicio productivo.

### REV-SEC-08 — BIA y recuperación aún no convierten metas propuestas en compromisos demostrados

**P0 · Brecha de evidencia · Responsable sugerido:** Operaciones/SRE, Arquitectura y dueño del BIA de la entidad.

**Hito afectado:** Antes de firmar un SLA/RPO, seleccionar una región como suficiente para un cliente o habilitar operación monetaria del piloto.

ADR-04 distingue correctamente durabilidad multizona y pérdida regional potencial, y exige fencing y conciliación. Faltan BIA del cliente, topología efectiva, independencia de dominios, capacidad remanente y ensayos con IAM/KMS/rieles. Los valores propuestos de recuperación no prueban recuperabilidad ni disponibilidad mensual.

**Impacto:** Contratar RPO cero regional sobre réplica asíncrona o reabrir con eventos posteriores al punto SQL puede perder operaciones reconocidas o generar doble efecto externo.

**Evidencia documental:**

- [Decisión propuesta y Aceptación y revisión](../../docs/adr/ADR-04-alta-disponibilidad.md): RPO regional depende del punto recuperado; metas quedan por validar.
- [FR-OPS-002 y FR-OPS-006 a FR-OPS-013](../../docs/functional/30-operacion-continuidad-terceros.md): Diseña BIA, persistencia, fencing, backups, restauración y reapertura, todos sin evaluar.
- [NFR-02-C03, NFR-02-C04, NFR-02-C05 y NFR-02-C06](../../docs/nfr/NFR-02-disponibilidad-recuperacion.md): Las metas exigen fallos/restore observados y reconciliación antes de reabrir.

**Acciones:**

- Acordar BIA por flujo y escenarios con pérdida máxima aceptable, tolerancia y dependencias, separando objetivo de contrato.
- Obtener evidencia de independencia de sitios/política síncrona/fencing y dimensionar capacidad tras pérdida de dominio.
- Ensayar pérdida de writer/región, copia limpia y desfase DB-broker con primario/adaptadores anteriores aislados y consulta de efectos externos ambiguos.

**Criterio de cierre:**

- Acta distingue meta, observado y brecha; registra punto WAL/offset y RPO real, incluidos commits reconocidos ausentes en DR si los hubiera.
- No hay dos escritores ni replay externo; reapertura exige conciliación y restricciones íntegras.
- Un ensayo corto no se presenta como disponibilidad mensual; si negocio exige RPO regional cero se revisa el diseño antes de prometerlo.

### REV-SEC-09 — Falta un calendario operativo ejecutable de incidentes, AML y reclamos

**P0 · Brecha de evidencia · Responsable sugerido:** Operaciones de la entidad, Cumplimiento/AML, Atención y responsable RRCI.

**Hito afectado:** Antes de recibir solicitudes/reclamos de clientes o hechos sujetos a notificación en el piloto.

OPS, AML, CST y COR conservan correctamente relojes distintos y hechos originales. No hay aún calendario poblado con disparadores, zona/calendario, canales efectivos, delegados/suplentes y procedimientos de envío/acuse. Falta un ejercicio que cruce incidente de tercero, reclamo, investigación reservada y aviso inicial sin esperar la causa raíz.

**Impacto:** Colas o transferencias entre proveedor/entidad pueden consumir el plazo mientras cada equipo cree que otro presentará; un caso puede cerrarse internamente sin respuesta al cliente o acuse externo.

**Evidencia documental:**

- [FR-OPS-016 a FR-OPS-019 y Contratos de operación](../../docs/functional/30-operacion-continuidad-terceros.md): Separa ocurrido/detectado, primera hora RRCI y cierre; preparación no acredita envío.
- [FR-AML-017, FR-AML-018, FR-AML-019 y FR-AML-020](../../docs/functional/20-prevencion-la-ft-fp.md): Mantiene relojes LA, FT y FP independientes y circuito reservado.
- [FR-CST-015, FR-CST-017 y FR-CST-018](../../docs/functional/26-canales-atencion-usuarios.md): Recibo del reclamo, suplencia, decisión y comunicación son hechos distintos.
- [FR-COR-019](../../docs/functional/32-corresponsalia-baas-plataformas.md): Incidente del tercero conserva hitos originales e impacto propio.

**Acciones:**

- Crear matriz de obligaciones/servicios activos con hecho disparador, plazo/fuente, calendario, dueño, suplente, canal y evidencia de recepción.
- Preparar runbooks de clasificación, comunicación autorizada, actualización, cierre y respuesta al usuario, manteniendo reserva AML y acceso mínimo.
- Realizar tabletop fuera del horario habitual con proveedor tardío, titular ausente y envío sin respuesta; usar canales simulados, sin comunicar externamente en esta revisión.

**Criterio de cierre:**

- El ejercicio produce una línea temporal única y expedientes vinculados con relojes que no se reinician por cola/ticket.
- Responsables preparan avisos/respuestas dentro de plazos del perfil y diferencian generado, enviado, recibido/aceptado; constancias simuladas están identificadas como tales.
- No se importa un aviso general AAIP de 72 horas ni otro plazo ajeno al inventario aplicable.

### REV-SEC-10 — El día operativo y la resolución manual todavía no fueron ensayados

**P0 · Brecha de evidencia · Responsable sugerido:** Operaciones de negocio, Conciliación y Finanzas de la entidad.

**Hito afectado:** Antes del primer cierre o conciliación que determine fondos, reporte o estado contractual del piloto.

REC y ASY exigen universos completos, excepciones trazables y ajustes aprobados por el núcleo. No constan perfiles de fuentes, horarios/cortes, umbrales de intervención, runbooks ni ejercicios de una jornada con archivo tardío, pago ambiguo, diferencia por titular y ajuste en período cerrado. Los FR ya cubren el comportamiento; falta convertirlo en operación repetible con personas distintas.

**Impacto:** Un total general correcto puede esconder asignación a otro titular; una excepción marcada resuelta puede liberar fondos o alimentar un reporte incompleto, o dejar un pago ambiguo sin dueño.

**Evidencia documental:**

- [FR-REC-001, FR-REC-020, FR-REC-021, FR-REC-022, FR-REC-023 y FR-REC-026](../../docs/functional/22-conciliacion-excepciones.md): Fuente, dueño, plazo, ajuste y completitud son condiciones del cierre, no sólo jobs terminados.
- [FR-ASY-019, FR-ASY-020 y FR-ASY-024](../../docs/functional/28-integraciones-eventos-trabajos.md): Exige deadlines, manifiesto y barreras de todas las fuentes.
- [NFR-12-C01 y NFR-12-C05](../../docs/nfr/NFR-12-operabilidad-costos.md): Runbook y ejecución por roles distintos aún requieren evidencia.

**Acciones:**

- Diseñar calendario de negocio y cortes por producto/riel/fuente con esperado, recibido y tratamiento de tardíos.
- Preparar runbook de diferencias y límites de acción manual: consulta, investigación, propuesta, aprobación, contabilización y reapertura.
- Ejecutar jornada sintética completa con cierre parcial, suplencia, ajuste rechazado y consulta externa ambigua, sin acceso SQL corrector de saldos.

**Criterio de cierre:**

- Cada diferencia tiene titular/moneda/importe, propietario, deadline y decisión; excepción aceptada no se etiqueta conciliación completa.
- Ajuste cambiado exige nueva aprobación y reintento no duplica asiento; período cerrado sigue política aprobada.
- Un operador distinto del autor reconstruye corte y reporte con fuentes/versiones y explica todos los faltantes.

### REV-SEC-11 — Corte, retorno y salida necesitan ensayo independiente de una cohorte representativa

**P0 · Brecha de evidencia · Responsable sugerido:** Migración, Operaciones, Finanzas y receptor de la cartera.

**Hito afectado:** Antes de cada migración/activación de cohorte real y antes de afirmar portabilidad o retirada del proveedor.

ADR-08 y MIG especifican bulk logged, unicidad entre corridas, transacción fuente completa, PREPARED aislado, una autoridad y retorno conciliado después de operar. No se acredita un origen, mapeo, población de control, ensayo completo o acta de corte/retorno ejecutada. La calidad del diseño no demuestra ventana, exclusión efectiva ni capacidad del receptor de salida.

**Impacto:** Un corte incompleto puede tener dos autoridades o fondos duplicados; volver con backup después de pagos reales pierde obligaciones; exportar sin reconstruir puede dejar al cliente cautivo.

**Evidencia documental:**

- [Aceptación, revisión y dependencias](../../docs/adr/ADR-08-carga-inicial-masiva.md): Los ensayos están pendientes de ejecución.
- [FR-MIG-021, FR-MIG-022, FR-MIG-029, FR-MIG-031 y FR-MIG-033](../../docs/functional/29-carga-inicial-migracion-salida.md): Barrera, autoridad, retorno tras actividad y restauración fuera del proveedor requieren resultados.
- [FR-COR-022](../../docs/functional/32-corresponsalia-baas-plataformas.md): La salida mantiene pendientes y obligaciones del proveedor regulado.

**Acciones:**

- Elegir origen/cohorte y modo de apertura o historia con Finanzas, mapeos versionados y universo esperado.
- Ensayar carga y cutover con fuente dividida, checksum modificado, nueva corrida duplicada, delta tardío, réplica atrasada y operaciones en vuelo.
- Ensayar retorno tras actividad sintética equivalente y reconstrucción en destino independiente con claves/documentos/reglas; asignar autoridad y procedimiento de decisión por rol real.

**Criterio de cierre:**

- Resultados incluyen cero diferencias inexplicadas por titular/moneda, ninguna exposición PREPARED a mayor/RI/eventos y un solo escritor por contrato.
- Ventana completa y efecto en cohortes activas se miden con WAL/durabilidad/seguridad activos; no se declara éxito sólo por terminar COPY.
- Retorno preserva liquidaciones y traslada novedades; destino independiente reconstruye cartera y pendientes con evidencia legible.

### REV-SEC-12 — La cadena de proveedores no tiene aún expediente operativo/contractual verificable

**P0 · Decisión pendiente · Responsable sugerido:** Compras/Legal, Seguridad, Operaciones y entidad contratante.

**Hito afectado:** Antes de contratar servicio crítico, habilitar país/subencargado o comprometer capacidades gestionadas y soporte de producción.

ADR-07 propone servicios gestionados y OPS/COR requieren responsabilidad compartida, derechos de auditoría, avisos, revisión SOC y salida. No se identifica proveedor/región/cadena contratada ni se aportan informes completos, CUEC, constancias de aviso o ejercicio de soporte/supervisión. Esto limita la contratación y activación concreta; no impide explorar alternativas o probar con datos sintéticos.

**Impacto:** Un tercero puede impedir inspección, no sostener el fencing o soporte prometido, trasladar datos sin margen para avisos o exigir costos/tiempos de salida que vuelvan inviable la operación.

**Evidencia documental:**

- [Decisión propuesta y Aceptación](../../docs/adr/ADR-07-stack-gestionado.md): La preferencia gestionada depende de garantías, jurisdicción, contrato y pruebas.
- [FR-OPS-029, FR-OPS-030, FR-OPS-031, FR-OPS-032, FR-OPS-033, FR-OPS-035 y FR-OPS-036](../../docs/functional/30-operacion-continuidad-terceros.md): Requiere cadena, contrato, supervisor, avisos/cambios, revisión SOC y salida, no acreditados.
- [FR-COR-020 y FR-COR-021](../../docs/functional/32-corresponsalia-baas-plataformas.md): Distingue corresponsalía de tercerización y rechaza sustituir acceso supervisor por un certificado.
- [BCRA-T26 a BCRA-T34 y STD31](../../docs/compliant.md): El análisis exige sujeto/servicio/criticidad, cadena completa y alcance/período de aseguramiento.

**Acciones:**

- Comparar candidatos con matriz técnica/contractual por servicio: administración, ubicación/control, subcontratistas, incidentes, recuperación, evidencia y sustitución.
- Revisar informes íntegros por alcance/período/excepciones/CUEC y comprobar controles del usuario en la configuración del core; ISO/SOC no son certificación de producto ni eximen al cliente.
- Cerrar avisos aplicables según entidad/criticidad/servicio digital con calendarios separados, y ensayar pedido de evidencia, soporte de incidente y salida.

**Criterio de cierre:**

- Expediente identifica cadena y responsables, brechas resueltas o limitación explícita de la contratación afectada, sin usar aceptación de riesgo para suprimir ley.
- Contrato permite derechos exigibles en toda cadena y evidencia de acceso/soporte/portabilidad del escenario, incluidos costos de egreso/inspección aplicables.
- Calendario distingue notificación y autorización y no asume que todo servicio o corresponsalía está sujeto al mismo aviso.

## Cuestiones institucionales pendientes

La entidad concreta debe determinar perfil/licencia, productos, facultades de los responsables, apetito/tolerancia de pérdida y política de contingencia de cada riel. Proveedor y cliente deben acordar horarios/guardia, soporte, responsabilidades de comunicación, acceso supervisor, países y presupuesto. Legal/Cumplimiento revalida fuentes y condiciones efectivas; Finanzas define cierre y ajustes, y el responsable de datos las obligaciones de conservación/derechos. Ninguna de estas decisiones se presume tomada por completar una tabla o por usar un servicio gestionado.

Los entregables sugeridos en el JSON son propuestas de trabajo; esta revisión sólo crea este informe y sus hallazgos estructurados. No crea controles, equipos, contratos ni evidencias de pruebas. Para cerrar un hallazgo se conserva por separado decisión, implementación, resultado observado y aprobación que corresponda al hito real.

## Fuentes efectivamente consultadas

La lectura focal cubrió arquitectura, mercado, cumplimiento TI/SI/privacidad/terceros y los módulos IAM, AML, FRD, REC, CST, DAT, ASY, MIG, OPS y COR. ENT, alcance, flujos y cobertura se usaron para encuadre; no se afirma una auditoría semántica independiente de cada producto bancario del inventario. Los skills listados se usaron como metodología de evaluación, sin invocar una facultad para enviar mensajes o desplegar.

El registro exacto de rutas leídas y todos los campos de cada hallazgo están en [findings/security_operations.json](findings/security_operations.json).

- [docs/market_analysis.md](../../docs/market_analysis.md)
- [docs/compliant.md](../../docs/compliant.md)
- [docs/achitecture.md](../../docs/achitecture.md)
- [docs/functional/README.md](../../docs/functional/README.md)
- [docs/functional/scope.md](../../docs/functional/scope.md)
- [docs/functional/flows.md](../../docs/functional/flows.md)
- [docs/functional/coverage.md](../../docs/functional/coverage.md)
- [docs/functional/01-entidades-perimetro.md](../../docs/functional/01-entidades-perimetro.md)
- [docs/functional/02-identidad-accesos.md](../../docs/functional/02-identidad-accesos.md)
- [docs/functional/20-prevencion-la-ft-fp.md](../../docs/functional/20-prevencion-la-ft-fp.md)
- [docs/functional/21-prevencion-fraude.md](../../docs/functional/21-prevencion-fraude.md)
- [docs/functional/22-conciliacion-excepciones.md](../../docs/functional/22-conciliacion-excepciones.md)
- [docs/functional/26-canales-atencion-usuarios.md](../../docs/functional/26-canales-atencion-usuarios.md)
- [docs/functional/27-auditoria-privacidad-archivo.md](../../docs/functional/27-auditoria-privacidad-archivo.md)
- [docs/functional/28-integraciones-eventos-trabajos.md](../../docs/functional/28-integraciones-eventos-trabajos.md)
- [docs/functional/29-carga-inicial-migracion-salida.md](../../docs/functional/29-carga-inicial-migracion-salida.md)
- [docs/functional/30-operacion-continuidad-terceros.md](../../docs/functional/30-operacion-continuidad-terceros.md)
- [docs/functional/32-corresponsalia-baas-plataformas.md](../../docs/functional/32-corresponsalia-baas-plataformas.md)
- [docs/adr/ADR-04-alta-disponibilidad.md](../../docs/adr/ADR-04-alta-disponibilidad.md)
- [docs/adr/ADR-06-aislamiento-por-celda.md](../../docs/adr/ADR-06-aislamiento-por-celda.md)
- [docs/adr/ADR-07-stack-gestionado.md](../../docs/adr/ADR-07-stack-gestionado.md)
- [docs/adr/ADR-08-carga-inicial-masiva.md](../../docs/adr/ADR-08-carga-inicial-masiva.md)
- [docs/nfr/NFR-02-disponibilidad-recuperacion.md](../../docs/nfr/NFR-02-disponibilidad-recuperacion.md)
- [docs/nfr/NFR-05-seguridad-accesos.md](../../docs/nfr/NFR-05-seguridad-accesos.md)
- [docs/nfr/NFR-06-privacidad-residencia-retencion.md](../../docs/nfr/NFR-06-privacidad-residencia-retencion.md)
- [docs/nfr/NFR-07-auditoria-observabilidad.md](../../docs/nfr/NFR-07-auditoria-observabilidad.md)
- [docs/nfr/NFR-12-operabilidad-costos.md](../../docs/nfr/NFR-12-operabilidad-costos.md)
- [.agents/skills/core-bancario-argentina/SKILL.md](../../.agents/skills/core-bancario-argentina/SKILL.md)
- [.agents/skills/core-bancario-argentina/references/controles.md](../../.agents/skills/core-bancario-argentina/references/controles.md)
- [.agents/skills/nfr-02-disponibilidad-recuperacion/SKILL.md](../../.agents/skills/nfr-02-disponibilidad-recuperacion/SKILL.md)
- [.agents/skills/nfr-05-seguridad-accesos/SKILL.md](../../.agents/skills/nfr-05-seguridad-accesos/SKILL.md)
- [.agents/skills/nfr-06-privacidad-residencia-retencion/SKILL.md](../../.agents/skills/nfr-06-privacidad-residencia-retencion/SKILL.md)
- [.agents/skills/nfr-07-auditoria-observabilidad/SKILL.md](../../.agents/skills/nfr-07-auditoria-observabilidad/SKILL.md)
- [.agents/skills/nfr-12-operabilidad-costos/SKILL.md](../../.agents/skills/nfr-12-operabilidad-costos/SKILL.md)
- [.agents/skills/adr-04-alta-disponibilidad/SKILL.md](../../.agents/skills/adr-04-alta-disponibilidad/SKILL.md)
- [.agents/skills/adr-06-aislamiento-por-celda/SKILL.md](../../.agents/skills/adr-06-aislamiento-por-celda/SKILL.md)
- [.agents/skills/adr-08-carga-inicial-masiva/SKILL.md](../../.agents/skills/adr-08-carga-inicial-masiva/SKILL.md)
