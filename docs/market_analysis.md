# Mercado de core bancario en Argentina

**Análisis estratégico para construir, comprar y comercializar una plataforma bancaria**

**Fecha de corte y consulta de fuentes:** 15 de octubre de 2026, Argentina.

**Versión:** 1.0. Importes de los modelos: USD constantes, salvo indicación contraria.

## 1. Decisión ejecutiva

La oportunidad más defendible para un nuevo proveedor consiste en resolver una parte delimitada de la operación financiera argentina con trazabilidad contable, integraciones locales y evidencia de control. Intentar competir desde el inicio como reemplazo integral de todos los sistemas de un banco universal exige una amplitud funcional, una capacidad de migración y un compromiso de soporte que no quedan demostrados por disponer de un buen ledger o de APIs modernas.

La recomendación inicial es **construir una plataforma modular de cuentas y/o administración de préstamos, con una capa argentina de contabilidad, conciliación, datos regulatorios y operación**, y validar un segmento antes de ampliar el catálogo. Para una entidad que necesita operar pronto, comprar un motor probado e integrar las capacidades que la diferencian suele ser una hipótesis de trabajo más razonable que desarrollar todo el core. Para un proveedor que pretende vender software, la construcción propia puede tener sentido si consigue clientes de diseño que financien parte del aprendizaje, un alcance común reutilizable y capacidad financiera para mantener el producto durante años. Son decisiones económicas distintas.

La escala de los pagos digitales y de la actividad crediticia respalda la necesidad de infraestructura, pero **no equivale a una demanda proporcional de reemplazos de core**. Una entidad puede modernizar canales, incorporar un procesador de pagos o cambiar su sistema de préstamos sin sustituir su libro central. El negocio es de confianza, integración y continuidad, además de tecnología.

Las conclusiones principales son:

1. La demanda se divide entre bancos, PSP que ofrecen cuentas de pago, prestamistas y proveedores de servicios financieros. Un producto y una oferta comercial únicos para todos estos compradores aumentan el costo de implementación.
2. La localización argentina puede ser una ventaja comercial si incluye cambios normativos versionados, datos reconciliables y responsabilidades contractuales. Ningún módulo garantiza por sí solo el cumplimiento de la entidad.
3. La base instalada y los implementadores locales favorecen a proveedores establecidos. Los entrantes pueden competir por productos nuevos, carteras acotadas, migraciones parciales y herramientas que faciliten la coexistencia.
4. SaaS, nube, arquitectura por eventos y procesamiento en tiempo real deben evaluarse por capacidades verificables. No eliminan cierres contables, reportes programados, tareas masivas ni dependencias externas.
5. No se identificó una fuente pública suficientemente sólida para publicar cuotas argentinas por proveedor, un TAM monetario del software de core o precios comparables de contrato. Este documento ofrece modelos reproducibles y escenarios ilustrativos, sin presentarlos como datos observados.

## 2. Alcance, método y calidad de la evidencia

### 2.1 Preguntas que responde el análisis

- ¿Qué problemas comprarían bancos, PSP y prestamistas argentinos?
- ¿Con qué productos, referencias y capacidades compite una nueva plataforma?
- ¿Qué debe quedar dentro del core y qué puede integrarse?
- ¿Qué costos y riesgos cambian entre comprar, construir y modernizar por partes?
- ¿Cómo convertir la hipótesis de mercado en una decisión de inversión verificable?

El insumo inicial fue el texto aportado por el usuario, titulado *El Mercado de Core Bancarios en la Argentina: Análisis Estratégico, Oferta de Proveedores y Comparativa Tecnológica*. Sus referencias del tipo `[cite: n]` no contenían bibliografía recuperable. Se utilizó para identificar temas y afirmaciones que requerían contrastación, sin tratarlo como fuente independiente de precios, clientes o normas.

Se consultaron publicaciones del BCRA, documentación de producto, casos publicados por proveedores y comunicaciones corporativas. Se distinguen cuatro categorías:

| Categoría | Uso en este documento | Limitación |
|---|---|---|
| Evidencia oficial | Estadísticas y delimitación institucional del BCRA | Cada serie tiene período, universo y rezago propios |
| Declaración del proveedor o del banco | Existencia de un producto y alcance declarado de un caso | Puede tener sesgo comercial, carecer de fecha o describir una versión anterior |
| Inferencia analítica | Posicionamiento, barreras, ventajas y recomendaciones | Debe validarse con entrevistas, pruebas y propuestas comerciales |
| Supuesto de modelo | Precios, volúmenes, costos y tasas de conversión ilustrativos | No constituye cotización, benchmark ni proyección de mercado |

**Criterio temporal:** un dato publicado antes de la fecha de corte no se convierte en dato de octubre de 2026. Se mantiene su período original. Las páginas sin fecha se identifican como tales. Se citan las últimas publicaciones localizadas para cada asunto; no se afirma haber descargado todas las actualizaciones publicadas hasta el corte.

**Trabajo pendiente para una due diligence comercial:** entrevistas con compradores, inventario deduplicado de entidades por CUIT y grupo económico, validación directa de referencias, RFI a proveedores y cotizaciones con el mismo alcance. No se realizaron contactos ni se accedió a contratos privados.

### 2.2 Correcciones al análisis de origen

| Afirmación del insumo | Tratamiento profesional |
|---|---|
| USD 2–10 por cuenta/año, USD 0,01–0,05 por transacción y licencias de USD 2–20 millones como precios típicos | Se retiran como referencias de mercado: faltan contratos, alcance, mínimos, país, fecha y definición de unidad facturable |
| Mantenimiento universal del 15–20% | Se considera una posible estructura contractual, sin atribuir un porcentaje a un proveedor sin oferta verificable |
| Un core cloud-native elimina completamente el batch | Incorrecto como generalización; la documentación de Pismo incluye reportes y entrega de eventos por lotes |
| Un cliente de canales digitales demuestra el uso del core del mismo proveedor | Se separan explícitamente canales, procesamiento, préstamos, depósitos y libro mayor |
| Mambu es necesariamente el core de todas las cuentas de Ualá Argentina | La evidencia localizada describe principalmente préstamos y expansión regional; no prueba todo el perímetro bancario actual |
| Caso de BNA Nueva York prueba localización argentina de Temenos | Una sucursal en Estados Unidos tiene un perímetro regulatorio distinto; no se utiliza como prueba argentina |
| Gravity es otra alternativa comercial disponible en la comparación | Se trata como referencia de desarrollo propio del Grupo Santander, sin oferta comercial abierta de core acreditada |
| La nube y los módulos locales garantizan cumplimiento automático | Se sustituyen por una matriz de obligaciones, controles, parametrización, evidencia y responsabilidades |
| Una referencia mundial o regional acredita implantación argentina | Se exige país, entidad legal, producto, alcance y fecha; lo no verificado queda señalado |
| Duración estándar de 18–36 meses y estabilización obligatoria de 60–90 días | Se reemplazan por escenarios de planificación y criterios de aceptación; no son plazos universales ni obligaciones legales generales |

Fuentes técnicas de la corrección sobre batch: [Pismo, evolución hacia eventos](https://www.pismo.io/blog/from-batch-jobs-to-an-event-driven-model/) y [reportes programados](https://developers.pismo.io/pismo-docs/docs/scheduled-reports). Pismo describe el reemplazo de buena parte de sus rutinas, no la inexistencia de toda tarea por lotes.

## 3. Qué mercado se está analizando

### 3.1 El perímetro funcional

Un core administra contratos y posiciones financieras y produce registros que permiten explicar qué se debe, a quién, en qué moneda y por qué. Según el alcance, puede incluir cuentas, depósitos, préstamos, intereses, comisiones, submayores y libro mayor. Una aplicación móvil, un switch de transferencias, un motor de scoring o un procesador de tarjetas puede integrarse con ese núcleo sin reemplazarlo.

| Capa | Responsabilidad predominante | Compra o desarrollo habitual que debe evaluarse por separado |
|---|---|---|
| Canales y experiencia | Web, aplicación, atención y flujos comerciales | Plataforma digital, diseño, identidad y accesibilidad |
| Originación y decisión | Alta, evaluación, scoring y contratación | KYC, fraude, decisión crediticia y firma |
| Core de productos | Contratos, intereses, cuotas, límites y estados | Depósitos, préstamos y cuentas |
| Ledger y contabilidad | Asientos, saldos, cierre, conciliación y trazabilidad | Submayores, libro mayor, plan de cuentas y ajustes |
| Pagos y tarjetas | Mensajería, autorización, compensación y liquidación | Integraciones con redes, cámaras y procesadores |
| Datos y cumplimiento | Información supervisora, fiscal, PLA/FT y atención de usuarios | Extracción, validación, expedientes, reportes y controles |
| Plataforma operativa | Disponibilidad, seguridad, cambios y recuperación | Infraestructura, observabilidad, soporte y continuidad |

No todos los productos incluyen cada capa. La comparación económica debe explicitar cuáles están incluidas y quién responde por las restantes.

### 3.2 Segmentos compradores

| Segmento | Necesidad principal | Qué vuelve difícil la compra | Oportunidad para un entrante |
|---|---|---|---|
| Bancos universales y grandes grupos | Consolidar productos, reducir complejidad y modernizar sin interrumpir | Integraciones históricas, carteras heterogéneas, gobierno y riesgo operacional | Core satélite, administración de una cartera, conciliación o herramientas de migración |
| Bancos regionales, públicos y entidades medianas | Evolucionar funcionalidad y controlar costo de soporte/localización | Operación de sucursales, convenios, compras institucionales y dependencia del implementador | Plataforma localizada con alcance estable y referencia comparable |
| Bancos digitales y nuevas iniciativas con licencia bancaria | Lanzar productos y escalar cuentas/crédito | Construir todos los controles operativos y reportes junto con el producto | Composición con motor probado y capa local reutilizable |
| PSP que ofrecen cuentas de pago —PSPCP— | Administrar saldos, pagos, conciliación y resguardo operativo | Alto volumen, márgenes ajustados y dependencia de terceros | Ledger de pagos, conciliación y operación con precio transparente |
| Prestamistas y otros proveedores no financieros de crédito | Administrar préstamos, mora, cobranzas y cesiones | Diversidad contractual, recupero, reglas fiscales y calidad de datos | Servicing especializado y migración de carteras |
| Emisores, procesadores y adquirentes | Autorizar y liquidar operaciones de tarjetas/pagos | Certificaciones de red, fraude, disputas y liquidación | Módulos de cuentas o contabilidad integrados al procesador |
| Empresas con finanzas embebidas | Ofrecer una experiencia financiera en su canal | Definir entidad responsable, contratos y acceso a infraestructura | Orquestación y componentes contratados con entidades habilitadas |

“Fintech” y “neobanco” describen modelos de negocio o marcas; no determinan por sí solos el régimen jurídico. Un grupo puede operar mediante varias sociedades: banco, PSP, emisor y prestamista. El BCRA distingue las cuentas de pago en empresas no bancarias de las cuentas del sistema financiero; su [descripción del Sistema Nacional de Pagos](https://www.bcra.gob.ar/sistema-nacional-de-pagos/) y los [registros de PSP](https://www.bcra.gob.ar/registro-de-proveedores-de-servicios-de-pago/) permiten delimitar ese universo. La aplicabilidad concreta se desarrolla en [compliant.md](compliant.md).

## 4. Evidencia de demanda y lectura del mercado argentino

### 4.1 Indicadores que sí pueden sostenerse

| Indicador público | Período del dato | Valor | Lectura para el producto |
|---|---|---|---|
| Personas humanas con cuentas | Diciembre de 2025 | Aproximadamente 37,8 millones | Gran parte de la oportunidad está en uso y profundidad, además de primeras aperturas |
| Titulares con cuentas bancarias y de pago simultáneamente | Diciembre de 2025 | 74% | La interoperabilidad y la conciliación entre proveedores son relevantes |
| Titulares con cuentas en moneda extranjera | Diciembre de 2025 | 62% | Importa separar moneda contractual, contable y de liquidación |
| Personas con financiamiento en el universo del informe | Diciembre de 2025 | 20,3 millones | Hay demanda de administración del ciclo de crédito |

Fuente de las cuatro filas: [BCRA, Informe de Inclusión Financiera, segundo semestre de 2025](https://www.bcra.gob.ar/publicaciones/informe-de-inclusion-financiera-segundo-semestre-de-2025/), publicado el 30/04/2026. Sus universos no son intercambiables con población total, clientes únicos de un proveedor ni contratos de software.

| Indicador público | Período del dato | Valor | Lectura para el producto |
|---|---|---|---|
| Transferencias inmediatas push en pesos | Julio de 2026 | 777,2 millones; +22,2% interanual en cantidad | Capacidad sostenida y pruebas de picos, reintentos y conciliación |
| Transferencias push con origen y/o destino CVU | Julio de 2026 | 76,5% | La operación atraviesa entidades bancarias y no bancarias |
| Cuentas de pago / cuentas de pago con saldo | Junio de 2026 | 67,3 millones / 14,7 millones | Cuentas abiertas y cuentas con saldo son bases distintas para diseñar precios |
| PSPCP incorporados al registro, según el informe | Situación informada al publicar julio de 2026 | 223 | Universo registral; requiere depurar actividad, grupos y posibilidad de compra |
| Billeteras interoperables / aceptadores de PCT registrados | Situación informada al publicar julio de 2026 | 91 / 64 | Roles distintos; no deben sumarse como compradores independientes |

Fuente de las cinco filas: [BCRA, Informe de Pagos Minoristas, julio de 2026](https://www.bcra.gob.ar/publicaciones/informe-mensual-de-pagos-minoristas-julio-de-2026/), publicado el 28/08/2026. “Con saldo” no equivale a cuenta activa mensual ni a cliente único. La página presenta cifras distintas de QR entre encabezado y desarrollo; ese indicador se excluye de los cálculos.

La [nómina de entidades financieras del BCRA](https://www.bcra.gob.ar/sistema-financiero-nomina-de-entidades/?bco=AAA00&tipo=1) es el punto de partida para un censo comercial bancario. La consulta depende de contenido dinámico y filtros; en esta revisión no se consolidó una descarga reproducible completa por fecha. Por ello no se publica una cantidad exacta de bancos ni se deduce a partir de números de página de informes.

### 4.2 Lo que esos datos permiten inferir

**Inferencia 1: el crecimiento de cuentas puede presionar el costo antes que el ingreso.** Si un contrato cobra por cuentas abiertas, la proliferación de cuentas con poco uso puede encarecer el servicio. Si cobra por actividad, debe definirse qué evento activa la facturación y cómo se audita. Las cuentas con saldo, con movimientos, abiertas y cerradas requieren métricas diferentes.

**Inferencia 2: competir por “más TPS” es insuficiente.** El comprador necesita que una operación ambigua no se duplique, que un rechazo no inmovilice fondos indefinidamente y que pueda explicar diferencias entre mensajes, liquidaciones, submayor y contabilidad. El valor está en la integridad del circuito completo.

**Inferencia 3: el préstamo es una puerta de entrada viable, con complejidad propia.** Un sistema de servicing puede venderse sin reemplazar todos los depósitos y canales. Sin embargo, intereses, refinanciaciones, mora, prepagos y tratamiento de impuestos requieren especialización; no es simplemente registrar débitos futuros.

**Inferencia 4: la contabilidad y los datos locales pueden constituir una barrera competitiva.** Una capa de reportes será diferenciadora si puede reconstruir cada dato desde contratos y asientos y versionar las reglas vigentes a cada fecha. Generar un archivo con el formato correcto es sólo una parte de ese trabajo.

### 4.3 Factores de demanda y frenos

| Factor | Efecto comercial esperado —inferencia— | Qué debe validar una entrevista |
|---|---|---|
| Operación de pagos continua | Necesidad de saldos disponibles y conciliación fuera del horario bancario | Incidentes actuales, ventanas de indisponibilidad y operación de guardia |
| Cambios del ciclo de crédito | Demanda de nuevos productos, servicing y cobranzas según cartera | Productos rentables y restricciones de capital, fondeo y cobranza |
| Cambios de tasas, monedas e índices | Valor de parametrización temporal y simulación | Qué modificaciones exigen hoy desarrollo y cuánto tardan |
| Sistemas fragmentados | Incentivo para reducir conciliaciones manuales | Costo real de reconciliación e interfaces y dueño de cada dato |
| Dependencia de plataformas antiguas | Incentivo de modernización | Si la presión viene de costos, fin de soporte o falta de talento |
| Riesgo de migración | Postergación de reemplazos completos | Qué cartera aceptaría mover el comité de riesgos |
| Contratos y presupuestos en varias monedas | Riesgo de descalce de costos | Moneda de cobro, indexación, impuestos y sensibilidad al tipo de cambio |
| Consolidación de entidades y grupos | Posible unificación de plataformas | Quién decide el core dentro del grupo y cuándo vence el contrato |

El [Informe sobre Bancos de julio de 2026](https://www.bcra.gob.ar/publicaciones/informe-sobre-bancos-julio-de-2026/), publicado el 18/09/2026, presenta un contexto más exigente: el crédito privado total cayó 1% real mensual, aunque creció 4,7% interanual; la irregularidad alcanzó 7,7% del crédito, con 12,9% en familias y 3,6% en empresas. No corresponde proyectar una expansión lineal desde los datos de 2025.

**Implicación analítica:** el caso de negocio de un sistema de préstamos debe incorporar administración de mora, cobranzas, refinanciación y calidad de datos, además de originación. El contexto bancario no permite deducir un presupuesto tecnológico; puede aumentar la necesidad operativa y a la vez restringir el gasto disponible.

## 5. Oferta competitiva y referencias verificadas

### 5.1 Matriz de oferta

La siguiente matriz separa **producto declarado** de **evidencia argentina**. No es un ranking de rendimiento, cuota o cumplimiento. Las capacidades exactas dependen de versión, módulos, implementación y contrato.

| Plataforma | Oferta y enfoque declarados | Evidencia argentina localizada | Principal comprobación antes de comprar |
|---|---|---|---|
| Bantotal | Suite de core y módulos especializados; reportes y ecosistema de integración | Caso Banco Formosa y experiencia local publicada por Accion Point | Versión, componentes instalados, alcance regulatorio y responsabilidades entre fabricante e implementador |
| Cyberbank Core / Galileo / SoFi | Motor de core basado en nube, junto con productos digitales y de pagos diferenciados | Caso local de Banco Nación corresponde a Cyberbank Digital; no acredita sustitución del core | Referencia argentina del módulo Core, paquete local, migración y soporte contractual vigente |
| Temenos Core Banking / Transact | Plataforma de core de alcance amplio, APIs, productos y opciones de despliegue | Casos Banco del Sol y Banco Credicoop | Alcance de localización argentina incluido, versión, interfaces y costo de actualización |
| Cobis Topaz / FinancialCore | Familia de soluciones Universal, Digital y Microfinance | Evidencia histórica de COBIS en Banco Ciudad; requiere verificar qué generación y módulos continúan | No equiparar COBIS instalado históricamente con una nueva oferta Topaz One ni extrapolar una arquitectura única |
| Pismo / Visa | Core y procesamiento emisor mediante APIs; arquitectura basada en nube y eventos | No se verificó en las fuentes revisadas un caso argentino de core completo con alcance identificable | Localización, cuentas/monedas, integraciones de pagos, contabilidad, salida de datos y referencia argentina |
| Mambu | Motor componible para depósitos, préstamos y cuentas de valor almacenado | Caso Ualá describe préstamos y expansión regional | Confirmar entidad legal, producto, país y etapa; no extrapolar a todas las cuentas bancarias del grupo |
| Oracle FLEXCUBE | Core universal y servicios bancarios de alcance global | Se incluye como candidato global; no se acreditó un caso argentino actual en esta revisión | Demostrar paquete argentino operativo, recursos locales y TCO completo |
| Finastra Essence | Core de banca universal con arquitectura modular e interfaces | Se incluye como candidato global; sin referencia argentina actual verificada aquí | Idoneidad local, versión, implementador y cartera de alcance comparable |
| Desarrollo interno / modernización del core actual | Control del código y de la evolución; reutilización de capacidades de la entidad | Gravity sirve como referencia corporativa global, no como oferta abierta verificada | Equipo, propiedad intelectual, costos futuros, riesgo de persona clave y sostenibilidad |

Fuentes de oferta: [Bantotal Core](https://www.bantotal.com/core.html), [Cyberbank Core y adopción anunciada por SoFi](https://tech.sofi.com/es/news/sofi-adoptara-cyberbank-core-de-galileo-para-patrocinio-bancario/), [APIs de Temenos](https://developer.temenos.com/transact-apis), [FinancialCore de Cobis Topaz](https://www.cobistopaz.com/es/topaz-one/financialcore), [adquisición de Pismo por Visa](https://investor.visa.com/news/news-details/2024/Visa-Completes-Acquisition-of-Pismo/default.aspx), [Mambu Core](https://mambu.com/en/core-capabilities), [Oracle FLEXCUBE](https://www.oracle.com/latam/financial-services/banking/flexcube/), [Finastra Essence](https://www.finastra.com/universal-banking/solutions/essence).

### 5.2 Bantotal: ventaja de localización y ejecución

El [caso Banco Formosa](https://www.bantotal.com/historias-de-exito/banco-formosa.html) identifica a Bantotal como core desde 2019. Accion Point publica experiencia argentina con distintas entidades, incluido Banco Santiago del Estero, en una [nota del 21/09/2026](https://accionpoint.com/blog/implementador-bantotal-latinoamerica/). Esta segunda evidencia acredita la experiencia declarada del implementador; no aporta por sí sola el inventario vigente de módulos y versiones de cada cliente.

**Evaluación analítica:** su posición es atractiva cuando el comprador valora conocimiento del negocio local, cobertura funcional y un socio de implementación. Para competir, un entrante deberá demostrar una mejora concreta en tiempo de cambio, costo total, integración o migración; el argumento de disponer de APIs no basta. La debida diligencia debe revisar qué personalizaciones conservan una ruta de actualización y qué compromisos mantiene cada parte sobre cambios normativos. No se infiere una cuota de mercado a partir de estas referencias.

### 5.3 Cyberbank: separar Core, Digital y procesamiento

SoFi [completó la adquisición de Technisys el 03/03/2022](https://www.sofi.com/newsroom/sofi-completes-acquisition-technisys/). La oferta de Cyberbank Core aparece actualmente dentro del ecosistema de tecnología de SoFi/Galileo. Un [anuncio del 16/10/2024](https://tech.sofi.com/es/news/sofi-adoptara-cyberbank-core-de-galileo-para-patrocinio-bancario/) describe su adopción por SoFi para un programa de servicios de pago comercial en Estados Unidos; el anuncio preveía una implementación posterior y no certifica por sí mismo su finalización.

En Argentina, el [caso Banco Nación](https://tech.sofi.com/es/blog/como-banco-nacion-transformo-su-experiencia-de-banca-digital-con-galileo/) se refiere a **Cyberbank Digital**. Se utiliza como evidencia de canales, no como prueba de que Cyberbank Core mantenga la contabilidad central del banco.

**Evaluación analítica:** candidato para modernización digital y arquitecturas donde interesa combinar capacidades del ecosistema. Para un reemplazo de core argentino, el RFI debe pedir una referencia del producto exacto y el detalle del paquete local. También debe identificar la sociedad contratante y los compromisos actuales de cada producto, dado que las marcas y estructuras comerciales evolucionan.

### 5.4 Temenos: referencias locales de distinto tipo

El [caso Banco del Sol](https://www.temenos.com/success-story/banco-del-sol-success-story/) describe implementación de core, mitigación de delitos financieros y datos con GlobalLogic. El [caso Banco Credicoop](https://www.temenos.com/success-story/bccl-success-story/) documenta un reemplazo gradual con coexistencia e interfaces. Este último contiene referencias a resultados de 2017 y tecnología de aquella etapa; no debe leerse como inventario técnico actual de 2026.

**Evaluación analítica:** ambos casos respaldan relevancia local, pero representan operaciones y momentos diferentes. La propuesta comercial debe especificar qué contiene el modelo de país argentino, qué cambios dependen de un partner, qué versión está disponible y qué ocurre con las extensiones al actualizar. La amplitud de una suite puede reducir compras periféricas o aumentar el alcance de un proyecto; la respuesta depende del perímetro contratado.

### 5.5 Cobis Topaz: evitar homogeneizar productos y generaciones

[FinancialCore](https://www.cobistopaz.com/es/topaz-one/financialcore) distingue Core Universal, Core Digital y Core Microfinance. No corresponde atribuir a toda la familia una única arquitectura, nube obligatoria o forma de cobro. La oferta por segmentos tampoco demuestra por sí sola que los reportes argentinos estén listos para cada versión.

Como evidencia local histórica, un [prospecto de Banco Ciudad de 2020, página 137](https://bancost.com.ar/wp-content/uploads/2020/09/Titulo-de-Deuda-Clase-XXII-Banco-Ciudad-Prospecto-de-Emision.pdf#page=137), alojado por un participante de la colocación, describe módulos COBIS y el proyecto de core. Es una fuente documental de la entidad distribuida por un tercero: debe contrastarse con documentación bancaria actual antes de una selección. Una [búsqueda laboral del banco](https://bancociudad.na.teamtailor.com/jobs/706332-desarrollador-a-core) también menciona Core Banking Cobis; es una corroboración operativa limitada, sin valor como certificación de la instalación.

**Evaluación analítica:** candidato relevante para una evaluación regional. La diligencia debe distinguir el producto instalado, su evolución y la propuesta nueva, con una prueba sobre productos, cartera y normativa argentinos. Los logotipos de clientes en una página de suite no demuestran el módulo usado por cada banco.

### 5.6 Pismo: core y tarjetas como capacidades relacionadas

Visa [completó la compra de Pismo el 16/01/2024](https://investor.visa.com/news/news-details/2024/Visa-Completes-Acquisition-of-Pismo/default.aspx). El comunicado identifica capacidades de core y procesamiento emisor; eso no acredita una localización argentina ni una implementación determinada en el país. La [documentación para desarrolladores](https://developers.pismo.io/pismo-docs/docs/welcome) permite investigar APIs, eventos y datos con mayor precisión que una descripción comercial.

**Evaluación analítica:** merece consideración cuando cuentas y tarjetas deben evolucionar de forma coordinada y existe capacidad para integrar los componentes locales. Debe contrastarse el alcance real de préstamos, libro mayor, conciliación y reportes. La arquitectura por eventos no permite concluir que toda la plataforma funciona sin tareas programadas, y tampoco que cada API tenga la misma consistencia o latencia. No se publica una lista argentina de clientes sin evidencia de producto y país.

### 5.7 Mambu: composición con carga de integración explícita

El [caso Ualá de Mambu](https://mambu.com/en/customer/uala) describe la plataforma como soporte para nuevos préstamos en línea y expansión entre Argentina, México y Colombia. La página no fecha con precisión cada implantación y presenta referencias temporales a integración y salida al mercado que no deben convertirse en un plazo general de cambio de core. No acredita que todo el ledger bancario argentino actual de Ualá esté en ese motor.

El [catálogo de capacidades](https://mambu.com/en/core-capabilities) y la documentación de [productos de depósito](https://support.mambu.com/docs/setting-up-new-deposit-products) permiten evaluar el motor. Las menciones del insumo a Naranja X y ank se mantienen fuera de la matriz de casos confirmados de core integral: no se verificó aquí una fuente con suficiente detalle de fecha, entidad, módulo y estado vigente.

**Evaluación analítica:** la composición puede permitir elegir componentes especializados y reducir dependencia funcional de una suite. A la vez, el comprador o integrador asume la coherencia de contratos, identidades, asientos, reportes y operación entre servicios. Debe presupuestarse esa función de integración. Un precio de un componente adicional, como [Mambu Insights](https://docs.mambu.com/docs/insights-pricing-and-consumption/), no es el precio del core completo.

### 5.8 Oracle, Finastra y alternativas que no son un nuevo core

[Oracle FLEXCUBE](https://docs.oracle.com/en/industries/financial-services/flexcube.html) y [Finastra Essence](https://www.finastra.com/universal-banking/solutions/essence) son alternativas globales que pueden ampliar un RFI bancario. Sin evidencia argentina actual suficiente en esta revisión, no se les asigna ventaja o desventaja local definitiva. La inclusión de otros fabricantes debe responder al segmento, disponibilidad de equipo y prueba del alcance, evitando una lista extensa sin posibilidad real de entrega.

El competidor comercial más importante puede ser el **core que el comprador ya tiene**, acompañado por una actualización, una capa de APIs o un motor satélite. También compiten la decisión de postergar el proyecto y los servicios administrados ofrecidos por terceros. Cámaras, redes, adquirentes, proveedores KYC y procesadores pueden ser socios o componentes, aunque algunos tengan ofertas que se superpongan parcialmente con cuentas o contabilidad.

### 5.9 Gravity: referencia de una decisión de construir

Santander describe [Gravity](https://www.santander.com/es/stories/7-preguntas-sobre-como-gravity-esta-transformando-santander), en una publicación del 16/07/2025, como tecnología desarrollada por el grupo y explica el procesamiento paralelo. El [anuncio de España del 19/06/2025](https://www.santander.com/es/sala-de-comunicacion/notas-de-prensa/2025/06/santander-culmina-la-digitalizacion-de-su-infraestructura-tecnologica-en-espana-con-la-implantacion-de-gravity) identifica ese despliegue nacional. No se trasladan a Argentina ni el estado de implantación español ni ahorros energéticos globales. No se verificó que Gravity esté disponible como core comercial para cualquier entidad.

La lección útil es económica y operativa: un grupo con escala puede amortizar una plataforma común, reutilizar equipos y probar su equivalencia con sistemas existentes. Esa capacidad no se presume para una nueva empresa o un banco pequeño. La metodología de comparación paralela también puede aplicarse sin adquirir Gravity o un producto específico de Google.

## 6. Dónde puede diferenciarse un nuevo core argentino

### 6.1 Propuesta de valor sugerida

**Hipótesis:** “Permitir que una entidad argentina lance y opere un conjunto definido de productos, con cuentas y contratos explicables hasta el asiento, conciliación reproducible y cambios locales versionados”.

El valor debe demostrarse en resultados que un comprador pueda medir:

- Días necesarios para configurar un producto usando funciones soportadas, sin modificar código del motor.
- Tiempo y porcentaje de diferencias resueltas automáticamente en conciliación, con explicación de excepciones.
- Duración y costo de incorporar un cambio local, incluidos pruebas y actualización de datos.
- Horas que necesita auditoría para reconstruir un saldo y las reglas aplicadas en una fecha histórica.
- Costo completo por contrato o cuenta realmente operada, con mínimo y pico incluidos.
- Tiempo de recuperación comprobado del servicio completo y pérdida máxima de datos aceptada.

Estas métricas se deben basar en una línea de base del cliente; no se asignan mejoras porcentuales sin piloto.

### 6.2 Prioridad de segmentos —juicio estratégico—

| Prioridad | Segmento de entrada | Oferta inicial | Condición para avanzar |
|---|---|---|---|
| 1 | Prestamista con cartera y necesidad concreta de evolución | Administración de préstamos, cuotas, cobranzas, contabilidad e información | Contratos reutilizables y acceso autorizado a datos representativos |
| 1 alternativa | PSP con problema verificable de conciliación/cuentas | Ledger de pagos, estados de operación y conciliación | Socio de pagos, perímetro regulatorio y soporte definidos |
| 2 | Banco que lanza una línea o cartera nueva | Motor satélite con interfaces y dueño de cada asiento | Aprobación interna de riesgos y coexistencia probada |
| 3 | Banco mediano que reemplaza varios módulos | Plataforma localizada y migración por oleadas | Referencias previas, equipo de soporte y cobertura funcional demostrada |
| Posterior | Reemplazo integral de banco universal | Suite y programa de transformación | Solvencia financiera, operación madura y experiencia comparable |

Las dos opciones de prioridad 1 no deberían ejecutarse simultáneamente con el mismo equipo inicial si multiplican los productos y rieles. Elegir una depende de los compradores disponibles, experiencia del equipo y costo de integración; los datos públicos no resuelven esa elección.

### 6.3 Arquitectura como condición comercial

El diseño inicial debe definir un límite de consistencia claro para el dinero. La disponibilidad de eventos o microservicios no reemplaza transacciones financieras correctas. Son necesarios, según el perímetro:

| Capacidad | Demostración exigible al producto |
|---|---|
| Libro por partida doble | Cada asiento balancea por moneda y entidad; no se modifica la historia para corregirla |
| Dinero y precisión | Escalas decimales y redondeos documentados; diferencia entre importe contractual y presentación |
| Concurrencia | Dos débitos simultáneos no consumen dos veces la misma disponibilidad |
| Idempotencia | Un reintento o mensaje duplicado tiene un único efecto financiero |
| Estado de pagos | Distinción entre recibido, autorizado, enviado, confirmado, rechazado, expirado y reversado |
| Fechas | Fecha de evento, valor, negocio y contabilización diferenciadas; calendarios y zonas horarias explícitos |
| Correcciones | Contrapartidas, reversos y ajustes con motivo, vínculo y autorización |
| Versiones | Contratos y tasas conservan reglas vigentes a cada fecha; los nuevos parámetros no reescriben el pasado |
| Integración | Eventos con identificador estable, reentrega, orden definido donde se necesita y reconciliación independiente |
| Operación | Procedimientos para pagos ambiguos, indisponibilidad de rieles, recuperación y cierre |
| Datos | Linaje desde contrato y asiento hasta el informe; exportación completa y documentada |
| Aislamiento | Separación por entidad legal, tenant, rol y ambiente; sin compartir permisos entre clientes |

Este cuadro expresa requisitos de producto propuestos, no una transcripción normativa. Los controles y su fundamento se vinculan en [compliant.md](compliant.md).

Una arquitectura modular con pocas fronteras bien elegidas puede ser más operable al principio que muchos microservicios. La consistencia fuerte puede ser necesaria dentro del registro financiero; la propagación eventual puede ser aceptable para determinadas consultas o analítica. El RFP debe examinar ambos casos, especialmente las lecturas de saldo inmediatamente posteriores a una operación.

## 7. Dimensionamiento económico sin fabricar un TAM

### 7.1 Unidades y universos

El mercado de software se mide por **contratos comprables**, no por habitantes, depósitos ni monto transaccionado. Una entidad puede usar varios cores; varias sociedades pueden comprar bajo un solo grupo; un PSP registrado puede no estar activo o contratar infraestructura a otra empresa. No debe sumarse un registro de PSP, una lista de bancos y otra de billeteras sin deduplicar.

La metodología propuesta es:

1. Obtener el censo por entidad legal y grupo desde registros oficiales.
2. Etiquetar actividad, licencia/rol, volumen, core actual, vencimientos, integraciones y capacidad de compra.
3. Separar cuentas objetivo de bancos, PSP y prestamistas; identificar decisiones centralizadas de grupo.
4. Estimar para cada entidad el alcance que el producto realmente puede operar.
5. Validar presupuesto y disposición a comprar mediante RFI, entrevistas y pilotos remunerados.

Definiciones para el modelo:

```text
TAM anual = suma del gasto anual potencial del universo completo definido.
SAM anual = suma del ACV de entidades que el producto y la entrega pueden servir.
Oportunidades a 36 meses = N de cuentas objetivo deduplicadas × proporción que abre compra.
Contratos esperados = oportunidades × tasa de adjudicación.
ARR de salida esperado = contratos implementados al mes 36 × ACV recurrente.
```

ACV significa valor recurrente anual del contrato; ARR, ingreso recurrente anualizado. La implementación cobrada una vez se contabiliza por separado. No se estima el TAM ni el SAM monetario real porque faltan un censo de gasto y precios comparables.

### 7.2 Escenarios de cartera comercial a tres años

**Todos los números siguientes son supuestos de planificación. No son tamaño de mercado, cotizaciones de competidores ni pronóstico de ventas.** El número de cuentas objetivo es una lista hipotética ya calificada, no una proporción acreditada del registro del BCRA. Las tasas de conversión requieren validación.

| Variable | Conservador | Base ilustrativa | Expansión |
|---|---:|---:|---:|
| Cuentas objetivo deduplicadas, N | 30 | 50 | 75 |
| Proporción que abre una compra en 36 meses | 25% | 35% | 45% |
| Adjudicación sobre esas oportunidades | 20% | 25% | 30% |
| Contratos esperados, sin redondear | 1,50 | 4,375 | 10,125 |
| ACV supuesto, USD millones | 0,20 | 0,30 | 0,40 |
| ARR esperado al mes 36, USD millones | 0,300 | 1,313 | 4,050 |
| Ingreso único por implementación, USD millones por cliente | 0,12 | 0,20 | 0,30 |
| Ingreso total esperado de implementación, USD millones | 0,180 | 0,875 | 3,038 |

Los contratos fraccionarios son valores esperados estadísticos, no clientes ejecutables. Se supone, de forma exigente, que todos los adjudicados están implementados al mes 36 y no hay bajas. El ARR de salida no es el ingreso acumulado de tres años: las altas tardías aportan menos meses facturados. Para convertirlo en ingresos y caja debe calendarizarse cada oportunidad, implementación, anticipo, aceptación y cobro, y aplicar probabilidad de demora o cancelación.

La mezcla de segmentos cambia el ACV y el costo de entrega. No se debería usar un promedio único hasta contar con un modelo separado para banca, pagos y crédito. Además, vender servicios de localización o conciliación a una entidad no significa ganar su contrato de core integral.

### 7.3 Economía del proveedor nuevo

La ecuación mínima es:

```text
Margen bruto recurrente = ARR − nube operativa atribuible − soporte directo
                         − licencias de terceros − costos directos de servicio.
Punto de equilibrio recurrente = costos fijos anuales / margen por cliente.
```

Ejemplo exclusivamente ilustrativo: con ACV de USD 300.000, margen bruto recurrente de 65% y costos fijos anuales de USD 2,4 millones, se necesitan aproximadamente **13 clientes equivalentes** para cubrir esos costos: `2.400.000 / (300.000 × 0,65) = 12,31`, redondeado hacia arriba. Quedan fuera financiamiento, impuestos y crecimiento de plantilla. Los ingresos de implementación pueden ayudar a financiar la entrega, pero no deben ocultar contratos recurrentes deficitarios.

El escenario base de cartera anterior, por sí solo, no cubre ese ejemplo de estructura fija. La decisión podría requerir menores costos, mayor ACV, venta de módulos a más compradores, expansión regional o financiación adicional. La expansión a otros países agrega localización; no debe suponerse que el mismo producto se despliega sin cambios.

## 8. Comprar, construir y modernizar: TCO a cinco años

### 8.1 Estructuras comerciales que deben compararse

Los contratos pueden combinar suscripción base, productos, cuentas, préstamos, transacciones, capacidad, ambientes, almacenamiento, soporte y servicios profesionales. Es necesario definir mínimos, escalas, descuentos, revisiones, moneda e indexación. Las páginas públicas consultadas no proporcionan una tarifa homogénea y suficiente para comparar estos proveedores como si vendieran el mismo alcance.

En particular, debe aclararse:

- Si una persona con tres productos genera una o tres unidades facturables.
- Si se cobran cuentas abiertas, activas, con saldo o contratos administrados.
- Si un reintento, rechazo, consulta, reverso o evento interno cuenta como transacción.
- Qué consumo se incluye en producción, réplica, contingencia, pruebas y sandbox.
- Quién paga egress, retención, observabilidad, claves, auditorías y requerimientos regulatorios nuevos.
- Qué costo aparece al superar capacidad contratada o reducir volumen.

### 8.2 Fórmula y supuestos comunes

```text
TCO5 = inversión inicial + Σ costos anuales de cinco años
       + migración/coexistencia + salida − costos efectivamente eliminados.
```

Si se calcula valor presente, debe aplicarse una tasa consistente con moneda y tipo de flujo: `VPN de costos = Σ costo_t / (1+r)^t`. No se mezclan flujos nominales en pesos con una tasa real en dólares.

El ejemplo siguiente compara un **perímetro hipotético de cuentas y préstamos minoristas**, sin comercio exterior, tesorería compleja ni procesamiento propio de tarjetas. No representa a una entidad real. Para comparar alternativas se mantiene el mismo volumen medio: 250.000 cuentas/contratos facturables y 36 millones de transacciones facturables por año. Cuenta y contrato se tratan aquí como unidad equivalente sólo para simplificar el ejercicio; un RFP debe separarlos.

El horizonte simplificado comprende preparación e inversión inicial más cinco años completos del servicio objetivo. Los costos de ejecución previos están en implementación; no se agregan cinco años de plataforma madura a un calendario de cinco años desde el inicio del desarrollo. Para un presupuesto de caja desde la fecha de inicio se necesita un cronograma distinto para cada alternativa.

### 8.3 Modelo ilustrativo reproducible

**No son precios de Bantotal, Mambu, Pismo, Temenos ni otro proveedor.** Se usan importes hipotéticos para mostrar qué conceptos cambian el resultado. Millones de USD constantes, sin descuento financiero.

| Concepto | SaaS comprado | Licencia y operación propia | Construcción propia |
|---|---:|---:|---:|
| Licencia inicial o desarrollo inicial del producto | 0,00 | 1,80 | 4,50 |
| Implementación e integración de la entidad | 1,10 | 1,40 | 0,90 |
| Migración y coexistencia | 0,65 | 0,65 | 0,65 |
| Localización/configuración inicial | 0,55 | 0,55 | 0,55 |
| Validación, seguridad y pruebas iniciales | 0,30 | 0,30 | 0,60 |
| Suscripción/consumo de plataforma en 5 años | 3,075 | 0,00 | 0,00 |
| Mantenimiento del fabricante en 5 años | Incluido arriba | 1,80 | 0,00 |
| Equipo interno de operación/evolución en 5 años | 3,50 | 4,50 | 6,25 |
| Infraestructura y servicios periféricos en 5 años | 1,20 | 1,80 | 2,25 |
| Salida y archivo al final del horizonte | 0,50 | 0,50 | 0,50 |
| **Subtotal** | **10,875** | **13,300** | **16,200** |
| Reserva de presupuesto, 20% del subtotal | 2,175 | 2,660 | 3,240 |
| **Presupuesto con reserva** | **13,050** | **15,960** | **19,440** |

Desglose del consumo hipotético SaaS: `5 × [300.000 + 250.000 × 0,90 + 36.000.000 × 0,0025] = USD 3.075.000`. El mantenimiento hipotético de licencia es `5 × USD 360.000`. Los equipos internos anuales presupuestados son USD 700.000, USD 900.000 y USD 1.250.000, respectivamente. Los equipos de construcción inicial y los de operación/evolución son partidas de funciones diferentes; no debe contarse dos veces a las mismas personas.

La reserva de 20% es una decisión de presupuesto ilustrativa, no una estimación de pérdida esperada. Aplicarla igual a las tres opciones facilita leer la fórmula, pero no implica que tengan el mismo riesgo. Debe reemplazarse por escenarios de demora, defectos y alcance con probabilidades y consecuencias documentadas.

Se excluyen impuestos recuperables y no recuperables, retenciones, costos financieros, capital regulatorio, fondeo de la cartera, costo de fraude, costo de oportunidad por lanzamiento tardío y costos del negocio que sean comunes a las opciones. También se excluye el costo residual del sistema anterior después de la coexistencia presupuestada. Si no puede apagarse, ese remanente debe incorporarse; no constituye ahorro. La clasificación contable como inversión o gasto requiere análisis propio y no deriva automáticamente de SaaS frente a desarrollo.

### 8.4 Sensibilidades y forma de decidir

| Cambio al supuesto | Efecto antes de reserva en el ejemplo SaaS |
|---|---:|
| Aumento de USD 1 por cuenta/contrato y año | +USD 1,25 millones en cinco años |
| Aumento de USD 0,001 por transacción | +USD 180.000 en cinco años |
| Doble de volumen, sin descuentos ni cambio de tarifa base | +USD 1,575 millones en cinco años |
| Seis meses extra de coexistencia a USD 100.000 por mes | +USD 600.000 |
| Un costo anual omitido de USD 200.000 | +USD 1 millón |

El modelo no demuestra que SaaS siempre sea más barato: demuestra que una tarifa atractiva puede ser secundaria frente a integración, personal, coexistencia y salida. Una institución con infraestructura amortizada y equipo experimentado puede tener un resultado diferente. Un proveedor que construye un producto vendible puede amortizar desarrollo entre clientes; un banco que construye para sí mismo no debe imputarse ingresos de licencias que no existen.

La comparación final debe incluir una alternativa de **modernización parcial del core existente** con costos y beneficios propios. No se le asigna una cifra genérica porque la calidad de interfaces y los costos que realmente se pueden retirar cambian radicalmente entre instituciones.

## 9. Migración y operación: el riesgo que define la compra

### 9.1 Estrategias posibles

| Estrategia | Ventaja | Riesgo/costo a gestionar |
|---|---|---|
| Producto nuevo en plataforma nueva | Reduce la cartera inicial que debe trasladarse | Mantiene dos plataformas y requiere visión consolidada del cliente |
| Migración por cohortes/carteras | Permite aprender y limitar impacto | Enrutamiento, reglas de convivencia, asientos intermedios y reportes combinados |
| Comparación paralela sin doble efecto externo | Permite medir equivalencia antes del cambio | Reproducir entradas, separar efectos financieros y explicar diferencias |
| Cambio integral en una ventana | Simplifica la convivencia posterior | Mayor alcance simultáneo, ventana estricta y reversión compleja |
| Encapsular y evolucionar el core actual | Puede entregar valor con menor cambio inicial | Prolonga dependencias y no elimina necesariamente costos heredados |

La comparación paralela no debe duplicar órdenes a redes, pagos o comunicaciones al cliente. Debe definirse qué sistema es autoritativo para cada contrato, saldo y efecto externo. Una vez liquidadas operaciones reales, “volver al sistema anterior” puede requerir conciliación y movimientos compensatorios; no se resuelve restaurando una base de datos.

### 9.2 Entregables de aceptación

1. **Inventario de datos y contratos:** campos, reglas, históricos, consentimientos, garantías, embargos y documentos, según alcance.
2. **Mapeo financiero:** equivalencia de productos, eventos y asientos; tratamiento de saldos, intereses devengados, cuotas, mora y partidas pendientes.
3. **Ensayos repetibles:** extracción, transformación, carga, tiempos, controles y resultados conservados.
4. **Conciliación:** por cuenta y contrato y también por moneda, producto, entidad y libro mayor; tolerancias justificadas para redondeos.
5. **Pruebas operativas:** picos, procesos masivos, fin de mes/año, calendarios, cortes, recuperación e indisponibilidad de terceros.
6. **Plan de transición:** responsables, criterios de abortar, comunicación, saldos iniciales y tratamiento de operaciones en tránsito.
7. **Estabilización:** monitoreo financiero y operativo, resolución de excepciones y validación independiente de cierres/reportes.
8. **Retiro del legado:** acceso al archivo histórico, conservación y eliminación conforme a cada obligación; fin de contratos y verificación de ahorros.

Las puertas de salida deben medirse por evidencia: ausencia de diferencias inexplicadas de dinero, capacidad de reconstrucción, límites de riesgo aprobados y recuperación ensayada. La duración depende del alcance y la calidad de datos; un piloto de producto y la migración de un banco universal no comparten un plazo estándar.

## 10. Estructura competitiva: cinco fuerzas y FODA

Las evaluaciones siguientes son inferencias del tipo de compra y de la oferta revisada, sin puntuaciones empíricas de participación.

### 10.1 Cinco fuerzas

| Fuerza | Evaluación | Implicación |
|---|---|---|
| Rivalidad | Alta en el proceso de selección, con propuestas poco homogéneas | Competir por alcance y resultado verificable, evitando comparaciones sólo de licencia |
| Poder del comprador | Alto antes de contratar; cambiar después puede ser costoso | Diseñar portabilidad y salida desde la negociación |
| Poder de proveedores e integradores | Relevante cuando concentran conocimiento, nube o componentes críticos | Evitar dependencia de un único equipo y documentar interfaces/configuración |
| Amenaza de entrantes | Es posible construir un motor; es difícil probar operación y migración a escala | La referencia de producción y el soporte son activos centrales |
| Sustitutos | Fuertes: conservar, actualizar, encapsular, usar core satélite o contratar un servicio | Demostrar beneficio frente a una mejora parcial, no sólo frente a otro core nuevo |

### 10.2 FODA de un nuevo proveedor localizado

| Fortalezas potenciales | Debilidades iniciales |
|---|---|
| Cercanía al negocio argentino y soporte en su horario/idioma | Falta de referencias y capacidad financiera reducida |
| Reglas y datos diseñados con trazabilidad desde el inicio | Catálogo funcional y herramientas de migración incompletos |
| Menor complejidad inicial si el segmento está acotado | Necesidad de operar guardias, seguridad y continuidad desde producción |
| Capacidad de integrar requisitos reales de clientes de diseño | Dependencia de personas clave y riesgo de personalizaciones por cliente |

| Oportunidades | Amenazas |
|---|---|
| Carteras nuevas, servicing y coexistencia | Competidores establecidos amplían módulos y bajan barreras de entrada |
| Conciliación y datos regulatorios como compra modular | Incidente que dañe la confianza antes de construir referencias |
| Automatizar evidencia y reducir trabajo manual medible | Demoras de contratación y cobro superiores a la caja disponible |
| Reutilización regional de capacidades comunes | Cambios regulatorios y de esquemas que aumenten costo de mantenimiento |

La localización se convierte en ventaja sólo si puede mantenerse con pocos cambios específicos por cliente. Una empresa de proyectos distintos para cada banco tiene una economía diferente de la de un producto de software reusable.

## 11. RFI/RFP para seleccionar o contrastar la propuesta propia

### 11.1 Información que debe entregar cada oferente

- Entidad contratante, productos, versión y esquema de despliegue concretos.
- Matriz de requerimientos con estados: disponible, configurable, extensión, tercero, desarrollo futuro o no soportado.
- Referencias del mismo país, producto y escala, indicando selección, piloto, producción o migración finalizada y sus fechas.
- Lista de módulos regulatorios/locales, fuente de las reglas, responsable de actualización y plazo contractual de entrega.
- Arquitectura de datos y consistencia; límites, cuotas, tiempos de respuesta y comportamiento ante fallas.
- Plan de integración, migración, transición y retirada del legado, con responsabilidades y dependencias.
- Modelo de seguridad, subcontratistas, ubicaciones, auditoría, incidentes y continuidad del servicio completo.
- Precio detallado con unidades y mínimos, curva de crecimiento/decrecimiento y ambientes incluidos.
- Portabilidad de datos/configuración, asistencia de salida, costos, formatos y tiempos.
- Solvencia, capacidad de soporte, equipos propuestos, condiciones de propiedad intelectual y gobierno de cambios.

### 11.2 Criterios de descarte

Un oferente no debería pasar a puntuación económica si no puede demostrar integridad financiera, exportación utilizable, recuperación coherente con el servicio, derechos contractuales de control/auditoría aplicables o una vía viable para cubrir los requisitos críticos del perímetro. La etiqueta “certificado” no reemplaza demostrar qué entidad, servicio y alcance cubre el certificado.

Las promesas de roadmap se valoran como trabajo pendiente, con plazo, costo y criterio de aceptación; no como funcionalidad ya disponible. Un paquete “Argentina” debe probar productos y reportes concretos con datos de ejemplo representativos.

### 11.3 Ponderación propuesta después de los filtros

| Dimensión | Peso |
|---|---:|
| Funcionalidad financiera y contabilidad | 20% |
| Localización, datos y cobertura de obligaciones aplicables | 20% |
| Resiliencia, seguridad y operación | 15% |
| Migración y capacidad de entrega | 15% |
| TCO y condiciones de precio/salida | 10% |
| Integración, arquitectura y portabilidad | 10% |
| Referencias y sostenibilidad del proveedor | 5% |
| Parametrización y experiencia del operador | 5% |
| **Total** | **100%** |

Escala propuesta: 0 = sin evidencia; 1 = promesa; 2 = demostración limitada; 3 = caso probado comparable; 4 = prueba satisfactoria con datos/carga representativos del comprador. Deben documentarse excepciones y no compensar un control crítico ausente con un precio menor.

### 11.4 Prueba de concepto mínima

La misma prueba para todos los finalistas debería incluir:

1. Dos débitos concurrentes contra disponibilidad insuficiente, reintentos y respuesta incierta del riel externo.
2. Contrato con cambio de tasa, intereses devengados y corrección retroactiva autorizada; reconstrucción del estado anterior.
3. Reverso posterior al cierre y conciliación entre transacción, cuenta, asiento y extracto de liquidación.
4. Producto en dos monedas sin compensar posiciones indebidamente y con reglas de redondeo explícitas.
5. Para crédito: prepago, atraso, refinanciación y cobranza parcial con imputación verificable.
6. Pérdida de una dependencia, recuperación y reanudación sin duplicar movimientos.
7. Exportación y reconstrucción de una muestra completa fuera del proveedor.
8. Producción de un reporte local relevante y explicación del linaje de cada importe agregado.

Los volúmenes y objetivos de latencia/disponibilidad se fijan desde el perfil real del comprador. Un promedio mensual nacional no es un requisito de TPS para una entidad específica; tampoco sustituye un estudio de picos, concurrencia y dependencia de otros servicios.

## 12. Estrategia de entrada, producto y ejecución

### 12.1 Oferta comercial inicial

Se propone vender un alcance verificable: diagnóstico corto remunerado, piloto con criterios de aceptación, implementación y suscripción. La propuesta debe separar producto común, localización común, integraciones específicas y operación. Las mejoras comunes necesitan una política de incorporación al producto para evitar forks permanentes.

Una estructura de precios a validar puede combinar un mínimo que financie operación y soporte, bandas de contratos/cuentas y consumo adicional definido. Conviene ofrecer simulador de factura y trazabilidad de consumo. El precio debe cubrir entornos, cambios normativos incluidos y guardia acordada; un descuento inicial que no cubre soporte perjudica tanto al proveedor como al comprador.

El canal de venta será consultivo: negocio y operaciones definen beneficios; tecnología e integración evalúan viabilidad; finanzas revisa TCO; riesgo, seguridad, cumplimiento y legales examinan controles y contrato. En entidades públicas o regionales pueden intervenir procesos de contratación específicos. El patrocinador comercial necesita un dueño operativo con capacidad de aprobar el cambio.

Las alianzas prioritarias son implementadores con experiencia de migración, profesionales de contabilidad/cumplimiento local y proveedores de infraestructura/pagos según el segmento. No debe ofrecerse una conexión como “lista” hasta tener alcance, contrato, pruebas y condiciones operativas acordadas con la contraparte.

### 12.2 Hoja de ruta con puertas de inversión

Los intervalos siguientes son metas de planificación desde el inicio del proyecto, no fechas de disponibilidad comprometidas.

| Etapa | Ventana ilustrativa | Entregable | Puerta de avance |
|---|---|---|---|
| Descubrimiento y delimitación | Meses 0–3 | Segmento, entrevistas, inventario de capacidades y obligaciones; modelo económico | Problema cuantificado y al menos dos clientes de diseño con alcance compatible |
| Diseño y validación financiera | Meses 3–6 | Modelo de contratos/asientos, APIs, datos y pruebas de invariantes | Contabilidad y flujos aceptados por operadores y revisores especializados |
| Piloto integrado | Meses 6–12 | Producto acotado, conciliación, migración de muestra y controles operativos | Pruebas funcionales, recuperación, integraciones y costo de servicio satisfactorios |
| Primera operación limitada | Meses 12–18 | Despliegue autorizado por el cliente y soporte activo | Cierres/reportes reconciliados, ausencia de diferencias inexplicadas y operación estable |
| Repetibilidad | Meses 18–24 | Segundo cliente con el mismo producto base | Costo y tiempo de implementación bajan sin mantener forks |
| Ampliación controlada | Desde mes 24 | Más productos o un segundo segmento | Margen, capacidad de soporte y mantenimiento normativo sostenibles |

No deben moverse todas las fechas hacia adelante si una puerta falla: puede ser necesario reducir alcance, asociarse con un motor existente o descartar el segmento.

### 12.3 Métricas para decidir continuar

| Frente | Medida | Señal de revisión |
|---|---|---|
| Mercado | Entrevistas calificadas, presupuesto identificado y conversión a piloto | Interés sin acceso a decisión o sin disposición a pagar |
| Producto | Proporción reutilizada y cambios específicos por implementación | Cada cliente requiere rediseñar contratos o contabilidad |
| Entrega | Horas/costo hasta aceptación y diferencia respecto a presupuesto | Implementaciones crecen más rápido que el valor recurrente |
| Integridad | Partidas sin explicar, duplicados y tiempo de conciliación | Movimientos no reconstruibles o correcciones manuales sin control |
| Operación | Incidentes, cumplimiento del servicio y recuperación probada | Dependencia continua del equipo fundador para operar |
| Economía | Margen por cliente, consumo real, caja y demora de cobro | Soporte y nube consumen el margen previsto |
| Concentración | Ingreso y conocimiento concentrados por cliente/persona | Un solo contrato decide la continuidad del proveedor |

### 12.4 Recomendación final por situación

| Situación | Decisión inicial recomendada | Qué puede cambiarla |
|---|---|---|
| Entidad que necesita salir pronto con productos estándar | Comprar motor y construir integración/experiencia/localización faltante | Propuestas no cubren el producto o no permiten control/salida suficiente |
| Banco con core estable y dificultad en una línea nueva | Modernizar por partes o usar core satélite | Costo de coexistencia supera beneficio o hay riesgo estructural del legado |
| Nuevo proveedor sin clientes ni experiencia operativa comparable | Validar módulo y segmento antes de financiar un core universal | Compromisos de compra, financiación y equipo pueden justificar ampliar alcance |
| Grupo con escala, plataforma común y equipo sostenido | Evaluar construcción propia y reutilización | El costo de mantener/localizar puede superar ventajas de control |

El próximo gasto autorizado internamente debería financiar evidencia: entrevistas, RFI comparable, prueba con datos representativos y caso de negocio por entidad. La decisión de construir todo el core sólo se justifica si esa evidencia demuestra una ventaja sostenible después de incorporar migración, soporte, cambios normativos y salida.

## 13. Registro de fuentes, fechas y límites

Todas las fuentes se consultaron el **15/10/2026**. “Sin fecha visible” significa que se verificó la página disponible al corte, no que el producto o caso haya nacido en 2026. Las fuentes de proveedores acreditan declaraciones y referencias, no auditoría independiente de desempeño o cumplimiento. No se utilizan como prueba los resultados agregados de una búsqueda sin identificar su documento.

| ID | Fuente | Fecha de publicación / período | Qué respalda y limitación |
|---|---|---|---|
| M01 | [BCRA, Inclusión Financiera 2S2025](https://www.bcra.gob.ar/publicaciones/informe-de-inclusion-financiera-segundo-semestre-de-2025/) | 30/04/2026; datos a diciembre de 2025 | Cuentas y crédito según universos del informe; no compradores de software |
| M02 | [BCRA, Pagos Minoristas julio 2026](https://www.bcra.gob.ar/publicaciones/informe-mensual-de-pagos-minoristas-julio-de-2026/) | 28/08/2026; julio y junio según serie | Volúmenes y registros; cuentas con saldo no son MAU. Inconsistencia de QR excluida |
| M03 | [BCRA, Informe sobre Bancos julio 2026](https://www.bcra.gob.ar/publicaciones/informe-sobre-bancos-julio-de-2026/) | 18/09/2026; julio de 2026 | Crédito e irregularidad; no presupuesto IT ni proyección lineal |
| M04 | [BCRA, Sistema Nacional de Pagos](https://www.bcra.gob.ar/sistema-nacional-de-pagos/) | Página institucional sin fecha única | Diferencias de roles y cuentas; revisar normas vigentes para aplicabilidad |
| M05 | [BCRA, Registro de PSP](https://www.bcra.gob.ar/registro-de-proveedores-de-servicios-de-pago/) | Registro dinámico | Base para censo de roles; no se descargó y deduplicó un padrón comercial completo |
| M06 | [BCRA, Nómina de entidades](https://www.bcra.gob.ar/sistema-financiero-nomina-de-entidades/?bco=AAA00&tipo=1) | Consulta dinámica con filtros | Punto de partida del censo; no se publica un conteo sin extracción reproducible |
| M07 | [Bantotal, Core](https://www.bantotal.com/core.html) | Sin fecha visible | Catálogo del fabricante; versión y contrato por verificar |
| M08 | [Bantotal, Banco Formosa](https://www.bantotal.com/historias-de-exito/banco-formosa.html) | Sin fecha visible; menciona 2019 | Referencia argentina declarada; no contrato ni inventario actual |
| M09 | [Accion Point, Implementador Bantotal](https://accionpoint.com/blog/implementador-bantotal-latinoamerica/) | 21/09/2026 | Experiencia local declarada; cifras de proyectos varían dentro de la misma página y no se usan para cuota |
| M10 | [SoFi, adquisición de Technisys completada](https://www.sofi.com/newsroom/sofi-completes-acquisition-technisys/) | 03/03/2022 | Historia corporativa; no cobertura actual de módulos |
| M11 | [SoFi/Galileo, Cyberbank Core para patrocinio bancario](https://tech.sofi.com/es/news/sofi-adoptara-cyberbank-core-de-galileo-para-patrocinio-bancario/) | 16/10/2024 | Caso anunciado en Estados Unidos; no prueba de implantación argentina o finalización |
| M12 | [SoFi/Galileo, Banco Nación](https://tech.sofi.com/es/blog/como-banco-nacion-transformo-su-experiencia-de-banca-digital-con-galileo/) | 30/07/2025 | Cyberbank Digital; no acredita core contable |
| M13 | [Temenos, Banco del Sol](https://www.temenos.com/success-story/banco-del-sol-success-story/) | Sin fecha visible; contexto de lanzamiento y pandemia | Core y componentes declarados; confirmar versión actual |
| M14 | [Temenos, Banco Credicoop](https://www.temenos.com/success-story/bccl-success-story/) | Sin fecha visible; resultados hasta 2017 | Migración y coexistencia históricas; no stack vigente de 2026 |
| M15 | [Temenos, APIs de Transact](https://developer.temenos.com/transact-apis) | Documentación viva | Interfaces por productos; comprobar versión ofertada |
| M16 | [Cobis Topaz, FinancialCore](https://www.cobistopaz.com/es/topaz-one/financialcore) | Sin fecha visible | Familia de productos; no deducir arquitectura única ni clientes por logotipos |
| M17 | [Banco Ciudad, prospecto de emisión, p. 137](https://bancost.com.ar/wp-content/uploads/2020/09/Titulo-de-Deuda-Clase-XXII-Banco-Ciudad-Prospecto-de-Emision.pdf#page=137) | 2020; documento de entidad alojado por tercero | Evidencia histórica COBIS; PDF descargado y contrastado, requiere actualización con el banco |
| M18 | [Banco Ciudad, búsqueda Desarrollador/a CORE](https://bancociudad.na.teamtailor.com/jobs/706332-desarrollador-a-core) | Activa/localizada al corte; sin fecha exacta acreditada | Corroboración limitada de nombre de sistema; puede retirarse o modificarse |
| M19 | [Visa, adquisición de Pismo](https://investor.visa.com/news/news-details/2024/Visa-Completes-Acquisition-of-Pismo/default.aspx) | 16/01/2024 | Propiedad y capacidades declaradas; sin caso argentino |
| M20 | [Pismo, documentación general](https://developers.pismo.io/pismo-docs/docs/welcome) | Documentación viva | APIs/eventos y datos; condiciones contratadas por verificar |
| M21 | [Pismo, reportes programados](https://developers.pismo.io/pismo-docs/docs/scheduled-reports) | Documentación viva | Existencia de reportes por lotes; no extrapolar a todo el procesamiento |
| M22 | [Pismo, de batch a eventos](https://www.pismo.io/blog/from-batch-jobs-to-an-event-driven-model/) | 03/08/2021 | Evolución arquitectónica declarada; no prueba de eliminación total de batch |
| M23 | [Mambu, caso Ualá](https://mambu.com/en/customer/uala) | Sin fecha visible | Préstamos y expansión regional; no toda la operación bancaria actual |
| M24 | [Mambu, capacidades del core](https://mambu.com/en/core-capabilities) | Sin fecha visible | Catálogo de capacidades; verificar configuración y contrato |
| M25 | [Mambu, configuración de depósitos](https://support.mambu.com/docs/setting-up-new-deposit-products) | Documentación viva | Parametrización de producto; no localización argentina completa |
| M26 | [Mambu Insights, precio y consumo](https://docs.mambu.com/docs/insights-pricing-and-consumption/) | Actualizada el 13/04/2026 | Modelo de un componente de datos; no tarifa del core |
| M27 | [Oracle, FLEXCUBE](https://www.oracle.com/latam/financial-services/banking/flexcube/) y [documentación](https://docs.oracle.com/en/industries/financial-services/flexcube.html) | Catálogo y documentación vivos | Oferta global; no referencia argentina validada aquí |
| M28 | [Finastra, Essence](https://www.finastra.com/universal-banking/solutions/essence) | Sin fecha visible | Oferta global; no referencia argentina validada aquí |
| M29 | [Santander, siete preguntas sobre Gravity](https://www.santander.com/es/stories/7-preguntas-sobre-como-gravity-esta-transformando-santander) | 16/07/2025 | Desarrollo del grupo y procesamiento paralelo; métricas globales no trasladadas a Argentina |
| M30 | [Santander, Gravity en España](https://www.santander.com/es/sala-de-comunicacion/notas-de-prensa/2025/06/santander-culmina-la-digitalizacion-de-su-infraestructura-tecnologica-en-espana-con-la-implantacion-de-gravity) | 19/06/2025 | Hito en España; no acredita implantación argentina ni venta abierta del core |

## 14. Pendientes de investigación que cambian la inversión

Antes de convertir este análisis en una decisión de capital deben cerrarse los siguientes faltantes:

1. Censo por entidad y grupo con actividad actual y decisiones de compra identificadas.
2. Entrevistas que cuantifiquen costo del problema y fecha probable de contratación.
3. Al menos tres propuestas comerciales normalizadas por segmento y alcance.
4. Confirmación de referencias locales del módulo exacto y estado de producción.
5. Matriz de obligaciones por entidad/producto y de cobertura por componente, enlazada con [compliant.md](compliant.md).
6. Presupuesto de localización y mantenimiento con responsables y calendario.
7. Evaluación de datos/migración de un cliente de diseño y plan de salida probado.
8. Modelo de caja mensual que incorpore retrasos de ventas, entrega y cobro.

Estas brechas no invalidan la oportunidad; determinan el tamaño de la inversión que puede justificarse con la evidencia disponible.
