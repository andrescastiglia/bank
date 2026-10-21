# Requisitos legales, regulatorios e impositivos para crear un banco en Argentina

**Fecha de investigación:** 16 de octubre de 2026, zona `America/Buenos_Aires`. **Base del proyecto:** `979dd2c8f48e13d17343965d2e7194ec79ca0ed2`. **Caso principal:** banco comercial privado de primer grado constituido desde cero en Argentina como sociedad anónima. Se distinguen cooperativas, sucursales extranjeras, bancos públicos y adquisiciones cuando cambia el régimen.

## 1. Resultado y alcance

Crear un banco exige coordinar **autorización del BCRA, constitución e inscripción societaria, integración patrimonial y habilitación para iniciar actividades**. Una sociedad inscripta, una CUIT, un core disponible o un registro como PSP no sustituyen esos actos. La evaluación incluye promotores, propietarios, autoridades, viabilidad, capital, gobierno, riesgos, prevención de delitos, sistemas, seguridad, contabilidad e información.

El adjunto se utilizó como hipótesis de trabajo y se contrastó con textos oficiales. Las correcciones de mayor impacto son:

- El piso básico consultado para bancos es **ARS 5.000 millones**, pero la necesidad real depende de riesgos, calidad del capital, pérdidas iniciales y condiciones de autorización.
- Además del arancel de evaluación de **10.000 UVA**, existe un canon de habilitación de **80.000 UVA** para bancos. No son aportes al capital.
- La nueva sociedad presenta inicialmente un proyecto; el régimen BCRA prevé su constitución después de la autorización. No exige que el banco futuro ya esté inscripto para comenzar todo el expediente.
- No se verificó una prórroga general automática de un año adicional para abrir ni una caución BCRA universal de alta para todos los directores.
- El IVA reducido no corresponde genéricamente a consumidores finales. La base de IIBB tampoco se deduce de una fórmula nacional de “spread”: el Convenio Multilateral distribuye, mientras los códigos fiscales definen bases y deducciones.
- Hay normas de 2026 posteriores a algunos textos ordenados: entre otras, A 8490 sobre inversiones FAL y capital, facturación bancaria RG 5866, CRS RG 5887 y transición laboral FAL RG 5907.

El relevamiento cubre las familias de requisitos de creación y apertura, y su continuidad operativa. **No constituye una solicitud real ni acredita autorización, implementación o cumplimiento.** Las cifras son referencias fechadas; no parámetros productivos permanentes. Faltan datos del caso para cerrar aplicabilidad: accionistas y control, domicilio, locales, provincias de actividad, productos, monedas, canales, cartera, personal, proveedores y fecha de apertura.

Se profundiza el régimen nacional y se verifican ejemplos fiscales de **CABA y provincia de Buenos Aires**. El inventario territorial posterior contempla las 24 jurisdicciones; no atribuye a las restantes una revisión de todas sus leyes anuales. La revisión de normas y cambios es amplia pero selectiva, con límites expresos en la sección de fuentes; no certifica exhaustividad universal ni anticipa la decisión del regulador.

## 2. Marco jurídico y decisiones que deben preceder al expediente

### 2.1 Autorización, clase y operaciones

La [Ley 21.526, texto actualizado](https://www.argentina.gob.ar/normativa/nacional/ley-21526-16071/actualizacion), arts. 1–4 y 7–9, regula la intermediación habitual y exige autorización previa. El BCRA evalúa conveniencia, características del proyecto, mercado, antecedentes, responsabilidad y experiencia de los solicitantes; no es una inscripción automática por aportar un monto.

La competencia del Directorio para autorizar se encuentra en la [Carta Orgánica, art. 14 inc. ñ](https://www.argentina.gob.ar/normativa/nacional/ley-20539-66194/actualizacion). La SEFyC realiza la supervisión y las funciones asignadas por sus arts. 43–49. No debe confundirse la tramitación ante la Superintendencia con una licencia concedida por un proveedor, registro societario o organismo fiscal.

| Decisión | Requisito y consecuencia |
|---|---|
| Clase de entidad | Distinguir bancos comerciales, de inversión e hipotecarios de las otras clases del art. 2 LEF. Su perímetro de operaciones difiere. El art. 21 permite al banco comercial las operaciones activas, pasivas y de servicios no prohibidas, bajo reglamentación BCRA. |
| Primer o segundo grado | El segundo grado tiene restricciones específicas de captación y relaciones con otras entidades. El modelo minorista del documento corresponde a primer grado; no reutilizarlo sin ajustar esa definición. |
| Canal digital | Operar principalmente por aplicación no crea una licencia bancaria autónoma ni exime del gobierno, capital, sistemas, atención o seguridad aplicables. Debe definirse qué instalaciones y funciones se tercerizan. |
| Actividades complementarias | Mercado de capitales, cambios, seguros, fideicomisos, custodia, tarjetas y determinados servicios de pago pueden añadir registros, autorizaciones o contratos. La licencia bancaria no demuestra automáticamente aptitud para todos ellos. |
| Denominación y captación | LEF art. 19 reserva denominaciones y regula el uso de expresiones propias de entidades. No publicitar depósitos u operaciones como banco autorizado durante la organización. |
| Responsabilidad | La persona jurídica bancaria responde por su operación aun si contrata el core, nube, procesador, agencia o prestador de prevención. El contrato no traslada al proveedor la autorización institucional. |

La entidad proveedora de software del repositorio y el banco que eventualmente lo opere son sujetos distintos. La licencia **GNU GPL v2** no permite captar fondos ni impone por sí misma obligaciones tributarias idénticas al operador y al contribuyente que presta tecnología.

### 2.2 Forma jurídica y registro

El artículo correcto para forma jurídica es el **9 de la LEF**:

| Alternativa | Encaje y documentación diferencial |
|---|---|
| Banco privado argentino S.A. | Regla de base; acciones con derecho a voto nominativas, instrumento constitutivo público, estatuto, capital, administración, fiscalización, domicilio y libros. Aplicar [Ley General de Sociedades 19.550](https://www.argentina.gob.ar/normativa/nacional/ley-19550-25553/actualizacion) y régimen bancario especial. Una SAS o SRL no es sustituto ordinario de la S.A. bancaria. |
| Banco comercial cooperativo | Admitido por LEF art. 9; Ley 20.337, INAES y régimen bancario. Revisar miembros, aportes, gobierno, retornos y fiscalidad propios; no trasladar automáticamente Ganancias y dividendos de una S.A. |
| Caja de crédito cooperativa | Categoría distinta, con régimen específico; no equivale a un banco comercial cooperativo ni hereda toda su operatoria. |
| Sucursal de banco extranjero | Autorización BCRA, representación/poderes suficientes, inscripción bajo LGS art. 118 y capital radicado efectiva y permanentemente en Argentina; LEF art. 13. No constituye una S.A. argentina por analogía. |
| Banco argentino con accionista extranjero | Sociedad local más requisitos del accionista extranjero, incluida inscripción LGS art. 123 cuando corresponde, control, beneficiarios finales y origen de fondos. No es lo mismo que una sucursal. |
| Banco público o mixto | Carta orgánica y competencia del ente creador, más autorización y regulación financiera; su gobierno y tratamiento fiscal pueden diferir. No presumir exención por participación estatal. |

El mínimo general de capital de una S.A. del art. 186 LGS consultado es **ARS 30 millones**, actualizado por Decreto 209/2024. Es una referencia societaria general: **no sustituye el piso especial bancario ni la RPC**. La integración, clases de acciones y derechos del proyecto deben satisfacer el régimen sectorial y la resolución particular del BCRA.

La IGJ actúa en CABA; en otras provincias interviene la autoridad registral local. Las facultades societarias se ejercen con la delimitación del art. 6 LEF. Prever reserva de denominación, publicación, inscripción, sede, autoridades, garantías societarias, libros/registros y registraciones de aportantes extranjeros. Para S.A. sujetas a fiscalización estatal permanente, revisar LGS arts. 255, 284 y 299, además de las reglas BCRA.

**Actualización IGJ relevante:** no utilizar como instrucción actual una guía que todavía remita íntegramente a RG 7/2015. La base RG 15/2024 tiene modificaciones posteriores, incluida [RG IGJ 11/2026, BO 22/9/2026](https://www.boletinoficial.gov.ar/detalleAviso/primera/347799/20260922): su art. 2 dispensa el dictamen de precalificación en los supuestos de constitución previstos y su art. 8 admite medios de acreditación de integración. Debe verificarse el supuesto concreto y su compatibilidad con el aporte efectivo exigido por BCRA; no convertir una simplificación registral en exención prudencial.

La [RG IGJ 15/2024 actualizada](https://www.argentina.gob.ar/normativa/nacional/resoluci%C3%B3n-15-2024-401548/actualizacion), art. 421, exige declaración de beneficiario final en los trámites enumerados; para sucursales extranjeras, también en el contexto de estados contables del art. 175. Es una obligación registral propia, adicional a la identificación BCRA/UIF/ARCA. La vigencia de IGJ 11/2026 comienza el 23/9/2026 conforme su art. 13.

## 3. Expediente de autorización ante BCRA

Fuentes principales: [TO Autorización y composición del capital](https://www.bcra.gob.ar/archivos/Pdfs/texord/t-ayccef.pdf), al 15/5/2025, A 8242, especialmente secciones 2, 5, 6 y 7; y [ficha oficial del trámite](https://www.bcra.gob.ar/solicitar-autorizacion-para-operar-como-entidad-financiera/). La fecha del TO es la de consolidación; el procedimiento y las normas deben revalidarse al presentar.

### 3.1 Promotores, propietarios y procedencia de fondos

| Carpeta | Requisitos a preparar / evidencia |
|---|---|
| Identidad del proyecto | Clase, denominación, ubicación, domicilio especial, proyecto de acta/estatuto, capital inicial y composición con nacionalidad, domicilios, derechos de voto y participaciones directas/indirectas. |
| Personas humanas | Antecedentes/FAP mediante APAEF; declaraciones de inhabilidades, sanciones, condición PEP y demás extremos solicitados; certificados penales; manifestación de bienes con fecha requerida y certificación profesional independiente. |
| Solvencia y liquidez | Acreditar propiedad, origen y disponibilidad de los fondos, capacidad de integración y responsabilidades futuras. Un activo ilíquido o financiamiento comprometido por un tercero no acredita por sí solo aporte admisible. |
| Información fiscal del aportante | TO 6.3.1 pide declaraciones y comprobantes de Ganancias/Bienes Personales de los últimos tres años, o declaración fundada de no estar alcanzado, según sujeto y supuesto. **Es documentación del expediente del promotor**, distinta de la prohibición de requerir DDJJ impositivas al cliente para formar su perfil UIF. |
| Personas jurídicas aportantes | Estatuto y constancias registrales, autoridades/propietarios, últimos dos ejercicios con estados auditados y memorias, asistencia a asambleas, certificación de disponibilidades/aportes y demás documentación de TO 6.3.2. Reconstruir cadena de control y beneficiario final. |
| Documentos extranjeros | Documentación del país de origen, poderes, legalización/apostilla y traducción pública cuando procedan; informes del supervisor de origen y régimen de supervisión consolidada para sucursales/controlantes comprendidos. |
| Formalidades | Certificados de antecedentes penales argentinos emitidos dentro de los **cinco días hábiles previos** a presentación; certificado del lugar de residencia exterior cuando corresponda; firmas/certificaciones profesionales y copias según TO 6.4. |
| Vinculadas | Información de vinculadas de propietarios y autoridades, incluyendo los supuestos de participación de 5% o más de TO 7.1, aun si no operan con el banco. |

El **5% no es una franquicia de anonimato**: el TO exige información de cada accionista de la nueva entidad y utiliza umbrales diferentes para restricciones, vinculadas y control. Promotores/fundadores que representen al menos **25% del capital y votos** deben acreditar la idoneidad/experiencia de TO 2.3.3; no confundirlo con el 25% de integración inicial del capital.

La revisión de elegibilidad comprende LEF art. 10 y LGS arts. 264/286, antecedentes y sanciones, listas aplicables y restricciones específicas del TO. Entre estas últimas se encuentran las relativas a juego/apuestas y concentración de ingresos gubernamentales. Debe contrastarse cada causal y su duración: **una multa histórica UIF/BCRA no equivale siempre a inhabilitación automática y perpetua**.

En particular, TO 2.3.2 alcanza actividades/participaciones de juego y apuestas de promotores/fundadores y titulares del 5% o más, y contempla concentración superior al 75% de ingresos gubernamentales en los sujetos y cómputos allí definidos. Registrar actividades y relaciones directas/indirectas; no sustituir ese análisis por un certificado penal limpio.

### 3.2 Proyecto económico e institucional

TO 2.4 exige, entre otros elementos:

1. Estudio de factibilidad y plan de negocios con proyecciones de **cinco años**, supuestos, capital, liquidez, riesgos, costos y evaluación profesional independiente en el alcance requerido.
2. Organización, funciones, circuitos, dotación, autoridades, gastos de constitución e instalación y capacidad administrativa.
3. Proyecto de contabilidad, información y controles; criterios prudenciales y de valuación, reportes y acceso supervisor.
4. Proyecto de prevención LA/FT/FP y sistemas informáticos, conforme la ficha oficial y las normas por materia.
5. Locales, modalidades de atención, seguridad, proveedores, dependencias y servicios a habilitar.
6. Mecanismos para demostrar que el modelo sigue siendo solvente ante pérdidas iniciales, retiros de depósitos, deterioro de cartera, fraude, incidentes y costos impositivos.

La documentación se carga por el procedimiento digital indicado; el análisis preliminar puede generar complementos. La presentación formal se instrumenta mediante nota y los canales oficiales vigentes. Deben conservarse originales y la declaración de fidelidad/disponibilidad de copias conforme TO 6.4.5. Este documento no realiza cargas ni envíos.

Una intimación a subsanar dentro de **30 días corridos**, prevista en TO 6.1, no es un plazo de aprobación del BCRA. Tampoco se verificó un plazo universal de respuesta favorable ni un mecanismo general de silencio positivo que permita abrir sin resolución.

## 4. Gobierno, autoridades y funciones de control

Aplicar [TO Autoridades](https://www.bcra.gob.ar/archivos/Pdfs/texord/t-autenf.pdf), al 30/12/2025, A 8383; [gobierno societario](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-lingob.pdf); gestión de riesgos; auditoría y legislación societaria.

| Objeto | Requisito / alcance |
|---|---|
| Directorio | Idoneidad, integridad, conocimientos y experiencia. TO 2.2.1 requiere experiencia destacada financiera de al menos dos tercios, y al menos 25% con experiencia en entidades financieras cuando no tenga calificación 1/2/3 o no esté calificada, con el cómputo/redondeo reglado. Aplicar también reglas de asistencia, no sólo contar CV. |
| Nueva entidad | Grupo de gobierno **B** mientras no exista información suficiente para la clasificación A/B. No confundir estos grupos con los grupos prudenciales 1/2 de capital. |
| Funciones ejecutivas | Separación según grupo y régimen; para entidades públicas rige el tratamiento específico. Una excepción de proporcionalidad no elimina conflictos de interés ni segregación operativa exigida por otras normas. |
| Gerencias y sucursal extranjera | Evaluación de idoneidad y antecedentes de gerencia general y cargos comprendidos; reglas específicas para la máxima autoridad de la sucursal. Registrar designación, autorización/certificación, renovación y cese según supuesto. |
| Domicilio | LGS 256 exige domicilio real en Argentina de la mayoría de directores; revisar poderes, residencia y representación efectiva. Las funciones responsables TI/SI deben ejecutarse en Argentina según su régimen. |
| Órganos y comités | Fiscalización societaria, auditoría interna/externa, riesgos, control de vinculadas, remuneraciones e integridad; determinar composición, independencia, funciones y proporcionalidad exigibles. No inventar un comité idéntico para todos los grupos. |
| Responsables especializados | Oficial de cumplimiento UIF titular/suplente; responsables TI y seguridad de la información; responsable de seguridad física titular/suplente; responsables de atención a usuarios y otras funciones aplicables. Son roles distintos aunque puedan existir compatibilidades reguladas. |

**Dos garantías diferentes:** LGS 256 y el régimen registral determinan la garantía societaria de directores. La garantía BCRA **de desempeño** de la sección 5 del TO Autoridades puede exigirse por decisión del Superintendente ante una presunta infracción susceptible de multa. No es una caución de apertura universal para cada director. Sus sujetos, monto y medios dependen del procedimiento y decisión correspondientes.

El banco debe mantener evaluación de propietarios y autoridades durante su vida, informar cambios y observar reglas sobre composición/control. La aprobación inicial no permite cambiar al controlante o incorporar actividades incompatibles sin el análisis y trámite exigibles.

## 5. Capital, solvencia, liquidez y garantía de depósitos

### 5.1 Piso y capital por riesgos

El [TO Capitales mínimos](https://www.bcra.gob.ar/archivos/Pdfs/texord/t-capmin.pdf), al 11/9/2026, A 8479, sección 1, establece para **bancos** una exigencia básica de **ARS 5.000 millones**. La tabla consultada no depende de una “categoría impositiva” del banco ni de una clasificación geográfica como plantea el adjunto.

La exigencia total se obtiene comparando ese piso con la suma de exigencias por **crédito, incluido contraparte, mercado y operacional**, según las carteras y reglas vigentes. La RPC debe satisfacer el mayor valor y las condiciones adicionales aplicables. No basta depositar el piso y consumirlo inmediatamente en gastos o activos deducibles.

| Elemento | Tratamiento que debe presupuestarse |
|---|---|
| Riesgo de crédito | TO 2: ponderadores, contrapartes, garantías, exposiciones fuera de balance y excesos. La fórmula incorpora factor `k`; para entidad sin calificación comunicada el texto consultado fija `1,03`, no un `k=1` universal. |
| Riesgo de mercado | Cartera de negociación, posiciones y periodicidad correspondientes. Validar instrumentos y metodologías de las secciones específicas. |
| Operacional de una entidad nueva | TO 7.4: primer mes, **10%** de la suma de la exigencia de crédito del mes y la exigencia de mercado para las posiciones del último día; meses 2–36, 10% del promedio de las exigencias computables transcurridas, en moneda homogénea. Desde el mes 37 aplica la metodología de su grupo. |
| Operacional después del arranque | Grupo prudencial 1: metodología de indicador de negocios y multiplicador según TO 7.1. Grupo 2: indicador básico del 15% de ingresos definidos normativamente, con exclusiones, moneda homogénea y topes de TO 7.2/7.3. El 15% no fue eliminado de todo supuesto, pero es incorrecto imponerlo a todo banco nuevo. |
| RPC y calidad | `RPC = PNb + PNc`, computados con deducciones y límites por nivel. No equivale al patrimonio contable; no restar dos veces deducciones ya incluidas. Software/intangibles, activos fiscales y participaciones requieren tratamiento particular. |
| Ratios mínimos | TO 8.5: capital ordinario nivel 1 neto ≥4,5% APR, patrimonio básico ≥6%, RPC ≥8%, usando las definiciones regulatorias de APR. No aplicar sólo el 8% sobre saldo de préstamos ni duplicar el uso de un mismo capital en varios márgenes. |
| Conservación y otros márgenes | [Distribución de resultados](https://www.bcra.gob.ar/archivos/Pdfs/texord/t-disres.pdf), sección 4: conservación 2,5% APR, ampliada a 3,5% para sistémicas en el supuesto previsto, integrada con COn1 neto; contracíclico y otros requerimientos dependen de exposiciones y decisiones. Entrar en el rango de conservación limita distribuciones y exige recomposición: no equivale por sí solo a cierre automático. |

**Actualización posterior al TO:** [A 8490, emitida 8/10/2026 y publicada 14/10](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8490.pdf), permite titularidad de cuotapartes FCI FAL y regula también certificados de participación de fideicomisos FAL; **deduce el saldo de las inversiones comprendidas de COn1** y excluye de lo distribuible los resultados definidos en esa comunicación. Afecta el caso que realice esas inversiones aunque todavía no figure en la portada de los TO descargados; no cambia el piso de ARS 5.000 millones. No se le atribuye la vigencia de noviembre de otras reglas FAL por analogía.

### 5.2 Liquidez, encajes y reserva legal

La [LEF, arts. 30–33](https://www.argentina.gob.ar/normativa/nacional/ley-21526-16071/actualizacion), y los TO de efectivo mínimo, riesgos y capital imponen obligaciones diferentes:

- **Efectivo mínimo:** base, moneda, plazo, grupo, período e integración admitida según [TO específico](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-efemin.pdf) y comunicaciones posteriores. No existe un único encaje aplicable a todo pasivo ni toda integración es necesariamente un depósito no remunerado.
- **LCR/NSFR:** determinar primero si la entidad queda alcanzada. [A 8445/2026](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8445.pdf) delimita el régimen para D-SIB y sucursales/subsidiarias G-SIB; hojas vigentes desde 5/6/2026 y tratamiento para nuevos sujetos alcanzados desde 1/10/2026. No imponer sin encuadre el mismo ratio a cualquier banco nuevo.
- **Reserva legal:** art. 33 LEF fija banda del 10% al 20% de utilidades, concretada por regulación BCRA; no reemplazarla por el 5% general societario ni confundir apropiación de resultados con encaje o impuesto. Antes de liquidar o distribuir, cerrar la norma contable aplicable y su cadena vigente; una comunicación histórica o un balance de otro banco no la acreditan por sí solos.
- **Distribuciones:** cumplir resultados distribuibles, restricciones, deducciones, liquidez, capital, márgenes y comunicaciones particulares antes de dividendos/remesas. No toda utilidad contable es distribuible o fiscalmente disponible.

### 5.3 Sistema de garantía de depósitos

[Ley 24.485](https://www.argentina.gob.ar/normativa/nacional/ley-24485-16877/actualizacion), [Decreto 540/1995](https://www.argentina.gob.ar/normativa/nacional/decreto-540-1995-16879/actualizacion) y [TO Seguro de garantía](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-seggar.pdf), al 5/3/2026, A 8407:

| Aspecto | Regla / trabajo de implementación |
|---|---|
| Aportes | Normal mensual **0,015%** del promedio mensual de saldos diarios de partidas comprendidas, con período de referencia del TO, más aporte adicional por riesgo cuando corresponda. Considerar metodología de entidad sin CAMELS, integración e información; no confundirlo con un impuesto, capital inicial o suma única de licencia. |
| Cobertura | Desde **1/4/2026**, límite consultado **ARS 50 millones**, con reglas por persona, acumulación, cotitulares, intereses, actualizaciones y conversión. No presentar cobertura ilimitada por cuenta o por marca. |
| Exclusiones | Tipos de depósitos y sujetos, vinculados, títulos adquiridos por endoso, depósitos entre entidades y límites de tasa/incentivos, entre otros supuestos del TO 5.2. Deben parametrizarse; no todo depósito captado está garantizado. |
| Operación y documentación | Incorporación al circuito institucional, aportes y reportes, contratos/leyendas y atención de consultas; conciliación de saldos y versiones. La cobertura no alcanza a una cuenta de pago sólo por usar el mismo software. |

## 6. Aranceles y cronograma desde la autorización

Los hitos siguientes provienen del TO Autorización, especialmente 2.5, 2.7–2.10. Son **plazos del solicitante**, no promesas sobre cuánto tarda el BCRA en resolver.

| Momento / hito | Exigencia verificada | Evidencia a conservar |
|---|---|---|
| Solicitud | Arancel de evaluación **10.000 UVA**, pagadero en pesos al valor oficial de fecha de pago. No se verificó en la fuente citada una regla general de reembolso: no afirmar devolución ni no devolución sin base adicional. | Liquidación, valor UVA, comprobante y vinculación al expediente. |
| Resolución favorable | Canon de habilitación para bancos **80.000 UVA**, en pesos al valor de la fecha de pago. | Resolución, cumplimiento de condiciones y pago. |
| Hasta 30 días corridos desde autorización | Acto constitutivo de la nueva sociedad, TO 2.9.1. | Escritura/acta, suscripción y autoridades. |
| Acto y hasta 60 días corridos desde autorización | Suscripción total; integración inicial en efectivo no inferior al 25% por accionista; resto en los 60 días corridos previstos. La totalidad del capital mínimo debe estar integrada **en efectivo** antes de iniciar. | Extractos, trazabilidad, registros societarios y cómputo RPC. |
| Al menos 30 días antes del inicio previsto | Cumplir las condiciones previas de TO 2.9.3, incluida inscripción y requisitos institucionales/operativos. | Carpeta completa, constancias registrales y comunicaciones. |
| Organización | Aplicaciones preparatorias admitidas por TO 2.9.4; balances trimestrales y reseñas del período en los términos de TO 2.9.3.5. | Contabilidad preoperativa y reportes. |
| Antes de abrir | Informar a SEFyC el cumplimiento para su pronunciamiento conforme TO 2.9.5; obtener constancia de habilitación y completar integraciones adicionales. | Pronunciamiento y condiciones efectivamente satisfechas. |
| Dentro de un año desde fecha de autorización | Habilitar/iniciar en el término de TO 2.8.2; el incumplimiento tiene las consecuencias de ese punto y TO 2.10. | Calendario de expediente y decisiones expresas. No se presume prórroga general por otro año. |

No resumir todo incumplimiento de integración como una “revocación automática al día 60” sin aplicar la norma y el acto concreto. La apertura debe coordinar el plazo anual con los avisos previos de canales, tercerización, locales y otros servicios; no programarlos después del comienzo de actividad.

## 7. Condiciones institucionales para estar en condiciones de abrir

### 7.1 Prevención de LA/FT/FP

Un banco es sujeto obligado bajo la [Ley 25.246 actualizada](https://www.argentina.gob.ar/normativa/nacional/ley-25246-62977/actualizacion), con las reformas de Ley 27.739 y régimen sectorial [UIF 14/2023 actualizado](https://www.argentina.gob.ar/normativa/nacional/resoluci%C3%B3n-14-2023-379085/actualizacion). Incluir modificaciones como UIF 199/2024 y [UIF 78/2025](https://www.argentina.gob.ar/normativa/nacional/norma-413643/texto), y resoluciones transversales aplicables.

La carpeta de apertura debe incluir registro del sujeto y responsables, designaciones de oficial titular/suplente, sistema preventivo aprobado, autoevaluación y matriz de riesgos, tolerancia, manual, formación, auditoría/revisión independiente, debida diligencia, beneficiarios finales, PEP, sanciones/listas, corresponsalía y monitoreo por productos/canales. Definir actualización de legajos, alertas, análisis, reportes sistemáticos, ROS/FT/FP, reserva y conservación con sus plazos específicos.

El **Comité de Prevención de LA/FT/FP** del art. 14 UIF 14/2023 actualizado integra el gobierno del banco; la excepción de ese artículo para determinadas entidades cambiarias no se traslada a una entidad LEF. Establecer composición, funciones, actas y relación con oficial de cumplimiento y Directorio.

**Perfil del cliente:** la modificación del art. 37 por UIF 78/2025 prohíbe requerir DDJJ impositivas para conformarlo. Se debe reunir información admisible según riesgo y norma, sin sustituirla por una exigencia tributaria prohibida. Ello no elimina la documentación fiscal de promotores requerida por el BCRA en otro expediente y con otra finalidad.

No fijar en este estudio todos los umbrales en pesos ni un plazo único para todos los reportes. Parametrizar norma, edición, unidad de referencia, fecha y disparador; proteger los casos reservados y sus acuses. Tener un motor de alertas no acredita un sistema preventivo institucional eficaz.

### 7.2 Tecnología, tercerización y seguridad

| Frente | Requisitos y fuente | Evidencia previa / continuidad |
|---|---|---|
| TI y SI | [TO Requisitos mínimos TI/SI](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-rmgcti.pdf), al 13/2/2026, A 8401: gobierno, riesgos, datos, software, activos, IAM, continuidad, incidentes y terceros. Funciones responsables de TI/SI en Argentina, punto 2.1.3. | Designaciones, inventarios, políticas, riesgos, diseño y pruebas, accesos, trazabilidad, restauración y auditorías. |
| Servicios digitales | [TO SFD](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-rmrtsd.pdf), A 7783: evaluación, autenticación por acción/riesgo, dispositivos, fraude, monitoreo y comunicación de nuevos servicios. | Aviso de nuevos productos/tipos de servicio al menos **60 días antes** de producción conforme alcance; no es el mismo aviso que tercerización. |
| Terceros críticos TI/SI | TO TI/SI 10: notificación al menos **60 días corridos** antes del inicio, expediente, contrato, países/localidades, subcontratistas, auditoría, continuidad y salida. | La notificación no se describe como aprobación tácita ni permiso universal de un proveedor o nube. Mantener responsabilidad y acceso supervisor. |
| Tercerización de actividades | [TO Expansión](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-expaef.pdf), actualizado **29/9/2026, A 8486**; sección 2 conserva reglas de comunicación y condiciones; atención al público tiene régimen específico. | Originales/documentación enumerados en 2.2.6 deben mantenerse en Argentina; determinar equivalencia de soporte digital y custodia, además de privacidad y transferencias internacionales. |
| Fraude | [A 8471](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8471.pdf), gobierno/riesgos para EF desde **1/12/2026**; [A 8473](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8473.pdf), controles de transferencias y score. | Para EF, A 8473 fija plazos de 60/90 días desde entrega de documentación técnica por el administrador para los acápites correspondientes. Registrar la recepción real; no inventar una fecha única. |
| Ciberincidentes | [TO RRCI](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-rrci.pdf), sección 3: notificación inicial dentro de la primera hora de ocurrido/detectado, actualizaciones y cierre en plazo regulado. | Guardia, responsables, canal alternativo, reloj y registro de comunicaciones. Diferenciar guía de buenas prácticas de sección 2 de obligación de notificar de sección 3. |
| Seguridad física | Ley 26.637 y [TO Seguridad](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-seguef.pdf), al 15/5/2025, A 8241. Exigencias por local, numerario, custodia y modalidad. | Responsable titular/suplente, legajos/informes, seguridad jurisdiccional, dispositivos, vigilancia, transporte/custodia según supuesto. No exigir por copia el mismo tesoro/blindaje a toda modalidad sin efectivo. |

La normativa exige resultados, gobierno y evidencia; no impone Rust, Kubernetes ni `FROM scratch` como condición de licencia. Esas son decisiones vigentes del proyecto. ISO, PCI, Swift y otros programas requieren matriz de aplicabilidad por servicio/red/contrato; no son todos leyes argentinas ni certificados que habilitan un banco.

### 7.3 Contabilidad, reportes, usuarios y datos

| Materia | Requisito y trabajo necesario |
|---|---|
| Contabilidad bancaria | LEF 36/37; marco contable BCRA/NIIF con excepciones/transiciones, plan de cuentas, moneda homogénea, valuación, clasificación de deudores/previsiones, cierres y auditoría. Reconciliar auxiliares, mayor y regímenes informativos. |
| Auditoría y control | [Normas de auditorías externas EF](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-nmaeef.pdf), controles internos y registro/idoneidad de profesionales aplicables. Contratar y obtener informes del alcance exigido; un scan técnico no sustituye auditoría contable o de sistemas. |
| Información prudencial | Capital, liquidez, efectivo mínimo, deudores, depósitos, vinculados, resultados, transparencia, instituciones/locales y demás RI del perfil. [A 8480](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8480.pdf) y [A 8492](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8492.pdf) muestran cambios de diseños/validaciones; esta última rige desde 1/11/2026. |
| Usuarios | [TO PUSF](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-pusf.pdf), Ley 24.240 y CCyC 1378–1389: responsables, atención/reclamos, transparencia, contratos, costos/CFT, publicidad, resúmenes, bajas, accesibilidad y protección frente a cláusulas/cargos no válidos. |
| Documentos | CCyC 320–331, Ley 25.506 y [TO conservación](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-consyr.pdf): libros, instrumentos, firma, prueba y archivo. Diferenciar firma electrónica/digital y soporte; un click no obtiene automáticamente presunciones de firma digital. |
| Secreto bancario | LEF 39/40: reserva y excepciones según operación, destinatario y fundamento. Instrumentar requerimientos judiciales/fiscales, reportes legales, accesos y exportación sin un permiso genérico de divulgación. |
| Datos personales | [Ley 25.326](https://www.argentina.gob.ar/normativa/nacional/64790/actualizacion), reglamentación y [obligaciones AAIP](https://www.argentina.gob.ar/aaip/datospersonales/responsables/obligaciones): bases comprendidas/registro, información, legitimación, derechos, seguridad, proveedores y transferencias internacionales. Marketing/No Llame tiene obligaciones propias. |
| Relaciones laborales | Alta empleador/trabajadores, seguridad social, ART, seguros obligatorios y salud/seguridad laboral; revisar encuadre convencional bancario, categorías, jornada, remuneraciones y homologaciones vigentes. No presupuestar sólo salario neto ni copiar una escala salarial histórica. |
| Presencia territorial | Habilitación/uso de inmueble, seguridad contra incendios, accesibilidad, cartelería y tasas/servicios municipales según local. La autorización BCRA no sustituye permisos locales ni prueba que toda tasa sea jurídicamente exigible. |
| Servicios adicionales | CNV/mercado/FCI, SSN/seguros, cambios, redes/pagos/tarjetas, transferencias, cheques/ECHEQ y actividades complementarias: seleccionar rol, registro, contratos, pruebas y régimen sectorial. No activarlos todos por defecto. |

## 8. Obligaciones fiscales: separación de roles y momentos

El banco puede ser simultáneamente **contribuyente por su renta/servicios/patrimonio, empleador, agente de recaudación y sujeto informante**. Cada rol requiere alta, base, período, retención, reporte y pago propios. El impuesto recaudado al cliente no es automáticamente costo propio ni ingreso del banco.

| Etapa | Obligaciones que deben resolverse |
|---|---|
| Preparación | Domicilio y jurisdicciones, CUIT/identidad fiscal, representantes y Clave Fiscal, Domicilio Fiscal Electrónico, actividad/nomencladores y encuadre. Costos/aranceles, aportes y contratos preoperativos con documentación válida. |
| Constitución | Inscripciones registrales y fiscales, capital y accionistas/beneficiarios finales; analizar sellos/exenciones, tributos y tasas de actos concretos. Una cuenta de integración no habilita captación del público. |
| Preapertura | Altas de impuestos y regímenes, puntos de venta/comprobantes, empleador/ART, retenciones, registros de cuentas y condición fiscal de clientes/proveedores; calendarios y pruebas de presentación. |
| Operación | Determinativas e informativas; conciliación fiscal-contable, pagos y acuses, agentes, padrones y exclusiones, percepciones, créditos fiscales y retenciones sufridas. Mantener historia y rectificaciones. |
| Distribución/cambios | Ganancias/dividendos/remesas, beneficiario exterior, precios de transferencia, operaciones de cambio, propiedad/control y retenciones. Incorporar requisitos BCRA previos al pago. |

La autorización bancaria no otorga exención impositiva general. Los números de impuesto, vencimientos, montos y aplicativos se verifican para el sujeto/período; no se infieren de una guía antigua que use AFIP en vez de ARCA.

## 9. Impuestos nacionales del banco

### 9.1 Altas y organización fiscal

Preparar CUIT de persona jurídica, domicilio legal/fiscal, Domicilio Fiscal Electrónico, administrador de relaciones, poderes, ejercicio, actividades y establecimientos. La [solicitud oficial de CUIT](https://www.arca.gob.ar/inscripcion/cuit-cdi/solicitud-cuit.asp) utiliza el servicio de inscripción/modificación de personas jurídicas y la documentación exigible por el canal. Un trámite parcialmente digital puede requerir certificaciones o requerimientos adicionales; no se presume asignación automática.

Dar de alta Ganancias, IVA, empleador y los roles de agente/informante que correspondan; altas locales/CM por separado. Asignar responsables y suplencias para DFE, declaraciones, certificados, VEP, pagos, acuses y rectificativas. No tener todavía préstamos o utilidades no elimina por sí solo obligaciones formales o declaraciones sin actividad de regímenes activos.

Los gastos de organización tienen opción de tratamiento en el primer ejercicio o amortización hasta cinco años bajo LIG 91c. Diferenciarlo de software, inversiones, aporte de capital, crédito fiscal y tratamiento prudencial de intangibles. Pagar un gasto no garantiza su deducibilidad inmediata ni su cómputo como capital regulatorio.

### 9.2 Impuesto a las Ganancias

Fuentes: [LIG, texto ordenado Decreto 824/2019 actualizado](https://www.argentina.gob.ar/normativa/nacional/decreto-824-2019-332890/actualizacion), [reglamentación Decreto 862/2019 actualizada](https://www.argentina.gob.ar/normativa/nacional/decreto-862-2019-332991/actualizacion) y [Ley 27.802](https://www.argentina.gob.ar/normativa/nacional/norma-423680/texto), publicada el 6/3/2026.

| Aspecto | Regla y consecuencia para la creación/operación |
|---|---|
| Sujeto y fuente | S.A. residente: rentas argentinas y extranjeras, con crédito exterior admitido y límites. Sucursal/establecimiento permanente: rentas atribuibles y art. 73b. La condición corporativa no comienza únicamente con la primera captación de depósitos. |
| Base | Resultado impositivo, con imputación y deducciones legales; no monto de préstamos, depósitos o ingresos brutos. Mantener conciliación entre estados BCRA y balance fiscal. |
| Escala | Art. 73: tasas marginales **25%, 30% y 35%** con tramos actualizables. No aplicar 35% a toda ganancia o sobre facturación sin evaluar el tramo. |
| Devengamiento | Art. 24, instrumentos y reglas particulares; identificar diferencias entre cobro, devengamiento contractual/contable y fiscal. No liquidar el tributo sólo desde movimientos de caja. |
| Deducciones | Causalidad, documentación y limitaciones específicas. El límite de intereses vinculados del cuarto párrafo de art. 85a tiene excepción expresa para entidades LEF: no imponer automáticamente el límite EBITDA 30% de una sociedad ordinaria. Restantes controles y precios de transferencia subsisten. |
| Incobrables | **LIG 91b y DR 862 arts. 214–218**, método/índices y documentación; revisar autorización de cambio de método y pequeños saldos. Las referencias art. 87b/DR 136 del adjunto corresponden a numeración anterior. |
| Previsiones | Previsión BCRA/NIIF 9 no equivale a deducción fiscal automática. Distinguir diferencias temporarias/permanentes, recuperos y reversos. Activo por impuesto diferido sólo si satisface reconocimiento y recuperabilidad; no por toda diferencia de previsión. |
| Inflación | Arts. 105–107 y condición de art. 106 por cierre; separar ajuste estático/dinámico del contable. No tratar los sextos de ejercicios históricos 2019/2020 como régimen general de un banco creado en 2026. |
| Quebrantos | Art. 25: plazo general de cinco años y restricciones por clase/fuente. Ley 27.802 art. 190 actualiza por IPC los originados en ejercicios iniciados desde 1/1/2025, conforme texto. No asumir pérdida siempre nominal o compensable con cualquier resultado. |
| Ingreso | Declaración anual, anticipos, retenciones sufridas, créditos y pagos con calendario por cierre/CUIT. Los anticipos extraordinarios históricos para determinadas grandes rentas no se transforman por analogía en un tributo permanente de apertura. |

**Escala de referencia 2026 verificada en [PDF oficial de ARCA](https://www.afip.gob.ar/gananciasYBienes/ganancias/personas-juridicas/determinacion/documentos/Ganancias-Escala-PJ-2026.pdf):** aplicable según inicio del ejercicio y regla anual del art. 73; revalidar para un ejercicio posterior.

| Ganancia neta imponible acumulada | Importe fijo | Más porcentaje sobre el excedente del límite inferior |
|---|---|---|
| Hasta ARS 133.514.185,74 | ARS 0 | 25% |
| Más de ARS 133.514.185,74 hasta ARS 1.335.141.857,38 | ARS 33.378.546,43 | 30% |
| Más de ARS 1.335.141.857,38 | ARS 393.866.847,93 | 35% |

No convertir esa tabla en constante sin ejercicio/versionado. No se calculó impuesto a una entidad real ni se proyectaron ganancias inexistentes.

**Distribución:** LIG 97 contempla retención del **7%** sobre dividendos/utilidades a personas humanas/sucesiones y beneficiarios del exterior, según régimen. No se suma a toda utilidad sin distribución ni indistintamente a dividendos intersocietarios residentes. La sucursal/EP tiene tasa adicional por remesa a matriz bajo 73b. Revisar convenio aplicable, documentación y restricciones prudenciales antes del pago. Los regímenes históricos de utilidades previas a 2018 sólo son relevantes si la estructura/operación los incorpora.

### 9.3 IVA por operación y condición del cliente

La [Ley de IVA actualizada, Decreto 280/1997](https://www.argentina.gob.ar/normativa/nacional/decreto-280-1997-42701/actualizacion), exige clasificar cada concepto:

| Operación | Tratamiento de referencia verificado | Evidencia / excepción |
|---|---|---|
| Intereses/comisiones alcanzados | General **21%**, salvo exención o tasa diferente prevista. | Naturaleza del servicio, sujeto, destino, contrato y fecha del hecho imponible. |
| Intereses/comisiones de préstamos de entidad LEF a tomador responsable inscripto | Art. 28 inc. d: **10,5%**, mitad de general, bajo sus condiciones. | Condición fiscal vigente del tomador. **No es la tasa reducida general para consumidores finales** que sugiere el adjunto. |
| Depósitos y operaciones interfinancieras comprendidas | Exenciones de art. 7, inc. h, ap. 16, pto. 1 con alcance propio. | No extenderlas a cualquier comisión del banco o a todo instrumento financiero. |
| Préstamos para vivienda | Art. 7, inc. h, ap. 16, pto. 8 exonera intereses de los préstamos para compra, construcción o mejoras de vivienda destinada a casa-habitación, con sus condiciones. | Probar destino. No importar como requisitos literales universales de esta exención IVA la hipoteca y el conjunto “única/familiar/permanente” de otros tributos. Analizar cargos y comisiones separadamente. |
| Compras afectadas a operaciones gravadas/exentas | Crédito fiscal, apropiación y prorrata de art. 13, con ajuste y conciliación. | El IVA de nube/software/gastos comunes puede no ser totalmente recuperable y modifica el costo. |
| Servicios del exterior | Importación de servicios o servicios digitales según arts. 1/4 y utilización efectiva. | Separar banco comprador de SaaS del intermediario que percibe IVA al usuario en un pago alcanzado por RG 4240. No suponer misma base ni responsable. |

No existe una reducción universal por ser PyME ni una exención de todo cargo de un crédito que tenga intereses exentos. Registrar condición fiscal, cambios y comprobantes; el caso se debe poder reconstruir para un período histórico.

**Presentación:** RG 5705/2025 establece IVA Simple/F 2051–Portal IVA para períodos noviembre 2025 y siguientes bajo su alcance. No diseñar el alta 2026 exclusivamente con un aplicativo histórico. [ARCA, sujetos/operaciones de IVA Simple](https://arca.gob.ar/iva/iva-simple/sujetos-operaciones-alcanzadas.asp).

### 9.4 Impuesto sobre créditos y débitos

[Ley 25.413 y Decreto 380/2001 actualizado](https://www.argentina.gob.ar/normativa/nacional/decreto-380-2001-66561/actualizacion): distinguir **recaudación a clientes** de **impuesto propio de la entidad**.

| Rol | Regla / consecuencia |
|---|---|
| Agente en cuentas/operaciones de clientes | Referencia general **6‰ por crédito y 6‰ por débito**, con hechos alternativos, reducciones y exenciones por cuenta/titular/uso. No cobrar sin clasificar ni eximir por nombre comercial de la cuenta. |
| Banco por pagos propios | Anexo art. 7 enumera pagos propios alcanzados, incluidos remuneraciones/cargas, honorarios, administración, organización/**software**, determinados tributos, dividendos y otros conceptos. Alícuota **12‰**, salvo el tratamiento específico de pagos a comercios de tarjetas **1,50‰**. Puede incidir antes de abrir al público. |
| Cuentas y movimientos especiales | Evaluar exclusiones/exenciones, exclusividad y documentación; gestionar registro de beneficios cuando corresponda. **No existe una exención general de todos los pagos del banco por llamarlos “cuentas técnicas”.** |
| Crédito contra otros tributos | Art. 13 y reglas aplicables: cómputo condicionado; no prometer recupero total a todos los sujetos ni computar como propio el importe recaudado por cuenta de clientes. |
| Administración | RG 2111 y modificatorias, registros de beneficios, liquidación/ingreso, certificados, falta de saldo, reversos y devoluciones según supuesto. Conservar conciliación cliente–banco–fisco. |

### 9.5 Patrimonio, participaciones y obligaciones condicionadas

- **Bienes Personales acciones/participaciones:** [Ley 23.966, título VI, artículo siguiente al 25](https://www.argentina.gob.ar/normativa/nacional/ley-23966-365/actualizacion). La S.A. actúa como responsable sustituto al **0,50%** en los supuestos de tenedores/base alcanzados, con derecho de recupero. No es un impuesto sobre el total de activos o depósitos del banco. Distinguir personas humanas/sucesiones y personas jurídicas del exterior de accionistas argentinos personas jurídicas, y excepciones concretas.
- **Información de participaciones/beneficiario final:** RG 4697 y modificatorias; coherencia con acciones, control y presentaciones BCRA/registrales/UIF, sin unificar umbrales diferentes por comodidad.
- **Banco cooperativo:** revisar exención de utilidades de LIG 26d y su reconocimiento, contribución sobre capital de [Ley 23.427](https://www.argentina.gob.ar/normativa/nacional/ley-23427-22268/actualizacion), referencia 2% con base/exclusiones y horizonte legal. La contribución extraordinaria de Ley 27.486 tiene período específico original; no se verificó prórroga general para 2026 y no se presupone. No usar sin ajuste la matriz S.A.
- **Ganancia mínima presunta:** el título V de Ley 25.063 fue derogado para ejercicios iniciados desde 1/1/2019 por [Ley 27.260, art. 76](https://biblioteca.arca.gob.ar/dcp/LEY_C_027260_2016_06_29). Una página vieja de aplicativo con base bancaria no acredita vigencia 2026 ni crea un aporte de apertura.
- **Impuesto PAIS:** finalizó en diciembre 2024; no es un tributo corriente 2026. Sí deben examinarse percepciones de Ganancias/Bienes Personales y el IVA de los flujos respectivos: su desaparición no elimina esos regímenes.
- **Inmuebles y otros activos:** evaluar impuesto inmobiliario/ABL, IVA/Ganancias y Sellos de cada adquisición, locación o garantía, sin agregar un “impuesto de constitución bancaria” nacional inexistente por analogía.

## 10. Agentes, facturación e información fiscal

### 10.1 Retenciones/percepciones y operaciones internacionales

Crear un registro por impuesto, régimen, sujeto/rol, concepto, alta, base, certificado, fecha y canal:

| Régimen / flujo | Tratamiento que debe resolverse |
|---|---|
| Ganancias a residentes | RG 830 y modificatorias, pagos/beneficiarios/exclusiones; no todos los pagos usan el mismo mínimo o alícuota. Nómina y dividendos tienen regímenes específicos. |
| Intereses de depósitos de personas humanas | RG 5822/2026 modifica exclusiones de retención RG 830; Ley 27.802 art. 191 modifica LIG 26h para 2026. No extender un beneficio del ahorrista persona humana a ingresos bancarios de una S.A. ni equiparar no retención con exención sin leer la norma sustantiva. |
| IVA como agente | Designación, nóminas y regímenes aplicables, por ejemplo RG 2854 en su alcance; no atribuir al banco todos los regímenes automáticamente. |
| Pagos a beneficiarios del exterior | LIG título V, RG 739, SIRE y régimen por concepto. Intereses, servicios, licencias y asistencia no tienen un único porcentaje o gross-up. Examinar precios de transferencia, vinculadas y jurisdicciones además de la retención. |
| Convenios para evitar doble imposición | [RG 5855/2026](https://www.argentina.gob.ar/normativa/nacional/norma-426363/texto), BO 3/6: residencia y documentación antes del pago/beneficio; si certificado no fija vigencia, referencia de 12 meses con condiciones. Aplicar apostilla/legalización o excepción de validación digital según texto; sin prueba no usar beneficio del tratado. |
| SICORE/SIRE | Coexistencia por impuesto/régimen: RG 3726 prevé sustitución progresiva. No declarar reemplazo total de SICORE; emitir certificados y DDJJ en el canal vigente del supuesto. |
| Pagos exteriores/digitales | [RG 5617 actualizada](https://www.argentina.gob.ar/normativa/nacional/norma-407430/actualizacion), RG 4240 y complementarias según flujo/rol; distinguir percepciones a clientes de tributos propios y de IVA por servicios importados. |

Llevar por separado retenciones **practicadas**, **sufridas**, importes a ingresar y créditos utilizables. El impuesto retenido al proveedor puede convertirse en costo del banco si se pacta gross-up, pero no por el mero hecho de ser agente.

### 10.2 Facturación bancaria: cronograma 2026–2027

[RG ARCA 5866/2026, texto y anexo](https://www.argentina.gob.ar/normativa/nacional/norma-427092/texto), emitida el 26/6 y publicada el 29/6/2026, modifica RG 1415/4291 y abroga 2668/2719/5824. No basar el producto en una excepción histórica general de facturación de entidades financieras.

Su vigencia general es **1/7/2026**, con excepciones y exigibilidades especiales del art. 4. La tabla muestra los hitos bancarios especiales; una operación no diferida no espera automáticamente hasta octubre o diciembre.

| Exigibilidad según operaciones y sujetos de art. 4 | Alcance a incorporar |
|---|---|
| **1/10/2026** | Leasing y operaciones de comercio exterior del supuesto bancario, incluidos ajustes. |
| **1/12/2026** | Préstamos otorgados salvo los generados por descubiertos; además, operaciones con sujetos que no sean RI/exentos de IVA según el inciso correspondiente; ingresos de liquidaciones a titulares de tarjetas y otros sujetos incluidos según rol. Leer incisos y operaciones, sin aplazar indiscriminadamente todo hasta diciembre. |
| **1/3/2027** | Liquidaciones a comercios adheridos y rendición de arancel integrado de actores comprendidos. |

La liquidación electrónica mensual permite documentar el conjunto mensual por cliente bajo las condiciones del régimen, conservando detalle y trazabilidad de operaciones; emisión al último día del mes y puesta a disposición dentro del plazo previsto de diez días corridos. Permanecen excepciones específicas: no es mandato de facturar todo movimiento de capital como ingreso.

La excepción transitoria de informar determinadas percepciones hasta 30/11/2026 requiere su detalle en extracto/documento comercial; no las vuelve inexistentes. Preparar puntos/canales, numeración, identificación fiscal, IVA, notas de ajuste y conciliación con contratos y contabilidad. La nueva obligación de comprobante no crea por sí sola un nuevo hecho imponible.

### 10.3 Información financiera, CRS y FATCA

| Objeto | Requisitos y actualización |
|---|---|
| Información local | RG 4298/2018 actualizada: cuentas, titulares/cotitulares, movimientos, préstamos, saldos y umbrales por supuesto; RG 3421 sólo en anexos todavía vigentes por producto. Parametrizar universo, período y diseños con sus versiones. |
| Umbrales 2026 | [RG 5814/2026](https://www.argentina.gob.ar/normativa/nacional/norma-422371/texto), publicada el 14/1, elimina el mecanismo de actualización semestral automática del último párrafo de art. 2 RG 4298, para información diciembre 2025 y siguientes. No seguir indexando por IPC una regla retirada. |
| Institución/cuentas reportables | [RG 4056 actualizada](https://www.argentina.gob.ar/normativa/nacional/norma-275036/actualizacion), RG 5303, acuerdos y clasificación: empadronamiento, debida diligencia, residencia/TIN, autocertificaciones, titulares/controlantes de entidades pasivas, cambios de circunstancias y reporte anual/rectificación. |
| Cambio 2026 | [RG 5887/2026](https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t%3ARAG%7Cn%3A5887%7Co%3A9%7Ca%3A2026%7Cf%3A13%2F08%2F2026), publicada el 18/8, modifica anexosII/III y aplica a información de período 2026 y siguientes. Revisar exclusiones/cuentas condicionadas y vehículos de inversión; no conservar como universal una lista anterior. |
| FATCA | Clasificación, obligaciones del IGA y registro/GIIN cuando corresponda. No equivale a exigir idéntico formulario a todo cliente ni a reportar cualquier cuenta sólo por tener un titular extranjero. |
| Secreto y conservación | Base legal de entrega, controles de acceso, trazabilidad y prueba. Un umbral de reporte fiscal no es un umbral AML, límite de saldo ni autorización de una operación. |

## 11. Empleador y transición FAL

Preparar altas de empleador y de cada trabajador antes del comienzo, F 931/pagos, retención de Ganancias de nómina, libro/sistemas salariales, obra social, ART, seguros y encuadre convencional. [Ley 27.541, art. 19](https://www.argentina.gob.ar/normativa/nacional/333564/actualizacion) distingue contribuciones patronales 20,40%/18% según clasificación legal; se añaden otros componentes laborales que no agotan esas tasas, con bases, detracciones y excepciones propias. No presumir condición MiPyME del banco por ser nuevo.

**Fondo de Asistencia Laboral:** [Ley 27.802, título II](https://www.argentina.gob.ar/normativa/nacional/norma-423680/texto), [Decreto 408/2026](https://www.argentina.gob.ar/normativa/nacional/norma-426272/texto) y [RG 5907/2026](https://www.argentina.gob.ar/normativa/nacional/norma-430768/texto), publicada el 1/10/2026:

- **Antecedente de la base al 16/10:** el texto de RG5907 prevé devengado **noviembre 2026**, vigencia desde 1/11 y efectos procedimentales de su art.19. La actualización siguiente obliga a revisar la transición antes de parametrizar; no se declara implementada.
- Distinguir declaración de empleador privado/público, cuenta y **IDFAL**, validación previa y canal de declaración/ingreso. Alta posterior requiere cumplir el plazo de su primer vencimiento.
- Contribución FAL de referencia: 1% para grandes empresas y 2,5% MiPyME en el supuesto legal. El [anexo oficial de RG 5907](https://www.argentina.gob.ar/sites/default/files/infoleg/430768/resgral5907-1-1.jpg), revisado visualmente, **reasigna** componentes manteniendo los totales 20,40%/18% de su cuadro: no sumar el FAL otra vez sobre ese mismo total.
- Presupuestar base y categoría correctas; el período de carencia de uso no elimina la contribución. Conciliar nómina, declaración y cuenta con la entidad habilitada.
- Ser banco no autoriza automáticamente a administrar/instrumentar FAL como entidad habilitada. Su rol como empleador es distinto de un posible rol de proveedor financiero/FAL, y las inversiones tienen el tratamiento prudencial A 8490 ya indicado.

**Actualización verificada al 20/10/2026:** el [Decreto1228/2026, BO20/10](https://www.boletinoficial.gob.ar/detalleAviso/primera/349294/20261020), vigente desde su publicación, sustituye los arts.15 y27 del Decreto408: prorroga el comienzo del régimen FAL al **1/12/2026** y establece **doce períodos mensuales completos y consecutivos de devengamiento y pago** de carencia, desde el mes de registro ante ARCA de la efectiva primera contribución del empleador. Sin ese hecho no hay fecha individual calculable. El texto recuperado de RG5907 art.19 aún menciona noviembre: no trasladar automáticamente todas sus obligaciones procedimentales o el uso de versión48; queda pendiente armonización por responsable fiscal/legal. Mantener separados empleador, vehículo/administrador y tratamiento prudencial de inversiones, sin presumir suspensión de A8490. Ver [análisis, perfiles y casos pendientes](../regulatory/PEN-DECRETO1228-2026.md).

## 12. Ingresos Brutos y Convenio Multilateral

### 12.1 Dos preguntas distintas: base local y distribución

El [art. 8 del Convenio Multilateral](https://www.ca.gob.ar/ordenamiento-juridico/convenio-multilateral-comarb/regimen-de-distribucion-de-ingresos-regimenes-especiales) establece un régimen especial para entidades LEF. Su sumatoria de **ingresos, intereses pasivos y actualizaciones pasivas** sirve para atribuir ingresos territorialmente bajo sus reglas; **no define una base nacional como ingresos menos todos los intereses/gastos**. Tampoco corresponde aplicar automáticamente el coeficiente general 50% ingresos/50% gastos.

El legajo debe separar:

1. Actividad, hecho imponible, base, devengamiento, deducciones/exclusiones/exenciones del código fiscal de cada jurisdicción.
2. Atribución por art. 8, casas/filiales y operaciones fuera de ellas, con interpretativas vigentes.
3. Código de actividad, alícuota y adicionales de la ley local correspondiente al período.
4. Anticipos, DDJJ anual/rectificativas, recaudaciones sufridas, saldos, reintegros y padrones, con papeles conciliables contra estados individuales/plan de cuentas.

Una exclusión de la sumatoria para distribución no equivale necesariamente a una exención del impuesto local. La jurisdicción de casa central, servidores o asiento contable tampoco resuelve por sí sola todas las atribuciones.

### 12.2 Banco exclusivamente digital

[RG COMARB 5/2024](https://www.argentina.gob.ar/normativa/nacional/resoluci%C3%B3n-5-2024-397558/texto), que incorpora RG 8/2022 ratificada por CP 9/2023, contempla entidades **exclusivamente digitales**, con aplicación desde período fiscal 2023. Se recuperó también el [PDF completo oficial](https://www.ca.gob.ar/comarb-generales?catid=441&id=8423%3A2024-5&task=download.send).

Considera presencia fiscal de casa/filial en jurisdicciones donde existen sus clientes, con atribución por domicilio del cliente/depositante para los conceptos definidos, y reglas específicas para otras cuentas y operaciones entre entidades. Exige detalle contable y datos de clientes; no significa abrir sucursales físicas en todas esas provincias. No se extiende sin análisis al banco que tiene sucursales y además una app.

El índice COMARB separa banca digital de entidades financieras. Un documento llamado “texto actualizado” que sólo reúna interpretativas 2014/2018 no agota el régimen digital; conservar la identidad y vigencia de RG 5/2024 al reconstruir el corpus.

### 12.3 CABA y PBA: ejemplos vigentes verificados

| Jurisdicción | Base bancaria y fuente | Alícuotas de referencia 2026 / límites |
|---|---|---|
| **CABA** | Código Fiscal TO 2026 aprobado por Decreto 172/2026, **art. 230**: total del haber de cuentas de resultado, sin deducciones, con reglas particulares. El decreto revoca el 147/2026. [Anexo oficial](https://documentosboletinoficial.buenosaires.gob.ar/publico/PE-DEC-AJG-AJG-172-26-ANX.pdf). | [Ley 6927, anexo actualizado](https://www.cedom.gob.ar/legislacion/normas/leyes/RepoLeyes/anexos/al6927.html), art. 14(2): banca LEF **8%**. Art. 16:1,5% para préstamos de bancos públicos de segundo grado a bancos con destino final productivo; art. 17:0% para hipotecarios a PH de vivienda única/familiar/permanente en CABA según condiciones. No generalizar excepciones. |
| **Provincia de Buenos Aires** | [Código Fiscal 10397 actualizado](https://normas.gba.gob.ar/documentos/V9rqlUP0.html), **art. 192**: haber de cuentas de resultado sin deducciones, reglas especiales de devengamiento/divisas y relación BCRA. | [Ley 15558, art. 20](https://normas.gba.gob.ar/documentos/Bd5moXfD.html): actividad 6419 **9%**;641932 **0%** para intereses/ajustes de hipotecarios del destino/persona indicados. Distinguir otros productos y requisitos. |

Estos textos **contradicen una deducción indiscriminada de intereses pasivos para liquidar como “spread”**. Las tasas son sobre bases y atribuciones jurídicamente determinadas, no un porcentaje nacional sobre margen neto. El 8%/9% no permite inferir el costo efectivo sin conocer mezcla de ingresos, exclusiones y territorialidad.

**Régimen derogado a no reimplantar:** [AGIP 173/2026](https://imagenes.agip.gob.ar/normativa/resoluciones/2026/resolucion-n-173agip2026), publicada el 30/4, deja sin efecto RI 108/2021 y dispone el tratamiento de presentaciones omitidas. Su derogación no elimina IIBB ni los demás regímenes aplicables.

### 12.4 Agentes de recaudación provincial

- **SIRCREB:** acreditaciones en cuentas bancarias y jurisdicciones adheridas, padrones y reglas de exclusión/restitución. Es recaudación a cuenta del impuesto del titular, **distinta del IIBB propio del banco**. Resolver designación/alcance, calendario, intercambio, DDJJ e ingreso; también los regímenes locales no subsumidos.
- **SIRCUPA:** [régimen oficial](https://www.ca.gob.ar/resoluciones-comarb/download/446-ta/8524-texto-actualizado-sircupa) para agentes PSP que ofrecen cuentas de pago comprendidos. No asignarlo automáticamente al banco por tener app o cuentas CBU. Si el grupo también opera un PSP, separar sociedad, registro, cuenta y fondos.
- Otras retenciones/percepciones provinciales: condición/designación por régimen, padrones, certificados, mínimos y exclusiones. No aplicar una tasa única de todas las provincias ni confundir retención sufrida con obligación de actuar como agente.

## 13. Sellos, inmuebles y municipios

Sellos requiere territorialidad, acto/instrumentación o hecho monetario, base, exención y responsabilidad local. Puede alcanzar constitución/contratos, créditos y garantías según caso, pero **no existe una tasa nacional uniforme sobre todo préstamo o capital social**.

| Ejemplo 2026 | Tratamiento / precaución |
|---|---|
| CABA | Ley 6927 arts. 30/31: referencia 1% general y 1,2% operaciones monetarias; CF arts. 352–356 regulan base/numerales y proporción temporal, exenciones y cargo; art. 362 agentes. No aplicar directamente el 1,2% al nominal de todo crédito. |
| PBA | Ley 15558 art. 39: referencia 12‰ para mutuos del apartadoA 14,12‰ para operaciones monetariasC 3 y 18‰ para derechos realesB 4, con excepciones. Código Fiscal define base, agentes y exenciones; no duplicar automáticamente mutuo, garantía y hecho monetario. |
| Inmuebles y locales | Determinar titularidad, adquisición/locación, inmobiliario/ABL, garantías y beneficios concretos. El costo varía por inmueble, municipio, plazo y acto. |
| Municipio | Habilitación, inspección/seguridad e higiene, publicidad/cartelería y otras tasas conforme hecho y servicio exigibles. Tener domicilio fiscal provincial no demuestra cumplimiento municipal de cada local. |

El expediente fiscal debe conservar instrumento, jurisdicciones, base, principal/garantía, prueba de exención y certificado/ingreso. La digitalización de la firma no elimina automáticamente el impuesto ni prueba que siempre haya instrumento gravado.

## 14. Inventario territorial de las 24 jurisdicciones

Se localizaron autoridades y entradas normativas oficiales contrastadas con el [directorio COMARB](https://www.ca.gob.ar/datos-jurisdicciones). **Localizar un portal no equivale a revisar íntegramente su código, ley impositiva y todas sus modificaciones.** CABA/PBA tienen las comprobaciones específicas de las secciones anteriores; las otras 22 requieren desarrollar el legajo antes de activar una operación alcanzada. No se inventan tasas para completar la tabla.

| Jurisdicción | Autoridad / entrada oficial localizada | Estado de la investigación |
|---|---|---|
| Ciudad Autónoma de Buenos Aires | [Administración Gubernamental de Ingresos Públicos (AGIP)](https://imagenes.agip.gob.ar/normativa/inicio) | Base y tasas seleccionadas 2026 verificadas; restantes supuestos/modificaciones por cerrar. |
| Buenos Aires | [Agencia de Recaudación de la Provincia de Buenos Aires (ARBA)](https://web.arba.gov.ar/biblioteca-legal) | Base y tasas seleccionadas 2026 verificadas; restantes supuestos/modificaciones por cerrar. |
| Catamarca | [Agencia de Recaudación Catamarca (ARCAT), Dirección General de Rentas](https://dgrentas.arcat.gob.ar/leyes.php) | Portal/índice localizado; corpus bancario 2026 y anexos por cerrar. |
| Chaco | [Administración Tributaria Provincial (ATP)](https://atp.chaco.gob.ar/legislacion-tributaria) | Portal/índice localizado; corpus bancario 2026 y anexos por cerrar. |
| Chubut | [Agencia de Recaudación de la Provincia del Chubut (ARECH)](https://www.arech.gob.ar/) | Portal/índice localizado; corpus bancario 2026 y anexos por cerrar. |
| Córdoba | [Dirección General de Rentas / Rentas Córdoba](https://www.rentascordoba.gob.ar/cms/legislacion/?_sft_category=decretos&sf_paged=5) | Portal/índice localizado; corpus bancario 2026 y anexos por cerrar. |
| Corrientes | [Dirección General de Rentas (DGR)](https://www.dgrcorrientes.gov.ar/rentascorrientes/consultarNormativas.do) | Portal/índice localizado; corpus bancario 2026 y anexos por cerrar. |
| Entre Ríos | [Administradora Tributaria de Entre Ríos (ATER)](https://www.ater.gov.ar/ater2/NormativaCodigo.asp) | Portal/índice localizado; corpus bancario 2026 y anexos por cerrar. |
| Formosa | [Administración Tributaria de la Provincia de Formosa (ATP)](https://www.atpformosa.gob.ar/descargas.php) | Portal/índice localizado; corpus bancario 2026 y anexos por cerrar. |
| Jujuy | [Dirección Provincial de Rentas](https://rentasjujuy.gob.ar/ley-impositiva/) | Portal/índice localizado; corpus bancario 2026 y anexos por cerrar. |
| La Pampa | [Dirección General de Rentas (DGR)](https://dgr.lapampa.gob.ar/) | Portal/índice localizado; corpus bancario 2026 y anexos por cerrar. |
| La Rioja | [Dirección General de Ingresos Provinciales (DGIP)](https://www.dgiplarioja.gob.ar/) | Portal/índice localizado; corpus bancario 2026 y anexos por cerrar. |
| Mendoza | [Administración Tributaria Mendoza (ATM)](https://atm.mendoza.gov.ar/codigo-fiscal/) | Portal/índice localizado; corpus bancario 2026 y anexos por cerrar. |
| Misiones | [Agencia Tributaria Misiones (ATM)](https://atmisiones.gob.ar/normativas/) | Portal/índice localizado; corpus bancario 2026 y anexos por cerrar. |
| Neuquén | [Dirección Provincial de Rentas (DPR)](https://dprneuquen.gob.ar/codigo-fiscal-2026/) | Portal/índice localizado; corpus bancario 2026 y anexos por cerrar. |
| Río Negro | [Agencia de Recaudación Tributaria](https://agencia.rionegro.gov.ar/?contID=13427) | Portal/índice localizado; corpus bancario 2026 y anexos por cerrar. |
| Salta | [Dirección General de Rentas (DGR)](https://www.dgrsalta.gov.ar/rentassalta/jsp/servicios/rentasOnLine.jsp) | Portal/índice localizado; corpus bancario 2026 y anexos por cerrar. |
| San Juan | [Dirección General de Rentas (DGR)](https://recaudacionrentas.sanjuan.gob.ar/) | Portal/índice localizado; corpus bancario 2026 y anexos por cerrar. |
| San Luis | [Dirección Provincial de Ingresos Públicos (DPIP)](https://dpip.sanluis.gov.ar/rentas_sanluis/?page_id=10659) | Portal/índice localizado; corpus bancario 2026 y anexos por cerrar. |
| Santa Cruz | [Agencia Santacruceña de Ingresos Públicos (ASIP)](https://www.asip.gob.ar/legislacion/) | Portal/índice localizado; corpus bancario 2026 y anexos por cerrar. |
| Santa Fe | [Administración Provincial de Impuestos (API)](https://www.santafe.gob.ar/index.php/web/content/view/full/111523) | Portal/índice localizado; corpus bancario 2026 y anexos por cerrar. |
| Santiago del Estero | [Dirección General de Rentas (DGR)](https://www.dgrsantiago.gov.ar/) | Portal/índice localizado; corpus bancario 2026 y anexos por cerrar. |
| Tierra del Fuego, Antártida e Islas del Atlántico Sur | [Agencia de Recaudación Fueguina (AREF)](https://www.aref.gob.ar/category/normativa/leyes/impositiva/) | Portal/índice localizado; corpus bancario 2026 y anexos por cerrar. |
| Tucumán | [Dirección General de Rentas (DGR)](https://extranet2.rentastucuman.gov.ar/nomina/rentastuc2/index.php) | Portal/índice localizado; corpus bancario 2026 y anexos por cerrar. |

Para cerrar cada fila se requiere: código fiscal y texto anual/modificatorias a la fecha de apertura; actividades y subcódigos; base/deducciones/exenciones; alícuotas/adicionales; alta local/CM y domicilio electrónico; anticipos/anual/rectificativas; regímenes de agentes y padrones; Sellos por instrumento; municipios/locales y calendario. El registro de sucursales y permisos municipales debe relevarse adicionalmente cuando corresponda.

Los portales pueden mostrar proyectos, TO antiguos o etiquetas por ejercicio: un proyecto oficial no es ley sancionada; un PDF 2023 no demuestra consolidación 2026; un índice con ley de ejercicio 2026 publicada 2025 no permite inventar su año de sanción. En banca exclusivamente digital, la presencia de clientes puede activar atribución aunque no haya una sucursal física. No se deriva cobertura municipal universal de inventariar 24 jurisdicciones.

## 15. Estructuras alternativas y operaciones que añaden requisitos

| Estructura / operación | Análisis adicional necesario |
|---|---|
| Banco comercial cooperativo | Constitución/matrícula INAES, gobierno cooperativo y Ley 20.337, más autorización BCRA. Exención de Ganancias y contribución al capital con condiciones propias; no denominar dividendos a todos los retornos ni usar sin adaptación la matriz S.A. |
| Sucursal extranjera | Representación, LGS 118, capital local permanente, opinión/supervisión de origen, consolidación y condición de no banco pantalla según TO. Contabilidad e impuestos de EP, remesas, pagos intragrupo y acceso supervisor; no presumir cobertura extranjera para depósitos locales. |
| Controlante extranjero de banco local | LGS 123 cuando corresponde, cadena de control/BF, documentación exterior y aportes, registros y régimen cambiario aplicable. Dividendos/CDI/precios de transferencia según operaciones. Los artículos históricos LEF sobre aprobación PEN/reciprocidad no se reutilizan sin advertir derogaciones. |
| Compra/fusión de banco existente | LEF 7/15 y TO autorización sección 5: aprobación BCRA de operaciones/control, documentación y límites a su consumación. Due diligence de pasivos legales/fiscales/AML, pérdidas, juicios, cartera, garantías, datos y patrimonio; no se “compra una licencia limpia” automáticamente. |
| Defensa de competencia | Si existe concentración alcanzada, Ley 27.442 y autoridad competente además del BCRA. La creación orgánica sin concentración no implica una autorización general adicional por este motivo. |
| Oferta pública/captación especializada | CNV y régimen de instrumentos/agentes, o registro/contratos de red según servicio. Distinguir ofrecer tecnología de intermediar, custodiar o distribuir un instrumento. |

**Transición de competencia:** [Disposición TDC 29/2026](https://www.argentina.gob.ar/normativa/nacional/norma-430371/texto) trata el régimen aplicable a operaciones notificadas antes de las **00:00 del 17/11/2026**, aun si cierran después, frente al régimen suspensivo de Ley 27.442. No afirmar que al 16/10 ya rige control previo universal ni que la autorización BCRA reemplaza la de competencia. El caso exige verificar umbral, excepciones, acuerdo vinculante, fecha y régimen de notificación; no se calculó una operación real.

## 16. Presupuesto de creación: capital no equivale a costo

| Componente | Cómo presupuestarlo | Evitar |
|---|---|---|
| Capital y márgenes | Plan de cartera/riesgos, RPC admisible, pérdidas de arranque, conservación y condiciones BCRA. Separar aporte, activo financiado y requerimiento a mantener. | Tratar ARS 5.000 millones como precio de una licencia suficiente para cualquier modelo. |
| Arancel/canon |10.000 UVA y 80.000 UVA, fechas y conversión oficiales por pago. | Suponer que integran RPC o convertirlos a una cifra USD sin tipo/fecha. |
| Organización y registro | Escribanía, publicaciones, tasas registrales, representación, legalizaciones/traducción y asesoría según actos/localidad. | Un arancel nacional único para todas las jurisdicciones o una cotización inventada. |
| Instalación y servicios | Personal, locales/seguridad, TI/SI, nube/core, IAM/KMS, auditoría, continuidad, conectores/redes y reportes. | Equiparar una arquitectura escrita con operación aprobada o presupuesto completo. |
| Tributos propios | Ganancias, IVA no recuperable, débitos/créditos propios, IIBB, Sellos, inmuebles y tasas efectivamente aplicables. | Modelar IIBB sobre un spread universal o IVA compras totalmente recuperable. |
| Pasivos por recaudación | Impuestos retenidos/percibidos a terceros y fechas de rendición, identificados por régimen. | Usarlos como ingresos/caja libre para pagar funcionamiento. |
| Liquidez y depósitos | Encajes, activos líquidos, stress y aportes FGD según perímetro; distinguir activos restringidos y costos. | Sumar todos los requerimientos como si fueran gastos independientes o contar dos veces el mismo recurso. |
| Impuesto diferido | Reconocimiento/recuperabilidad y deducción prudencial cuando corresponde. | Presentarlo como caja disponible o capital admisible automático. |
| Contingencias y salida | Rechazos, rectificativas, litigios, capital adicional, transición de proveedores y conservación. | Presumir cero costo por licencia libre o por contratar un servicio gestionado. |

Construir flujo mensual durante organización y primeros ejercicios, con escenarios de crecimiento, inflación, tasa, mora, retiro de depósitos, interrupción y cambios regulatorios. La liquidez de apertura y la solvencia son restricciones diferentes. Este estudio no dispone de cartera, costos contratados o accionistas para calcular el financiamiento real necesario.

## 17. Checklist de expediente y apertura

La siguiente es una **síntesis de trabajo**, que debe completarse con la resolución particular y normas aplicables; no una sustitución del listado oficial ni una aceptación institucional. Los roles son responsables sugeridos, no designaciones efectivas del proyecto.

| Hito | Evidencia concreta esperada | Responsable sugerido |
|---|---|---|
| Definición | Clase/grado, sociedad, accionistas/control, jurisdicciones, productos, moneda, canales y fecha objetivo. | Promotores, Legal y Producto. |
| Elegibilidad | FAP/APAEF, certificados, inhabilidades/antecedentes, participaciones, origen de patrimonio/fondos, solvencia y liquidez. | Legal, accionistas y auditor/contador independiente. |
| Viabilidad | Plan a cinco años y supuestos, riesgos, costos, impuestos, capital/RPC y liquidez, sensibilidad y capacidad de nuevos aportes. | Finanzas y Riesgos. |
| Solicitud | Proyecto societario/institucional/TI/prevención, documentación íntegra, arancel, nota y constancias de expediente. | Promotores y representantes. |
| Resolución y constitución | Autorización y condiciones; acto en plazo, aportes e inscripción y BF; canon. | Legal, Finanzas y órganos societarios. |
| Gobierno | Autoridades evaluadas/designadas, matriz de incompatibilidades, comités y funciones de control, auditorías contratadas. | Directorio, Gerencia y control. |
| Altas fiscales | CUIT/DFE, impuestos/empleador, agentes/información, puntos/comprobantes y altas locales/CM. | Contabilidad e Impuestos. |
| Prevención | Registro UIF, OC/comité, políticas y riesgo, onboarding/legajos/listas, monitoreo, reportes, reserva y controles probados. | Cumplimiento y Directorio. |
| Locales | Régimen de casa/dependencia, habilitaciones/avisos, seguridad física, responsables, custodia y servicios. | Operaciones, Seguridad y Legal. |
| TI/proveedores | Evidencia de gobierno, seguridad, contratos/terceros/países, avisos previos, continuidad/restauración y acceso supervisor. | Tecnología, Seguridad y Riesgos. |
| Producto/usuario | Contratos y costos, consentimiento, comprobantes/extractos, reclamos, responsables, accesibilidad y circuitos de reverso. | Producto, Legal y Atención. |
| Contabilidad/datos/reportes | Cuadre, cálculos reproducibles, cortes, diseños, certificados, acuses, rectificación, secreto y archivo. | Finanzas, Impuestos y Datos. |
| Redes y contrapartes | Cuentas y acceso necesarios, contratos/admisiones y pruebas/homologación de rieles/servicios por perfil. | Tesorería e Integraciones. |
| Personal | Altas, nómina, contribuciones/FAL si corresponde, ART, seguros y formación. | RRHH e Impuestos. |
| Habilitación | Cumplimiento de condiciones y pronunciamiento SEFyC; fecha/horario y controles de primera operación. | Representantes y Operaciones. |
| Continuidad | Calendario normativo/fiscal, monitoreo, capital/liquidez/FGD, revisiones, presentación/pago y gestión de cambios. | Cada dueño institucional. |

**Casos materiales propuestos, todavía no ejecutados sobre un banco:** capital que cae por gastos/deducciones; aporte de origen no trazable; préstamo RI frente a consumidor; vivienda y comisión con tratamiento diferente; prorrata IVA; previsión contable todavía no deducible; quebranto por clase/fecha; pago propio de software frente a rendición tributaria de terceros; retención exterior sin certificado; sujeto excluido CRS condicionado; cambio de domicilio para CM; impuesto percibido y devolución; comprobante por fecha de transición; aporte FAL sin duplicar totales; reporte rechazado; datos/ROS reservados y restauración sin duplicar pagos.

## 18. Relación con la documentación y requisitos del core

| Materia de este estudio | Documentación existente a utilizar | Brecha que el expediente real debe cerrar |
|---|---|---|
| Sociedad/licencia/propietarios | [Cumplimiento](compliant.md), [ENT](functional/01-entidades-perimetro.md), [CLI](functional/03-personas-clientes-kyc.md) y [COR](functional/32-corresponsalia-baas-plataformas.md). | Operador y autorizaciones reales, cadena BF/propietarios y encuadre por función; no inferirlos de la marca. |
| Capital/liquidez/contabilidad | [LED](functional/08-ledger-contabilidad-cierres.md), [TRE](functional/17-tesoreria-liquidez.md), [RSK](functional/23-riesgos-prudencia-exposiciones.md), [RPT](functional/25-reportes-localizacion.md). | Regla por grupo/período, capital admisible, patrimonio/cartera y oráculos prudenciales/contables independientes. |
| Impuestos y comprobantes | [TAX](functional/24-tributos-recaudaciones.md), [CFG](functional/04-productos-configuracion.md), INT/CON/RPT. | Paquete por impuesto/jurisdicción/rol y diseño vigente, con pruebas de base/fecha/exención y reconciliación. |
| Gobierno y prevención | [IAM](functional/02-identidad-accesos.md), [AML](functional/20-prevencion-la-ft-fp.md), [FRD](functional/21-prevencion-fraude.md) y OPS. | Designaciones, facultades, evidencias, política por producto y segregación efectiva de persona/función. |
| Tecnología, terceros y archivo | [Arquitectura](achitecture.md), [ADR](adr/README.md), [NFR](nfr/README.md), [DAT](functional/27-auditoria-privacidad-archivo.md), [OPS](functional/30-operacion-continuidad-terceros.md), [MIG](functional/29-carga-inicial-migracion-salida.md). | Infraestructura/contratos reales, países/custodia, avisos, pruebas y recepción institucional; bulk no permite cargar saldos sin invariantes. |

Los módulos/FR ya exigen habilitación por perfil, configuración fechada y trazabilidad; no se declaran funciones ausentes sólo porque falte el caso de un banco concreto. Tampoco se declara la biblioteca implementada por agregar este estudio. No se modifican IDs ni el denominador del catálogo de 1.016 FR, ADR, NFR o controles.

Aplicar los skills locales [core-bancario-argentina](../.agents/skills/core-bancario-argentina/SKILL.md), [vigilancia](../.agents/skills/core-regulatory-watch/SKILL.md) y los coordinadores FR/NFR/ADR cuando se conviertan los hallazgos en cambios autorizados. Esta investigación temática no reinicia ni adelanta los checkpoints de la vigilancia diaria y no activa reglas productivas.

## 19. Correcciones trazables del texto de origen

| Afirmación a corregir o delimitar | Resultado del contraste |
|---|---|
| Forma jurídica art. 7 LEF | Art. 7: autorización; **art. 9: forma jurídica**. |
| Sólo 10.000 UVA de trámite | Añadir **80.000 UVA de canon** bancario; valores por fecha de cada pago, fuente A 8242/TO. |
| Banco ya inscripto antes de solicitar | Proyecto en expediente; secuencia de constitución posterior y condiciones previas a apertura. |
| Evaluación sólo por 5% | Umbrales tienen funciones distintas; no ocultan a fundadores/accionistas menores. |
| Toda sanción impide participar para siempre | Distinguir inhabilidades legales y evaluación de antecedentes/sanciones del TO. |
| Caución BCRA general de directores | Diferenciar garantía societaria de garantía de desempeño por actuación específica. |
| Piso por categoría impositiva/geográfica | Tabla bancaria consultada: **ARS 5.000 millones**, más comparación por riesgos y calidad RPC. |
| Operacional 15% de ingresos para todo banco | Régimen especial de nueva entidad durante 36 meses; luego metodología por grupo/topes. |
| Reserva legal/encaje/capital son equivalentes | Son obligaciones diferentes, con bases, fechas y efectos propios. |
| Apertura 12 meses más prórroga general idéntica | TO prevé un año desde autorización; no se verificó esa prórroga universal. |
| Previsión bancaria siempre deducible y genera activo diferido | Deducción fiscal por reglas propias; diferencia temporaria/permanente y recuperabilidad por evaluar. |
| IVA 10,5% para consumidores finales | Reducción del supuesto verificado requiere tomador **RI**; vivienda y otros beneficios tienen condiciones diferentes. |
| Banco exento de todo débito/crédito propio | Art. 7 Decreto 380 alcanza pagos propios enumerados y establece alícuotas específicas. |
| IIBB art. 8 CM es spread universal | CM distribuye; códigos locales definen base. CABA/PBA verificadas: haber de resultados sin deducción general de pasivos. |
| Sellos 1–1,5% sobre cualquier nominal | Requiere acto/hecho, jurisdicción, base, exención y posible agente; tasas diferenciadas, no promedio nacional implementable. |
| Parámetros y trámites permanecen iguales | Incorporar cambios 2026, vigencias futuras y revisión antes del expediente/apertura. |

## 20. Fuentes, fechas de verificación y límites

### 20.1 Registro de fuentes principales

Todas las consultas de este trabajo son del **16/10/2026**. Los enlaces específicos aparecen junto a los requisitos; la tabla identifica el corpus y su uso, sin presentar índices o guías como normas sustantivas.

| Autoridad / identidad | Texto o edición contrastados | Disposiciones / uso |
|---|---|---|
| Nación — LEF 21.526 | Texto actualizado oficial. | Arts. 1–10,13,15,19–21,30–33,36–41; autorización, clase, capital y deberes. |
| Nación/BCRA — Carta Orgánica | Consolidada bajo Ley 20.539 sustituida por Ley 24.144 y modificatorias; BCRA y Normativa Nacional. | Art. 14, inc. ñ y 43–49; competencia y supervisión. No confundir propuesta de reforma con ley vigente. |
| Nación — LGS 19.550 | Texto actualizado; Decreto 209/2024 para mínimo general. | Constitución, sociedades extranjeras, directorio/fiscalización/libros; capital societario distinto del bancario. |
| IGJ 15/2024 y 11/2026 | Texto actualizado y BO 22/9/2026; vigencia de 11/2026 desde 23/9. | Constitución, integración/documentación y BF; alcance territorial CABA. |
| BCRA — Autorización | TO 15/5/2025, A 8242; 47 páginas PDF y ficha de trámite. | Sec. 2/5/6/7; arancel, canon, expediente, plazos y cambios de control. |
| BCRA — Capitales mínimos | TO 11/9/2026, A 8479; 207 páginas PDF; secciones seleccionadas 1/2/7/8. | Piso, riesgos, nueva entidad, RPC y límites; complemento A 8490. |
| BCRA — Autoridades | TO 30/12/2025, A 8383; 25 páginas; A 8364. | Sec. 1–6; idoneidad, grupos A/B y garantías. |
| BCRA — Liquidez/resultados | A 8445; TO Distribución 19/3/2026, A 8410. | Alcanzados LCR/NSFR, conservación y distribuible; suplemento A 8490. |
| BCRA — Garantía depósitos | TO 5/3/2026, A 8407; Ley 24.485/Decreto 540. | Aportes, exclusiones y cobertura 50 millones desde 1/4/2026. |
| BCRA — Tecnología/digital/expansión | TI/SI 13/2/2026A 8401; SFD 2/6/2023A 7783; RRCI 17/7/2025A 8280; Expansión 29/9/2026A 8486. | Secciones pertinentes a gobierno, aviso, tercero, custodia, incidentes y locales. |
| BCRA — Cambios recientes seleccionados | A 8471(27/8), A 8473(3/9), A 8480(11/9), A 8490(8/10), A 8492(15/10/2026), cuerpos/anexos pertinentes. | Fraude, RI, FAL y versiones de capital/información; no se atribuye a todas la misma fecha de exigibilidad. |
| UIF — Ley 25.246/14/2023 | Texto actualizado,199/2024 y 78/2025; transversales según caso. | Sujeto bancario, prevención, comité, responsables, debida diligencia/reportes y DDJJ del cliente. |
| Nación — CCyC/consumo/datos | Ley 26.994,24.240,25.326/25.506 y guías/procedimientos AAIP. | Contratos, secreto/datos, información, derechos y prueba. |
| Nación/ARCA — Ganancias | Decreto 824/2019 y reglamento 862/2019 actualizados; Ley 27.802; escala oficial 2026 de una página. | Sujeto/base, tasas, incobrables, inflación, quebrantos, dividendos y exterior. |
| Nación/ARCA — IVA | Decreto 280/1997 actualizado; RG 5705 y portal IVA. | Arts. 1/3/4/7/13/28; tasas, exenciones, importación y prorrata. |
| Nación/ARCA — Créditos/débitos | Decreto 380/2001 actualizado y regímenes administrativos seleccionados. | Anexoarts.1–8/13; clientes/pagos propios y créditos. |
| Nación/ARCA — Patrimonio/otros | Ley 23.966,23.427,27.260; regímenes de participaciones y normas por estructura. | Responsable sustituto, cooperativa y derogación de mínima presunta. |
| ARCA — Retenciones e información | RG 830/3726 y modificaciones; RG 5814,5822,5855,5866,5887/2026; RG 4056 actualizada. | Separación de roles, CDI, comprobantes y reportes de cuentas. |
| Nación/ARCA — Laboral/FAL | Ley 27.541,27.802; Decreto 408; RG 5907/2026, BO 1/10, y anexo de distribución revisado visualmente. | Empleador, declaración, categoría, cuenta/ID y vigencia noviembre. |
| COMARB | Art. 8CM, RG 5/2024 completa, régimen digital y SIRCUPA; entradas SIRCREB. | Atribución territorial y recaudación; algunos accesos directos devolvieron 500, pero textos señalados se leyeron mediante navegación oficial. |
| CABA | CF Decreto 172/2026, Anexo I; 246 páginas PDF. Ley 6927 anexo consultado con modificación 6948; AGIP 173/2026. | Art. 230 y secciones Sellos; tasas/excepciones 2026 y RI derogado. |
| PBA | CF 10397 actualizado hasta reformas comprendidas 15558; Ley 15558. | CF 192; leyart.20/39; base, tasas y Sellos. |
| Competencia | Ley 27.442 y Disposición TDC 29/2026, cuerpo oficial. | Supuesto M&A y transición 17/11/2026; no autorización universal de creación orgánica. |
| Jurisdicciones restantes | Directorio COMARB y portales oficiales individualizados. | Localización/inventario; no revisión normativa bancaria completa. |

### 20.2 Evidencia y calidad de la comprobación

Se consultaron los textos oficiales y anexos pertinentes, con contraste por materia y revisión cruzada de las afirmaciones de mayor impacto. Se comprobó visualmente el anexo FAL y el art. 230 CABA. No se publican cuerpos completos de terceros, certificados personales, datos bancarios reales ni expedientes.

Referencias de contenido descargado, útiles ante URLs vivas:

| Documento | SHA-256 de descarga del 16/10/2026 |
|---|---|
| TO Autorización 47 páginas | `aa5e3e43a920c904d47e81526ea4a61ea6b683418a2d4890b3254a029e6de9c5` |
| TO Capitales mínimos 207 páginas | `5eb5a43079b7a0d5d1126bce1142ee0cecd296550762f044ef7d55f0172bebd8` |
| Escala Ganancias PJ 2026, PDF | `4e68e78d013d315c3dcd16128db334927c38967029d6132318e0a6f0f201b2bf` |
| Código Fiscal CABA 2026, PDF Anexo I | `25c7663edcb8deca5f088261dc1da81f4dc5e7658ddc659296db3a67e5204580` |

Una huella identifica bytes; no certifica autenticidad jurídica, vigencia futura o completitud del corpus. Un HTTP 200, un índice o una página genérica no prueban lectura de una norma. Se descartaron rutas fallidas y guías históricas cuando hubo texto normativo actualizado. Los accesos COMARB fallidos por descarga directa se distinguen de la lectura recuperada por navegación; no se declara la fuente entera ausente.

### 20.3 Qué debe cerrarse para un caso real

1. Perfil de accionistas/beneficiarios, productos, capital y riesgos; resolución individual y totalidad de condiciones BCRA.
2. Todas las comunicaciones posteriores a cada consolidación y normas fiscales posteriores a los hitos seleccionados, hasta fecha efectiva de presentación/apertura. No se hizo un barrido universal de cada comunicación/resolución histórica.
3. Legajo fiscal de cada jurisdicción/municipio activado; 22 provincias tienen entrada localizada sin análisis integral de 2026. CABA/PBA tampoco equivalen a examen de todas las operaciones posibles.
4. CDI, pagos intragrupo, nacionalidad/residencia, beneficios regionales, exenciones/cooperativa y situación laboral concretos; normativa de cada servicio complementario.
5. Regla contable vigente que concrete reserva legal, estados/proyecciones, tratamiento de pérdidas y controles prudenciales; no se cierra su vigencia sólo con una comunicación histórica de 1984.
6. Contratos, designaciones y pruebas efectivas de sistemas/operación, registro de presentaciones/pagos, auditorías y habilitación. No se ejecutaron trámites, declaraciones, pruebas bancarias ni presentaciones oficiales.

La creación del documento o su integración al repositorio no constituye autorización bancaria ni aceptación por una entidad, un registro o una autoridad fiscal.
