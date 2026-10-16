# Revisión comercial y de Dirección: viabilidad y rentabilidad

**Fecha de revisión:** 16/10/2026. **Baseline:** `2e5d579103b94ab70c16d81debe73bf5840ba0c8`. **Fuentes documentales:** 15/10/2026. **Estado:** revisión documental; no acredita clientes, equipo, presupuesto, entrevistas, contratos, producto implementado ni ensayos. No se actualizaron fuentes jurídicas por el mero cambio de fecha.

## Diagnóstico por perspectiva

**Comercial y marketing:** hay una hipótesis de entrada defendible —administración de préstamos o cartera satélite, con conciliación y localización explicables— y un reconocimiento correcto del poder del legado. Falta convertirla en una decisión sobre un comprador, un problema prioritario y un compromiso verificable de compra. La biblioteca de 32 módulos permite describir el horizonte; no acredita que el mercado compre toda esa suite ni que el primer producto deba financiarla completa.

**Dirección y rentabilidad:** el diseño exige servicios y responsabilidades cuyo costo no desaparece al usar infraestructura gestionada. El caso de negocio necesita una contribución por cliente y caja mensual que financien implementación, guardia, cambios locales y salida. El ejemplo del propio análisis ya muestra que su escenario base comercial no alcanza el punto de equilibrio de su ejemplo de estructura fija; ambos siguen siendo supuestos. Aprobar investigación o una prueba reversible es distinto de comprometer una plataforma, precio de producción o SLA financiados.

## Fortalezas verificadas en la documentación

- [Mercado](../market_analysis.md), §§2, 4 y 13: separa datos oficiales, declaraciones de proveedores, inferencias y supuestos; retira precios sin respaldo y no publica un TAM inventado. Esa disciplina debe mantenerse en propuestas.
- Mercado §§5.2, 5.8 y 6.2: reconoce referencias locales de incumbentes, modernización parcial y decisión de no cambiar; propone una entrada delimitada y evita financiar simultáneamente crédito y pagos con el mismo equipo inicial.
- [Arquitectura](../achitecture.md), §1, y [alcance funcional](../functional/scope.md): diferencian perfil/licencia y biblioteca futura de producto inicial; no ofrecen depósitos, BaaS o tarjetas por el solo hecho de disponer de código.
- Mercado §§8–9 y [MIG](../functional/29-carga-inicial-migracion-salida.md), FR-MIG-027 y FR-MIG-032: incorporan coexistencia, migración, retención, egreso y salida, además de licencias; reconocen que restaurar una base no revierte liquidaciones.
- [ADR-07](../adr/ADR-07-stack-gestionado.md), [NFR-12](../nfr/NFR-12-operabilidad-costos.md) y [OPS](../functional/30-operacion-continuidad-terceros.md), FR-OPS-027 y FR-OPS-028: exigen costo por celda, capacidad remanente y fuente de costos. El repositorio no afirma que ya estén medidos.
- [README funcional](../functional/README.md) y [cobertura](../functional/coverage.md): 1.016 FR en 32 módulos están identificados como especificación, con implementación/habilitación sin evaluar. La revisión no propone convertir el porcentaje de cobertura en una promesa de cumplimiento.

## Prioridad y fase de resolución

P0 significa resolver **antes del compromiso material indicado en cada hallazgo**, no incidente actual ni prohibición de análisis/desarrollo independiente. P1 exige decisión o evidencia para entrega controlada, escalado o retorno económico. No se piden contactos, contratos, despliegues ni cambios del baseline en esta revisión. Varias brechas ya estaban identificadas por el análisis de mercado: se convierten aquí en puertas de inversión verificables, sin presentarlas como errores aritméticos o capacidades inexistentes.

| Hallazgo | Prioridad | Decisión o evidencia necesaria |
|---|---|---|
| REV-COM-01 | P0 | El primer comprador y su caso de compra siguen sin seleccionarse |
| REV-COM-02 | P0 | La demanda comprable aún no está demostrada por evidencia de compradores |
| REV-COM-03 | P0 | La biblioteca de 1.016 FR todavía no tiene un manifiesto financiado de primera entrega |
| REV-COM-04 | P1 | La diferenciación necesita comparación y retorno demostrados en el problema elegido |
| REV-COM-05 | P1 | El proceso de compra y su calendario no están instanciados por oportunidad |
| REV-COM-06 | P1 | Faltan paquetes y unidades contractuales para convertir costo de servicio en precio defendible |
| REV-COM-07 | P0 | El piso de costo de una celda aislada todavía no está contrastado con el primer ACV |
| REV-COM-08 | P0 | La promesa de operación continua no tiene aún dotación y costo de guardia acreditados |
| REV-COM-09 | P1 | El TCO del comprador no resuelve la decisión de construir de un proveedor nuevo |
| REV-COM-10 | P1 | Alianzas y concentración se reconocen, pero aún no tienen una ruta comercial de sustitución |
| REV-COM-11 | P1 | La localización y la salida requieren alcance contractual y financiación durante toda la vida del servicio |
| REV-COM-12 | P0 | El escenario base aún no financia la estructura ilustrativa y falta un modelo mensual de caja |

## Hallazgos y acciones

### REV-COM-01 — El primer comprador y su caso de compra siguen sin seleccionarse

**Prioridad:** P0. **Tipo:** `missing_decision`. **Momento:** Antes de aprobar presupuesto material y un alcance/fecha de primera entrega para un segmento concreto.

La recomendación prioriza servicing de un prestamista y conserva pagos/PSPCP como alternativa. Es una buena estrategia provisional, pero no se documenta una selección efectiva de entidad compradora, problema urgente, cartera, dueño del presupuesto y rol responsable de aceptar el servicio. Bancos, PNFC y PSP no compran el mismo conjunto de integraciones ni soporte.

**Evidencia:**

- [docs/market_analysis.md](../market_analysis.md), §§3.2, 6.2 y 12.1: Hay siete segmentos y dos rutas iniciales de prioridad 1; el análisis dice expresamente que no deberían ejecutarse simultáneamente con el mismo equipo.
- [docs/achitecture.md](../achitecture.md), §1, supuestos: Se recomienda préstamos o cartera satélite; no hay entidad operadora, licencia, equipo, volumen o región elegidos.
- [docs/functional/01-entidades-perimetro.md](../functional/01-entidades-perimetro.md), FR-ENT-003, FR-ENT-019: Se especifican perfil y etapas de activación, sin evidencia de un perfil comercial ya elegido. IDs: FR-ENT-003, FR-ENT-019.

**Impacto:** Un mismo presupuesto puede terminar financiando dos productos con compradores, plazos y costos de servicio distintos; la propuesta comercial pierde precisión y aumenta el trabajo específico.

**Acciones propuestas:**

- Aprobar una ficha del cliente ideal inicial con sociedad/rol, tipo de cartera, problema cuantificado, disparador de compra, comprador económico, usuario beneficiario, dueño operativo y criterios de descarte.
- Elegir CREDITO o PAGOS para la primera inversión; conservar la otra ruta en la biblioteca, sin comprometer su implementación simultánea.

**Criterio de cierre:**

- Una decisión fechada identifica un solo perfil inicial y explica qué evidencia cambiaría la elección.
- Cada capacidad y dependencia de la primera propuesta se vincula al problema y al responsable de ese comprador; el segmento alternativo tiene condición explícita de entrada.

**Responsable sugerido:** Dirección y responsable de Producto/Comercial. **Dependencias:** Descubrimiento comercial; Cliente de diseño; Aplicabilidad por entidad y producto.

**Entregables sugeridos, aún no creados:** `docs/commercial/initial-icp.md`.

### REV-COM-02 — La demanda comprable aún no está demostrada por evidencia de compradores

**Prioridad:** P0. **Tipo:** `evidence_gap`. **Momento:** Antes de financiar el programa de construcción como negocio de producto o usar el escenario de ventas para justificar una inversión material.

El análisis distingue correctamente actividad financiera de demanda de reemplazo de core y declara pendientes entrevistas, censo y RFI. No se aportan en el corpus revisado oportunidades calificadas, disposición a pagar ni compromisos de clientes de diseño. Las 50 cuentas objetivo y tasas de adjudicación del escenario base son supuestos, no pipeline.

**Evidencia:**

- [docs/market_analysis.md](../market_analysis.md), §§2.1, 4.1, 7.1, 7.2 y 14: No hubo contactos ni acceso a contratos privados; las cuentas objetivo y conversiones se identifican como hipotéticas. El propio plan exige dos clientes de diseño compatibles.
- [docs/functional/coverage.md](../functional/coverage.md), MKT-01 y MKT-06: La cobertura vincula necesidades de producto con FR; no constituye validación de presupuesto o compra. IDs: FR-ENT-019, FR-ENT-030.

**Impacto:** Se puede completar un producto regulatoriamente exigente que las entidades no prioricen, no puedan comprar o sólo quieran como proyecto particular.

**Acciones propuestas:**

- Preparar el registro deduplicado de cuentas objetivo por sociedad y grupo, con fuente, actividad, sistema actual, motivo para cambiar, presupuesto y estado comprobado de compra; separar desconocidos.
- Ejecutar en una fase autorizada el descubrimiento previsto y registrar evidencia del problema, alternativas actuales, acceso a decisión y compromiso de piloto; no tratar interés informal como venta.
- Aplicar la puerta de dos clientes de diseño de mercado §12.2, comparando alcance común, aportes del cliente, condiciones y evidencia real del compromiso.

**Criterio de cierre:**

- Las hipótesis N, apertura de compra y conversión tienen fuente o se muestran como sensibilidad, nunca como oportunidades existentes.
- La puerta de diseño tiene evidencia de al menos dos clientes con problema/presupuesto/decisor y alcance compatible, o Dirección registra que no se cumplió y reduce/pospone la inversión afectada.

**Responsable sugerido:** Responsable Comercial y Dirección. **Dependencias:** ICP seleccionado; Autorización para contactos comerciales futuros; Acceso autorizado a datos representativos.

**Entregables sugeridos, aún no creados:** `docs/commercial/demand-evidence.md`, `docs/commercial/design-partner-gate.md`.

### REV-COM-03 — La biblioteca de 1.016 FR todavía no tiene un manifiesto financiado de primera entrega

**Prioridad:** P0. **Tipo:** `missing_decision`. **Momento:** Antes de estimar precio fijo, fecha de piloto integrado o capacidad de entrega del primer producto.

El alcance distingue claramente biblioteca completa y rutas iniciales; por tanto, los 32 módulos no son un MVP anunciado. Sin embargo, no se encuentra un manifiesto de release que seleccione FR, dependencias, integraciones y obligaciones de un cliente concreto con esfuerzo, capacidad y presupuesto. La clasificación BASE/CREDITO/PAGOS por sí sola no calcula qué debe entregarse.

**Evidencia:**

- [docs/functional/README.md](../functional/README.md), Módulos y cómo convertirlos en una entrega verificable: El inventario contiene 1.016 FR en 32 módulos y pide seleccionar módulos/dependencias.
- [docs/functional/scope.md](../functional/scope.md), Perfiles y activación: CREDITO y PAGOS son alternativas y las etapas no aplazan controles aplicables.
- [docs/functional/01-entidades-perimetro.md](../functional/01-entidades-perimetro.md), FR-ENT-019, FR-ENT-020 y FR-ENT-030: Existe soporte funcional para etapas, dependencias y preparación; no hay evidencia de selección/aprobación efectiva. IDs: FR-ENT-019, FR-ENT-020, FR-ENT-030.

**Impacto:** La estimación puede incluir toda la suite por precaución o excluir controles transversales indispensables para el producto activo; ambos extremos invalidan costo y fecha comercial.

**Acciones propuestas:**

- Derivar un manifiesto del primer release por sociedad/producto con FR incluidos, dependencias transitivas, controles, datos, integraciones, criterios de aceptación y exclusiones fundadas.
- Estimar paquetes de trabajo y capacidad real, separando producto común, localización reutilizable, configuración e integración específica.
- Conservar la biblioteca integral y su trazabilidad; reducir exposición/funciones ofrecidas en vez de eliminar controles legales del perfil elegido.

**Criterio de cierre:**

- Cada FR incluido y dependencia material tiene responsable, estimación y aceptación; cada exclusión tiene fundamento por perfil y no por falta de tiempo.
- Precio y fecha se calculan desde ese manifiesto y la capacidad financiada, con cambios de alcance versionados y aprobados.

**Responsable sugerido:** Dirección de Producto, Arquitectura y Entrega. **Dependencias:** ICP; Perfil normativo del cliente; Capacidad del equipo y terceros.

**Entregables sugeridos, aún no creados:** `docs/commercial/first-release-manifest.md`, `docs/commercial/delivery-estimate.md`.

### REV-COM-04 — La diferenciación necesita comparación y retorno demostrados en el problema elegido

**Prioridad:** P1. **Tipo:** `evidence_gap`. **Momento:** Antes de afirmar una ventaja cuantificada en una propuesta o elegir el posicionamiento de venta.

Trazabilidad contable, cambios locales y conciliación constituyen una hipótesis coherente, pero proveedores establecidos también comercializan localización e integración. El análisis no ofrece un benchmark comparativo ni línea de base de cliente. Tener APIs, más FR o una matriz normativa extensa no demuestra reducción de costo o tiempo frente a conservar/mejorar el sistema actual.

**Evidencia:**

- [docs/market_analysis.md](../market_analysis.md), §§5.2, 5.8, 6.1 y 11.4: Se reconoce al legado/modernización como sustituto y se exige medir valor desde una línea de base, sin porcentajes inventados.
- [docs/functional/04-productos-configuracion.md](../functional/04-productos-configuracion.md), FR-CFG-030: Se propone registrar tiempo, costo y trabajo específico por cambio. IDs: FR-CFG-030.
- [docs/functional/coverage.md](../functional/coverage.md), MKT-02, MKT-03 y MKT-06: Localización, coexistencia y piloto tienen soporte funcional propuesto, no resultados comerciales medidos.

**Impacto:** La venta se reduce a una lista de funcionalidades y compite con referencias/solvencia superiores sin demostrar por qué conviene asumir el riesgo de un proveedor nuevo.

**Acciones propuestas:**

- Elegir dos o tres resultados decisivos del ICP, como horas para reconstruir saldo, costo de conciliación o costo/tiempo de cambio local, y fijar su medición antes del piloto.
- Comparar contra el proceso actual y una mejora parcial viable, con el mismo volumen y alcance; incluir integración, coexistencia y costo del cambio.
- Convertir sólo los resultados observados en mensajes comerciales y mantener separados funcionalidad diseñada, demostrada, homologada y productiva.

**Criterio de cierre:**

- Un acta del piloto preserva línea de base, muestra, costos, reglas de medición y resultado observado, incluido un resultado desfavorable.
- La propuesta vincula el precio con beneficio atribuible y verificable; no contabiliza como ahorro un costo del legado que continúa existiendo.

**Responsable sugerido:** Producto/Marketing, Operaciones del cliente y Finanzas. **Dependencias:** Cliente de diseño; Acceso a línea de base; Criterios de piloto acordados.

**Entregables sugeridos, aún no creados:** `docs/commercial/value-proof.md`.

### REV-COM-05 — El proceso de compra y su calendario no están instanciados por oportunidad

**Prioridad:** P1. **Tipo:** `specification_gap`. **Momento:** Antes de comprometer fecha de firma, ingresos, piloto con datos reales o puesta en producción de una oportunidad.

El análisis identifica correctamente a negocio, tecnología, finanzas, riesgos, seguridad, legales y compras, pero no existe una ruta concreta por oportunidad que relacione decisores, aprobaciones, acceso a datos, contrato, participación de terceros y calendario regulatorio aplicable. Los meses ilustrativos de la hoja de ruta no son duración acreditada de compra bancaria.

**Evidencia:**

- [docs/market_analysis.md](../market_analysis.md), §§11.1, 12.1 y 12.2: Se describe venta consultiva y puertas de entrega, sin tiempos reales de contratación ni oportunidades instanciadas.
- [docs/functional/30-operacion-continuidad-terceros.md](../functional/30-operacion-continuidad-terceros.md), FR-OPS-032 y FR-OPS-041: Tercerización y nuevo servicio digital tienen expedientes y plazos distintos según aplicabilidad; no sustituyen firma contractual ni uno al otro. IDs: FR-OPS-032, FR-OPS-041.
- [docs/functional/01-entidades-perimetro.md](../functional/01-entidades-perimetro.md), FR-ENT-020: La activación requiere dependencias documentales, operativas y contractuales. IDs: FR-ENT-020.

**Impacto:** La caja puede contar ventas antes de que compras/seguridad permitan contratar o de que el cliente pueda entregar datos y completar avisos; se asigna equipo a oportunidades que no avanzan.

**Acciones propuestas:**

- Preparar un plan de compra/entrega por oportunidad con comprador económico, beneficiario, responsable operativo, aprobadores, compras, contratos, datos y contraparte de riel.
- Separar descubrimiento, demostración, piloto sin efectos reales, piloto productivo, firma, facturación, activación y cobro; registrar evidencia de paso entre etapas.
- Incorporar avisos/homologaciones sólo si aplican al sujeto/servicio y dejar su validación al responsable competente; no imponer un plazo bancario a todo PNFC o prueba sintética.

**Criterio de cierre:**

- Cada oportunidad incluida en caja tiene responsable, próxima decisión y fechas con fundamento, además de dependencias del cliente/tercero.
- El escenario de demora muestra impacto en recursos y cobros; la fecha comercial no precede dependencias indispensables sin una excepción legítima y documentada.

**Responsable sugerido:** Comercial/Entrega, Compras y responsables institucionales del cliente. **Dependencias:** Oportunidad calificada; Revisión Legal/Cumplimiento; Contrapartes y datos.

**Entregables sugeridos, aún no creados:** `docs/commercial/opportunity-plan.md`.

### REV-COM-06 — Faltan paquetes y unidades contractuales para convertir costo de servicio en precio defendible

**Prioridad:** P1. **Tipo:** `missing_decision`. **Momento:** Antes de emitir una cotización vinculante o desarrollar facturación de consumo para el proveedor.

El mercado propone diagnóstico, piloto, implementación y suscripción y enumera mínimos/bandas, pero no define paquetes, unidad facturable, incluidos, sobreconsumo ni política de cambios. FR-OPS-027 mide costo técnico y FR-CFG-013 cargos del producto financiero: ninguno demuestra que la facturación SaaS del proveedor esté definida.

**Evidencia:**

- [docs/market_analysis.md](../market_analysis.md), §§4.2, 8.1 y 12.1: Se advierte sobre cuentas abiertas/activas, reintentos facturables, entornos, salida y cargos; los precios son una estructura a validar.
- [docs/functional/30-operacion-continuidad-terceros.md](../functional/30-operacion-continuidad-terceros.md), FR-OPS-027: El costo por celda/cuenta/unidad técnica es una funcionalidad propuesta, no una tarifa de venta. IDs: FR-OPS-027.
- [docs/functional/04-productos-configuracion.md](../functional/04-productos-configuracion.md), FR-CFG-013 y FR-CFG-030: Se distinguen comisiones del producto y esfuerzo de cambio, útiles para medir pero diferentes de una licencia SaaS. IDs: FR-CFG-013, FR-CFG-030.

**Impacto:** Cuentas inactivas, amplificación técnica, descuentos o soporte no limitado pueden producir una factura que el comprador no entiende y un contrato recurrente deficitario.

**Acciones propuestas:**

- Definir paquetes por resultado y perfil, separando producto común/localización, integraciones, migración, operación, entornos y cambios específicos; no presentar BANCA/EXT como incluidos por existir FR.
- Elegir y definir cada unidad facturable y su identidad/deduplicación, estados contados, mínimo, bandas y regla de reverso/corrección; documentar quién paga terceros e impuestos.
- Preparar simulador de factura contractual separado del cobro financiero a usuarios, con reglas de descuento y aprobación por contribución esperada.

**Criterio de cierre:**

- Un mes de actividad sintética con inactivos, duplicados, rechazos, reversos y pico produce factura reproducible y explicable según contrato.
- El precio/mínimo de cada paquete cubre el costo del perfil y margen aprobado bajo la sensibilidad adversa; las hipótesis de precio no se anuncian como cotizaciones reales.

**Responsable sugerido:** Comercial, Finanzas y Producto. **Dependencias:** Costo por perfil; Unidad de valor validada; Condiciones contractuales y fiscales.

**Entregables sugeridos, aún no creados:** `docs/commercial/packages-pricing-policy.md`, `docs/commercial/billing-examples.md`.

### REV-COM-07 — El piso de costo de una celda aislada todavía no está contrastado con el primer ACV

**Prioridad:** P0. **Tipo:** `evidence_gap`. **Momento:** Antes de firmar precio de producción, capacidad y SLO de una celda para un cliente.

La separación por entidad, PostgreSQL HA, bus multizona, región pasiva, claves, entornos y evidencia generan costos fijos además del costo por transacción. ADR-07 y NFR-12 exigen medirlos; no hay cotización/consumo ni un margen por perfil demostrado. El escenario de 250.000 cuentas no sirve por sí solo para el costo del primer prestamista pequeño.

**Evidencia:**

- [docs/achitecture.md](../achitecture.md), §§1, 10, 14 y 15: Una celda contiene inicialmente una entidad; se diseña HA y recuperación con costos explícitos pendientes de validar.
- [docs/adr/ADR-07-stack-gestionado.md](../adr/ADR-07-stack-gestionado.md), Decisión, consecuencias y aceptación: Se reconoce costo mínimo, dependencia contractual y alternativa de cola más simple si se revisa la semántica. IDs: ADR-07.
- [docs/nfr/NFR-12-operabilidad-costos.md](../nfr/NFR-12-operabilidad-costos.md), NFR-12-C03 y NFR-12-C04: Costo calculable y capacidad/presupuesto contrastados son propuestos y no medidos. IDs: NFR-12-C03, NFR-12-C04.
- [docs/functional/30-operacion-continuidad-terceros.md](../functional/30-operacion-continuidad-terceros.md), FR-OPS-027 y FR-OPS-028: Existen funciones propuestas de costeo y evaluación antes de ampliar exposición. IDs: FR-OPS-027, FR-OPS-028.

**Impacto:** Un ACV atractivo en un promedio de cartera puede no cubrir la primera celda o la región/retención contratadas; crecer añade pérdida en lugar de financiar el producto.

**Acciones propuestas:**

- Costear el perfil real desde cotizaciones o consumo de ensayo, separando recursos dedicados y compartidos con una regla de asignación y evitando suponer un cluster Kafka exclusivo por cliente.
- Modelar piso, costo marginal y escalones por entidad/volumen/retención/región, incluyendo capacidad para perder un dominio de fallo.
- Si no cierra, revisar precio, segmento, alcance o alternativa de plataforma mediante ADR; demostrar nuevamente durabilidad, aislamiento, orden y replay, sin recortar controles legales para obtener margen.

**Criterio de cierre:**

- El modelo del primer cliente contiene fuente/fecha, moneda, mínimos, cargos compartidos, escenarios de carga y retención, costo mensual y contribución.
- La configuración ofrecida y el costo permiten el margen/apetito aprobados con controles activos; si no, se rediseña o no se compromete ese precio/perfil.

**Responsable sugerido:** Finanzas, Plataforma y Dirección. **Dependencias:** Perfil de despliegue; Cotizaciones/ensayo de consumo; Precio y margen objetivo aprobados.

**Entregables sugeridos, aún no creados:** `docs/commercial/cell-unit-economics.md`.

### REV-COM-08 — La promesa de operación continua no tiene aún dotación y costo de guardia acreditados

**Prioridad:** P0. **Tipo:** `evidence_gap`. **Momento:** Antes de contratar soporte/recuperación continuos o admitir fondos reales bajo ese perfil operativo.

Los documentos piden dueños, suplencia, guardia y procedimientos ejecutables por personas distintas del autor. No hay equipo, disponibilidad ni costo acreditados. Servicios gestionados no asumen investigación de pagos ambiguos, decisión institucional, atención al cliente, avisos ni conciliación. Es una necesidad de implementación, no una función ausente del catálogo.

**Evidencia:**

- [docs/achitecture.md](../achitecture.md), §§1 y 15: No hay equipo elegido; se requieren guardia y runbooks para riel, diferencias, claves y recuperación.
- [docs/nfr/NFR-12-operabilidad-costos.md](../nfr/NFR-12-operabilidad-costos.md), NFR-12-C01, NFR-12-C02 y NFR-12-C05: Se exige cobertura real del inventario crítico y ejecución por roles distintos del autor. IDs: NFR-12-C01, NFR-12-C02, NFR-12-C05.
- [docs/functional/30-operacion-continuidad-terceros.md](../functional/30-operacion-continuidad-terceros.md), FR-OPS-003, FR-OPS-018 y FR-OPS-021: Se distingue suplencia operativa de comunicación por responsable autorizado. IDs: FR-OPS-003, FR-OPS-018, FR-OPS-021.

**Impacto:** El fundador absorbe servicio y desarrollo simultáneamente; incidentes y obligaciones de respuesta consumen margen y pueden dejar sin cobertura la producción o impedir nuevas implementaciones.

**Acciones propuestas:**

- Construir matriz proveedor/entidad/tercero de cobertura, primera y segunda línea, suplentes, escalamiento, funciones incompatibles y autorizaciones fuera de horario.
- Presupuestar turnos/guardia, descanso, ausencias, formación, seguridad, auditoría y ensayos; distinguir guardia pasiva de atención activa continua.
- Ensayar un incidente nocturno y un cierre con personal de reemplazo y ajustar capacidad antes de vender el perfil; declarar dependencias personales restantes.

**Criterio de cierre:**

- Hay cobertura nominada y financiada del perfil acordado y de sus funciones institucionales, con suplencia verificable y sin violar segregación.
- El ejercicio conserva tiempos, escalamiento, decisiones y evidencia por un rol distinto del autor; su costo está asignado una sola vez en el modelo económico.

**Responsable sugerido:** Dirección, Operaciones/SRE y funciones responsables de la entidad. **Dependencias:** SLA/BIA y alcance; Contratos de terceros; Disponibilidad de personas y presupuesto.

**Entregables sugeridos, aún no creados:** `docs/commercial/service-staffing-cost.md`.

### REV-COM-09 — El TCO del comprador no resuelve la decisión de construir de un proveedor nuevo

**Prioridad:** P1. **Tipo:** `missing_decision`. **Momento:** Antes de financiar construcción propia de un motor completo o pactar reventa/OEM de un tercero.

El análisis distingue correctamente banco comprador y fabricante de producto, y no concluye que construir sea superior. La tabla de TCO es un ejemplo del comprador con alcance acotado; no contiene cotizaciones ni economía de derechos, licencias/OEM, distribución y reutilización del proveedor nuevo. No se documenta una elección efectiva entre motor propio, motor comprado más capa local o módulo satélite.

**Evidencia:**

- [docs/market_analysis.md](../market_analysis.md), §§1, 5.8, 7.3, 8.2, 8.3 y 12.4: Se separan las dos decisiones; el TCO excluye varias partidas y se rotula como hipotético, sin precios reales de fabricantes.
- [docs/adr/ADR-07-stack-gestionado.md](../adr/ADR-07-stack-gestionado.md), Alternativas y consecuencias: La plataforma gestionada es una decisión de infraestructura y no una comparación de motores financieros comprados. IDs: ADR-07.

**Impacto:** Se puede asumir un riesgo de producto/soporte multianual porque un ejemplo de TCO permite construir, sin demostrar ventaja económica frente a comprar o coexistir.

**Acciones propuestas:**

- Comparar para el mismo ICP tres rutas viables: motor propio acotado, motor contratado con localización y módulo satélite/coexistencia; usar el RFI y al menos tres propuestas comparables previstos en mercado §14 cuando corresponda.
- Separar TCO del cliente de economía del proveedor: propiedad/derechos, regalías/mínimos, integraciones, SLA, cambios locales, actualización, portabilidad y financiación.
- Registrar un ADR/decisión de inversión con qué capacidades diferencian, qué se compra y evidencia que obligaría a cambiar la opción.

**Criterio de cierre:**

- Las alternativas tienen idéntico alcance y calidad de servicio, fuentes separadas entre cotización/supuesto/medición y cronogramas propios.
- La opción elegida conserva margen, control y salida para el negocio proveedor y caso de valor para el cliente; no se usa la tabla hipotética como oferta comercial.

**Responsable sugerido:** Dirección, Finanzas, Arquitectura y Legal. **Dependencias:** ICP; RFI/cotizaciones autorizados; Modelo de propiedad intelectual y salida.

**Entregables sugeridos, aún no creados:** `docs/commercial/build-buy-investment-decision.md`.

### REV-COM-10 — Alianzas y concentración se reconocen, pero aún no tienen una ruta comercial de sustitución

**Prioridad:** P1. **Tipo:** `evidence_gap`. **Momento:** Antes de ofertar un riel, implementación o soporte que dependa de un único partner, banco o persona, y antes de ampliar exposición comercial.

El mercado identifica implementadores, especialistas locales y proveedores de pagos como aliados y registra concentración por cliente/persona. FR-OPS y COR especifican due diligence y contratos. No se aportan acuerdos, capacidad reservada, economía del canal ni prueba de qué ocurre si falla la dependencia comercial/operativa principal.

**Evidencia:**

- [docs/market_analysis.md](../market_analysis.md), §§10.1, 10.2, 12.1 y 12.3: Se reconoce poder de integradores/proveedores y riesgo de un solo contrato/persona; no se acreditan alianzas firmadas.
- [docs/functional/30-operacion-continuidad-terceros.md](../functional/30-operacion-continuidad-terceros.md), FR-OPS-029 y FR-OPS-036: Concentración y salida están especificadas, sin evidencia de evaluación o sustitución. IDs: FR-OPS-029, FR-OPS-036.
- [docs/functional/32-corresponsalia-baas-plataformas.md](../functional/32-corresponsalia-baas-plataformas.md), FR-COR-005 y propósito: Se requieren contrato y responsabilidades por participante; BaaS no es licencia. IDs: FR-COR-005.

**Impacto:** Un proveedor puede comprometer entregas sin acceso efectivo al riel o capacidad del implementador; un cliente grande puede condicionar roadmap/caja y un partner capturar el margen o la relación comercial.

**Acciones propuestas:**

- Preparar mapa de dependencias críticas y comerciales con propietario de relación, responsabilidad de soporte, capacidad, condiciones económicas, derechos sobre cliente/código y posibilidad real de sustitución.
- Medir exposición a cliente/grupo, partner, custodio y personas; fijar apetito y escenario de pérdida del principal, incluyendo costos y tiempo de transición.
- Si no hay sustituto viable, registrar la concentración y acotar compromisos/respaldo; no inventar disponibilidad de un segundo proveedor por completar una casilla.

**Criterio de cierre:**

- Cada dependencia de una oferta tiene acuerdo/evidencia de acceso y capacidad o figura como condición suspensiva visible de esa oferta.
- Dirección dispone de escenario de pérdida del principal cliente/partner con efecto en caja, servicio y roadmap, decisión de exposición y acciones financiadas.

**Responsable sugerido:** Dirección Comercial, Operaciones y Gestión de Terceros. **Dependencias:** Contratos de partners y clientes; Mapa operativo de dependencias; Modelo mensual de caja.

**Entregables sugeridos, aún no creados:** `docs/commercial/partners-concentration.md`.

### REV-COM-11 — La localización y la salida requieren alcance contractual y financiación durante toda la vida del servicio

**Prioridad:** P1. **Tipo:** `specification_gap`. **Momento:** Antes de incluir cambios normativos, certificaciones, conservación o asistencia de salida en un precio/plazo vinculantes.

La documentación exige localización versionada, pruebas independientes según alcance, archivo, portabilidad y salida, y los reconoce como costos. No existe un paquete operativo/económico que distinga mantenimiento común, nueva función/país/estándar, personalización y trabajo de salida. Tampoco se acredita quién financia datos/consultas/archivo y transición después de terminar la suscripción.

**Evidencia:**

- [docs/market_analysis.md](../market_analysis.md), §§8.1, 8.3, 9.2, 11.1 y 14: Quedan pendientes presupuesto de localización y mantenimiento; salida/archivo son partidas ilustrativas, no precios contratados.
- [docs/functional/30-operacion-continuidad-terceros.md](../functional/30-operacion-continuidad-terceros.md), FR-OPS-025, FR-OPS-030 y FR-OPS-042: Se registran QA/evidencia externa, contratos y programas por alcance; no toda ISO/PCI es obligatoria. IDs: FR-OPS-025, FR-OPS-030, FR-OPS-042.
- [docs/functional/29-carga-inicial-migracion-salida.md](../functional/29-carga-inicial-migracion-salida.md), FR-MIG-032: El costo observado de salida incluye egreso, claves, retención y coexistencia. IDs: FR-MIG-032.
- [docs/functional/04-productos-configuracion.md](../functional/04-productos-configuracion.md), FR-CFG-030: Se propone medir trabajo específico y tiempo de cambio. IDs: FR-CFG-030.

**Impacto:** Una suscripción aparentemente rentable puede absorber cambios ilimitados, auditorías/homologaciones nuevas y años de deberes remanentes; cobrar por salir sin previsión deteriora confianza y portabilidad.

**Acciones propuestas:**

- Definir en contrato qué cambios comunes están incluidos, responsables/fuentes, proceso de impacto/prueba y tratamiento de ampliación de producto/país/red; no condicionar el cumplimiento exigible a una excepción económica.
- Costear actualización normativa, revisión profesional, pruebas/regresión y evidencia independiente según perímetro, separando costos comunes y específicos sin doble asignar personal.
- Preparar anexo de salida/archivo con objetos, formatos, claves, servicios remanentes, ventana, precios o reglas de cálculo y fuente de financiación tras terminación; probarlo sin dependencia del proveedor saliente.

**Criterio de cierre:**

- El primer contrato y presupuesto vinculan cada obligación de mantenimiento/archivo/salida con responsable, alcance y costo; no anuncian certificaciones pendientes como incluidas/obtenidas.
- Un escenario de terminación antes de recuperar la implementación y uno de nueva exigencia aplicable muestran costo remanente y financiación, manteniendo deberes legales y acceso acordado.

**Responsable sugerido:** Dirección, Legal/Cumplimiento, Finanzas y Operaciones. **Dependencias:** Perfil normativo y contratos; Plan de salida; Cotización de evidencia y terceros aplicables.

**Entregables sugeridos, aún no creados:** `docs/commercial/localization-service-scope.md`, `docs/commercial/exit-retention-economics.md`.

### REV-COM-12 — El escenario base aún no financia la estructura ilustrativa y falta un modelo mensual de caja

**Prioridad:** P0. **Tipo:** `evidence_gap`. **Momento:** Antes de aprobar el programa de inversión, contratar costos fijos relevantes o firmar un acuerdo cuyo cobro dependa del go-live del cliente.

Mercado §7.2 estima 4,375 contratos y ARR de salida de USD 1,3125 millones al mes 36, suponiendo que todos están implementados y no hay bajas. §7.3 usa por separado ACV de USD 300.000, margen bruto 65% y costo fijo anual USD 2,4 millones: con esas mismas hipótesis, la contribución del escenario base es USD 0,853125 millones/año y el faltante frente a ese costo fijo es USD 1,546875 millones/año. El propio documento advierte la brecha; no hay error aritmético ni prueba de pérdida real, pero tampoco caja/runway o financiación acreditados que la resuelvan.

**Evidencia:**

- [docs/market_analysis.md](../market_analysis.md), §§7.2 y 7.3: La base de 4,375 contratos no cubre los aproximadamente 13 clientes equivalentes del ejemplo separado. ARR de salida no es ingreso acumulado ni caja.
- [docs/market_analysis.md](../market_analysis.md), §§8.2, 8.3, 8.4, 12.2 y 14: Hay costos excluidos, plazos de entrega ilustrativos y un pendiente explícito de caja mensual con demoras de venta/entrega/cobro.
- [docs/nfr/NFR-12-operabilidad-costos.md](../nfr/NFR-12-operabilidad-costos.md), NFR-12-C03 y NFR-12-C04: Se pide presupuesto por perfil, pero no hay presupuesto/margen aprobado ni consumo observado. IDs: NFR-12-C03, NFR-12-C04.

**Impacto:** Puede agotarse la caja antes de convertir las primeras ventas en servicios aceptados y cobrados; ingresos de implementación y ARR contratado pueden ocultar pérdida recurrente o capital de trabajo insuficiente.

**Acciones propuestas:**

- Construir modelo mensual por cohorte con reservas comerciales, contratos firmados, fecha de implementación/activación, ingreso reconocido y cobros separados; documentar moneda, impuestos/retenciones, indexación y pagos a terceros.
- Asignar costos de construcción, adquisición/venta, implementación, COGS, mantenimiento común y administración sin doble contar personas ni esconder trabajo directo como desarrollo reutilizable.
- Negociar hitos objetivos de alcance/datos/aceptación/cobro, anticipos y cambio de alcance con Legal; modelar dependencia del cliente, retenciones, penalidades y costo de demora sin presumir contratos existentes.
- Someter inversión a escenarios de demora, baja conversión, churn del principal, sobrecosto de implementación, cambio local y descalce de moneda; fijar hitos de continuar/reducir/detener y financiación comprometida.

**Criterio de cierre:**

- Un modelo reconciliable de ingresos, contribución, caja y fondos comprometidos cubre hasta la siguiente puerta y la operación contratada bajo el escenario aprobado, con acción explícita si la caja mínima se vulnera.
- Supuestos de ACV, margen, costos y fechas tienen fuente o etiqueta de hipótesis; un contrato no implementado no se presenta como cliente en producción ni como cobro.
- Las aprobaciones de precio, descuento, nueva contratación y expansión muestran impacto en caja y margen por cliente/cohorte.

**Responsable sugerido:** Dirección y Finanzas, con Comercial/Entrega y Legal. **Dependencias:** ICP y pipeline calificado; Costo por celda/servicio; Dotación y términos de contrato; Financiación y apetito económico.

**Entregables sugeridos, aún no creados:** `docs/commercial/monthly-cash-and-runway.md`, `docs/commercial/investment-gates.md`.

## Modelo económico mínimo y sensibilidades

Las fórmulas proponen una forma de decisión; no constituyen precios ni costos observados. Usar una moneda/base temporal consistente y separar costo técnico, unidad facturable y unidad de valor. El TCO del comprador y la rentabilidad del proveedor son modelos relacionados, pero diferentes.

```text
Contribución recurrente_i = ingreso recurrente neto_i − COGS atribuible_i
Margen bruto_i = contribución recurrente_i / ingreso recurrente neto_i
Contribución de implementación_i = ingreso de implementación_i − costo directo de entrega_i
Resultado operativo de período = Σ contribuciones − costos comunes no asignados
Clientes de equilibrio = costos fijos / contribución recurrente anual por cliente
Caja_cierre_mes = caja_apertura + cobros efectivos − pagos efectivos
Financiación necesaria = déficit máximo acumulado + colchón aprobado
```

No asignar la misma persona simultáneamente al desarrollo inicial, COGS y costos fijos. Registrar cómo se distribuye su tiempo. La contribución recurrente no absorbe automáticamente costo de adquisición, desarrollo inicial ni capital de trabajo; deben aparecer en la decisión de inversión/caja. Sin evidencia de retención no calcular un LTV de precisión aparente mediante una tasa de churn supuesta e invisible.

La sensibilidad aritmética de REV-COM-12 usa sólo los ejemplos existentes: `4,375 × 300.000 × 0,65 = USD 853.125/año`; contra `USD 2.400.000/año` de costo fijo hipotético, queda `USD 1.546.875/año` por financiar o eliminar. No es un presupuesto real ni la pérdida observada de una empresa. No se extrapola el margen del 65 % a otros segmentos como hecho.

Antes de decidir, variar por separado: conversión y fecha de firma; demora de datos/aceptación/go-live; calendario de cobros/anticipos/retenciones; sobrecosto de implementación y soporte; costo mínimo/marginal de cada celda; mezcla de perfiles; crecimiento de archivo/egreso; cambio normativo específico; moneda/indexación; baja o impago del principal cliente y pérdida del partner crítico. Mostrar contribución, caja mínima, financiación y acción de Dirección para cada escenario. ARR contratado, ARR implementado, ingreso reconocido y efectivo cobrado se muestran separados.

## Cuestiones institucionales pendientes

Dirección debe elegir perfil y apetito de inversión; Comercial debe aportar evidencia de compra; Producto/Entrega debe cerrar el manifiesto y aceptación; Finanzas debe resolver precio, contribución y financiación; Operaciones debe acreditar cobertura; Legal/Cumplimiento deben concretar contratos, perímetro y avisos aplicables. Una aceptación de riesgo no elimina una obligación legal ni convierte un costo sin financiar en servicio disponible.

La contratación de terceros, contactos comerciales, presupuesto, personal y pruebas productivas requieren su fase y responsables reales. Esta revisión sólo documenta decisiones/evidencia necesarias; no afirma que haya ocurrido ninguna de ellas ni modifica FR, NFR, ADR, skills o índices del baseline.

## Documentos revisados y límites

Se leyó completo el análisis de mercado, con su tabla TCO, fuentes y límites; el inventario de 32 módulos/1.016 FR y su alcance; las decisiones/cualidades pertinentes y los módulos comerciales/operativos citados. En fuentes técnicas y regulatorias se revisaron las secciones relevantes; no se rehízo una due diligence jurídica ni se evaluaron uno a uno los 1.016 FR desde todas las disciplinas. Los archivos siguientes identifican lecturas completas o selectivas; el registro estructurado conserva la misma lista.

- [docs/README.md](../README.md)
- [docs/market_analysis.md](../market_analysis.md)
- [docs/achitecture.md](../achitecture.md)
- [docs/compliant.md](../compliant.md)
- [docs/functional/README.md](../functional/README.md)
- [docs/functional/scope.md](../functional/scope.md)
- [docs/functional/catalog.json](../functional/catalog.json)
- [docs/functional/coverage.md](../functional/coverage.md)
- [docs/functional/01-entidades-perimetro.md](../functional/01-entidades-perimetro.md)
- [docs/functional/04-productos-configuracion.md](../functional/04-productos-configuracion.md)
- [docs/functional/28-integraciones-eventos-trabajos.md](../functional/28-integraciones-eventos-trabajos.md)
- [docs/functional/29-carga-inicial-migracion-salida.md](../functional/29-carga-inicial-migracion-salida.md)
- [docs/functional/30-operacion-continuidad-terceros.md](../functional/30-operacion-continuidad-terceros.md)
- [docs/functional/32-corresponsalia-baas-plataformas.md](../functional/32-corresponsalia-baas-plataformas.md)
- [docs/adr/ADR-02-autoridad-sql.md](../adr/ADR-02-autoridad-sql.md)
- [docs/adr/ADR-03-outbox-inbox.md](../adr/ADR-03-outbox-inbox.md)
- [docs/adr/ADR-05-configuracion-versionada.md](../adr/ADR-05-configuracion-versionada.md)
- [docs/adr/ADR-06-aislamiento-por-celda.md](../adr/ADR-06-aislamiento-por-celda.md)
- [docs/adr/ADR-07-stack-gestionado.md](../adr/ADR-07-stack-gestionado.md)
- [docs/adr/ADR-08-carga-inicial-masiva.md](../adr/ADR-08-carga-inicial-masiva.md)
- [docs/nfr/NFR-01-integridad-financiera.md](../nfr/NFR-01-integridad-financiera.md)
- [docs/nfr/NFR-04-asincronia-durable.md](../nfr/NFR-04-asincronia-durable.md)
- [docs/nfr/NFR-08-interoperabilidad-portabilidad.md](../nfr/NFR-08-interoperabilidad-portabilidad.md)
- [docs/nfr/NFR-11-calidad-datos-reportes.md](../nfr/NFR-11-calidad-datos-reportes.md)
- [docs/nfr/NFR-12-operabilidad-costos.md](../nfr/NFR-12-operabilidad-costos.md)
- [docs/nfr/NFR-13-accesibilidad-experiencia.md](../nfr/NFR-13-accesibilidad-experiencia.md)
- [.agents/skills/core-bancario-argentina/SKILL.md](../../.agents/skills/core-bancario-argentina/SKILL.md)
- [.agents/skills/core-bancario-argentina/references/controles.md](../../.agents/skills/core-bancario-argentina/references/controles.md)
- [.agents/skills/core-adr-arquitectura/SKILL.md](../../.agents/skills/core-adr-arquitectura/SKILL.md)
- [.agents/skills/core-nfr-calidad/SKILL.md](../../.agents/skills/core-nfr-calidad/SKILL.md)
- [.agents/skills/adr-07-stack-gestionado/SKILL.md](../../.agents/skills/adr-07-stack-gestionado/SKILL.md)
- [.agents/skills/nfr-12-operabilidad-costos/SKILL.md](../../.agents/skills/nfr-12-operabilidad-costos/SKILL.md)

Datos estructurados y todos los campos de seguimiento: [findings/commercial.json](findings/commercial.json). No se realizaron entrevistas, solicitudes de cotización ni consultas externas de vigencia en esta revisión.
