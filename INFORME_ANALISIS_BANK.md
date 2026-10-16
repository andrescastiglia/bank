# Informe de análisis y datos relevados — Bank

**Fecha:** 16/10/2026, zona `America/Buenos_Aires`. **Repositorio:** [andrescastiglia/bank](https://github.com/andrescastiglia/bank). **Base examinada:** `main` en `979dd2c8f48e13d17343965d2e7194ec79ca0ed2`, con Rust y runtime propio `FROM scratch` ya integrados. **Naturaleza:** investigación documental y contraste de fuentes públicas; implementación y aceptación institucional sin evaluar.

## 1. Conclusiones principales

El proyecto tiene una biblioteca extensa y coherente en sus principios: autoridad financiera SQL, aislamiento por entidad, configuración fechada, asincronía durable y migración con conciliación. Su principal brecha frente a una operación bancaria real sigue siendo la falta de contratos ejecutables, implementación y evidencia independiente. La cantidad de requisitos y la cobertura de referencias no permiten inferir cumplimiento, seguridad, rendimiento ni disponibilidad efectiva.

| Eje | Resultado del contraste | Novedad frente al estado recuperado |
|---|---|---|
| Legal y normativo | Se verificaron los anexos CER/UVA y una disposición de pagos públicos al exterior. Se mantienen las transiciones SISCEN, A8492 y CNV ya identificadas. | Recuperación de evidencia pendiente de B13247; B13246 y disposición conjunta CGN/TGN 2/2026 incorporadas al análisis. Ningún parámetro activado. |
| Mercado | Siete ofertas muestran composición modular, APIs, parametrización y servicios operativos. Buena parte de sus capacidades ya tiene FR; faltan demostraciones comparables y localización comprobada. | Fineract amplía la comparación de alternativas libres; las demás páginas revalidan ofertas, sin demostrar lanzamientos nuevos ni cambios contractuales. |
| Tecnología | Rust 1.99.1 fue anunciado el 15/10/2026; corrige regresiones de enlace y FFI. La ejecución asíncrona requiere concurrencia acotada y persistencia explícita. | Release nueva verificada; selección concreta de toolchain y dependencias sigue pendiente. |
| Seguridad, crítico | La superficie incluye identidades, autorización de objetos, dinero, efectos externos, dependencias, importación, datos reservados y recuperación. Scratch reduce componentes, pero conserva estas superficies. | Dos avisos RustSec del 14/10 se incorporan como contexto del ecosistema, con alcance condicionado. No hay evidencia de Wasmtime instalado ni de explotación del proyecto. |

La vigilancia tiene resultado **PARTIAL**. Se recuperaron los **110 cuerpos de avisos** enumerados en las ediciones del 15 y 16 de octubre, pero sólo **3 de 40 archivos anexos identificados**; la revisión sustantiva se concentró en los actos pertinentes al core. Persisten fuentes y ventanas sin cobertura completa. Esta mejora de recuperación no cierra la cobertura del Boletín ni la del universo normativo.

Este informe conserva el [plan de implementación existente](PLAN_DE_IMPLEMENTACION_BANK.md) como antecedente. Presenta hechos, diferencias y evidencia faltante; sus recomendaciones finales son complementarias. No modifica la licencia GPL v2 ni el gobierno de merges exclusivos del mantenedor.

## 2. Alcance, método y estado del repositorio

### 2.1 Ventana y continuidad

La corrida `RUN-20261016T030400Z` comenzó a las **00:04:00 del 16/10/2026 en Argentina** (`03:04:00 UTC`). Ventana objetivo: **[15/10/2026 00:00:00 −03:00, 16/10/2026 00:04:00 −03:00)**. Se recuperaron el inventario `2026-10-16.2`, dos corridas previas, sus gaps y cinco hitos de agenda; no se reinició desde el seed. El solapamiento de siete días queda limitado por el inicio solicitado del backfill, 15/10/2026. Textos anteriores necesarios para interpretar una publicación, y avisos técnicos del 14/10, se identifican como contexto.

Las consultas se efectuaron después del inicio. La edición del BO del 16/10 ya era accesible durante ellas, pero no se acreditó su hora de publicación. Se informa como **observación de esa fecha**, sin atribuir todos sus actos a los primeros cuatro minutos del día ni acreditar cobertura del resto del 16/10. Los actos con fecha sin hora deben volver a solaparse en la siguiente corrida.

Se leyó `main` mediante el conector GitHub, incluidas las instrucciones de gobierno y vigilancia; se contrastó el commit con Git y se consultaron las PR abiertas: ninguna al iniciar. La rama operativa no estaba publicada; el estado más reciente recuperable estaba integrado en `main`. Se conserva ese historial y se restablece su persistencia separada, sin incorporar bitácoras de esta corrida al diff del informe.

### 2.2 Qué se examinó y qué demuestra

| Conjunto | Evidencia y alcance de la revisión |
|---|---|
| Repositorio base | Inventario de 189 archivos versionados, 125 Markdown y 28 skills. Huellas por archivo en el manifiesto operativo. Inventariar no equivale a auditar semánticamente cada cláusula. |
| Especificación | Mercado, cumplimiento, arquitectura, ocho ADR, trece familias NFR, alcance/catálogo funcional y módulos pertinentes a los hallazgos. El catálogo declara 1.016 FR/32 módulos, 173 entradas de cumplimiento, 71 criterios NFR y 21 controles. |
| Revisiones previas | Los seis análisis por perspectiva, sus 63 hallazgos, 14 paquetes y el plan de implementación son antecedentes. Se reutilizan sus IDs; no se cierran ni duplican por repetir una observación. |
| Stack vigente | [Contrato Rust/scratch](docs/deployment/rust-scratch.md), ADR-07 y FR-OPS-026. No hay `Cargo.toml`, `Cargo.lock`, archivos `.rs` ni Dockerfile de producto en la base inventariada. |
| Fuentes externas | Texto primario y anexos de actos seleccionados; índices oficiales; documentación técnica del responsable; declaraciones de fabricantes. Se registran URL solicitada/final, hora de consulta, resultado y SHA-256 de bytes. |
| Fuera de evaluación | Código bancario ejecutado, dependencias instaladas, pentest, infraestructura real, homologación de rieles, contratos privados, dictamen del operador y certificación. No se infiere ausencia de evidencias externas al repositorio. |

**Hecho** significa dato observado en la fuente citada. **Interpretación** explicita su posible consecuencia bajo un perfil. **Brecha** identifica evidencia o detalle faltante en el repositorio. Una promesa de un proveedor acredita su oferta declarada, no sus resultados, precio, cuota ni cumplimiento argentino. Una huella HTML distinta puede reflejar fecha de cabecera, token o plantilla: no se clasifica como reforma sin comparar el contenido pertinente.

## 3. Aspectos legales y normativos

### 3.1 Regla de aplicabilidad

El [perímetro funcional](docs/functional/01-entidades-perimetro.md) ya distingue EF, PSPCP, otros PSP, PNFC, PSCPP y proveedor tecnológico. PSAV y agentes CNV requieren su propio encuadre; una cuenta de pago no se transforma en depósito y una licencia de software no habilita actividades financieras. Las obligaciones de la empresa proveedora tampoco son idénticas a las del operador.

Para cada acto se necesitan sociedad, registro, función, producto, moneda, canal, jurisdicción y fecha. Sin operador seleccionado, las conclusiones siguientes son **condicionales**. La ubicación de una norma bajo ARCA, BCRA o CNV no basta para convertirla en una regla común a todos los módulos.

### 3.2 Datos regulatorios verificados y fechas

| Identidad / fuente primaria | Emisión y publicación | Vigencia, exigibilidad y contenido comprobado | Alcance y contraste con Bank |
|---|---|---|---|
| **BCRA B13246/2026 — CER**, [PDF de dos páginas](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/B13246.pdf), [BO aviso 349002](https://www.boletinoficial.gov.ar/detalleAviso/primera/349002/20261015) | Emitida 13/10; publicada 15/10/2026. | Anexo con 31 valores diarios, 16/10–15/11. Ejemplos observados: CER 854,9776 el 16/10 y 870,6933 el 15/11. El texto advierte que las series de datos ofrecen más decimales que el cuadro. Las fechas de cada valor no son una nueva fecha general de exigibilidad. | Comunicada a EF; relevante para contratos y valuaciones que efectivamente usan CER. FR-CFG-011/012 y el motor de intereses contemplan fuentes y versiones; falta materializar el paquete de serie, precisión y controles. |
| **BCRA B13247/2026 — UVA**, [PDF de dos páginas](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/B13247.pdf), [BO aviso 349003](https://www.boletinoficial.gov.ar/detalleAviso/primera/349003/20261015) | Emitida 13/10; publicada 15/10/2026. El aviso ya había sido descubierto; se completó evidencia de su anexo. | 31 valores diarios, 16/10–15/11: UVA ARS 2.157,79 el 16/10 y ARS 2.196,12 el 15/11, cuadro con dos decimales. No confundir UVA/CER con UVI/ICC ni reutilizar el redondeo mostrado para toda operación financiera. | EF y contratos alcanzados. CFG, INT, cuentas/créditos y documentos deben conservar serie, fecha efectiva, fuente y versión. No se cargaron estos importes en configuración productiva. |
| **BCRA B13248/2026**, [PDF](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/B13248.pdf) y [manual SISCEN](https://www.bcra.gob.ar/archivos/Pdfs/PublicacionesEstadisticas/siscen.pdf) | Emitida 15/10. El resultado del buscador no acredita fecha BO. | SISCEN-0019, versión 03, desde enero de 2027: umbral ARS 1.700 millones y `VALOR 2 = 1700`; el tramo previo del manual usa ARS 1.300 millones/código 1300. El estrato ordinario 30–35 días admite la excepción de inhábiles consecutivos; un plazo de 36 días puede conservar `VALOR 5 = 51` si satisface esa regla. | EF informante y depósitos comprendidos. Ya analizada en P-REG-01; FR-RPT-001/002/007/008/012/038 son marco genérico, no un paquete SISCEN probado. No es novedad duplicada de esta corrida. |
| **BCRA A8492**, [PDF y hojas](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8492.pdf) | Emitida 15/10; fecha BO no acreditada por el índice consultado. | Desde 1/11/2026; cambios del RI Efectivo mínimo y Aplicación de Recursos, partida 102200 y control 538. Hash revalidado sin cambio. | EF y presentación según grupo. RPT-08, FR-RPT-021 y FR-RSK-019 ya la contemplan; la brecha es ensayo del período y entrega aceptada, no ausencia total de requisito. |
| **CNV RG1172/2026**, [texto y anexo en BO](https://www.boletinoficial.gov.ar/detalleAviso/primera/348986/20261015) | Emitida 14/10; publicada 15/10/2026. | Vigencia general 16/10; art. 40.b, información periódica desde 1/11. Primer período y fecha concreta de presentación dependen de situación del sujeto; no se inventa vencimiento. | PSAV registrados y categorías aplicables. P-REG-02 ya detectó que INV/RPT genéricos no especifican todo el régimen. No extenderlo automáticamente a PSP o PNFC. |
| **CNV RG1173/2026**, [texto BO](https://www.boletinoficial.gov.ar/detalleAviso/primera/348987/20261015) | Emitida 14/10; publicada y vigente 15/10/2026. | Examen/registro de idóneos y transición particular hasta 15/12/2026. El hito no es un plazo general para todo usuario del core. | Personas/entidades alcanzadas por idoneidad CNV. IAM/COR/INV pueden necesitar evidencia de habilitación; no implica construir un sistema de exámenes. Antecedente P-REG-04 revalidado. |
| **CGN/TGN, disposición conjunta 2/2026**, [texto BO](https://www.boletinoficial.gov.ar/detalleAviso/primera/349055/20261016), anexo `IF-2026-100377699-APN-TGN#MEC` | Emitida 15/10; publicación 16/10, hora no acreditada. Observada después del corte objetivo. | Vigente desde publicación; abroga disposición conjunta 2/2019. Procedimiento para gastos y pagos a beneficiarios del exterior de SAF que operan dentro de CUT. Texto y archivo anexo recuperados y leídos. | SAF de Administración Nacional/CUT, TGN/CGN y circuito BNA, con excepciones indicadas para SAF 355/356. No es un nuevo mandato de pagos exteriores de toda EF o fintech. Requiere paquete específico sólo si se selecciona ese servicio. |

Las fechas de consulta son del 16/10 UTC y Argentina, con hora exacta por evidencia. El cambio de fecha de la cabecera del portal BO no cambia la publicación del acto: se contrastaron identidad, URL por edición y pie de publicación. Los comunicados C de tasas, tipo de cambio, reservas y pasivos se separaron de reformas de reglas generales; un dato de referencia sólo alimenta el producto que lo tenga pactado.

### 3.3 Hallazgos nuevos o con evidencia ampliada

**INF-REG-01 — Series CER/UVA: se resolvió evidencia pertinente, falta el paquete ejecutable.** Los anexos BCRA y los archivos anexos del BO de B13246/B13247 se recuperaron por sus mecanismos oficiales. Los PDF BCRA tienen dos páginas cada uno; los del BO incluyen su propia presentación y tablas como imagen, revisadas visualmente tras renderizarlos. Huellas diferentes por formato/procedencia no prueban valores incompatibles. Se contrastaron período y extremos de las tablas; la verificación automatizada fila a fila de dos formatos y de la serie con mayor precisión sigue pendiente.

El diseño ya exige fuente, unidad, vigencia y regla de cálculo en FR-CFG-011/012/022, CTL-02/06 y NFR-01-C04. La brecha es materializar ingestión controlada, completitud por fecha, decimal exacto, corrección vinculada y oráculos independientes del cálculo contractual. Faltar un valor o recibir otra versión no habilita extrapolación silenciosa. La corrección de un índice tampoco debe reescribir automáticamente asientos históricos. ADR-05 y los skills de configuración/integridad financiera ya orientan ese tratamiento.

**INF-REG-02 — Pagos públicos al exterior: nueva especialización condicionada.** La disposición CGN/TGN establece un único beneficiario por orden, débito sobre CUT, autorización TGN mediante Nota de Pago y vínculo de identidad entre orden, solicitud en plataforma Comex BNA, Nota y medio de pago. El art. 8 exige mantener inalterable la identidad del beneficiario y su cuenta a lo largo del circuito. El anexo indica que el campo de cuenta bancaria no se informa en la orden de pago: esto no permite eliminar la cuenta del resto del proceso ni omitir su trazabilidad.

El anexo también atribuye al SAF, cuando corresponde, la retención de Ganancias al beneficiario exterior y la entrega del certificado SIRE dentro de **48 horas desde la emisión del medio de pago**. Para IVA como responsable sustituto prevé VEP y documentación según el circuito indicado, con alternativa de entrega dentro de esas 48 horas. Se citan RG 739 y 4356 como referencias del anexo, sin afirmar una revisión integral de sus modificatorias. No se determina una fecha calendario: falta el evento de cada pago y el perfil fiscal concreto.

FR-FXT-001/002, TAX-001/002, FR-RPT-001, ASY y COR ofrecen bases comunes. No se encontró un contrato específico e-SIDIF/CUT–BNA ni los estados y documentos de este circuito. **Interpretación:** si el primer servicio excluye SAF/CUT, registrar no aplicabilidad fundada; si lo incluye, se requiere especialización de integración, identidad y reloj fiscal, con Finanzas/Legal del operador. No trasladar el deber tributario del SAF al proveedor de software por mera automatización.

**INF-REG-03 — Actos financieros que no son nuevas obligaciones universales.** La [resolución conjunta 62/2026](https://www.boletinoficial.gov.ar/detalleAviso/primera/349042/20261016), emitida 14/10 y publicada 16/10, amplía emisiones del Tesoro: letras y bonos, incluidos TAMAR, dual CER/TAMAR y TAMAR/dólar linked. Rige desde su dictado. Es relevante para catálogo y valuación si el operador mantiene esos instrumentos; no obliga a comercializarlos ni permite reconstruir todos sus términos sin los actos originales.

La [resolución conjunta 61/2026](https://www.boletinoficial.gov.ar/detalleAviso/primera/349041/20261016) amplía una letra **intransferible** para el BCRA: no se clasifica como producto vendible a cualquier cliente. Los avisos de tasas BNA acreditan condiciones de esa entidad, no precios obligatorios para otros bancos. Los avisos BCRA de la edición del 16 revisados son edictos particulares; no se copiaron identidades ni se convirtieron sus plazos en requisitos generales.

**INF-REG-04 — ARCA: distinguir organización administrativa de reforma fiscal.** La [disposición 140/2026](https://www.boletinoficial.gov.ar/detalleAviso/primera/348992/20261015) trata asignación de funciones; la [66/2026 de Neuquén](https://www.boletinoficial.gov.ar/detalleAviso/primera/348993/20261015), reemplazos de jefaturas; la [92/2026 de Rosario](https://www.boletinoficial.gov.ar/detalleAviso/primera/349046/20261016), régimen de reemplazos. Su lectura no sostiene un cambio de alícuotas, padrón, diseño de registro o obligación informativa del core. La biblioteca ARCA y sus portadas se consultaron, pero no se completó una búsqueda cronológica con todos los textos y anexos: **no se concluye ausencia de novedades fiscales**.

### 3.4 Agenda heredada, sin duplicar alertas

| Hito | Situación al 16/10/2026 | Evidencia pendiente |
|---|---|---|
| RG1172, vigencia general 16/10 | Fecha alcanzada; condición PSAV aún no seleccionada. Norma ya registrada. | Encadre/categoría, relación con actividad efectiva y paquete de controles. |
| RG1172 art. 40.b y A8492, 1/11 | Transiciones próximas, conocidas. | Período/primer vencimiento del PSAV; versión RI y pruebas para EF. |
| RG1173, transición particular 15/12 | Pendiente por sujeto alcanzado. | Mecanismo de idoneidad y evidencia real de la persona/entidad. |
| B13248, 1/1/2027 | Versión futura de SISCEN-0019. | Casos por umbral, moneda, período y excepción de inhábiles. |
| CGN/TGN 2/2026, 48 h por evento | Nuevo disparador condicional, no vencimiento fechado. | Perfil SAF/CUT y hora efectiva de emisión del medio de pago; registrar agenda sólo si se activa ese alcance. |

### 3.5 Brecha de cumplimiento y trazabilidad

El [inventario de cumplimiento](docs/compliant.md) mantiene su corte histórico. Este informe amplía evidencia y análisis, sin afirmar que sus 173 entradas incorporen cada nueva especialización. La falta de un paquete CER/UVA o CUT no significa que falten motores genéricos de índices o pagos; el problema es la descomposición verificable por perfil y edición.

| Materia | Documentos/requisitos afectados | NFR / ADR / controles | Skill y criterio material a concretar |
|---|---|---|---|
| CER/UVA | Cumplimiento LAW-16/BCRA-F06; CFG, INT, ACC/CRE y documentos contractuales | NFR-01/09/11; ADR-05; CTL-02/06/19 | `core-regulatory-watch`, `core-bancario-argentina`, `adr-05-configuracion-versionada`: conservar identidad/serie/precisión, fecha y prueba de cambio/corrección. |
| RI/SISCEN | RPT-08; FR-RPT-021/038, FR-RSK-019 y paquete SISCEN aún pendiente | NFR-09/11; ADR-05; CTL-06/19 | Coordinadores FR/NFR: casos con oráculo por período, límites y calendario, más estado de aceptación del receptor. |
| PSAV/idóneos | LAW-18; INV/RPT/ENT/IAM/COR, especialización condicionada | NFR-05/06/11; ADR-05/06; CTL-08/09/17/19 | Revisar sujeto, categoría, información/custodia y habilitación; no expandir por defecto el denominador de todos los perfiles. |
| CUT/exterior | FXT/TAX/RPT/COR/ASY; contrato y operación SAF/BNA | NFR-01/04/07/08/11; ADR-03/05; CTL-04/06/12/19 | `core-fr-requisitos` y vigilancia: identidad consistente, estados autorizados y reloj de 48 h desde evento, sólo con alcance aplicable. |

No se modificaron reglas monetarias, reportes, contratos ni skills por una interpretación aún no seleccionada. La revisión competente debe resolver aplicabilidad; el desarrollo con datos sintéticos puede continuar sobre contratos explícitos. Los hallazgos REV-LEG-01/08/10, REV-ACC-01/04 y REV-QA-05 siguen siendo pertinentes.

## 4. Mercado y competencia

### 4.1 Oferta observada

Las páginas siguientes se reconsultaron el 16/10/2026. Son documentación viva u oferta del responsable; salvo las fechas expresas, no se les asigna fecha de lanzamiento. No se obtuvieron cotizaciones, contratos, resultados de una PoC ni nuevas cifras verificadas de cuota o demanda comprable. Las referencias locales del [análisis de mercado](docs/market_analysis.md) siguen fechadas y requieren confirmar entidad, versión, país y perímetro.

| Oferta y fuente | Capacidades declaradas/visibles | Contraste con Bank y dato que falta |
|---|---|---|
| [Mambu](https://mambu.com/en) | Plataforma componible; préstamos de consumo/empresa y banca/depósitos. | CFG, CRE, ACC e INT cubren principios similares. Faltan evidencia de parametrización reutilizable, esfuerzo de integración y costo; no extrapolar el caso regional Ualá a todas las cuentas argentinas. |
| [Pismo](https://developers.pismo.io/pismo-docs/docs/welcome) | Guías/APIs de cuentas, emisión de tarjetas, catálogo de productos, eventos y ciclo de vida/deprecación de APIs. | ACC/CRD/PAY/ASY tienen FR. La oportunidad concreta es sandbox y contratos versionados que un integrador pueda usar. No se acreditó un core completo localizado en Argentina ni un nuevo release por cambiar el hash HTML. |
| [Bantotal](https://www.bantotal.com/) | Core, cash management, BaaS, finanzas embebidas, pagos, canales, servicios SaaS e IA según oferta del fabricante. | COR/PAY/CST/AIG ya prevén esas familias. Su cobertura declarada exige comparar módulos concretos, implantación y mantenimiento; «BaaS» no transfiere al socio la licencia del banco. |
| [Topaz](https://www.topazevolution.com/) | Topaz One integra core, prevención de fraude, canales/onboarding, pagos, inversiones, originación y automatización regulatoria/contable. | Bank tiene módulos equivalentes de alcance documental. Faltan recorridos integrados y responsabilidad por adaptadores. Las cifras comerciales del sitio no se usan como cuota argentina ni como prueba de eficacia. |
| [Temenos](https://www.temenos.com/products/core-banking/) | Modernización progresiva, arquitectura componible, SaaS, copilotos/agentes de IA y segmentos bancarios. | ADR-01/08, MIG y AIG contemplan modernización y gobierno. Diferenciación requiere prueba de coexistencia y límites de autonomía; una referencia de otro país no prueba localización argentina. |
| [Thought Machine Vault Core](https://www.thoughtmachine.net/vault-core) | Ledger unificado y lógica de producto desacoplada/programable; flexibilidad de despliegue según fabricante. | ADR-02/05 separan autoridad y configuración. No hay evidencia para sustituir reglas limitadas por ejecución arbitraria de código: aumentaría validación, soporte y superficie de seguridad. |
| [Apache Fineract](https://fineract.apache.org/) | Core libre: clientes, cartera de préstamos/ahorros, contabilidad integrada en tiempo real, reportes, productos configurables, documentos KYC y flujos de cuatro ojos. | Comparador adicional para no atribuir la diferenciación a la mera apertura del código. No se verificó localización argentina, migración del caso ni costo total. No se incorporó código o dependencia. |

Fineract declara **Apache License 2.0**. La [FSF distingue su compatibilidad con GPL v3 y su incompatibilidad con GPL v2](https://www.gnu.org/licenses/license-list.html#apache2). Para este proyecto bajo GPL v2, el estudio de sus capacidades no autoriza copiar/combinar código: una eventual integración debe examinar obras, distribución, componentes y licencias concretas. Este hallazgo no modifica la licencia del repositorio ni decide por sí solo el encuadre de una integración entre procesos independientes.

### 4.2 Mapa de capacidades e integraciones

| Necesidad observada | Ya documentado | Brecha verificable / clasificación |
|---|---|---|
| Productos reutilizables sin fork por cliente | FR-CFG-001–030; ADR-05; NFR-09 | Falta un producto ejecutable con ejemplos de cambio y límites de configuración. Brecha de evidencia, relacionada con REV-COM-03/04. |
| APIs, eventos, SDK/sandbox y deprecación | FR-ASY-007/008/014/015; NFR-08; ADR-03 | Contratos y simulador consumibles no acreditados; REV-ARC-01. API-first no demuestra integración argentina homologada. |
| Modernización gradual y carga inicial | FR-MIG-006/011/017–026/030/031; ADR-08 | Falta ensayo de cohorte con barrera, delta, ambigüedad externa y salida independiente. REV-ARC-03 y REV-SEC-11. |
| Onboarding, atención y operación de excepciones | CLI, IAM, CST, REC y FR-ASY-032 | Falta recorrido utilizable por titular/operador con estados fieles y accesibilidad probada. No es ausencia de módulos de atención. |
| Pagos, tarjetas y finanzas embebidas | PAY, CRD, COR y FR-PAY-031 | Faltan versión de contraparte, responsabilidades/homologación y costos del riel. ISO 20022 no sustituye el perfil real de mensajes. |
| Localización y actualización regulatoria | TAX/RPT, FR-CFG-019, FR-RPT-038 y vigilancia | Faltan paquetes efectivos por sujeto, pruebas y compromiso de mantenimiento cuando se presten servicios. GPL no sustituye ese servicio. |
| SaaS/soporte y portabilidad | OPS, MIG, NFR-08/12; exportación y recuperación | Falta oferta medible de servicio, guardia, costos y salida. REV-COM-07/08/11 y REV-SEC-07/12. |
| IA en atención/operación | AIG, CTL-21 y NFR de seguridad/privacidad | Falta caso de uso y evaluación. Una promesa comercial de agentes no justifica capacidad autónoma para liberar fondos o cambiar reglas. |

### 4.3 Lectura comercial y económica

**Hecho:** hay convergencia de ofertas hacia modularidad, integración y operación acompañada. **Inferencia:** para Bank, «Rust + APIs + open source» describe opciones técnicas, pero aún no demuestra una ventaja económica para un operador argentino. Una diferenciación defendible podría surgir de localización explicable, migración conciliada, reglas reproducibles y salida comprobable; su demanda y costo siguen sin medirse.

No se verificaron precios públicos comparables de core, margen por cliente ni un TAM nuevo. Las cifras ilustrativas de la documentación previa siguen siendo supuestos, no precios observados. La unidad relevante de costo debe incluir celda/entidad, bases y réplicas, broker, retención, KMS/IAM, soporte, actualizaciones y egreso. El costo de contribuir al proyecto libre es distinto del de ofrecer una operación con SLA.

Los hallazgos REV-COM-01/02/04/07/08/11 conservan su utilidad, bajo el gobierno actualizado: seleccionar un caso para validar no convierte ventas o ARR en condición para contribuir. No se contactó a fabricantes ni clientes y no se concluye cuál proveedor gana una licitación sin su perfil y evidencia.

## 5. Innovación tecnológica y arquitectura

### 5.1 Novedad de toolchain

El [anuncio oficial de Rust 1.99.1](https://blog.rust-lang.org/2026/10/15/Rust-1.99.1/) del **15/10/2026** identifica tres correcciones: símbolo `wcslen` faltante en ciertos targets; compilación incorrecta de retornos FFI `bool` en x86_64 por extensión del registro; y carga de `libLLVM` por `rust-lld` en macOS fuera del proxy de rustup. El [manifiesto estable](https://static.rust-lang.org/dist/channel-rust-stable.toml), consultado el 16/10, informa fecha 15/10 y Rust `1.99.1 (58cf8f9c3 2026-10-13)`.

**INF-TEC-01 — Release relevante, adopción pendiente.** Las correcciones de FFI/enlace merecen evaluación por el contrato de binarios estáticos y posibles clientes nativos. No se demostró afectación del futuro binario Linux ni se clasificó el anuncio como una CVE. Sin workspace o toolchain fijado no hay upgrade aplicado. El contrato vigente ya exige `rust-toolchain.toml`, lockfile, targets/features e inspección ELF: la evidencia necesaria es build y prueba por arquitectura, no apuntar a `stable` flotante.

### 5.2 Frameworks y ejecución asíncrona

La [documentación de axum consultada](https://docs.rs/axum/latest/axum/) muestra **0.8.9**, fechada 22/9/2026, integración con Tokio/Tower y dependencias/feature flags. Es un candidato observado, anterior a la ventana; no una dependencia seleccionada. [Tokio, tareas](https://tokio.rs/tokio/tutorial/spawning) y [puentes entre código síncrono/asíncrono](https://tokio.rs/tokio/topics/bridging) explican mecanismos de ejecución; no garantizan durabilidad de una obligación de negocio.

**Interpretación para Bank:** un framework puede acelerar contratos HTTP, middleware, límites y trazas. La elección debe contrastar soporte, licencias, cancelación, errores, TLS y dependencias nativas con NFR-03/05/09. Limitar pools y concurrencia evita que hashing, compresión, cómputo de intereses o importaciones bloqueen el executor. Una tarea en memoria aceptada sin estado durable no satisface FR-ASY-001/016, aunque use `async`.

### 5.3 Contraste de patrones con el diseño vigente

| Patrón/dato técnico | Situación en la arquitectura | Consecuencia y evidencia que falta |
|---|---|---|
| Núcleo modular y frontera financiera local | ADR-01/02; un escritor autorizado, transacción SQL y guardianes | Evita sumar RPC al débito, pero falta esquema/contrato de locks. Un lenguaje con tipos fuertes no impide doble gasto por intercalado lógico. REV-ARC-01/02. |
| Outbox/inbox, trabajos durables y proyecciones | ADR-03, FR-ASY-004–029, NFR-04 | Ya diseñado; no presentarlo como funcionalidad recién descubierta. Faltan secuencias, retención, backpressure y ensayos de reentrega/ambigüedad. REV-ARC-04/08. |
| Configuración fechada y linaje | ADR-05; CFG, RPT, DAT | Adecuado para transición y rectificación; faltan paquete concreto y oráculos con fechas de negocio. Separar vigencia de regla y momento de conocimiento. |
| Celdas y HA local/DR regional activo-pasivo | ADR-04/06, NFR-02/05/12 | Falta contrastar proveedor, dominio de fallo y recuperación de IAM/KMS. No hay prueba de latencia/99,95 % ni de RPO por nombrar Kubernetes o réplica. REV-ARC-06/07. |
| Bulk por staging y aplicación por conjuntos | ADR-08; FR-MIG-006/007/011/012/022/026 | `COPY FROM STDIN` puede acelerar ingestión; no es el punto de aceptación financiera. Mantener RLS/ACL, invariantes, conciliación, generación preparada y activación controlada. |
| Snapshot/barreras para reportes | FR-ASY-024 y NFR-11 | Un offset máximo de Kafka no demuestra un corte multifuente completo; falta protocolo concreto. REV-ARC-05. |
| Observabilidad y auditoría separadas | NFR-07 y CTL-12/14 | Traces pueden muestrearse según perfil; evidencia material de dinero/autorización no puede desaparecer por muestreo. Falta instrumento y registro de corridas. |

Estos patrones son establecidos y ya forman parte del diseño; no se les atribuye un lanzamiento en octubre de 2026. La innovación útil para el proyecto es convertirlos en un flujo demostrable con menor costo y riesgo medidos. No hay un benchmark que justifique cambiar SQL por otra autoridad, eliminar persistencia síncrona o prometer exactamente una vez entre SQL y un riel externo.

### 5.4 Scratch: contrato y límites observables

La [documentación de Docker sobre imágenes base](https://docs.docker.com/build/building/base-images/#create-a-minimal-base-image-using-scratch) describe scratch como base mínima. Bank requiere binarios Linux realmente estáticos, recursos de CA/calendarios explícitos, UID/GID no root, raíz de sólo lectura, probes sin shell y terminación SIGTERM controlada. Los [security contexts de Kubernetes](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) permiten declarar controles, pero su presencia en YAML debe comprobarse contra el proceso y plataforma efectivos.

**INF-TEC-02 — La imagen mínima desplaza responsabilidades al artefacto.** CA vencidas, tzdata incompleta, DNS, bibliotecas nativas, carga de plugins o apagado durante commit/ACK pueden fallar sin una distribución Linux. Falta construir imagen por arquitectura y probar TLS válido/inválido, zona de negocio, filesystem, probes y recuperación de trabajo. La [regla de lockfiles de Cargo](https://doc.rust-lang.org/cargo/guide/cargo-toml-vs-cargo-lock.html) favorece reproducibilidad; la release necesita además builder/digest, linker, features, SBOM y procedencia. No se ejecutaron builds, inspección ELF ni scans de imágenes porque no existen esos artefactos en el alcance.

## 6. Seguridad informática — eje crítico

### 6.1 Avisos y exposición efectiva

| Fuente verificada | Dato observado y fecha | Evaluación de aplicabilidad |
|---|---|---|
| [RustSec RUSTSEC-2026-0352](https://rustsec.org/advisories/RUSTSEC-2026-0352.html), [aviso upstream](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-m9f7-9w4p-gv38) | Emitido 14/10/2026; `wasmtime-wasi`, escape de sandbox por renombrar symlinks con barras finales; CVSS 4.0 8,8. RustSec identifica **macOS/FreeBSD**. Ramas corregidas: `>=36.0.18,<37.0.0`; `>=48.0.6,<49.0.0`; `>=49.0.3`. | Contexto anterior al backfill, nuevo para este relevamiento. No hay Wasmtime seleccionado. El alcance macOS/FreeBSD no demuestra exposición del runtime Linux scratch; evaluar también herramientas de desarrollo si se incorporara ese paquete. |
| [RustSec RUSTSEC-2026-0363](https://rustsec.org/advisories/RUSTSEC-2026-0363.html), [aviso upstream](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-q554-3cjc-rx7p) | Emitido 14/10; `wasmtime`, tablas de handles del component model con límite sólo por instancia y sin cargo a un límite global; agotamiento de recursos, CVSS 3.1 6,2. Mismas ramas corregidas indicadas arriba. | Condicional a versión, funcionalidad y entorno. No es una vulnerabilidad de todo servicio Rust. Sin árbol de dependencias no se emite resultado de exposición o de `cargo audit`. |
| [PostgreSQL CVE-2026-14666](https://www.postgresql.org/support/security/CVE-2026-14666/) y [CVE-2026-19385](https://www.postgresql.org/support/security/CVE-2026-19385/) | Avisos del 13/8/2026 revalidados, ya registrados: RLS/plan con permisos obsoletos y ejecución de código mediante transform malicioso en `pg_dump`. Versiones corregidas: 18.6, 17.11, 16.15, 15.19 y 14.24. | PostgreSQL es tecnología propuesta; versión/servicio no seleccionados. Verificar componente servidor y cliente de backup/restauración por separado. No asumir RLS como única frontera ni usar herramientas antiguas sobre fuentes no confiables. |
| [CISA KEV, repositorio oficial](https://raw.githubusercontent.com/cisagov/kev-data/develop/known_exploited_vulnerabilities.json) | Catálogo `2026.10.15`, publicación `2026-10-15T17:00:11.2795Z`, 1.746 entradas; mismo hash que la corrida anterior. El caso Atlassian CVE-2026-21589 ya estaba identificado. | No se genera otra alerta idéntica. Inventario efectivo ausente; los plazos CISA no son automáticamente plazos legales argentinos. Un catálogo estable no acredita que todo el stack carezca de otros avisos. |

**INF-SEC-01 — Gestión de exposición por artefacto, no por lenguaje.** Rust evita clases de errores de memoria dentro de su modelo seguro, pero `unsafe`, FFI, crates, librerías C/TLS, builder y herramientas operativas conservan superficie. La evidencia mínima futura debe vincular aviso → componente/versión/features/OS → artefacto/digest → decisión de tratamiento → prueba. `cargo audit`/herramienta equivalente, SBOM y revisión de licencias son mecanismos candidatos; no se informa un resultado ficticio sin lockfile o imagen.

Los dos RustSec tienen severidades de escalas CVSS diferentes. Ninguno se eleva a «incidente crítico de Bank» por el título de esta sección. El riesgo del negocio requiere exposición, capacidades del atacante, fondos/datos y controles del despliegue concreto.

### 6.2 Vectores de ataque y controles existentes

La tabla es un modelo de amenazas documental. Los escenarios son plausibles y útiles para aceptación; **no son ataques observados ni pruebas ejecutadas**.

| Frontera / vector | Efecto bancario posible | Diseño existente y evidencia material que falta |
|---|---|---|
| Robo de sesión, phishing y recuperación débil de autenticadores | Aprobar pagos o reemplazar el contacto/factor del titular. | FR-IAM-003/009/011–015, NFR-05 y BCRA-T36/41/42. Falta política por acción/canal, revocación efectiva, recuperación y pruebas de reuso/acción diferente. |
| BOLA/BFLA y abuso de autorización por campo | Leer/modificar cuenta ajena, consultar respuesta idempotente de otra entidad o asignarse atributos privilegiados. | FR-IAM-004/005/010, ADR-06 y CTL-09/17. Falta matriz endpoint–objeto–campo–rol y casos negativos en API/SQL/worker/exportación. REV-SEC-01. |
| Operador con dos identidades o delegación encubierta | Crear y aprobar su propio ajuste, regla, carga o reporte. | FR-IAM-007 y NFR-05-C03. Falta concretar independencia por persona y delegación, no sólo comparar nombres de usuario. REV-SEC-02. |
| Carrera entre débitos, reserva, revocación o cambio de límite | Doble gasto o autorización con facultad/límite vencidos. | BAL/LED, ADR-02, CTL-01/03/04. Faltan modelo SQL, guardianes y oráculos de intercalados; no lo resuelve sólo ownership de Rust. |
| Callback falso, replay o timeout interpretado como rechazo | Doble liquidación, liberación prematura de reserva o inconsistencia entre fondos y riel. | FR-ASY-011–014/023/029, PAY y REC. Falta contrato real de autenticidad, deduplicación/fencing remoto y resolución de estado ambiguo. |
| Abuso de API, SSRF, payload excesivo y agotamiento de pools | Denegación de servicio, acceso lateral o fuga mediante URL de callback/documento. | ASY, IAM, NFR-03/04/05 y aislamiento por celda. Faltan cuotas por recurso/entidad, límites de tamaño/tiempo, egress autorizado y ensayos de saturación con controles activos. |
| Manipulación de configuración, índices o archivos bulk | Cambiar tasas/impuestos/destinos o publicar saldos preparados. | ADR-05/08, FR-CFG-020/027, FR-MIG-006/007/011/017/024, CTL-02/09/20. Faltan manifiestos firmados/verificados, permisos y casos de archivo alterado, repetido y malicioso; no usar `COPY PROGRAM` ni desactivar RLS. |
| Cadena de suministro/CI, imagen o clave de firma comprometida | Introducir binario/regla con privilegios o sustituir release. | FR-OPS-026, NFR-09, contrato scratch y CTL-15. Faltan build reproducible, revisión de dependencias, SBOM/procedencia/firma y política de admisión por digest. REV-SEC-06. |
| Pérdida/abuso de IAM, KMS o credenciales de soporte | Abarcar varias celdas, descifrar copias o impedir su recuperación. | ADR-04/06 y CTL-09/10/13. Faltan dominios administrativos, bootstrap, recuperación/rotación/revocación de raíces y ensayo sin acceso a la región original. REV-SEC-03. |
| Datos en logs, eventos, DLQ, analítica, backup o herramientas de IA | Divulgar legajos, PAN o ROS; reintroducir datos vencidos durante restore. | AML/DAT/AIG, NFR-06/07, CTL-08/10/11/12/21. Falta mapa poblado de finalidad/residencia/retención y prueba de minimización/restore. REV-SEC-05. |
| Ransomware, restauración incompleta o split brain | Reabrir egresos con hechos perdidos o pagar otra vez después del desastre. | ADR-04, NFR-02, FR-ASY-029 y MIG/REC. Falta recuperación medida, reconciliación con el riel y aislamiento del escritor anterior; restaurar SQL no revierte pagos externos. |

### 6.3 Identidad, cifrado, APIs y estándares

**Identidad.** OIDC/OAuth autentican e intercambian autorizaciones; no sustituyen KYC, poderes ni controles de negocio. Se necesita validar emisor, audiencia, firma, tiempo y contexto, y revalidar facultades materiales al serializar el comando. El refuerzo de autenticación debe corresponder a la acción y al perfil argentino. Una guía internacional no autoriza eliminar requisitos BCRA específicos, ni convertir una excepción de canal en regla general.

**Cifrado y claves.** El diseño ya exige transporte/reposo protegidos, secretos separados, mínimos permisos y rotación/recuperación. Falta elegir proveedor TLS/KMS/HSM, cadenas de confianza, algoritmos y política temporal con soporte efectivo. Certificado válido, cifrado de disco y mTLS cubren controles distintos. Una imagen scratch debe validar nombre/cadena y cargar el trust store; «sin paquetes» no demuestra criptografía segura. El esquema de claves debe sobrevivir al restore sin copiar secretos al repositorio o a trazas.

**APIs financieras.** [FAPI 2.0 Security Profile](https://openid.net/specs/fapi-security-profile-2_0-final.html), final del **22/2/2025**, ofrece un perfil OAuth de alta seguridad con mecanismos como PAR, PKCE y tokens vinculados al emisor de la prueba mediante mTLS/DPoP según perfil. No se obtiene conformidad por habilitar JWT ni por incorporar sólo un mecanismo. Bank necesita una decisión de perfil aplicable, matriz de requisitos y ensayos de replay, redirecciones, claves y compatibilidad con el IAM escogido. La autorización por objeto/campo y la idempotencia financiera siguen siendo controles propios.

**Verificación de aplicaciones.** [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) mantiene la referencia ASVS 5.0 de la documentación; el HTML reconsultado no demuestra una edición normativa nueva por variar de hash. ASVS y API Top 10 sirven para requisitos y amenazas complementarias: no son un pentest ejecutado ni una certificación de Bank. NIST, ISO/IEC, PCI y Swift conservan naturaleza técnica, voluntaria o contractual según alcance; el disparador real puede ser una norma, contrato o participación de red. No se accedió ni se copiaron textos restringidos completos de ISO/Swift, ni se acreditó cobertura universal de sus ediciones.

FR-OPS-042 ya exige registrar edición/programa, contrato activador y evidencia. PCI necesita delimitar CDE y rol; Swift, arquitectura/participación y evaluación correspondiente; un certificado de gestión no homologa todos los servicios del core. Este informe no atribuye esas obligaciones a un perfil que no procese tarjetas o no participe en la red.

### 6.4 Impacto trazable de seguridad

Los avisos de PostgreSQL remiten a ADR-02/06/08, NFR-05/09/10 y CTL-09/15/20; Rust/FFI/scratch, a ADR-07, FR-OPS-026 y NFR-05/09; identidad/API, a IAM/PAY/ASY, ADR-03/06, NFR-05/08 y CTL-04/09/17. Los hallazgos previos REV-SEC-01/02/03/05/06 y REV-ARC-01/02/06 siguen abiertos en su alcance documental.

Los skills de stack, seguridad, integridad, asincronía y migración ya prescriben separación entre diseño y prueba. La mejora relevante es que una futura selección de crates/servicios aporte evidencia concreta consumible por esos skills. Añadir otra instrucción genérica o declarar «scan aprobado» sin artefacto no cierra esa brecha.

## 7. Cobertura real, evidencia y pendientes

### 7.1 Resultado por fuente

| Fuente del inventario | Resultado y evidencia de esta consulta | Pendiente / checkpoint |
|---|---|---|
| WATCH-BO | **PARTIAL**. Índices por fecha 15/10 y 16/10: 55 avisos cada uno; 110 cuerpos recuperados. Se reintentaron y recuperaron los 49 cuerpos pendientes de la corrida anterior. Se identificaron 21 archivos anexos para el 15 y 19 para el 16; recuperados dos y uno respectivamente. | 37 archivos anexos identificados pendientes; revisión jurídica integral de otros actos fuera del foco no acreditada. Fechas 15/16 no aparecen en la lista de suplementos anunciados por el índice consultado; no se infiere ausencia universal de archivos. Corte completo sigue nulo. |
| WATCH-BCRA-COM | **COMPLETE sólo para [15/10 00:00, 16/10 00:00)** en el buscador oficial. POST por fechas 15–16, página 1/1, seis registros: A8492, B13248 y C102432–102435; seis PDF, 14 páginas recuperadas/leídas. No aparecen registros del 16 en esa respuesta. | Corte avanza desde 15/10 22:47:13 a 16/10 00:00 −03:00. El tramo global 00:00–00:04 y publicaciones/indexaciones posteriores quedan para solapamiento; no se declara todo el 16 cubierto. |
| WATCH-BCRA-TO | **PARTIAL**. Índice oficial con 103 textos ordenados, revalidado. | Falta recuperar/comparar todo texto y modificatorias pertinentes. Corte nulo. |
| WATCH-BCRA-RI | **PARTIAL**. Faceta oficial con 55 regímenes; t-optico y manual SISCEN consultados. | Otros documentos/anexos, canales y secuencia histórica pendientes. Corte nulo. |
| WATCH-UIF | **PARTIAL**. Índices sectorial y transversal accesibles y reconsultados. | No se acredita recorrido cronológico completo ni todos los textos/anexos. Corte nulo. |
| WATCH-AAIP | **PARTIAL**. Formulario/entrada oficial accesible. | No hay resultados cronológicos y anexos completos acreditados. Corte nulo. |
| WATCH-ARCA | **PARTIAL**. Biblioteca y páginas temáticas; actos administrativos seleccionados en BO. | Portada o formulario no prueban cobertura. Faltan búsqueda cronológica y textos/anexos. Corte nulo. |
| WATCH-COMARB | **UNAVAILABLE**. Sitio y rutas SIRCREB/SIRCUPA devolvieron HTTP 500 en los intentos de esta corrida. | Se conserva el gap previo; no es falla nueva ni exención fiscal. Corte nulo. |
| WATCH-CNV | **PARTIAL**. Marco regulatorio/panel y BO RG1172/1173 reconsultados. | Restantes actos, historia y comparación de anexos pendientes. Corte nulo. |
| WATCH-JURIS, condicional | **NOT_APPLICABLE_WITH_BASIS al relevamiento local**: no se seleccionó operador ni jurisdicciones subnacionales; se conserva el fundamento anterior. | No implica exención del futuro operador ni cobertura provincial/municipal por leer un índice nacional. |
| WATCH-STANDARDS, condicional | **PARTIAL**. FAPI/ASVS y fuentes de seguridad/técnicas consultadas para el alcance solicitado. | Matriz contractual y ediciones completas/restringidas no verificadas; corte nulo. |

El intervalo completo de una fuente es distinto del resultado global y de su última hora de intento. Los índices de TO/RI sin cambio y el KEV estable no prueban ausencia de cambios en fuentes incompletas. Un HTTP 200 acredita recuperación de esos bytes; no necesariamente texto sustantivo, anexos ni aplicabilidad. La recuperación de cuerpos BO mejora un gap conocido; no reescribe las fallas previas ni incrementa artificialmente el corte.

### 7.2 Procedencia durable y deduplicación

La evidencia de esta corrida se guarda separadamente en [`automation/regulatory-state`, manifiesto RUN-20261016T030400Z](https://github.com/andrescastiglia/bank/blob/automation/regulatory-state/.regulatory-watch/evidence/RUN-20261016T030400Z.json), con bitácora y estado en esa misma rama. Las fuentes enlazadas en el informe son primarias; el manifiesto identifica el contenido realmente recuperado. Los cuerpos comerciales, datos de personas de edictos y textos restringidos no se publican en el repositorio.

Los anexos BO se recuperaron mediante el endpoint público `POST /pdf/download_anexo`, cuyos parámetros se identificaron leyendo el script del portal **como datos**, sin ejecutarlo. Se registran sección, número, ID de anexo, fecha, hash de la respuesta JSON y hash del PDF decodificado. Para reproducir la evidencia no basta un enlace genérico al endpoint sin esos parámetros.

Se conserva identidad autoridad/tipo/número/año/jurisdicción. B13247 pasa de candidato con anexo pendiente a texto/anexo verificado; A8492, B13248, RG1172/1173 y los avisos PostgreSQL mantienen sus identidades previas. Fechas dinámicas o HTML distinto sin diferencia sustantiva no generan otra norma. Nuevas evidencias y propuestas se agregan como revisiones vinculadas, preservando las listas históricas y los dos runs anteriores.

| Evidencia seleccionada | SHA-256 de los bytes consultados |
|---|---|
| B13246, PDF BCRA completo | `5ef9de3ecaea789f9ed64a66c6cd8d95fa960fb9f351b407050861a770c49115` |
| B13247, PDF BCRA completo | `78bef969ea3f905c721385cd77c1fab0e4aaa396577a33d2d13c4a611ec307d9` |
| CGN/TGN 2/2026, PDF anexo BO decodificado | `2cae61d6ce6d05de0094c4d29d222d9a2b596f38c2644911ef94d9df31c70a53` |
| Anuncio Rust 1.99.1, HTML | `1b4bcf8f6c0cc680ca6bafda173750d059db641f1d69d23f556b858a14461db1` |
| Manifiesto estable de Rust, TOML | `fb152be80975c194aa5fc684b2aec3a6e14e2b855efe2faa4e5f8ae6e590f463` |

Las huellas son identificadores de evidencia, no firmas de autenticidad ni certificados jurídicos. Una URL viva puede cambiar después de esta consulta.

### 7.3 Comprobaciones y límites

Las comprobaciones documentales verifican catálogo/hashes, referencias/skills, inventario de vigilancia y regresiones de cobertura/continuidad; no prueban lectura jurídica suficiente ni producto bancario. La transición de esta corrida debe conservar como prefijos exactos `changes`, `agenda` y `run_index`, indexar una sola vez su ID y no avanzar fuentes incompletas. La propuesta no contiene nuevas bitácoras operativas destinadas a `main`.

No se ejecutaron aplicaciones bancarias, migración con fondos, builds Rust, escaneos de dependencias/imágenes, pruebas de intrusión ni de recuperación. No hay base para declarar una vulnerabilidad explotada, un control operativo eficaz, una certificación ni un SLA cumplido. Las protecciones de `main` siguen con la limitación de verificación documentada en [GOVERNANCE.md](GOVERNANCE.md); esta investigación no cambia permisos ni las verifica por ensayo destructivo.

## 8. Observaciones finales derivadas de los datos

1. Seleccionar perfil y primer recorrido para poder convertir fuentes y FR genéricos en un paquete con oráculos. Mantener PSAV, CUT y jurisdicciones como alcances condicionados hasta esa decisión.
2. Evaluar Rust 1.99.1 al fijar el primer toolchain y exigir evidencia por target, dependencias nativas, TLS y apagado en scratch. Conservar reproducibilidad y una política de actualización; no adoptar una versión sólo por ser la última observada.
3. Demostrar un flujo financiero pequeño, incluida carga inicial/conciliación y salida, con permisos y estados externos ambiguos. Es la evidencia que conecta arquitectura, valor comercial y calidad.
4. Retomar los 37 anexos BO y los gaps oficiales preservados. La vigilancia permanece parcial aunque haya hallazgos válidos; no declarar «sin novedades» global ni duplicar alertas sin variación material.

Las decisiones, prioridades y merges corresponden al mantenedor. La aplicación jurídica y la aceptación operativa corresponden al sujeto y funciones competentes; este informe aporta evidencia y preguntas concretas para esas decisiones.
