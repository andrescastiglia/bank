# Informe de análisis y datos relevados — Bank

**Corte vigente: 20/10/2026 22:47:55**, zona `America/Buenos_Aires` (`21/10/2026 01:47:55 UTC`). **Corrida:** `RUN-20261021T014755Z`. **Main comprobado:** `f7d9495a172bcc9b2a68371a05509a664f12748d`, con conector GitHub y Git. Inventario `2026-10-16.2`. **Resultado global: PARTIAL**. La PR #9 sigue abierta y se amplía; no se atribuye implementación o aceptación institucional a esa propuesta.

## Alcance y conclusiones del corte del 20/10

Se recuperaron desde GitHub siete corridas reales, 40 entradas históricas de cambios y16 de agenda. El seed no constituye cobertura. Ventana solicitada **[15/10/2026 00:00:00 −03:00, 20/10/2026 22:47:55 −03:00)**: todos los gaps y solapamiento configurado de siete días limitado por el comienzo del backfill. Se preservan fechas reales de consulta y las fechas sin hora de cada documento; la observación posterior al corte no cambia su fecha de emisión/publicación.

| Eje prioritario | Hallazgo verificado | Conclusión y brecha |
|---|---|---|
| Legal y normativo | BCRA C102451 corrige versiones de hojas A8493; B13251 publica referencia de tarjetas para emisores no financieros; Decreto 1228 prorroga FAL y modifica carencia. | Mantener rectificatorias, ciclos y disparadores individuales. El antecedente FAL de LEGAL_TAX necesita actualización fechada; no mover automáticamente todos los procedimientos ARCA. |
| Mercado | Siete ofertas reconsultadas; los nuevos datos delimitan financiación de tarjetas y una transición de FAL/vehículos de inversión. | Oportunidad de configuración e integración por rol, sin asumir licencia de emisor/administrador ni lanzar un producto FAL por una prórroga. No se verificaron nuevos precios, cuotas auditadas u homologaciones argentinas. |
| Tecnología | Avisos de mantenimiento basic-toml y fallos Wasmtime/Cranelift, además de trust stores Rust. | Lenguaje, sandbox e imagen mínima requieren dependencias/targets/features y pruebas efectivas. Bank no seleccionó un runtime Wasm ni permite scripting monetario arbitrario. |
| Seguridad, crítico | RustSec0381/0382/0383 comparten CVE de confianza TLS, con componentes distintos; seis altas KEV20/10 y seis avisos Wasmtime. | Priorizar inventario y origen efectivo de confianza, también en binarios scratch. Sin artefacto desplegado no hay exposición ni parcheo confirmado. Plazos CISA no son plazos argentinos. |

## 1. Aspectos legales y normativos

### 1.1 BCRA: fe de erratas y referencia por ciclo

La [C102451](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/C102451.pdf), emitida **20/10**, contiene cuatro páginas y reemplaza tres hojas A8493 para corregir su versión: sección1 página3 **6a→1a**; sección5 página2 **7a→3a**; sección7 página16 **11a→2a**. Se compararon las hojas y párrafos pertinentes; **vigencia 1/11/2026 permanece**, sin reforma de fondo identificada en ese cotejo. Se [actualiza el análisis A8493](regulatory/BCRA-A8493-2026.md), conservando comunicación original y relación de rectificación; no se crea una segunda obligación monetaria ni se cambia su calendario por una corrección editorial. Publicación BO independiente no verificada.

La [B13251](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/B13251.pdf), emitida **20/10**, está dirigida a **empresas no financieras emisoras de tarjetas de crédito/compra**. Su anexo comunica **63,15% TNA**, promedio de préstamos personales sin garantía real, información de octubre para operaciones del **ciclo de facturación de noviembre**. Se contrastó TO `t-tasint`, sección2.1.2 y contexto: ese dato de referencia no es la tasa pactada ni el límite final aislado; la regla dice «no superar en más del25%» al promedio, no sumar25 puntos. No copiar este régimen a EF u otros préstamos/tarjetas.

El [análisis B13251](regulatory/BCRA-B13251-2026.md) propone selector por sujeto/producto/ciclo, referencia exacta y evidencia de aprobación; casos de borde y recálculo sin reescritura. `published_at=null`; la operación del ciclo es el disparador y no se inventa vigencia universal a medianoche del1/11. Faltan operador, contratos/ciclos reales, verificación integral de modificaciones posteriores al TO y pruebas de cálculo.

La consulta BCRA por emisión15–20/10, tipos A/B/C/P sin restricción, devuelve **27 registros, página1/1**. Se recuperaron **27/27 PDF,69 páginas**, anexos integrados. Los19 documentos del conjunto anterior mantienen sus huellas. Además de B13251/C102451, los nuevos C102445–449 publican estadísticas/referencias con fechas propias: no son cinco reformas generales ni tasas a instalar en todos los contratos. C102450 es una suspensión individual de operaciones de cambio: se registra su identidad y fuente, sin publicar datos del expediente o convertirla en prohibición general. Su eventual efecto requiere contraparte/operador efectivamente alcanzado y encuadre revisado. El texto exige autorización previa BCRA para cursar operaciones de cambio o anulaciones a nombre/por cuenta de las personas individualizadas, y abstenerse de transmitir al exterior las formalizadas pendientes de aviso. Mapear FR-FXT-003/005/006/016 y CTL-03/09/12, con identidad/alcance verificados en circuito restringido y revisión de pendientes antes de enviar; no congelar todas las cuentas o personas por analogía. Sin operador/caso concreto, queda candidato de aplicabilidad, sin activar una lista o regla productiva.

B13250, ya analizada y con primer valor de serie20/10, obtuvo [procedencia BO20/10](https://www.boletinoficial.gob.ar/detalleAviso/primera/349343/20261020?anexos=1). Su anexo gráfico fue recuperado y revisado visualmente; conservar nueva huella/representación y fecha de publicación. La fecha del documento gráfico no reemplaza la emisión de la comunicación; **cotejo automatizado de todos los valores pendiente**, sin declarar una rectificatoria económica probada.

### 1.2 Decreto 1228: FAL, carencia y armonización pendiente

El [Decreto 1228/2026](https://www.boletinoficial.gob.ar/detalleAviso/primera/349294/20261020), emitido **19/10**, publicado/vigente **20/10**, sustituye arts.15 y27 del Decreto 408. Comienzo del régimen FAL: **1/12/2026** en reemplazo del antecedente1/11. Carencia mínima: **doce períodos mensuales completos y consecutivos de devengamiento y pago**, contados desde el mes de registro ante ARCA de la **efectiva primera contribución del empleador**. No calcularla desde publicación, solicitud, apertura de cuenta o un pago sólo ordenado.

Se leyó Decreto 408 original y RG 5907, especialmente art.19; su texto recuperado aún indica noviembre para vigencia/devengado y versión48 para ciertas presentaciones de períodos anteriores. **Queda pendiente armonización fiscal/legal**: no trasladar automáticamente un mes todos los procedimientos, registros y sistemas. La [actualización de LEGAL_TAX §11](docs/LEGAL_TAX.md#11-empleador-y-transición-fal) conserva el antecedente fechado y añade el cambio, sin hacer pasar la base de16/10 por una evaluación originalmente realizada el20.

El [análisis acotado](regulatory/PEN-DECRETO1228-2026.md) separa empleador privado, proveedor tecnológico y rol financiero habilitado (instrumentación/administración/custodia/inversión). La prórroga no habilita esos roles ni prueba suspensión del tratamiento prudencial A8490. Faltan sujeto, rol, evento individual y revisión integral CNV/UIF/ARCA relacionados; no activar todos los perfiles ni inventar final de carencia.

### 1.3 Otros organismos y agenda

Se reconsultaron UIF sectorial y transversal, AAIP, ARCA, COMARB/SIRCREB/SIRCUPA y CNV. Se leyó también [RG 5913, BO20/10](https://www.boletinoficial.gob.ar/detalleAviso/primera/349317/20261020): abroga RG3983(DGI) y4003(DGI) con vigencia de publicación, referidas al régimen de empresas de servicios eventuales. Es un candidato condicionado al encuadre laboral/contratación real; no una derogación general de retenciones de Ganancias o de todo control del core. No se configura nómina por leer ese acto.

La agenda conserva RG5908, A8492/A8493, A8487, COMARB DP11, RPI, CNV1172/1173, B13248 y series ICL/UVI, junto al disparador CGN/TGN pendiente. No se repiten alertas de esas normas como nuevas. Se incorpora el comienzo FAL1/12 y se conserva pendiente su disparador individual. Los plazos concretos de declaraciones y ciclos requieren sujeto/período/documentación; ninguna PR sustituye esa decisión.

## 2. Mercado y competencia

Se reconsultaron [Mambu](https://mambu.com/en), [Pismo](https://developers.pismo.io/pismo-docs/docs/welcome), [Bantotal](https://www.bantotal.com/), [Topaz](https://www.topazevolution.com/), [Temenos](https://www.temenos.com/products/core-banking/), [Vault Core](https://www.thoughtmachine.net/vault-core) y [Fineract](https://fineract.apache.org/). Sus páginas permiten contrastar oferta declarada de productos/composición, APIs/eventos, pagos/tarjetas, tesorería y reportes, según proveedor. La descarga de una portada no demuestra roadmap implementado, precio, soporte local ni homologación. No se verificó un lanzamiento comercial nuevo que justifique una alerta adicional.

| Capacidad / modelo de oferta | Correspondencia con Bank | Decisión que la evidencia exige |
|---|---|---|
| Composición de productos y configuración: Mambu/Vault/Fineract | CFG/CRD/INT/ACC, ADR-01/05 | Demostrar referencia versus precio, ciclo/contrato y reproducción histórica. La propuesta no habilita fórmulas monetarias arbitrarias de terceros. |
| APIs, eventos y operación de pagos/tarjetas: Pismo/Topaz/Temenos | ASY/PAY/CRD/REC, ADR-03/06 | Mostrar estados y conciliación, rechazos por perfil y límites de dependencia. Comparar latencia/capacidad con el mismo escenario y costo. |
| Localización y amplitud bancaria regional: Bantotal/Topaz/Temenos | TAX/RPT/TRE/OPS | Evidenciar normas/versiones, soporte y responsabilidades por sociedad/rol. «Regional» no acredita cobertura argentina integral. |
| Integración de vehículos FAL y transición regulatoria | INV/TRE/TAX/RPT/CON, extensión condicionada | Validar primero administrador/vehículo/contrato, interfaces y economía del servicio. Una prórroga no prueba demanda, licencia o rentabilidad ni justifica afirmar soporte ya disponible. |
| Migración y servicio profesional sobre GPLv2 | MIG/OPS, ADR-08 | Carga inicial con manifiesto, conciliación, recuperación y salida; TCO real de operación/soporte, sin convertir una comparación cualitativa en ventaja de precio cuantificada. |

**Conclusión comercial:** trazabilidad de transiciones, soporte de integración y evidencia de calidad siguen siendo diferenciales a demostrar. La referencia B13251 y la prórroga FAL son hechos regulatorios del mercado, no precios de Bank. Mantener las condiciones BNA del corte anterior como antecedente de producto específico; no generalizarlas ni repetirlas como novedad del20.

## 3. Innovación tecnológica y arquitectura

Se reconsultaron Rust estable/feed, PostgreSQL, FAPI y ASVS. No se verificó una nueva versión de plataforma aplicable que sustituya el análisis previo por el simple cambio de HTML/feed. [RustSec0374](https://rustsec.org/advisories/RUSTSEC-2026-0374.html) es **INFO de mantenimiento**: basic-toml no mantenido, Reported26/9 e Issued20/10; no se lo presenta como exploit. El registro orienta a alternativas, sin adoptarlas automáticamente.

Las novedades refuerzan tres decisiones de arquitectura existentes: ADR-05 necesita distinguir referencia, regla, ciclo y fecha de conocimiento; ADR-07 debe inventariar backend TLS y raíces efectivas, además del crate; ADR-06 debe tratar un runtime de plugins como frontera a probar y no garantía de aislamiento. Wasmtime no es una dependencia seleccionada de Bank ni condición necesaria para usar Rust.

Para trabajos no urgentes, propuesta de preparación asíncrona durable de expedientes, ingesta de referencias, simulación y conciliación con manifiesto/cursor. La selección financiera al ejecutar usa versión aplicable local, sin consultar portales bajo lock ni tratar un `202` como operación liquidada. Carga inicial: ADR-08 conserva staging y publicación controlada; no ejecuta pagos/avisos históricos por replay ni importa automáticamente un trust store o calendario vigente sobre toda la historia.

La base sigue sin Cargo.toml/Cargo.lock, fuentes Rust o Dockerfile propio de producto. El contrato `FROM scratch` requiere prueba de ELF/payload/TLS/DNS/usuario/rotación en el digest final; no hubo build, benchmark o scan de producto. Rust seguro no corrige por sí solo un trust anchor obsoleto, un compilador de sandbox vulnerable o un cálculo financiero incorrecto.

## 4. Seguridad informática — eje crítico

### 4.1 TLS: una familia relacionada con tres componentes

Se leyeron fichas y registros oficiales [0381](https://rustsec.org/advisories/RUSTSEC-2026-0381.html), [0382](https://rustsec.org/advisories/RUSTSEC-2026-0382.html) y [0383](https://rustsec.org/advisories/RUSTSEC-2026-0383.html), y PR upstream pertinentes. Comparten **CVE-2026-111943**, conservando tres identidades: webpki-roots, rustls-webpki y webpki-root-certs. Las fuentes señalan aceptación posible de cadenas por intermediarias emSign de confianza retirada, con claves privadas conocidas, **si las raíces/configuración permiten ese camino**. Issued20/10; Reported19/10 para roots/certs y20/10 para verificador; sin hora exacta.

Correcciones declaradas: roots/certs **>=1.0.10**; rustls-webpki **>=0.103.16,<0.104.0-alpha.1** o **>=0.104.0-alpha.8**. No recomendar prerelease por defecto. El [análisis TLS](regulatory/RUSTSEC-2026-0381-0383.md) propone inventariar versiones transitivas y origen de confianza. Un bundle del sistema actualizado no prueba remediación de raíces compiladas ni del artefacto restaurado; no se desactiva validación de cadena/nombre. Sin código/digest no hay exposición confirmada.

### 4.2 Wasmtime: protocolos, tipos y escapes condicionales

Se recuperaron seis fichas/registros RustSec y **seis GHSA HTML oficiales**. La API GHSA devolvió404 y se conserva ese intento, sin afirmar que faltó todo acceso al aviso. [Análisis0375–0380](regulatory/RUSTSEC-2026-0375-0380.md): framing HTTP inválido/smuggling condicionado al receptor, trailers que eluden hook, panic por un recorrido concreto de streams/futures con tipos borrados, y dos fallos críticos de Cranelift con posible escape del sandbox.

Los críticos distinguen **aarch64/br_table** (0379) de **bit-packing SSA anterior a43, cualquier arquitectura** (0380). Los rangos corregidos no son idénticos. En0377, el embedder que personalizó `is_forbidden_header` debe revisar `forbidden_header_filter`: actualizar el número de versión puede ser insuficiente para conservar la política de trailers. Upstream indica que no conoce ataque habilitado por0377; no se transforma esa advertencia en explotación observada.

### 4.3 KEV: explotación conocida, inventario todavía desconocido

[CISA KEV](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json), versión**2026.10.20**, `dateReleased=2026-10-20T19:00:31.8765Z`,1754 entradas, incorpora **seis altas20/10**: SiteGuard Server Edition CVE-2026-106931, cuatro CVE de Plex Media Server y Siemens Software Center CVE-2026-110936. Se leyeron los avisos de proveedores y el [análisis específico](regulatory/CISA-KEV-20261020.md) conserva versiones, precondiciones y procedencias. La alta KEV no es la fecha de publicación inicial o primer parche.

SiteGuard exige revisar variante/estadísticas y preservación del diagnóstico; no se extiende a todas sus ediciones. Plex tiene cadena de fallos con explotación declarada por proveedor, sin motivo para instalarlo en el core. Siemens requiere producto/versión y escenario local autenticado. Revisar perímetro, puestos de administración, NAS y terceros si esos activos existen: no se presume presencia ni compromiso de Bank. `Unknown` para ransomware no equivale a ausencia de explotación. **`dueDate`/BOD CISA no se convierten en plazos legales argentinos.**

### 4.4 Evaluación de vectores y evidencia necesaria

| Escenario bancario | Control / propuesta | Evidencia pendiente |
|---|---|---|
| Suplantación de API/KMS/webhook/telemetría mediante cadena TLS aceptada indebidamente | NFR-05-C04, ADR-07, CTL-10/15; origen efectivo de confianza, versiones y digest | PKI sintética válida/denegada, rutas alternativas, raíces compiladas/montadas, rotación y rollback; nunca certificados de clientes. |
| Guest/plugin con escape, tipo borrado o framing HTTP conflictivo | ADR-06/07, NFR-03/05/08; backend/target/features, hooks y cuotas | Ensayo aislado del host/proxy con corpus revisado, oráculo de efectos fuera del guest; no sólo «no crash». |
| BOLA/BFLA, replay y privilegios en servicios asíncronos | NFR-05, ADR-02/03/06, CTL-04/09/17; revalidación por entidad/cuenta/objeto, idempotencia | Casos negativos, revocación concurrente, referencias ajenas y worker atrasado; sin producto: no evaluado. |
| Compromiso del perímetro/puesto y movimiento lateral a backups/identidad | FR-OPS, NFR-02/05/12, CTL-13/14/15/16 | Inventario/versiones/exposición, segmentación, triage y restauración limpia según investigación; no borrar evidencia por parchear primero. |
| Documentación firmada, BF/PEP y reportes sensibles | NFR-06/07/11; CTL-07/09/11/19; fuente, finalidad, retención y facultad | Artefactos restringidos con destinatario autorizado; ningún secreto, ROS o dato de clientes en este repositorio. |

ISO/PCI/Swift/NIST/FAPI/OWASP mantienen naturaleza y activador propios; no se leyó ni copió material comercial restringido. No se hizo pentest, explotación, escaneo de red, intervención productiva, presentación o contacto con terceros/reguladores.

## 5. Trazabilidad, cobertura real y validación

| Hallazgo | Documentación y perfiles/FR | NFR/ADR/CTL/skills y decisión pendiente |
|---|---|---|
| C102451→A8493 | compliant.md PAY-11/LAW-10; TRE/RPT/OPS y expediente MEP; participante habilitado | NFR-07/09/11, ADR-05, CTL-11/12/19; cumplimiento/configuración. Conservar hojas originales/rectificadas sin doble aplicación. |
| B13251 | compliant.md LAW-09/BCRA-F07/PAY-10; FR-CRD-001/002/017/018/021, FR-INT-001/002/006/009/014/017 y FR-CFG-011 | NFR-01/09/11/13, ADR-05, CTL-02/06/18/19; confirmar emisor, ciclo, fórmula y pruebas. |
| Decreto 1228 | LEGAL_TAX §11, FR-ENT-031, FR-TAX-001/002/018/030/031, FR-RPT-001/007/009/010/038; INV/TRE según rol | NFR-01/04/07/09/11/12, ADR-05, CTL-02/05/06/14/19; armonización normativa y primer aporte registrado pendientes. |
| TLS/Wasmtime/KEV | Contrato Rust/scratch; FR-OPS-001/024/025/026 y los casos de integración/migración de cada análisis | NFR-02/03/05/07/08/09/10/12, ADR-04/05/06/07/08, CTL-09/10/13/14/15/16/17/20; skills seguridad/stack existentes. Inventario y pruebas del artefacto pendientes. |

| Fuente | Cobertura actual | Checkpoint / continuidad |
|---|---|---|
| BCRA A/B/C/P | **COMPLETE** para emisión15–20/10 y ventana declarada:1página,27 registros/27PDF/69páginas, anexos integrados. | Avanza desde19/10 22:08:02 a20/10 22:47:55 −03; sólo esa fuente/filtro, con solapamiento para indexaciones tardías. |
| BO primera sección | **PARTIAL**: índices15/16,19 y20;19 recupera106URLs al unir9rubros (incluidas6 faltantes y sus cuerpos);20 muestra61. Un anexo UVI adicional recuperado/revisado visualmente. | Se cierra el gap de enumeración19, **no** cuerpos/anexos/suplementos. Tres anexos de los seis cuerpos recuperados y37 lecturas sustantivas anteriores pendientes, más cuerpos/anexos de20 y extraordinarias.17/18 redirigen portada; no acredita ausencia. |
| BCRA TO/RI | **PARTIAL**: facetas103/55 reconsultadas, t-optico y t-tasint recuperados; cotejo C102451/A8493. | Restantes textos/versiones/modificatorias y anexos pendientes; cortes nulos. |
| UIF/AAIP/ARCA/CNV | **PARTIAL**, entradas oficiales y cuerpos seleccionados descritos. | Cronología/anexos no completados por obtener índices o un acto; sin avance de corte. |
| COMARB/SIRCREB/SIRCUPA | **UNAVAILABLE** en sus rutas propias,500 persistente; DP11 leído en corrida anterior sigue registrado. | No vuelve a declararse desconocido el cuerpo DP11 recuperado; resto de cobertura/calendarios pendientes, corte nulo. |
| Jurisdicciones | Opcional omitida, checkpoint y fundamento anteriores íntegros. | Sin operador/jurisdicciones activadas; candidatos locales no acreditan cobertura universal. |
| Estándares/seguridad | **PARTIAL**, índices y avisos seleccionados revisados. | No todos los estándares/transiciones ni inventario desplegado/contratos de red; sin checkpoint completo. |

La nueva evidencia y estado se conservan en [RUN-20261021T014755Z](https://github.com/andrescastiglia/bank/blob/659cbd9220d4d93960d03c5889013959f2b57657/.regulatory-watch/evidence/RUN-20261021T014755Z.json), rama `automation/regulatory-state`: filtros, intentos404/500, URL final, fecha de consulta, huellas, páginas, anexos y relaciones. Historiales de cambios/agenda/índice se preservan como prefijos exactos; la corrida se añade una sola vez. Descargar/anunciar/abrir PR no equivale a cubrir toda una fuente ni a implementar.

**Validación ejecutada:** catálogo reproducible (1016 FR/32 módulos), inventario y 69 fixtures de vigilancia; transición `--state --run --previous-state`; 119 huellas de descargas/decodificaciones y109 referencias FR del informe/análisis/LEGAL_TAX contrastadas, incluidas abreviaciones. Se comprueban además enlaces y estructura documental antes de publicar. Estos checks validan documentos/integridad, no la eficacia del producto. Las pruebas materiales propuestas no se ejecutaron; no hay afirmación de cumplimiento, rendimiento, parcheo, homologación o aceptación institucional. No se verificaron rulesets/permisos técnicos en esta corrida. GNU GPLv2 y merge exclusivo del mantenedor permanecen vigentes.

---

## Antecedente íntegro — corte del 19/10

El contenido siguiente conserva fechas y resultados anteriores. Sus cifras y fallas corresponden a sus propias corridas; prevalece el nuevo corte anterior.

**Corte vigente:** **19/10/2026 22:08:02**, `America/Buenos_Aires` (`20/10/2026 01:08:02 UTC`). **Corrida:** `RUN-20261020T010802Z`. **Base comprobada por conector GitHub y Git:** `main f7d9495a172bcc9b2a68371a05509a664f12748d`. Inventario `2026-10-16.2`. **Resultado global: PARTIAL**. Se amplía la **PR #9**, sin merge ni cambios en `main`, licencia, permisos o despliegue.

## Alcance y conclusión del nuevo corte

Se recuperaron seis corridas reales, 33 entradas de cambios y ocho hitos desde `automation/regulatory-state`; el seed no se cuenta como cobertura. Ventana solicitada: **[15/10/2026 00:00:00 −03:00, 19/10/2026 22:08:02 −03:00)**, incluidos todos los pendientes y solapamiento de siete días limitado por el inicio. Las consultas posteriores al corte conservan su fecha real. No se atribuye hora a normas que sólo muestran día.

Se verificó una nueva **actualización consolidada MEP A8493**, se recuperó el texto oficial del candidato **COMARB DP11**, y se incorporaron hitos de normas anteriores: **Ganancias PJ desde hoy**, **firma/trámites MEP desde noviembre** y **feriado bancario 10/11**. Además se verificó una disposición del **RPI Capital Federal**, de aplicación condicionada. Los análisis distinguen obligaciones de la sociedad operadora, del participante/profesional y del proveedor tecnológico.

| Eje | Evidencia relevada | Conclusión / brecha material |
|---|---|---|
| Legal/normativo | BCRA: 19 registros A/B/C/P, 19 PDF y 52 páginas; A8493 y antecedentes; BO19 y actos seleccionados; RG5908/4626, COMARB DP11, RPI DTR11 y anexos. | Falta vincular calendarios, firma/canal, sociedad/rol y expedientes a implementación y responsables. No convertir consolidado en obligación nueva universal ni confundir regímenes fiscales. |
| Mercado | Siete páginas de oferta reconsultadas y aviso BNA publicado en BO19. | Las tasas y condiciones de un banco son datos competitivos específicos. Priorizar producto configurable con historia, integración y evidencia de operación; no copiar una tarifa a todos los clientes ni anunciar homologación local no probada. |
| Tecnología | Rust estable, feed, PostgreSQL, FAPI, ASVS y versiones TO consultados. | No se verificó un lanzamiento técnico relevante adicional frente a la corrida anterior. La configuración por vigencia y la separación entre aceptación local y liquidación externa siguen siendo decisiones centrales. |
| Seguridad, crítico | RustSec y CISA KEV con las mismas huellas; nuevas condiciones verificadas de firma/identidad y contingencia MEP. | No hay un aviso nuevo en esos dos índices consultados. Sí debe evaluarse el circuito de firmas/mandatos y la recuperación frente a canales caídos; una imagen scratch o un PDF firmado no acreditan por sí solos autorización ni continuidad. |

## 1. Aspectos legales y normativos

### 1.1 MEP: consolidación, antecedentes y fechas diferentes

[A8493](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8493.pdf), emitida **19/10**, distribuye hojas de reemplazo con vigencia **1/11/2026**; se leyeron sus 17 páginas y correlaciones. La publicación BO independiente no se verificó. Remite a A8474, B13105 y B13164, recuperadas con sus anexos: firma/canales y contingencia; V04/DZ5; D22/GC3/GB3. Las dos B ya indicaban producción **26/1** y **24/4**, respectivamente: no se las fecha como funcionalidades nuevas de octubre ni se difiere su efecto a noviembre.

El [análisis específico](regulatory/BCRA-A8493-2026.md) delimita IDEAR, firma digital Ley25.506, alternativa GDE para sujetos habilitados y papel excepcional; registro de firmantes; pruebas de operatorias y contingencia física BCRA como último recurso sujeto a conformidad y disponibilidad. No se accedió a Extranet/manual reservado ni se enviaron notas. No se presupone participación MEP por tener una cuenta de pago o por desarrollar software.

**Brecha:** PAY-11/LAW-10, los módulos TRE/PAY/RPT/OPS y NFR existentes establecen capacidades generales, pero no un expediente MEP probado con firmante, facultad, canal y recuperación. El TO oficial `t-snp-mep.pdf` todavía identifica A8343, 14/10/2025; firmas A8414 y cuentas BCRA A8131. Conservar versiones y modificaciones fechadas; un TO recuperado no garantiza consolidación de todas las comunicaciones posteriores. Se identificó y excluyó como vigente el archivo legado `t-mep.pdf` de 2014.

### 1.2 Ganancias PJ: un hito vigente, sin nuevo vencimiento general

[RG5908](https://www.argentina.gob.ar/normativa/nacional/norma-430864/texto) fue emitida **1/10**, publicada/vigente **5/10**; su servicio comienza **19/10**. Se contrastó el [BO](https://www.boletinoficial.gob.ar/detalleAviso/primera/348496/20261005), RG4626 actualizada y la [guía ARCA](https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-juridicas/declaracion-jurada/presentacion.asp). Para sujetos RG4626 y cierres desde junio de 2026, etapa opcional **19/10–28/2/2027**, obligatoria **1/3/2027**; cierres anteriores continúan en aplicativo y rectificativas conservan el medio de la original conforme art.3. Analizar conjuntamente excepciones y transición.

La norma cambia el canal de confección/presentación F.713, no una alícuota ni el vencimiento particular del impuesto. Falta sociedad, cierre, CUIT, originales y mandato para asignarlo. No confundir impuesto propio de la sociedad con retenciones a clientes. El [expediente propuesto](regulatory/ARCA-RG5908-2026.md) mapea TAX/RPT, documentos históricos, canal original y acuses; no inventa API ni delegación para presentar.

### 1.3 COMARB DP11: candidato recuperado por fuente oficial alternativa

El [BO19](https://www.boletinoficial.gob.ar/detalleAviso/primera/349247/20261019) permitió leer íntegramente la disposición emitida **16/10**, publicada **19/10**, sin anexo anunciado. La caída del dominio COMARB no impide verificar este acto por BO, pero tampoco queda resuelta la cobertura general COMARB/SIRCREB/SIRCUPA.

- **SIRCAR:** segunda quincena de octubre, fechas 9 y 10/11 pasan a **13/11 inclusive**.
- **SIRTAC:** misma quincena, agentes cuyo dígito verificador CUIT termina en **5–9**, fecha 11/11 pasa a **13/11**.
- **SIFERE:** anticipo octubre, **17–20/11**, con distribución según calendario aplicable todavía por verificar para cada CUIT.

No se modifica por analogía SIRCREB/SIRCUPA, alícuotas, padrones o todos los vencimientos IIBB. La norma no fija un inicio general separado; se registran sus fechas específicas, sin asignar una obligación individual desconocida. [Análisis y casos](regulatory/COMARB-DP11-2026.md): calendario versionado, designación/sistema/período/CUIT y exclusión de perfiles semejantes no alcanzados.

### 1.4 Agenda bancaria y perímetro inmobiliario

[A8487](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8487.pdf), emitida **1/10**, [publicada 5/10](https://www.boletinoficial.gob.ar/detalleAviso/primera/348507/20261005), establece **feriado bancario nacional 10/11/2026**. Se verificó texto primario, sin derivarlo de noticias o del considerando COMARB. El [análisis](regulatory/BCRA-A8487-2026.md) propone distinguir riel, producto, atención y calendario: no cerrar todas las APIs ni extender automáticamente todos los plazos fiscales/contractuales.

La [DTR11 RPI Capital Federal](https://www.boletinoficial.gob.ar/detalleAviso/primera/349248/20261019?anexos=1), emitida **16/10**, publicada **19/10**, vigente **8/11**, fue leída con **2/2 anexos**. Delimita actividades específicas, profesionales sujetos obligados, PEP/BF, excepciones y formularios; deroga cuatro disposiciones anteriores. El [análisis de alcance](regulatory/RPI-CABA-DTR11-2026.md) conserva la dependencia UIF93 y revisión competente: no es el régimen AML universal de bancos ni cobertura de todas las provincias. Impacto potencial en documentación de inmuebles y operaciones efectivamente presentadas allí, sin activar una jurisdicción del operador aún no definida.

### 1.5 Publicación adicional y datos de referencia

Se verificó publicación BO **19/10** de [B13248](https://www.boletinoficial.gob.ar/detalleAviso/primera/349258/20261019) y [B13249](https://www.boletinoficial.gob.ar/detalleAviso/primera/349259/20261019?anexos=1), ya analizadas por sus PDF BCRA. Se incorporan como procedencias y fechas verificadas, sin generar una segunda norma o repetir alertas. B13249 tiene anexo BO recuperado, tabla revisada visualmente y metadatos separados del PDF BCRA; la representación y huella diferentes no se descartan como duplicado. El cotejo automatizado valor por valor sigue pendiente; se registra relación y revisión de representación, no rectificatoria sustantiva probada.

C102441/442 publican reservas/pasivos al 15/10; C102443 tipo de cambio de referencia del 19/10; C102444 tasas y series con anexos, algunas fechas hasta el 20. Son datos oficiales distintos de reformas generales. No se copian valores a parámetros productivos ni se toma el tipo A3500 como precio universal de una operación. Manifestación, fecha observada y fecha de cada valor deben conservarse separadas. Continúan los hitos anteriores A8492, B13248, CNV1172/1173, ICL/UVI y el disparador particular CGN/TGN; no se inventa un vencimiento documental a partir de publicación.

## 2. Mercado y competencia

Se reconsultaron [Mambu](https://mambu.com/en), [Pismo](https://developers.pismo.io/pismo-docs/docs/welcome), [Bantotal](https://www.bantotal.com/), [Topaz](https://www.topazevolution.com/), [Temenos](https://www.temenos.com/products/core-banking/), [Vault Core](https://www.thoughtmachine.net/vault-core) y [Apache Fineract](https://fineract.apache.org/). Son ofertas declaradas por sus proveedores/comunidad; no se obtuvo evidencia nueva de precio comparable, cuota auditada, soporte contractual argentino o homologación. Variaciones de HTML quedan registradas; no se convierten automáticamente en lanzamiento o mejora.

| Capacidad competitiva a considerar | Relación con Bank | Evidencia/criterio que falta |
|---|---|---|
| Composición de productos, préstamos y depósitos: Mambu, Vault, Fineract | CFG/CRD/ACC/INT, ADR-01/05 | Mostrar un cambio contractual fechado, cálculo reproducible y migración sin bifurcación por cliente; no incorporar scripting monetario arbitrario. |
| APIs, eventos e integración de pagos/tarjetas: Pismo, Topaz y Temenos | ASY/PAY/CAR, ADR-03/06 | Contratos, límites de consumo, semántica de aceptación, orden y reconciliación por riel. Comparar latencia con mismo volumen/entorno. |
| Amplitud regional y operación bancaria: Bantotal/Topaz/Temenos | TAX/RPT/TRE/OPS | Localización por sociedad/rol, catálogos de fecha efectiva, soporte de incidentes, homologación y evidencia concreta. La marca regional no demuestra cumplimiento argentino integral. |
| Migración y costo total | MIG/OPS, ADR-08; licencia GPLv2 | Ensayo de carga inicial, conciliación, salida/exportación, costo de infraestructura/soporte y operación. No se verificaron tarifas que permitan afirmar una ventaja económica cuantificada. |

El [aviso BNA BO19](https://www.boletinoficial.gob.ar/detalleAviso/primera/349257/20261019) publica condiciones de adelantos con caución de certificados de obra e intereses mensuales vencidos: TAMAR de cinco días hábiles anteriores al inicio del período más un spread diferenciado según condición MiPyME. Es una referencia de oferta de **ese banco/producto**, con antecedentes desde enero y tasas publicadas para octubre; no un lanzamiento del día ni un mandato para todos los bancos. Refuerza la necesidad de índice/fecha de observación, calendario, clasificación documentada y spread contractual versionado en CRD/INT/CFG. No adoptar esas condiciones sin contrato y encuadre del producto.

**Conclusión comercial:** la oportunidad de Bank sigue dependiendo de demostrar localización, continuidad y trazabilidad, además de amplitud funcional. No se puede sostener todavía «100% conforme», menor costo o latencia superior a competidores. El diagnóstico y la matriz históricos posteriores amplían segmentación y modelos de atención, con sus fechas originales.

## 3. Innovación tecnológica y arquitectura

El manifiesto estable Rust, PostgreSQL y FAPI conservan huellas previas; el feed Rust cambió metadatos pero su entrada más reciente continúa Rust1.99.1 ya analizada. ASVS y algunas páginas comerciales cambian representación: no se verificó una nueva edición técnica relevante a partir de ello. No se eligió biblioteca nueva, se ejecutó código descargado o modificó el stack Rust/scratch.

Los datos primarios nuevos concretan desafíos de diseño ya presentes:

| Problema | Propuesta técnica dentro de la arquitectura existente | Aceptación pendiente |
|---|---|---|
| Canal fiscal/documental cambia por ejercicio/original y fecha | ADR-05: paquete local versionado por sociedad/rol/período y original; preparar y validar en trabajos asíncronos con expediente. | Casos fronterizos y rectificativas; preservar canal y acuses históricos. No consultar una página remota mientras se bloquea dinero. |
| Instrucción MEP inmediata frente a tareas diferibles | ADR-02/03: persistencia e idempotencia para el efecto financiero; colas durables para archivo, conciliación y tareas no urgentes. | No convertir V04 en crédito eventual sin respetar la exigencia de acreditación inmediata aplicable; medir extremo a extremo y no prometer plazo arbitrario. |
| Contingencia depende de firma, facultades, red y actuación institucional | ADR-04/06: recuperar servicio completo y expediente, con aislamiento del emisor anterior y conciliación. | Simular canal caído, resultado externo ambiguo, credencial revocada y reapertura; un cambio de pod no demuestra recuperación. |
| Importación inicial y referencias financieras | ADR-08: staging, manifiesto, cobertura, validación y publicación controlada de cohortes. | No ejecutar pagos/avisos históricos al cargar; conservar fuente/fecha de índices y reglas, separar PREPARED de datos operativos. |

La inspección de la base sigue sin aplicación propia Rust/Cargo.lock/Dockerfile de producto. La propuesta documental de Rust y runtime `FROM scratch` exige verificación posterior sobre el digest final (TLS/CA, DNS, usuario/permisos y recuperación). No se atribuye baja latencia, capacidad o resistencia a ataques a una elección de lenguaje o imagen sin ensayo.

## 4. Seguridad informática — evaluación crítica

Se reconsultaron [RustSec](https://rustsec.org/advisories/) y [CISA KEV](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json): huellas idénticas a las recuperadas en la corrida anterior; KEV mantiene `dateReleased=2026-10-16T17:15:48.8752Z`. No se detecta aviso nuevo en **esos índices y esa foto**, no ausencia universal de vulnerabilidades. Se mantienen abiertos los análisis ammonia, parsers/ZIP/Wasmtime/PostgreSQL y productos de borde ya registrados. Sin inventario instalado no se afirma exposición ni corrección efectiva; los plazos CISA no son plazos legales argentinos.

| Vector / escenario bancario | Control y trazabilidad aplicables | Evidencia necesaria y brecha |
|---|---|---|
| Suplantación, recuperación de cuenta y firma fuera de facultades | IAM/CON/TRE; NFR-05, CTL-09/10/18; firma digital y registro BCRA cuando apliquen | Probar firmante/certificado revocado, otra entidad, doble control y validez al liberar. Un login/OTP o PDF válido no prueba mandato para mover fondos. |
| BOLA/BFLA, tokens entre entidades, APIs/workers de soporte | ADR-06; NFR-05/06; FAPI/ASVS como estándares adoptables, no ley general | Pruebas negativas por objeto/acción/celda, revocación concurrente, audiencias/scopes y límites de abuso. Sin código/inventario: no evaluado. |
| Replay, doble crédito, timeout de MEP y reenvío tras DR | TRE/PAY/REC; ADR-02/03/04; CTL-04/05/13 | Identidad económica persistente, prueba de origen autenticado, inbox y conciliación externa. No reenviar por TTL/lease vencido o asumir que un timeout significa rechazo. |
| Ransomware y caída conjunta de red/IDEAR/IAM/KMS | NFR-02/05/12; CTL-10/13/14 | Copia limpia, recuperación de claves/facultades, dependencias y runbook institucional. Acceso físico BCRA requiere conformidad y personal; no se declara contingencia disponible por leer la norma. |
| Documentos BF/PEP y fiscales, exportación y filtrado | CON/DAT/RPT; NFR-06/07; CTL-07/09/11/19 | Finalidad, minimización, retención/hold, destinatario y permisos; firmas/documentos reales fuera del repo público. Ammonia conocido requiere revisar renderer efectivo si existe. |
| Dependencias, parsers y carga inicial maliciosa | OPS/MIG/ASY; NFR-03/05/09/10; ADR-07/08 | SBOM/Cargo.lock, artefacto firmado/procedencia y límites de CPU/memoria/expansión; ZIP no puede escribir fuera de staging. Scratch no corrige una dependencia vulnerable. |
| Cifrado y APIs externas | NFR-05/06/08, gestor de claves soportado, contrato Rust/scratch | TLS/mTLS según interfaz efectiva, confianza CA, rotación/restauración y separación de secretos. No imponer algoritmo/protocolo inexistente en contrato reservado no consultado. |

ISO, PCI, Swift, NIST, FAPI y OWASP requieren edición, alcance y activador contractual/regulatorio. No se copiaron textos restringidos ni se presentan como leyes argentinas por defecto. No se ejecutó pentest, explotación, consulta de ROS, acceso a clientes, credenciales fiscales ni comunicaciones a reguladores.

## 5. Mapeo, cobertura y decisiones pendientes

| Hallazgo | Documentos / FR afectados | NFR, ADR, controles y skills |
|---|---|---|
| A8493 y transición A8474 | compliant.md PAY-11/LAW-10; FR-TRE-016/018/019/020, FR-PAY-001/026/027/029/030/031, FR-OPS-003/011/012/013, FR-RPT-011/012/013/014 | NFR-02/05/07/08/09/12; ADR-03/04/05; CTL-04/05/09/10/11/13/14/18; skills cumplimiento, disponibilidad, seguridad, configuración. |
| RG5908 | LEGAL_TAX.md y compliant.md TAX-01/03/09; FR-TAX-001/018/028/031/032 y FR-RPT-001/002/007/009/010/011/012/013/014/015/035/038 | NFR-05/06/07/09/11/12; ADR-05; CTL-02/09/11/19; skills cumplimiento, FR y configuración. |
| COMARB DP11 / A8487 | TAX/RPT/CFG/TRE/PAY/OPS, calendarios por régimen y contratos; detalle en documentos acotados | NFR-02/04/09/11/12; ADR-05; CTL-02/13/14/19; skills cumplimiento, configuración, operación. |
| RPI Capital Federal | Perímetro local, CLI/AML/GRN/CON/DAT/RPT, contratos profesionales y formularios | NFR-05/06/07/09/11; ADR-05; CTL-07/09/11/18/19; cumplimiento y privacidad. Aplicación condicional, no activación local universal. |

No se sustituyen reglas monetarias ni se crean FR duplicados: se entrega impacto y escenarios para revisión competente. La aprobación de la PR no prueba parametrización, homologación, pruebas ni aceptación institucional.

| Fuente | Cobertura real de esta corrida | Checkpoint / pendiente |
|---|---|---|
| BCRA comunicaciones A/B/C/P | **COMPLETE** para filtro emisión15–19/10, página1/1,19 registros/19 PDF/52 páginas; anexos integrados. Los14 documentos previos tienen las mismas huellas. | `covered_through` avanza del18/10 22:53:15 al19/10 22:08:02 −03. Publicaciones tardías sujetas a solapamiento. |
| BCRA TO / RI | **PARTIAL**, índice103TO/55RI; MEP/firmas/cuentas y RI seleccionado recuperados. | Versiones, textos, modificaciones/anexos restantes pendientes; cortes nulos. |
| BO primera sección | **PARTIAL**. Fallos503 iniciales; reintentos oficiales recuperaron15/16 (55 avisos cada uno),19 (100 URLs visibles),17/18 redirigen portada. Once cuerpos seleccionados del19 y dos del5;3 anexos nuevos recuperados (ICL y2RPI). | Índice19 muestra categorías por106 avisos pero sólo100 URLs visibles: paginación pendiente. Sin completar cuerpos/anexos restantes,37 anexos sustantivos anteriores, suplementos/extraordinarias; no se presume ausencia17/18. |
| UIF sectorial/transversal / AAIP / ARCA / CNV | **PARTIAL**. Entradas reconsultadas; ARCA5908/4626 y guía leídas selectivamente. | Índices/formularios no completan cronología/anexos. Sin avances de corte. |
| COMARB / SIRCREB / SIRCUPA | **PARTIAL**: sitio propio sigue500, pero candidato DP11 completo recuperado por BO. | Se cierra sólo el pendiente de cuerpo de ese candidato; índices, cambios y calendarios base pendientes. Corte nulo. |
| Jurisdicciones | Checkpoint opcional omitido íntegro; RPI analizado como candidato condicionado. | No se conoce operador/jurisdicción activada ni se afirma exención/cobertura universal. |
| Estándares / seguridad | **PARTIAL**, revisión selectiva y revalidación de índices. | Sin inventario desplegado, textos restringidos completos ni evaluación de contratos de redes. |

Evidencia, intentos fallidos, filtros, URL final, fechas, páginas, anexos, relaciones y SHA-256: [manifiesto de la corrida](https://github.com/andrescastiglia/bank/blob/ffa061ece43df870aab46a3ba185154c2f411c55/.regulatory-watch/evidence/RUN-20261020T010802Z.json). El checkpoint completo de una fuente es distinto de la ejecución, descubrimiento, publicación de PR y aceptación. Los historiales anteriores se conservan como prefijos exactos y el nuevo run se indexa una sola vez en la rama de estado.

**Validación ejecutada:** catálogo reproducible (1016 FR/32 módulos), revisión/enlaces/28 skills, inventario de vigilancia, 69 fixtures y transición `--state --run --previous-state`; 87 huellas de descargas/decodificaciones y 89 referencias FR del informe/propuestas contrastadas, incluidas abreviaciones. Son checks documentales y de integridad de evidencia. Las pruebas de firma, dinero, carga, vulnerabilidades, cifrado, recuperación y presentación descritas son propuestas; no se ejecutaron contra producto. No se verificaron rulesets/permisos técnicos en esta corrida ni se afirma que CODEOWNERS garantice exclusividad técnica de merges.

---

## Antecedente íntegro — corte del 18/10

El contenido siguiente conserva resultados y fechas previos. Sus cifras de cobertura y fallas describen su propia corrida; prevalece el nuevo corte anterior.

**Corte vigente:** **18/10/2026 22:53:15**, zona `America/Buenos_Aires` (`19/10/2026 01:53:15 UTC`). **Corrida:** `RUN-20261019T015315Z`. **Base comprobada:** `main f7d9495a172bcc9b2a68371a05509a664f12748d`, mediante conector GitHub y Git. La PR #9 continúa abierta y se amplía esa propuesta. **Resultado global: PARTIAL**.

## Análisis del corte del 18/10

Se recuperaron cinco corridas reales desde `automation/regulatory-state`, su inventario `2026-10-16.2`, ocho hitos y los pendientes de cada fuente. Ventana objetivo: **[15/10/2026 00:00:00 −03:00, 18/10/2026 22:53:15 −03:00)**. El solapamiento configurado de siete días se limita por el inicio del backfill, sin recortar gaps a ayer. Las consultas posteriores al corte conservan su `fetched_at`; las fechas sin hora no reciben una hora inventada.

| Eje | Datos verificados en esta corrida | Conclusión / brecha |
|---|---|---|
| Legal y normativo | BCRA recuperó resultados y PDF: 14 registros, página 1/1 y 28 páginas de PDF, todos con las mismas huellas del conjunto recuperado anteriormente. Índices: 103 TO / 55 RI; t-optico, TI/SI y tres RI seleccionados recuperados, también con huellas previas. | Se cierra el gap de acceso de comunicaciones y avanza su corte hasta el objetivo declarado. No se declara una reforma nueva por recuperar el acceso ni completitud global de BCRA/BO/otros organismos. |
| Mercado | Se reconsultaron siete ofertas; continúan composición, APIs/eventos, productos especializados y operación cloud. | No se verificó un lanzamiento, precio o integración argentina nueva. Persisten demostración operativa, localización y comparación de costos pendientes. |
| Tecnología | Se verificaron avisos informativos RustSec 0370/0371/0372 sobre mantenimiento de crates del ecosistema zbus. El manifiesto estable Rust mantiene su versión/huella anterior. | Los avisos INFO de mantenimiento no son por sí solos vulnerabilidades explotables. Antes de seleccionar componentes, evaluar soporte, migración y features; no se adoptó ninguna biblioteca. |
| Seguridad, crítico | Se verificó **RUSTSEC-2026-0373, ammonia**, antes no incorporado al historial: filtrado CSS de URLs sensible a mayúsculas. | Bypass de política de URLs/seguimiento bajo una configuración concreta. La fuente descarta XSS y limita su utilidad para exfiltración. Requiere inventario y renderer efectivo antes de afirmar exposición. |

### Legal y normativo: recuperación y alcance

El [buscador BCRA](https://www.bcra.gob.ar/buscador-de-comunicaciones/) se consultó por POST con `mode=fecha`, desde 15/10 hasta 18/10, sin limitar los tipos A/B/C/P, página 1 y tamaño 100. La respuesta acredita una sola página y **14 registros** emitidos el 15–16; no enumera otros para el 17–18 en esa foto. Se recuperaron **14/14 PDF completos**, anexos integrados incluidos, **28 páginas**. Sus huellas coinciden con las evidencias anteriores del conjunto, incluidas A8492, B13248/B13249/B13250 y P51237. La comparación de bytes no sustituye interpretación jurídica; en este conjunto no se detecta revisión de contenido.

**WATCH-BCRA-COM pasa a COMPLETE únicamente para ese filtro, fuente y ventana**; se reconcilia el estado, se cierran sus gaps de acceso y `covered_through` avanza desde 16/10 22:43:04 hasta 18/10 22:53:15 −03:00. Las publicaciones/indexaciones tardías siguen sujetas al solapamiento. Esto no acredita cobertura de todos los TO/RI, fuentes o jurisdicciones.

Se reconsultaron las dos facetas del índice oficial: **103 TO / 55 RI**, misma huella; el TO TI/SI, t-optico y RI de efectivo mínimo, deudores y PSP se recuperaron con huellas coincidentes con la evidencia anterior. La lectura pertinente y la comparación de estos documentos no completan los restantes textos, versiones y modificatorias. La última comunicación incorporada del TO TI/SI continúa siendo A8401, fechado 13/2/2026; se leyó su contexto de gestión de vulnerabilidades/desarrollo para el análisis técnico, sin presentarlo como norma nueva del día.

La agenda conserva A8492/CNV1172 para noviembre, B13248 para enero, CNV1173 para diciembre, el disparador particular CGN/TGN y las series ICL/UVI. No se reconstruye un vencimiento individual sin sujeto/período/disparador. UVI tiene primer valor el 20/10 según el análisis previo; sólo importa al contrato/producto que la incorpore válidamente. El catálogo KEV mantiene los avisos y fechas ya analizados; sus plazos estadounidenses no se convierten en vencimientos argentinos.

BO primera sección, UIF sectorial/transversal, AAIP, ARCA, COMARB y CNV se consultaron de nuevo. Las ediciones BO del 15 y 16 enumeran 55 avisos cada una; las URLs del 17 y del 18 redirigen a la portada, cuya fecha visible es el 16. Esa redirección **no prueba ausencia** de edición o suplemento extraordinario. Los 110 cuerpos y 40 anexos recuperados en corridas previas no se cuentan como descargas nuevas: continúan los 37 anexos pendientes de lectura sustantiva, junto con suplementos y búsquedas cronológicas no concluidas.

COMARB mantiene 500 en sus entradas, SIRCREB/SIRCUPA, índice anual y candidato DP11. No se deriva un calendario de sus snippets ni se renueva la alarma sin cambio material. UIF/AAIP/ARCA/CNV mantienen cobertura parcial: recuperar sus índices/formularios no permite declarar ausencia de actos o anexos. La investigación LEGAL_TAX y el directorio local siguen siendo contexto, no activación de todas las jurisdicciones ni cobertura provincial/municipal universal.

### Mercado y tecnología: contraste acotado

Se recuperaron nuevamente [Mambu](https://mambu.com/en), [Pismo](https://developers.pismo.io/pismo-docs/docs/welcome), [Bantotal](https://www.bantotal.com/), [Topaz](https://www.topazevolution.com/), [Temenos](https://www.temenos.com/products/core-banking/), [Vault Core](https://www.thoughtmachine.net/vault-core) y [Fineract](https://fineract.apache.org/). La correspondencia con CFG/CRD, ASY/PAY, FXT/FRD/TRE y MIG/OPS del análisis anterior se mantiene como comparación de oferta declarada. No se obtuvo evidencia nueva de localización argentina, contrato de soporte, benchmark comparable, tarifa o cuota auditada. Las variaciones HTML no se clasifican automáticamente como nuevos productos.

El [índice RustSec](https://rustsec.org/advisories/) incorpora avisos **INFO de mantenimiento** sobre [zvariant (0370)](https://rustsec.org/advisories/RUSTSEC-2026-0370.html), [zbus_names (0371)](https://rustsec.org/advisories/RUSTSEC-2026-0371.html) y [zvariant_derive (0372)](https://rustsec.org/advisories/RUSTSEC-2026-0372.html). Se leyeron sus fichas: no se deben traducir «sin versiones parchadas» o «unmaintained» en un exploit ni en un mandato de instalar un paquete alternativo. Para zvariant la ficha orienta hacia zbus 6.0.0/módulo wire, o zgvariant según formato. Antes de una elección real, ADR-07, NFR-09 y FR-OPS-026 requieren evaluar compatibilidad, soporte y costos. Es contexto de selección de dependencias, no una tecnología instalada en Bank.

Se reconsultaron el manifiesto estable y feed de Rust, PostgreSQL, FAPI, ASVS y KEV. No se verificó un cambio sustantivo nuevo que justifique repetir sus alertas conocidas. Las decisiones sobre asincronía durable, cancelación efectiva, aislamiento y scratch del informe anterior siguen siendo propuestas pendientes de evidencia ejecutable. La base sigue sin Cargo.toml/Cargo.lock, archivos Rust o imagen propia de producto.

### Seguridad: aviso nuevo para el registro y alcance exacto

El [análisis acotado RUSTSEC-2026-0373](regulatory/RUSTSEC-2026-0373.md) conserva fuentes, configuración activadora y criterios propuestos. Se leyeron [RustSec](https://rustsec.org/advisories/RUSTSEC-2026-0373.html), su registro oficial y la PR upstream 267. **Reported/campo `date`: 16/10; Issued: 17/10**, sin hora/zona de publicación exacta. Descubrimiento/observación en esta corrida del 18/10 argentino; no se lo fecha como publicación del 18. El GHSA enlazado no pudo recuperarse por API (404), limitación que no se sustituye con una lectura ficticia.

La condición involucra `ammonia` con sanitización CSS y estilos permitidos: una URL interior citada se filtra usando comparación sensible a mayúsculas de `url`, por lo que `URL(...)` puede eludir políticas de esquema/dominio. El impacto declarado es **introducir seguimiento que se pretendía impedir**; el aviso dice expresamente que **no permite XSS** y limita su utilidad para exfiltración. Rangos corregidos declarados: **`>=4.2.4`** o **`>=4.1.8,<4.2.0`**. No se atribuye a todas las configuraciones por defecto ni a todo servicio Rust.

Aplica al análisis si un componente directo/transitivo usa esa biblioteca y representa contenido enriquecido con la configuración afectada. Considerar plantillas y notificaciones, reclamos de terceros, backoffice y renderer de documentos. Se relaciona con **FR-CON-001/002; FR-CST-012/015/016; FR-OPS-024/026; NFR-05/06/09; ADR-05/06/07; CTL-09/15/17**, DATA-03 y gestión de vulnerabilidades/desarrollo BCRA según sujeto real. Los skills existentes de seguridad, privacidad y stack proporcionan el marco; falta definir políticas/oráculos del renderer y vincularlas al artefacto. No se crea una familia de requisitos duplicada ni se impone admitir HTML.

La aceptación propuesta contrasta mayúsculas/minúsculas, URLs citadas/no citadas, esquemas y relativos con destinos sintéticos controlados; observa las solicitudes efectivas del renderer además de la salida del sanitizer y conserva documentos históricos. No se ejecutó ese ensayo ni se enviaron solicitudes a terceros. Exposición, implementación y aceptación institucional siguen sin evaluar. El nuevo escenario de privacidad no reemplaza las amenazas ya documentadas de identidad, autorización por objeto/entidad, replay/doble pago, claves, APIs, dependencias, importación y recuperación.

### Cobertura real y validación

| Fuente | Resultado actual | Continuidad |
|---|---|---|
| BCRA comunicaciones | **COMPLETE**: 14 registros/14 PDF/28 páginas, fuente/filtro/ventana indicados. | Corte completo actualizado al 18/10 22:53:15 −03:00; gap de acceso cerrado, sin norma nueva en ese conjunto. |
| BCRA TO / RI | **PARTIAL**: índice 103/55 y documentos seleccionados recuperados. | Restantes textos/versiones/modificatorias/anexos pendientes; cortes nulos. |
| BO | **PARTIAL**: índices 15–16; consultas 17–18 redirigidas a portada. | Pendientes de anexos sustantivos, suplementos y ediciones extraordinarias; corte nulo. |
| UIF / AAIP / ARCA / CNV | **PARTIAL**: entradas oficiales reconsultadas. | Cronología/textos/anexos incompletos; cortes nulos. |
| COMARB | **UNAVAILABLE**, falla conocida persistente. | Candidato DP11 sin cuerpo completo; conserva gap/corte nulo. |
| Jurisdicciones | Fuente opcional omitida, checkpoint y fundamento previos íntegros. | Sin operador/ámbito local activado; no constituye exención. |
| Estándares y seguridad | **PARTIAL**: revisión selectiva, nuevo análisis ammonia y contexto de mantenimiento. | Sin inventario instalado, cobertura universal ni lectura de estándares restringidos/contratos de red. |

La evidencia de esta corrida, con intentos, filtros, URLs finales, hora y SHA-256, se conserva en [RUN-20261019T015315Z](https://github.com/andrescastiglia/bank/blob/9d269d68bc1a7d397ec534ea8f5da371d25288eb/.regulatory-watch/evidence/RUN-20261019T015315Z.json). Los historiales se mantienen como prefijos exactos y la corrida se indexa una sola vez, en `automation/regulatory-state`; las bitácoras operativas no se agregan al diff de `main`.

**Validación:** checks de catálogo reproducible, revisión/enlaces/skills, inventario y fixtures de vigilancia; transición con `--state --run --previous-state`, referencias FR y huellas contrastadas. Se contrastaron además 31 IDs FR explícitos del informe/propuestas y las huellas de las descargas actuales. Son verificaciones documentales. No se ejecutaron cargo audit, sanitización/rendering de producto, builds, pruebas financieras, pentest, parcheo, despliegue ni certificación. Las correcciones/rangos de un aviso no demuestran adopción, prueba o cumplimiento de Bank.

---

## Antecedente íntegro — corte del 17/10 a las 22:00

El contenido siguiente conserva las fechas y resultados de corridas anteriores; las fallas de acceso BCRA que allí se describen no son el resultado de esta nueva consulta. Prevalece la actualización anterior para el corte vigente.

**Corte vigente:** 17/10/2026, **22:00:17**, `America/Buenos_Aires` (`18/10/2026 01:00:17 UTC`). **Corrida:** `RUN-20261018T010017Z`. **Base:** `main f7d9495a172bcc9b2a68371a05509a664f12748d`, comprobada mediante conector GitHub y Git. **Resultado global: PARTIAL**. Esta actualización integra la propuesta de la PR #9, que continúa abierta; su integración/implementación no se presume.

## Resultado del relevamiento del 17/10

Se recuperaron desde GitHub cuatro corridas reales, inventario `2026-10-16.2`, ocho hitos y todos los gaps. Ventana objetivo: **[15/10/2026 00:00:00 −03:00, 17/10/2026 22:00:17 −03:00)**. El solapamiento de siete días queda limitado por el inicio del backfill; no se recortó el trabajo perdido a ayer. `covered_through` de comunicaciones BCRA se conserva en **16/10/2026 22:43:04 −03:00**, aun cuando la nueva consulta haya fallado. Las demás fuentes no adquieren un corte completo por recuperar índices o preparar una PR.

| Eje prioritario | Hecho de esta corrida | Conclusión y brecha |
|---|---|---|
| Legal/normativo | Se reconsultaron BO, BCRA, UIF sectorial/transversal, AAIP, ARCA, COMARB y CNV. El buscador BCRA falló con 502 en cuatro consultas; PDF seleccionados también fallaron. | Hay una **degradación nueva** respecto del acceso anterior. No se puede declarar ausencia de comunicaciones nuevas o rectificatorias. Se preserva evidencia previa y se mantiene agenda, sin activar parámetros. |
| Mercado | Se recuperaron nuevamente siete fuentes de fabricantes/proyectos, con APIs, composición, eventos y operación especializada. | No se verificó un lanzamiento, tarifa o localización argentina nueva. Las capacidades declaradas siguen requiriendo demostración y costos comparables para la oferta de Bank. |
| Tecnología | Se contrastó la documentación de Tokio 1.53.3: una tarea `spawn_blocking` iniciada no se cancela con `abort`; dejar de esperarla tampoco la detiene. | La asincronía necesita límites y cancelación efectiva, especialmente con parsing/importación. Se propone evaluar contención según escenario, sin adoptar un nuevo componente por este informe. |
| Seguridad, crítico | Se completó el análisis de RustSec 0365–0369, fichas con Issued 17/10 y fechas Reported anteriores. Sus HTML conservan la huella de los candidatos ya observados. | Nueva conclusión de análisis de candidatos previos, **no cinco descubrimientos recién publicados ni revisiones del contenido**. Riesgos de aborto por recursos y extracción ZIP insegura; exposición del producto sin evaluar por falta de artefactos/dependencias. |

### Legal y normativo: continuidad, agenda y acceso real

Los filtros del buscador BCRA fueron POST por fecha, sin limitar tipo A/B/C/P, página 1 y tamaño 100: intervalo 15–17/10, reintento del mismo intervalo, solapamiento 15–16 y día 17 separado. Los cuatro devolvieron **HTTP 502**, sin lista ni paginación legibles. La portada recuperada es sólo el formulario; no acredita cobertura de comunicaciones. Se intentaron revalidar A8492, B13248/B13249/B13250 y P51237: sus PDF no pudieron recuperarse en esta corrida. No se presume que cambiaron o fueron derogados por el fallo, ni se reutilizan las huellas anteriores como evidencia de una descarga nueva.

El JSON oficial de ordenamiento sí conserva la misma huella y enumera **103 TO / 55 RI**. No sustituye los documentos: t-optico, riesgos TI/SI y tres RI seleccionados tuvieron 502/timeouts. La interpretación sustantiva anterior continúa como antecedente fechado. En particular, no se declara revalidada toda la vigencia normativa por un índice estable.

La agenda recuperada incluye A8492 y CNV1172 para noviembre, B13248 para enero, CNV1173 para diciembre, el disparador particular CGN/TGN y los primeros valores ICL/UVI. No se repiten como novedades. ICL ya tiene su primera fecha de valor del 17/10 y UVI comienza el 20/10 según el análisis anterior: su aplicación depende del contrato/producto real. Fecha de valor, entrada en vigor y vencimiento de reporte son conceptos distintos. Sin operador y hecho disparador no se fija un plazo individual.

El BO enumera los mismos **55 avisos por edición del 15 y del 16** (110 URLs únicas en total). Se recuperaron nuevamente los **14 cuerpos** antes limitados con 429. Su clasificación distingue edictos/actos particulares, registros y disposiciones laborales de una obligación bancaria general; no se publican sus datos personales. Los **40 anexos identificados recuperados acumuladamente** pertenecen a la evidencia de corridas anteriores: no se contaron como descargas nuevas y los 37 pendientes de revisión sustantiva conservan sus cursores. La URL de edición del **17/10 redirigió a la portada**, que muestra el 16; no demuestra inexistencia de edición o suplemento extraordinario. La portada enlazó un suplemento del 14/8, fuera de la ventana, sin que ese enlace acredite el universo de suplementos de octubre.

UIF sectorial/transversal, AAIP, biblioteca ARCA y marco/panel CNV se reconsultaron, pero falta completar sus búsquedas cronológicas, textos, modificaciones y anexos. No se infiere ausencia de cambios. **COMARB DP11 sigue pendiente de cuerpo oficial completo**: fallan las rutas e índices consultados; la URL candidata de un PDF directo devolvió 404 y el lector web de otra ruta timeout. Los extractos del buscador no se transforman en vencimientos. Se conserva el candidato y su procedencia; no se renueva la alarma idéntica de indisponibilidad.

Las jurisdicciones locales siguen condicionadas a un operador/producto/territorio aprobado. LEGAL_TAX y su directorio no acreditan cobertura universal ni seleccionan una entidad autorizada. Los estándares ISO/PCI/Swift/NIST mantienen el alcance técnico/contractual o el activador normativo que corresponda, no carácter legal argentino por defecto.

### Mercado: capacidades y valor verificable

Se reconsultaron [Mambu](https://mambu.com/en), [Pismo](https://developers.pismo.io/pismo-docs/docs/welcome), [Bantotal](https://www.bantotal.com/), [Topaz](https://www.topazevolution.com/), [Temenos](https://www.temenos.com/products/core-banking/), [Vault Core](https://www.thoughtmachine.net/vault-core) y [Fineract](https://fineract.apache.org/). Cinco conservaron la huella anterior; Pismo y Temenos cambiaron HTML, sin diferencia funcional fechada verificada. La comparación detallada anterior permanece vigente como observación de oferta, no como benchmark ni prueba contractual.

El portal Pismo muestra entrega de eventos en tiempo real, lotes/archivos, recuperación y deprecación de APIs: corresponden a ASY/RPT/MIG e interoperabilidad de Bank. La propuesta ya contempla esos comportamientos; falta un contrato versionado con reintento, recuperación, identidad del evento y compatibilidad de consumidores comprobados. Las promesas de composición de Mambu/Temenos/Vault y la especialización de Bantotal/Topaz no eliminan localización, conciliación o operación. Fineract conserva valor comparativo como alternativa libre; no se incorporó código ni se alteró GNU GPL v2.

**Conclusión comercial:** sigue pendiente demostrar un recorrido argentino con producto/perfil, integración, servicio operativo y costo. Los hechos relevados no justifican declarar ventaja de latencia, cumplimiento o precio frente a competidores ni lanzar un nuevo plan comercial.

### Tecnología y seguridad: procesamiento hostil y asincronía

El [análisis acotado RustSec](regulatory/RUSTSEC-2026-0365-0369.md) separa fechas, alcance, versiones corregidas, condiciones de exposición y criterios propuestos. Se leyeron las cinco fichas y los cinco registros del repositorio oficial. Las referencias GHSA de `zip` no se pudieron leer por API (404); esta limitación queda registrada.

| Aviso / fuente primaria | Riesgo documentado | Perfil/funcionalidad potencial y corrección declarada |
|---|---|---|
| [RUSTSEC-2026-0365](https://rustsec.org/advisories/RUSTSEC-2026-0365.html) | `negentropy`: reserva de memoria basada en conteo no validado; mensaje pequeño puede abortar el proceso con `std`. | Sólo integración que utilice esa crate/API/features. Corregidas `>=0.4.4,<0.5.0` o `>=0.5.2`; `<0.2.0` declaradas no afectadas. Un límite de bytes o `catch_unwind` no contiene por sí solo este caso. |
| [RUSTSEC-2026-0366](https://rustsec.org/advisories/RUSTSEC-2026-0366.html) | `pest_grammars`: JSON profundamente anidado puede agotar pila; el umbral depende del entorno. | Parser concreto, no todo JSON de Rust. Corregida `>=2.9.3`; límites de trabajo/memoria/concurrencia siguen necesarios, con restricciones de `std`/plataforma. |
| [RUSTSEC-2026-0367](https://rustsec.org/advisories/RUSTSEC-2026-0367.html) | Extracción ZIP conserva bits privilegiados; impacto según privilegios del extractor y entorno. | Importador, CI/builder o herramienta que realmente use esa extracción. Corrección declarada `zip >=9.0.0`. |
| [RUSTSEC-2026-0368](https://rustsec.org/advisories/RUSTSEC-2026-0368.html) | Destinos de symlinks pueden escapar del directorio; demostración en 9.0.0-pre2/Linux/macOS. | Validar destino efectivo y acceso posterior; no extrapolar la versión demostrada a toda rama sin revisar. Corrección declarada `>=9.0.0`. |
| [RUSTSEC-2026-0369](https://rustsec.org/advisories/RUSTSEC-2026-0369.html) | Aplicación de permisos sigue symlinks sin confinar su destino. | Extracción que use las APIs afectadas; verificar permisos/rutas, no sólo nombre del archivo. Corrección declarada `>=9.0.0`. |

**Issued** es 17/10 en las cinco fichas, sin hora/zona. **Reported / campo `date`**: 14/10, 16/10, 9/10, 9/10 y 10/10, respectivamente. No se construye una hora de publicación ni un vencimiento. Se trata de fuentes observadas al consultar este corte y candidatos del relevamiento anterior analizados ahora; no se fuerza una precisión temporal que la fuente no aporta.

El repositorio base continúa sin `Cargo.toml`, `Cargo.lock`, `.rs` o Dockerfile de producto. El inventario efectivo debe incluir dependencia transitiva, features, OS/API, permisos, builder y digest antes de afirmar exposición. Los problemas son relevantes incluso para una imagen final scratch si el builder extrae archivos con privilegios, o si el binario aborta al parsear. No se confunde lenguaje con aislamiento de procesos ni se atribuyen esas crates a Bank.

La documentación de [Tokio `spawn_blocking`, versión observada 1.53.3](https://docs.rs/tokio/1.53.3/tokio/task/fn.spawn_blocking.html) respalda acotar trabajo CPU y distinguir cancelación de dejar de esperar. Ante un parser que puede abortar el proceso, evaluar validación/librería corregida y límites en proceso frente a contención en proceso supervisado, con sus costos. Es una alternativa para revisar ADR-03/06/07/08, no una decisión ya aceptada ni una release nueva del día. Cargar por COPY hacia staging y usar colas durables no convierte la extracción ni el parser en seguros.

El impacto se mapea a **FR-MIG-004, FR-ASY-016/022/026, FR-OPS-024/026; NFR-03/04/05/09/10; CTL-09/15/17/20** y skills existentes de seguridad/carga masiva/stack. Faltan formatos admitidos, límites medibles por celda, confinamiento de rutas/permisos, cancelación efectiva y oráculos de rechazo sin efectos financieros. Los ensayos propuestos en el análisis acotado siguen sin ejecutarse; no se añaden requisitos duplicados ni se cambia la aceptación de los actuales.

Se reconsultaron KEV, los avisos BeyondTrust/Fortinet, PostgreSQL, FAPI y ASVS. KEV y PostgreSQL mantienen su huella; ASVS varió HTML sin nueva edición sustantiva verificada. Las identidades de seguridad ya notificadas permanecen pendientes según inventario, sin una alarma repetida. El modelo de amenazas anterior sigue cubriendo apropiación de identidad, autorización por entidad/objeto, replay/doble pago, secretos, APIs, claves y recuperación. Los avisos analizados de parsing amplían escenarios de disponibilidad e importación, no reemplazan esos controles.

### Cobertura de la corrida y evidencia

| Fuente | Estado / alcance observado | Pendiente y checkpoint |
|---|---|---|
| BO | **PARTIAL**. Tres consultas por fecha; dos ediciones válidas, 110 URLs enumeradas, 14 cuerpos pendientes recuperados. URL 17/10 redirige a portada. | Lectura sustantiva de anexos previos, suplementos/ediciones extraordinarias y cobertura restante; corte nulo. |
| BCRA comunicaciones | **UNAVAILABLE para resultados/documentos**. Formulario accesible; cuatro POST con 502, PDF seleccionados fallidos. | Gap nuevo de acceso; conserva corte completo anterior 16/10 22:43:04 −03:00, sin adelantarlo. |
| BCRA TO / RI | **PARTIAL**, índice oficial 103/55 revalidado; PDF seleccionados con 502/timeouts. | Lectura/versiones/modificatorias no completadas; cortes nulos. |
| UIF / AAIP / ARCA / CNV | **PARTIAL**, entradas oficiales consultadas; UIF incluye sector y transversal. | Faltan cronología, textos y anexos completos; cortes nulos. |
| COMARB | **UNAVAILABLE**, fallos conocidos persistentes; candidato DP11 conserva referencia pendiente. | No se deriva calendario ni ausencia de cambios; corte nulo. |
| Jurisdicciones locales | Opcional omitida, fundamento y checkpoint anteriores conservados íntegros. | Sin operador ni ámbito local activado; no es exención. |
| Estándares / seguridad | **PARTIAL**, consulta selectiva y análisis de cinco candidatos técnicos completado. | Sin inventario instalado, pruebas o cobertura universal de estándares/avisos; corte nulo. |

La bitácora registra cada intento, filtros/paginación no recuperada, redirección, URLs finales, fechas y SHA-256. Las fallas y los 40 anexos acumulados no se reescriben como recuperaciones nuevas. Los historiales `changes`, `agenda` y `run_index` se conservan como prefijos exactos; la corrida se indexa una sola vez. Evidencia de este corte: [RUN-20261018T010017Z](https://github.com/andrescastiglia/bank/blob/d8e7b816df484501be4707bd2d1972223b56f9b5/.regulatory-watch/evidence/RUN-20261018T010017Z.json). El estado operativo se publica exclusivamente en `automation/regulatory-state`.

**Validación:** checks documentales de catálogo reproducible, revisión/enlaces/skills, inventario y fixtures de vigilancia; transición contrastada con el estado anterior mediante `check_watch.py --state --run --previous-state`. No se ejecutaron producto, `cargo audit`, extracción hostil, builds, pentest, parcheo ni ensayos de carga/DR. Se contrastaron 29 IDs FR explícitos del informe/propuestas y las huellas de todas las descargas actuales, sin payloads truncados. La estructura válida no demuestra lectura jurídica completa, control operativo eficaz o aceptación institucional.

**Decisiones pendientes:** inventario/formatos que realmente se admitirán, perfil y contratos del operador, recursos por celda y evidencia de contención. No se fija un vencimiento de parcheo argentino a partir de RustSec/CISA. La propuesta continúa conforme a GPL v2 y sólo el mantenedor decide su merge.

---

## Antecedente íntegro de la actualización del 16/10 a las 22:43

El contenido siguiente conserva sus fechas y resultados históricos; para el corte vigente prevalece la actualización anterior. La recuperación de anexos y estados de acceso indicados debajo no son consultas nuevas de esta corrida.

**Actualización:** 16/10/2026, 22:43:04, `America/Buenos_Aires` (17/10 01:43:04 UTC). **Base:** `main` en `f7d9495a172bcc9b2a68371a05509a664f12748d`, recuperada mediante GitHub y contrastada con Git. **Corrida:** `RUN-20261017T014304Z`. **Resultado global: PARTIAL**.

## Actualización de los cuatro ejes

### Alcance y conclusiones del nuevo corte

La ventana solicitada es **[15/10/2026 00:00:00 −03:00, 16/10/2026 22:43:04 −03:00)**. Se recuperaron tres corridas reales de `automation/regulatory-state`, sus checkpoints, gaps, agenda y propuestas. El seed no se contó como corrida. El solapamiento de siete días se limita por el inicio del backfill, sin eliminar trabajo perdido. Las consultas realizadas después del corte se identifican por `fetched_at`; una fecha de publicación sin hora no demuestra que todo un día estuviera publicado a medianoche.

| Eje | Hallazgo o contraste de este corte | Consecuencia para Bank |
|---|---|---|
| Legal y normativo | El buscador BCRA ahora enumera 14 comunicaciones del 15–16/10, frente a las seis del 15 observadas antes. Se recuperaron los 14 PDF. B13249 y B13250 publican series ICL/UVI; P51237 anuncia una nueva actualización de la Central de Deudores. | Son datos y versiones de insumos, no una habilitación ni una reforma universal de productos. Configuración y cálculos necesitan fuente, fecha y versión por contrato. |
| Mercado | Se reconsultaron siete fabricantes/proyectos: Mambu, Pismo, Bantotal, Topaz, Temenos, Thought Machine y Apache Fineract. | Se mantiene la brecha entre capacidad documentada y demostración comercial/localización efectiva. No se verificó un lanzamiento fechado nuevo ni un cambio de precio o cuota. |
| Tecnología | El manifiesto estable de Rust mantiene la misma huella; los índices BCRA conservan 103 TO y 55 RI. El repositorio sigue sin producto Rust ejecutable. | No se justifica reemplazar arquitectura por una portada nueva. Faltan contratos ejecutables, selección de dependencias y mediciones; los requisitos existentes ya proporcionan el marco. |
| Seguridad, crítico | CISA agregó el 16/10 dos vulnerabilidades explotadas al KEV: CVE-2026-102764 y CVE-2025-61624. Se leyeron también los avisos de BeyondTrust y Fortinet. | Revisar inventario de soporte remoto, red y administración antes de concluir exposición. Los equipos operativos y terceros están dentro de la superficie aunque la imagen propia sea scratch. |

`main` ya integra [LEGAL_TAX.md](docs/LEGAL_TAX.md) y el informe anterior por decisiones del mantenedor. Esto amplía el contexto jurídico y tributario disponible; no acredita implementación ni aceptación del operador. Se conserva íntegro el informe anterior al final como antecedente fechado: **sus cifras de recuperación, estado KEV y cortes son históricos; para esta corrida prevalece la actualización presente**.

### Legal y normativo: datos primarios y aplicabilidad

| Identidad / texto oficial | Publicación, observación y fechas efectivas | Hecho verificado | Perfiles y brecha |
|---|---|---|---|
| [BCRA B13249, PDF completo de tres páginas](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/B13249.pdf) | Emisión 16/10/2026; fecha BO vacía en el buscador, no acreditada. Observación en esta corrida. | Anexo con 31 valores ICL, **17/10–16/11/2026**, base 30/6/2020 = 1, dos decimales: 36,90 al inicio y 37,53 al final. Incluye metodología en la tercera página. | Comunicación a EF; utilizar sólo en contratos o gastos que remitan válidamente a ICL. No obliga a indexar todo alquiler nuevo ni todo crédito. FR-CFG-011, FR-INT-006 y contratos requieren identificar serie y cláusula aplicable. |
| [BCRA B13250, PDF completo de dos páginas](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/B13250.pdf) | Emisión 16/10; publicación BO no acreditada. Valores efectivos **20/10–19/11/2026**, sin inventar vencimiento de presentación. | 31 valores UVI/ICC, base 31/3/2016 = ARS 14,05: ARS 1.587,72 al 20/10 y ARS 1.610,77 al 19/11. No es UVA/CER. | EF destinataria y contratos alcanzados. FR-CFG-012, FR-INT-006/007; falta paquete de insumo y oráculos ejecutados, no una nueva familia FR. |
| [BCRA P51237, una página](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/P51237.pdf) | Emitido 16/10; sin fecha BO acreditada. | Anuncia disponibilidad de la **tercera actualización de agosto 2026** de la Central de Deudores, por el mecanismo de sección 4/anexo I de Centrales de información. | Integraciones de riesgo/crédito que consulten esa central. Actualización de agosto no equivale a cartera de octubre. No se descargó base de personas ni se procesaron datos de deudores. Requiere controlar versión, fecha del dato y acceso autorizado. |
| BCRA C102436–C102440 | Emitidas 16/10; PDFs recuperados, sin atribuirles fecha BO no informada. | Circulación, reservas, pasivos, tipo de cambio y tasas/series. C102440 distingue las metodologías y admite reiterar el último dato de cajas de ahorro cuando no hay información contemporánea. | Son insumos condicionados al producto/contrato. La fecha de observación no reemplaza fecha de referencia ni calidad del dato. Una tasa de referencia no se convierte automáticamente en tasa contractual. |

El [análisis acotado de las dos series](regulatory/BCRA-B13249-B13250-2026.md) conserva criterios de aceptación y alcance. Se revisaron texto y tablas de B13249/B13250, incluida inspección visual de la página 2 de ambos PDF; no se cargaron series en producción. Propuesta de aceptación: verificar identidad y 31 fechas únicas/continuas de cada serie, comparar contra una fuente estructurada oficial antes de importar, conservar precisión/metodología, rechazar el intercambio UVI/UVA, probar dato ausente y corrección histórica sin sobrescritura. **Esos ensayos de producto todavía no se ejecutaron.**

Los hitos conocidos **A8492 (1/11), B13248 (enero 2027), CNV1172 (vigencia general 16/10 y art. 40.b desde 1/11), CNV1173 (transición particular 15/12)** continúan en agenda. Alcance por sujeto y primer período siguen condicionados. No se recrean como novedades ni se inventa fecha de entrega sin disparador. La integración de LEGAL_TAX tampoco selecciona una sociedad bancaria ni activa todos los regímenes de su inventario.

**COMARB: candidato pendiente, no regla verificada.** El buscador localizó una ficha oficial titulada Disposición de Presidencia 11/2026, fechada 16/10, sobre vencimientos; su título, ruta y referencias a sistemas no coinciden plenamente. El [enlace oficial](https://www.ca.gob.ar/resoluciones-comarb/download/455-2026/8707-disposicion-de-presidencia-n-11-2026-modificacion-del-vencimiento-de-las-ddjj-y-pagos-de-sircar-sircupa-y-sifere-correspondiente-al-anticipo-10-2027-vfinal) devolvió HTTP 500 y el lector alternativo timeout. No se recuperaron texto completo, descarga ni publicación BO: no se deriva calendario, feriado o parámetro productivo del snippet. Se conserva el candidato y su URL para reintento; no se afirma cobertura de SIRCREB/SIRCUPA ni de provincias.

**Brecha transversal.** LEGAL_TAX incorpora constitución/autorización, capital, impuestos nacionales y un directorio de autoridades locales con ejemplos CABA/PBA. [compliant.md](docs/compliant.md), TAX/RPT y los skills siguen siendo requisitos y procedimientos genéricos: faltan matriz por operador, parámetros tributarios versionados, acuses reales y revisión profesional pertinente. No se infiere cobertura local universal de ese directorio ni de índices nacionales.

### Mercado y competencia: contraste actualizado

Las siete fuentes se recuperaron nuevamente; son declaraciones de sus responsables. No se obtuvieron contratos, tarifas, benchmarks comparables, resultados de homologación argentina ni cuotas auditadas. Una huella distinta de HTML dinámico se conserva como observación, sin clasificarla como nueva funcionalidad.

| Oferta / fuente | Capacidades declaradas observadas | Correspondencia y evidencia que falta en Bank |
|---|---|---|
| [Mambu](https://mambu.com/en) | Composición, préstamos de consumo/empresas, financiación embebida y pagos. | CFG/CRD/COR: demostrar composición y economía por producto; el anuncio comercial de pagos transfronterizos requiere fecha y alcance antes de llamarlo lanzamiento nuevo. |
| [Pismo](https://developers.pismo.io/pismo-docs/docs/welcome) | APIs, eventos, guía de seguridad, ciclo de vida/deprecación y configuraciones de préstamos/pagos. | ASY/PAY/CARD: faltan contratos OpenAPI/eventos versionados, compatibilidad y pruebas de consumidores. |
| [Bantotal](https://www.bantotal.com/) | Core regional, microfinanzas, pagos y comercio exterior; capacidades empaquetadas. | La oportunidad exige comparar un recorrido argentino concreto, conectores y soporte operativo; una oferta regional no prueba cumplimiento local completo. |
| [Topaz](https://www.topazevolution.com/) | Core modular, tesorería y suite antifraude. | RSK/FRD/TRE: falta ensayo de caso, límites, conciliación y costo de operar controles. Sus cifras comerciales no se extrapolan a Argentina. |
| [Temenos](https://www.temenos.com/products/core-banking/) | Composición y modernización progresiva, pagos y gestión financiera. | MIG/CFG/OPS: demostrar corte/retorno por cohorte y coexistencia conciliada, sin doble autoridad financiera. |
| [Vault Core](https://www.thoughtmachine.net/vault-core) | Parametrización de productos, datos en tiempo real y operación cloud. | CFG/LED/ASY: la personalización requiere reglas reproducibles y autorización; no deriva en un motor de código arbitrario aceptado por Bank. |
| [Apache Fineract](https://fineract.apache.org/) | Software abierto, APIs headless, clientes, préstamos, ahorro, contabilidad y reportes. | Alternativa para comparar funcionalidades y costos. No se adoptó su código ni se cambió GPL v2; cualquier integración necesita revisión de licencia/procedencia y localización. |

**Interpretación comercial:** la documentación cubre muchas funciones competitivas, pero falta una demostración repetible con perfil, operación, condiciones comerciales, conectores y costo. Priorizar una oferta verificable por segmento sigue siendo más defendible que prometer cobertura universal. No se presenta una nueva hoja de ruta ni se altera el plan existente.

### Tecnología: arquitectura y mantenibilidad

La base examinada no contiene `Cargo.toml`, `Cargo.lock`, `.rs` ni Dockerfile de producto. Rust, Tokio, autoridad SQL, outbox/inbox, aislamiento por celda y scratch son decisiones/requisitos documentales; no son componentes cuyo rendimiento haya sido medido. El [manifiesto estable de Rust](https://static.rust-lang.org/dist/channel-rust-stable.toml) revalidó la huella anterior de 1.99.1. No se seleccionó otra release por fecha o por variación de la portada.

El impacto de las series y de las actualizaciones externas refuerza ADR-05: separar `published_at`, fecha efectiva del valor y `observed_at`, fijar fuente/unidad/versión y evitar recalcular historia confirmada con el último dato. ADR-03 permite adquirir/validar insumos asíncronamente con idempotencia y cuarentena; la liquidación definitiva debe esperar el dato admisible. ADR-02 conserva la autoridad transaccional, y ADR-08 requiere que una carga inicial preserve la serie y versión de origen sin disparar efectos externos históricos.

Para rendimiento y disponibilidad siguen faltando percentiles bajo carga representativa, recuperación tras pérdida de commit/ACK, backpressure, fencing y conciliación externa. No se aportan cifras sintéticas como evidencia de SLO. La comparación de proveedores no exige adoptar una arquitectura distribuida adicional.

### Seguridad crítica: novedades, exposición y pruebas propuestas

El [KEV oficial de CISA](https://raw.githubusercontent.com/cisagov/kev-data/develop/known_exploited_vulnerabilities.json) consultado es una versión posterior al catálogo del antecedente: fecha `2026-10-16T17:15:48.8752Z`. Se identificaron **dos altas del 16/10** que no estaban en el estado recuperado. La inclusión acredita el criterio de explotación del catálogo, no un incidente en Bank.

| Identidad y fuentes primarias | Fechas y hechos | Aplicabilidad y tratamiento propuesto |
|---|---|---|
| **CVE-2026-102764**, [BeyondTrust BT26-05](https://www.beyondtrust.com/trust-center/security-advisories/bt26-05), KEV | Aviso del fabricante 15/10; alta KEV 16/10. Remote Support valida insuficientemente el origen de mensajes internos, permitiendo operaciones sobre archivos. CVSS 4.0 **9,3** del fabricante. Afecta versiones hasta 26.2.3; parche **BT26-05-RS** para 24.3.1–26.2.3. Versiones anteriores requieren actualizar para aplicar el parche. El fabricante declara SaaS parchado desde 9/10. | Condicionado a Remote Support propio o de tercero con acceso al entorno. Verificar modalidad/versión/parche real; una versión sin comprobar parche no basta. No se detectó ese producto instalado ni se inspeccionó infraestructura privada. |
| **CVE-2025-61624**, [Fortinet FG-IR-26-122](https://fortiguard.fortinet.com/psirt/FG-IR-26-122), KEV | Aviso inicial **14/4/2026**, alta KEV **16/10/2026**: novedad de explotación catalogada, no publicación nueva del defecto. Path traversal en CLI de FortiOS, FortiPAM, FortiProxy y FortiSwitchManager; requiere privilegios administrativos, permite escritura/borrado. CVSS 3.1 **6,0** del fabricante. | Sólo si alguno de esos productos/ramas está presente. Ejemplos corregidos: FortiOS 7.6.5/7.4.10; FortiProxy 7.6.5/7.4.12; FortiPAM 1.7.1 (1.8 no afectada); FortiSwitchManager 7.2.8/7.0.7. Consultar tabla y camino de actualización del fabricante; ramas antiguas indicadas requieren migración. |

Ambas entradas KEV tienen `dueDate = 19/10/2026`, **plazo del programa federal estadounidense, no vencimiento legal argentino ni SLA automáticamente adoptado por Bank**. La prioridad local debe surgir de presencia, exposición, privilegios, activos y política del operador. Las escalas CVSS son distintas y no se convierten en una puntuación de riesgo del proyecto.

La [propuesta acotada de exposición y criterios](regulatory/CISA-KEV-20261016.md) mapea FR-IAM-008/026, FR-OPS-024/025/026, NFR-05, NFR-09, ADR-06/07 y CTL-09/15. Incluir soporte remoto, gateways, PAM, CI y terceros en el inventario evita que el alcance se limite a los crates del core. Un atacante con control de esos planos puede alcanzar credenciales, backups y cambios de parámetros aunque el runtime de la aplicación no tenga shell.

Se conservan las amenazas del antecedente: autorización por objeto/entidad, replay, doble pago, manipulación de parámetros, secuestro de identidad, filtración de secretos, importación maliciosa, ransomware y restauración inconsistente. OIDC/OAuth no sustituyen facultades de negocio; cifrado necesita custodia/rotación/restauración de claves y validación efectiva TLS; las APIs requieren límites, autorización e idempotencia por operación. FAPI/ASVS fueron reconsultados como referencias técnicas, sin alegar certificación. ISO/PCI/Swift/NIST requieren activador contractual/normativo o de red y no se convierten por defecto en leyes argentinas.

RustSec 0365–0369 aparecieron en el índice consultado con fecha de emisión **17/10**, sin hora/zona suficiente para asignarlos al corte argentino del 16/10. Se conservan para verificación temporal posterior, sin notificarlos como publicaciones confirmadas dentro de la ventana ni atribuir esas crates al proyecto. El contexto anterior Wasmtime/PostgreSQL y el aviso Atlassian conocido no se vuelve a notificar como novedad.

### Cobertura real, continuidad y límites

| Fuente | Resultado de esta corrida y cobertura real | Continuidad |
|---|---|---|
| WATCH-BO | **PARTIAL**. Ediciones 15 y 16/10; 110 URLs de cuerpos únicos, 96 recuperados nuevamente y 14 revalidaciones con 429. 37 de 37 anexos antes pendientes descargados/extraídos; seis fallos 503 iniciales se resolvieron con reintento. Total acumulado recuperado: 40 de 40 identificados, incluidos tres del antecedente. | Sin corte completo. Pendientes lectura sustantiva de anexos recuperados, reintentos, suplementos/ediciones adicionales y universo de anexos no identificado. Los 110 cuerpos recuperados anteriormente no se cuentan como 110 recuperados en esta corrida. |
| WATCH-BCRA-COM | **COMPLETE para el filtro y ventana declarados**. Consulta POST por fecha 15–16/10, todos los tipos A/B/C/P, página 1/1, 14/14 registros; 14 PDF y sus anexos integrados, 28 páginas. Un timeout inicial B13250 se resolvió con reintento. | Avance contiguo desde 16/10 00:00 hasta 16/10 22:43:04 −03:00. La foto consultada después del corte queda fechada; debe solaparse por indexaciones tardías. No es completitud del resto de fuentes BCRA. |
| WATCH-BCRA-TO | **PARTIAL**. Índice de 103 TO y seis PDF seleccionados: depósitos, cuenta corriente, garantía, protección de usuarios, seguridad física y riesgos TI/SI. | Índice no paginado recuperado; lectura selectiva, comparación histórica y restantes textos/modificatorias pendientes. Corte conservado nulo. |
| WATCH-BCRA-RI | **PARTIAL**. Faceta oficial de 55 RI; t-optico, efectivo mínimo, deudores, PSP y manual SISCEN recuperados. | Otros textos/anexos y secuencia de versiones pendientes. Corte nulo. |
| WATCH-UIF | **PARTIAL**. Índices sectorial y transversal reconsultados; selección por rol, sin convertir obligaciones de abogados/registros en reglas de EF. | Falta búsqueda temporal completa y lectura de todas las modificatorias/anexos pertinentes. Corte nulo. |
| WATCH-AAIP | **PARTIAL**. Formulario oficial accesible, sin serie de resultados cronológicos completa acreditada. | Mantiene gap y corte nulo; no se concluye ausencia de novedades. |
| WATCH-ARCA | **PARTIAL**. Biblioteca y entrada institucional; la ruta temática ensayada devolvió 404. | Búsqueda cronológica y anexos incompletos; LEGAL_TAX es contexto de repositorio, no evidencia de cobertura externa de esta corrida. Corte nulo. |
| WATCH-COMARB | **UNAVAILABLE para recuperación directa**. Portales, sistemas, índice anual y candidato DP11 devolvieron 500; lector alternativo timeout. | Conserva falla conocida y candidato descubierto; sin texto completo ni corte. Snippets no cierran cobertura ni se convierten en calendarios. |
| WATCH-CNV | **PARTIAL**. Marco/panel oficial reconsultados; conserva RG1172/1173 en contexto de agenda. | Resto de actos/historia/anexos pendientes; corte nulo. |
| WATCH-JURIS | **NOT_APPLICABLE_WITH_BASIS al relevamiento local**, fuente opcional omitida en esta corrida y checkpoint conservado íntegro. | Sin operador ni jurisdicciones activadas. No es exención ni cobertura de las 24 jurisdicciones. |
| WATCH-STANDARDS | **PARTIAL**. KEV, avisos técnicos, PostgreSQL, Rust, FAPI y ASVS en alcance documental. | No inventario instalado, cobertura universal de avisos, edición contractual de red ni texto restringido completo de estándares; corte nulo. |

Los índices TO/RI se procesaron en sus dos facetas oficiales. Recuperar un PDF no acredita revisar todas sus modificatorias: la lectura sustantiva se concentró en los actos/segmentos relevantes indicados, conservando cursores para el resto. Suplementos/ediciones adicionales del BO y búsqueda cronológica completa de cada autoridad continúan pendientes. Las respuestas 429 detuvieron la secuencia de reintento de cuerpos; no se eludieron límites ni se infirió ausencia de normas.

El estado registra filtros, URLs finales, fechas y hashes de bytes, además de la huella separada de cada PDF anexo decodificado. Un documento distinto por hash queda para comparación de contenido pertinente; no se descarta ni se proclama reforma por la plantilla HTML. Los anexos recuperados pero no interpretados permanecen pendientes de lectura sustantiva. Se conservan agendas, cambios y corridas previas como prefijos exactos, sin convertir una PR en cobertura o implementación.

**Evidencia durable de esta corrida:** [manifiesto RUN-20261017T014304Z](https://github.com/andrescastiglia/bank/blob/26be655b0bad9b29f84798e398e9138f25a6b89a/.regulatory-watch/evidence/RUN-20261017T014304Z.json). La bitácora, snapshots y estado permanecen en `automation/regulatory-state`; no se incorporan nuevas bitácoras operativas a `main`.

### Validación y decisiones pendientes

Se ejecutaron los checks documentales de catálogo funcional, enlaces/revisión/skills, inventario de vigilancia y sus fixtures de regresión. La transición de estado se verificó con `check_watch.py --state --run --previous-state`, además de conservar prefijos históricos e indexar una sola vez esta corrida. No se ejecutaron builds Rust, importación de series, cálculos financieros, escaneos de infraestructura/dependencias, pentest, parcheo ni recuperación. Se contrastaron además los 27 IDs FR explícitos del informe/propuestas con el catálogo y las huellas de bytes con las descargas. Los checks validan estructura y consistencia documental, no completitud jurídica ni eficacia de controles.

Para una decisión concreta faltan perfil del operador, productos/contratos que usan ICL/UVI y presencia de BeyondTrust/Fortinet en activos propios o de proveedores. Sin esos datos se propone análisis y verificación, sin activar importes/reglas, escanear redes ajenas, presentar reportes o comunicar a autoridades. GPL v2 y los merges exclusivos de `@andrescastiglia` se mantienen.

---

## Antecedente conservado — corte del 16/10/2026 a las 00:04

El contenido siguiente conserva los resultados y límites de la corrida anterior; no reemplaza la actualización ni representa nuevas pruebas de este corte.


**Fecha:** 16/10/2026, zona `America/Buenos_Aires`. **Repositorio:** [andrescastiglia/bank](https://github.com/andrescastiglia/bank). **Base examinada:** `main` en `979dd2c8f48e13d17343965d2e7194ec79ca0ed2`, con Rust y runtime propio `FROM scratch` ya integrados. **Naturaleza:** investigación documental y contraste de fuentes públicas; implementación y aceptación institucional sin evaluar.

### 1. Conclusiones principales

El proyecto tiene una biblioteca extensa y coherente en sus principios: autoridad financiera SQL, aislamiento por entidad, configuración fechada, asincronía durable y migración con conciliación. Su principal brecha frente a una operación bancaria real sigue siendo la falta de contratos ejecutables, implementación y evidencia independiente. La cantidad de requisitos y la cobertura de referencias no permiten inferir cumplimiento, seguridad, rendimiento ni disponibilidad efectiva.

| Eje | Resultado del contraste | Novedad frente al estado recuperado |
|---|---|---|
| Legal y normativo | Se verificaron los anexos CER/UVA y una disposición de pagos públicos al exterior. Se mantienen las transiciones SISCEN, A8492 y CNV ya identificadas. | Recuperación de evidencia pendiente de B13247; B13246 y disposición conjunta CGN/TGN 2/2026 incorporadas al análisis. Ningún parámetro activado. |
| Mercado | Siete ofertas muestran composición modular, APIs, parametrización y servicios operativos. Buena parte de sus capacidades ya tiene FR; faltan demostraciones comparables y localización comprobada. | Fineract amplía la comparación de alternativas libres; las demás páginas revalidan ofertas, sin demostrar lanzamientos nuevos ni cambios contractuales. |
| Tecnología | Rust 1.99.1 fue anunciado el 15/10/2026; corrige regresiones de enlace y FFI. La ejecución asíncrona requiere concurrencia acotada y persistencia explícita. | Release nueva verificada; selección concreta de toolchain y dependencias sigue pendiente. |
| Seguridad, crítico | La superficie incluye identidades, autorización de objetos, dinero, efectos externos, dependencias, importación, datos reservados y recuperación. Scratch reduce componentes, pero conserva estas superficies. | Dos avisos RustSec del 14/10 se incorporan como contexto del ecosistema, con alcance condicionado. No hay evidencia de Wasmtime instalado ni de explotación del proyecto. |

La vigilancia tiene resultado **PARTIAL**. Se recuperaron los **110 cuerpos de avisos** enumerados en las ediciones del 15 y 16 de octubre, pero sólo **3 de 40 archivos anexos identificados**; la revisión sustantiva se concentró en los actos pertinentes al core. Persisten fuentes y ventanas sin cobertura completa. Esta mejora de recuperación no cierra la cobertura del Boletín ni la del universo normativo.

Este informe conserva el [plan de implementación existente](PLAN_DE_IMPLEMENTACION_BANK.md) como antecedente. Presenta hechos, diferencias y evidencia faltante; sus recomendaciones finales son complementarias. No modifica la licencia GPL v2 ni el gobierno de merges exclusivos del mantenedor.

### 2. Alcance, método y estado del repositorio

#### 2.1 Ventana y continuidad

La corrida `RUN-20261016T030400Z` comenzó a las **00:04:00 del 16/10/2026 en Argentina** (`03:04:00 UTC`). Ventana objetivo: **[15/10/2026 00:00:00 −03:00, 16/10/2026 00:04:00 −03:00)**. Se recuperaron el inventario `2026-10-16.2`, dos corridas previas, sus gaps y cinco hitos de agenda; no se reinició desde el seed. El solapamiento de siete días queda limitado por el inicio solicitado del backfill, 15/10/2026. Textos anteriores necesarios para interpretar una publicación, y avisos técnicos del 14/10, se identifican como contexto.

Las consultas se efectuaron después del inicio. La edición del BO del 16/10 ya era accesible durante ellas, pero no se acreditó su hora de publicación. Se informa como **observación de esa fecha**, sin atribuir todos sus actos a los primeros cuatro minutos del día ni acreditar cobertura del resto del 16/10. Los actos con fecha sin hora deben volver a solaparse en la siguiente corrida.

Se leyó `main` mediante el conector GitHub, incluidas las instrucciones de gobierno y vigilancia; se contrastó el commit con Git y se consultaron las PR abiertas: ninguna al iniciar. La rama operativa no estaba publicada; el estado más reciente recuperable estaba integrado en `main`. Se conserva ese historial y se restablece su persistencia separada, sin incorporar bitácoras de esta corrida al diff del informe.

#### 2.2 Qué se examinó y qué demuestra

| Conjunto | Evidencia y alcance de la revisión |
|---|---|
| Repositorio base | Inventario de 189 archivos versionados, 125 Markdown y 28 skills. Huellas por archivo en el manifiesto operativo. Inventariar no equivale a auditar semánticamente cada cláusula. |
| Especificación | Mercado, cumplimiento, arquitectura, ocho ADR, trece familias NFR, alcance/catálogo funcional y módulos pertinentes a los hallazgos. El catálogo declara 1.016 FR/32 módulos, 173 entradas de cumplimiento, 71 criterios NFR y 21 controles. |
| Revisiones previas | Los seis análisis por perspectiva, sus 63 hallazgos, 14 paquetes y el plan de implementación son antecedentes. Se reutilizan sus IDs; no se cierran ni duplican por repetir una observación. |
| Stack vigente | [Contrato Rust/scratch](docs/deployment/rust-scratch.md), ADR-07 y FR-OPS-026. No hay `Cargo.toml`, `Cargo.lock`, archivos `.rs` ni Dockerfile de producto en la base inventariada. |
| Fuentes externas | Texto primario y anexos de actos seleccionados; índices oficiales; documentación técnica del responsable; declaraciones de fabricantes. Se registran URL solicitada/final, hora de consulta, resultado y SHA-256 de bytes. |
| Fuera de evaluación | Código bancario ejecutado, dependencias instaladas, pentest, infraestructura real, homologación de rieles, contratos privados, dictamen del operador y certificación. No se infiere ausencia de evidencias externas al repositorio. |

**Hecho** significa dato observado en la fuente citada. **Interpretación** explicita su posible consecuencia bajo un perfil. **Brecha** identifica evidencia o detalle faltante en el repositorio. Una promesa de un proveedor acredita su oferta declarada, no sus resultados, precio, cuota ni cumplimiento argentino. Una huella HTML distinta puede reflejar fecha de cabecera, token o plantilla: no se clasifica como reforma sin comparar el contenido pertinente.

### 3. Aspectos legales y normativos

#### 3.1 Regla de aplicabilidad

El [perímetro funcional](docs/functional/01-entidades-perimetro.md) ya distingue EF, PSPCP, otros PSP, PNFC, PSCPP y proveedor tecnológico. PSAV y agentes CNV requieren su propio encuadre; una cuenta de pago no se transforma en depósito y una licencia de software no habilita actividades financieras. Las obligaciones de la empresa proveedora tampoco son idénticas a las del operador.

Para cada acto se necesitan sociedad, registro, función, producto, moneda, canal, jurisdicción y fecha. Sin operador seleccionado, las conclusiones siguientes son **condicionales**. La ubicación de una norma bajo ARCA, BCRA o CNV no basta para convertirla en una regla común a todos los módulos.

#### 3.2 Datos regulatorios verificados y fechas

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

#### 3.3 Hallazgos nuevos o con evidencia ampliada

**INF-REG-01 — Series CER/UVA: se resolvió evidencia pertinente, falta el paquete ejecutable.** Los anexos BCRA y los archivos anexos del BO de B13246/B13247 se recuperaron por sus mecanismos oficiales. Los PDF BCRA tienen dos páginas cada uno; los del BO incluyen su propia presentación y tablas como imagen, revisadas visualmente tras renderizarlos. Huellas diferentes por formato/procedencia no prueban valores incompatibles. Se contrastaron período y extremos de las tablas; la verificación automatizada fila a fila de dos formatos y de la serie con mayor precisión sigue pendiente.

El diseño ya exige fuente, unidad, vigencia y regla de cálculo en FR-CFG-011/012/022, CTL-02/06 y NFR-01-C04. La brecha es materializar ingestión controlada, completitud por fecha, decimal exacto, corrección vinculada y oráculos independientes del cálculo contractual. Faltar un valor o recibir otra versión no habilita extrapolación silenciosa. La corrección de un índice tampoco debe reescribir automáticamente asientos históricos. ADR-05 y los skills de configuración/integridad financiera ya orientan ese tratamiento.

**INF-REG-02 — Pagos públicos al exterior: nueva especialización condicionada.** La disposición CGN/TGN establece un único beneficiario por orden, débito sobre CUT, autorización TGN mediante Nota de Pago y vínculo de identidad entre orden, solicitud en plataforma Comex BNA, Nota y medio de pago. El art. 8 exige mantener inalterable la identidad del beneficiario y su cuenta a lo largo del circuito. El anexo indica que el campo de cuenta bancaria no se informa en la orden de pago: esto no permite eliminar la cuenta del resto del proceso ni omitir su trazabilidad.

El anexo también atribuye al SAF, cuando corresponde, la retención de Ganancias al beneficiario exterior y la entrega del certificado SIRE dentro de **48 horas desde la emisión del medio de pago**. Para IVA como responsable sustituto prevé VEP y documentación según el circuito indicado, con alternativa de entrega dentro de esas 48 horas. Se citan RG 739 y 4356 como referencias del anexo, sin afirmar una revisión integral de sus modificatorias. No se determina una fecha calendario: falta el evento de cada pago y el perfil fiscal concreto.

FR-FXT-001/002, TAX-001/002, FR-RPT-001, ASY y COR ofrecen bases comunes. No se encontró un contrato específico e-SIDIF/CUT–BNA ni los estados y documentos de este circuito. **Interpretación:** si el primer servicio excluye SAF/CUT, registrar no aplicabilidad fundada; si lo incluye, se requiere especialización de integración, identidad y reloj fiscal, con Finanzas/Legal del operador. No trasladar el deber tributario del SAF al proveedor de software por mera automatización.

**INF-REG-03 — Actos financieros que no son nuevas obligaciones universales.** La [resolución conjunta 62/2026](https://www.boletinoficial.gov.ar/detalleAviso/primera/349042/20261016), emitida 14/10 y publicada 16/10, amplía emisiones del Tesoro: letras y bonos, incluidos TAMAR, dual CER/TAMAR y TAMAR/dólar linked. Rige desde su dictado. Es relevante para catálogo y valuación si el operador mantiene esos instrumentos; no obliga a comercializarlos ni permite reconstruir todos sus términos sin los actos originales.

La [resolución conjunta 61/2026](https://www.boletinoficial.gov.ar/detalleAviso/primera/349041/20261016) amplía una letra **intransferible** para el BCRA: no se clasifica como producto vendible a cualquier cliente. Los avisos de tasas BNA acreditan condiciones de esa entidad, no precios obligatorios para otros bancos. Los avisos BCRA de la edición del 16 revisados son edictos particulares; no se copiaron identidades ni se convirtieron sus plazos en requisitos generales.

**INF-REG-04 — ARCA: distinguir organización administrativa de reforma fiscal.** La [disposición 140/2026](https://www.boletinoficial.gov.ar/detalleAviso/primera/348992/20261015) trata asignación de funciones; la [66/2026 de Neuquén](https://www.boletinoficial.gov.ar/detalleAviso/primera/348993/20261015), reemplazos de jefaturas; la [92/2026 de Rosario](https://www.boletinoficial.gov.ar/detalleAviso/primera/349046/20261016), régimen de reemplazos. Su lectura no sostiene un cambio de alícuotas, padrón, diseño de registro o obligación informativa del core. La biblioteca ARCA y sus portadas se consultaron, pero no se completó una búsqueda cronológica con todos los textos y anexos: **no se concluye ausencia de novedades fiscales**.

#### 3.4 Agenda heredada, sin duplicar alertas

| Hito | Situación al 16/10/2026 | Evidencia pendiente |
|---|---|---|
| RG1172, vigencia general 16/10 | Fecha alcanzada; condición PSAV aún no seleccionada. Norma ya registrada. | Encadre/categoría, relación con actividad efectiva y paquete de controles. |
| RG1172 art. 40.b y A8492, 1/11 | Transiciones próximas, conocidas. | Período/primer vencimiento del PSAV; versión RI y pruebas para EF. |
| RG1173, transición particular 15/12 | Pendiente por sujeto alcanzado. | Mecanismo de idoneidad y evidencia real de la persona/entidad. |
| B13248, 1/1/2027 | Versión futura de SISCEN-0019. | Casos por umbral, moneda, período y excepción de inhábiles. |
| CGN/TGN 2/2026, 48 h por evento | Nuevo disparador condicional, no vencimiento fechado. | Perfil SAF/CUT y hora efectiva de emisión del medio de pago; registrar agenda sólo si se activa ese alcance. |

#### 3.5 Brecha de cumplimiento y trazabilidad

El [inventario de cumplimiento](docs/compliant.md) mantiene su corte histórico. Este informe amplía evidencia y análisis, sin afirmar que sus 173 entradas incorporen cada nueva especialización. La falta de un paquete CER/UVA o CUT no significa que falten motores genéricos de índices o pagos; el problema es la descomposición verificable por perfil y edición.

| Materia | Documentos/requisitos afectados | NFR / ADR / controles | Skill y criterio material a concretar |
|---|---|---|---|
| CER/UVA | Cumplimiento LAW-16/BCRA-F06; CFG, INT, ACC/CRE y documentos contractuales | NFR-01/09/11; ADR-05; CTL-02/06/19 | `core-regulatory-watch`, `core-bancario-argentina`, `adr-05-configuracion-versionada`: conservar identidad/serie/precisión, fecha y prueba de cambio/corrección. |
| RI/SISCEN | RPT-08; FR-RPT-021/038, FR-RSK-019 y paquete SISCEN aún pendiente | NFR-09/11; ADR-05; CTL-06/19 | Coordinadores FR/NFR: casos con oráculo por período, límites y calendario, más estado de aceptación del receptor. |
| PSAV/idóneos | LAW-18; INV/RPT/ENT/IAM/COR, especialización condicionada | NFR-05/06/11; ADR-05/06; CTL-08/09/17/19 | Revisar sujeto, categoría, información/custodia y habilitación; no expandir por defecto el denominador de todos los perfiles. |
| CUT/exterior | FXT/TAX/RPT/COR/ASY; contrato y operación SAF/BNA | NFR-01/04/07/08/11; ADR-03/05; CTL-04/06/12/19 | `core-fr-requisitos` y vigilancia: identidad consistente, estados autorizados y reloj de 48 h desde evento, sólo con alcance aplicable. |

No se modificaron reglas monetarias, reportes, contratos ni skills por una interpretación aún no seleccionada. La revisión competente debe resolver aplicabilidad; el desarrollo con datos sintéticos puede continuar sobre contratos explícitos. Los hallazgos REV-LEG-01/08/10, REV-ACC-01/04 y REV-QA-05 siguen siendo pertinentes.

### 4. Mercado y competencia

#### 4.1 Oferta observada

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

#### 4.2 Mapa de capacidades e integraciones

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

#### 4.3 Lectura comercial y económica

**Hecho:** hay convergencia de ofertas hacia modularidad, integración y operación acompañada. **Inferencia:** para Bank, «Rust + APIs + open source» describe opciones técnicas, pero aún no demuestra una ventaja económica para un operador argentino. Una diferenciación defendible podría surgir de localización explicable, migración conciliada, reglas reproducibles y salida comprobable; su demanda y costo siguen sin medirse.

No se verificaron precios públicos comparables de core, margen por cliente ni un TAM nuevo. Las cifras ilustrativas de la documentación previa siguen siendo supuestos, no precios observados. La unidad relevante de costo debe incluir celda/entidad, bases y réplicas, broker, retención, KMS/IAM, soporte, actualizaciones y egreso. El costo de contribuir al proyecto libre es distinto del de ofrecer una operación con SLA.

Los hallazgos REV-COM-01/02/04/07/08/11 conservan su utilidad, bajo el gobierno actualizado: seleccionar un caso para validar no convierte ventas o ARR en condición para contribuir. No se contactó a fabricantes ni clientes y no se concluye cuál proveedor gana una licitación sin su perfil y evidencia.

### 5. Innovación tecnológica y arquitectura

#### 5.1 Novedad de toolchain

El [anuncio oficial de Rust 1.99.1](https://blog.rust-lang.org/2026/10/15/Rust-1.99.1/) del **15/10/2026** identifica tres correcciones: símbolo `wcslen` faltante en ciertos targets; compilación incorrecta de retornos FFI `bool` en x86_64 por extensión del registro; y carga de `libLLVM` por `rust-lld` en macOS fuera del proxy de rustup. El [manifiesto estable](https://static.rust-lang.org/dist/channel-rust-stable.toml), consultado el 16/10, informa fecha 15/10 y Rust `1.99.1 (58cf8f9c3 2026-10-13)`.

**INF-TEC-01 — Release relevante, adopción pendiente.** Las correcciones de FFI/enlace merecen evaluación por el contrato de binarios estáticos y posibles clientes nativos. No se demostró afectación del futuro binario Linux ni se clasificó el anuncio como una CVE. Sin workspace o toolchain fijado no hay upgrade aplicado. El contrato vigente ya exige `rust-toolchain.toml`, lockfile, targets/features e inspección ELF: la evidencia necesaria es build y prueba por arquitectura, no apuntar a `stable` flotante.

#### 5.2 Frameworks y ejecución asíncrona

La [documentación de axum consultada](https://docs.rs/axum/latest/axum/) muestra **0.8.9**, fechada 22/9/2026, integración con Tokio/Tower y dependencias/feature flags. Es un candidato observado, anterior a la ventana; no una dependencia seleccionada. [Tokio, tareas](https://tokio.rs/tokio/tutorial/spawning) y [puentes entre código síncrono/asíncrono](https://tokio.rs/tokio/topics/bridging) explican mecanismos de ejecución; no garantizan durabilidad de una obligación de negocio.

**Interpretación para Bank:** un framework puede acelerar contratos HTTP, middleware, límites y trazas. La elección debe contrastar soporte, licencias, cancelación, errores, TLS y dependencias nativas con NFR-03/05/09. Limitar pools y concurrencia evita que hashing, compresión, cómputo de intereses o importaciones bloqueen el executor. Una tarea en memoria aceptada sin estado durable no satisface FR-ASY-001/016, aunque use `async`.

#### 5.3 Contraste de patrones con el diseño vigente

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

#### 5.4 Scratch: contrato y límites observables

La [documentación de Docker sobre imágenes base](https://docs.docker.com/build/building/base-images/) describe scratch como base mínima. Bank requiere binarios Linux realmente estáticos, recursos de CA/calendarios explícitos, UID/GID no root, raíz de sólo lectura, probes sin shell y terminación SIGTERM controlada. Los [security contexts de Kubernetes](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) permiten declarar controles, pero su presencia en YAML debe comprobarse contra el proceso y plataforma efectivos.

**INF-TEC-02 — La imagen mínima desplaza responsabilidades al artefacto.** CA vencidas, tzdata incompleta, DNS, bibliotecas nativas, carga de plugins o apagado durante commit/ACK pueden fallar sin una distribución Linux. Falta construir imagen por arquitectura y probar TLS válido/inválido, zona de negocio, filesystem, probes y recuperación de trabajo. La [regla de lockfiles de Cargo](https://doc.rust-lang.org/cargo/guide/cargo-toml-vs-cargo-lock.html) favorece reproducibilidad; la release necesita además builder/digest, linker, features, SBOM y procedencia. No se ejecutaron builds, inspección ELF ni scans de imágenes porque no existen esos artefactos en el alcance.

### 6. Seguridad informática — eje crítico

#### 6.1 Avisos y exposición efectiva

| Fuente verificada | Dato observado y fecha | Evaluación de aplicabilidad |
|---|---|---|
| [RustSec RUSTSEC-2026-0352](https://rustsec.org/advisories/RUSTSEC-2026-0352.html), [aviso upstream](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-m9f7-9w4p-gv38) | Emitido 14/10/2026; `wasmtime-wasi`, escape de sandbox por renombrar symlinks con barras finales; CVSS 4.0 8,8. RustSec identifica **macOS/FreeBSD**. Ramas corregidas: `>=36.0.18,<37.0.0`; `>=48.0.6,<49.0.0`; `>=49.0.3`. | Contexto anterior al backfill, nuevo para este relevamiento. No hay Wasmtime seleccionado. El alcance macOS/FreeBSD no demuestra exposición del runtime Linux scratch; evaluar también herramientas de desarrollo si se incorporara ese paquete. |
| [RustSec RUSTSEC-2026-0363](https://rustsec.org/advisories/RUSTSEC-2026-0363.html), [aviso upstream](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-q554-3cjc-rx7p) | Emitido 14/10; `wasmtime`, tablas de handles del component model con límite sólo por instancia y sin cargo a un límite global; agotamiento de recursos, CVSS 3.1 6,2. Mismas ramas corregidas indicadas arriba. | Condicional a versión, funcionalidad y entorno. No es una vulnerabilidad de todo servicio Rust. Sin árbol de dependencias no se emite resultado de exposición o de `cargo audit`. |
| [PostgreSQL CVE-2026-14666](https://www.postgresql.org/support/security/CVE-2026-14666/) y [CVE-2026-19385](https://www.postgresql.org/support/security/CVE-2026-19385/) | Avisos del 13/8/2026 revalidados, ya registrados: RLS/plan con permisos obsoletos y ejecución de código mediante transform malicioso en `pg_dump`. Versiones corregidas: 18.6, 17.11, 16.15, 15.19 y 14.24. | PostgreSQL es tecnología propuesta; versión/servicio no seleccionados. Verificar componente servidor y cliente de backup/restauración por separado. No asumir RLS como única frontera ni usar herramientas antiguas sobre fuentes no confiables. |
| [CISA KEV, repositorio oficial](https://raw.githubusercontent.com/cisagov/kev-data/develop/known_exploited_vulnerabilities.json) | Catálogo `2026.10.15`, publicación `2026-10-15T17:00:11.2795Z`, 1.746 entradas; mismo hash que la corrida anterior. El caso Atlassian CVE-2026-21589 ya estaba identificado. | No se genera otra alerta idéntica. Inventario efectivo ausente; los plazos CISA no son automáticamente plazos legales argentinos. Un catálogo estable no acredita que todo el stack carezca de otros avisos. |

**INF-SEC-01 — Gestión de exposición por artefacto, no por lenguaje.** Rust evita clases de errores de memoria dentro de su modelo seguro, pero `unsafe`, FFI, crates, librerías C/TLS, builder y herramientas operativas conservan superficie. La evidencia mínima futura debe vincular aviso → componente/versión/features/OS → artefacto/digest → decisión de tratamiento → prueba. `cargo audit`/herramienta equivalente, SBOM y revisión de licencias son mecanismos candidatos; no se informa un resultado ficticio sin lockfile o imagen.

Los dos RustSec tienen severidades de escalas CVSS diferentes. Ninguno se eleva a «incidente crítico de Bank» por el título de esta sección. El riesgo del negocio requiere exposición, capacidades del atacante, fondos/datos y controles del despliegue concreto.

#### 6.2 Vectores de ataque y controles existentes

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

#### 6.3 Identidad, cifrado, APIs y estándares

**Identidad.** OIDC/OAuth autentican e intercambian autorizaciones; no sustituyen KYC, poderes ni controles de negocio. Se necesita validar emisor, audiencia, firma, tiempo y contexto, y revalidar facultades materiales al serializar el comando. El refuerzo de autenticación debe corresponder a la acción y al perfil argentino. Una guía internacional no autoriza eliminar requisitos BCRA específicos, ni convertir una excepción de canal en regla general.

**Cifrado y claves.** El diseño ya exige transporte/reposo protegidos, secretos separados, mínimos permisos y rotación/recuperación. Falta elegir proveedor TLS/KMS/HSM, cadenas de confianza, algoritmos y política temporal con soporte efectivo. Certificado válido, cifrado de disco y mTLS cubren controles distintos. Una imagen scratch debe validar nombre/cadena y cargar el trust store; «sin paquetes» no demuestra criptografía segura. El esquema de claves debe sobrevivir al restore sin copiar secretos al repositorio o a trazas.

**APIs financieras.** [FAPI 2.0 Security Profile](https://openid.net/specs/fapi-security-profile-2_0-final.html), final del **22/2/2025**, ofrece un perfil OAuth de alta seguridad con mecanismos como PAR, PKCE y tokens vinculados al emisor de la prueba mediante mTLS/DPoP según perfil. No se obtiene conformidad por habilitar JWT ni por incorporar sólo un mecanismo. Bank necesita una decisión de perfil aplicable, matriz de requisitos y ensayos de replay, redirecciones, claves y compatibilidad con el IAM escogido. La autorización por objeto/campo y la idempotencia financiera siguen siendo controles propios.

**Verificación de aplicaciones.** [OWASP ASVS](https://owasp.org/projects/asvs) mantiene la referencia ASVS 5.0 de la documentación; el HTML reconsultado no demuestra una edición normativa nueva por variar de hash. ASVS y API Top 10 sirven para requisitos y amenazas complementarias: no son un pentest ejecutado ni una certificación de Bank. NIST, ISO/IEC, PCI y Swift conservan naturaleza técnica, voluntaria o contractual según alcance; el disparador real puede ser una norma, contrato o participación de red. No se accedió ni se copiaron textos restringidos completos de ISO/Swift, ni se acreditó cobertura universal de sus ediciones.

FR-OPS-042 ya exige registrar edición/programa, contrato activador y evidencia. PCI necesita delimitar CDE y rol; Swift, arquitectura/participación y evaluación correspondiente; un certificado de gestión no homologa todos los servicios del core. Este informe no atribuye esas obligaciones a un perfil que no procese tarjetas o no participe en la red.

#### 6.4 Impacto trazable de seguridad

Los avisos de PostgreSQL remiten a ADR-02/06/08, NFR-05/09/10 y CTL-09/15/20; Rust/FFI/scratch, a ADR-07, FR-OPS-026 y NFR-05/09; identidad/API, a IAM/PAY/ASY, ADR-03/06, NFR-05/08 y CTL-04/09/17. Los hallazgos previos REV-SEC-01/02/03/05/06 y REV-ARC-01/02/06 siguen abiertos en su alcance documental.

Los skills de stack, seguridad, integridad, asincronía y migración ya prescriben separación entre diseño y prueba. La mejora relevante es que una futura selección de crates/servicios aporte evidencia concreta consumible por esos skills. Añadir otra instrucción genérica o declarar «scan aprobado» sin artefacto no cierra esa brecha.

### 7. Cobertura real, evidencia y pendientes

#### 7.1 Resultado por fuente

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

#### 7.2 Procedencia durable y deduplicación

La evidencia de esta corrida se guarda separadamente en [`automation/regulatory-state`, manifiesto RUN-20261016T030400Z](https://github.com/andrescastiglia/bank/blob/71c12cfc6daf997c6b36302941242508abb9919f/.regulatory-watch/evidence/RUN-20261016T030400Z.json), con bitácora y estado en esa misma rama. La referencia al commit publicado es inmutable. Las fuentes enlazadas en el informe son primarias; el manifiesto identifica el contenido realmente recuperado. Los cuerpos comerciales, datos de personas de edictos y textos restringidos no se publican en el repositorio.

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

#### 7.3 Comprobaciones y límites

Se ejecutaron y aprobaron las comprobaciones del catálogo reproducible (1.016 FR), revisión documental/enlaces/28 skills, inventario de vigilancia y 69 fixtures de regresión. También aprobó `check_watch.py` con `--state`, `--run` y `--previous-state` de esta corrida: conserva como prefijos exactos `changes`, `agenda` y `run_index`, indexa una sola vez su ID y no avanza fuentes incompletas. Se contrastaron los 23 IDs FR explícitos del informe contra el catálogo y las cinco huellas seleccionadas contra las descargas. Estos controles no prueban lectura jurídica suficiente ni producto bancario. La propuesta no contiene nuevas bitácoras operativas destinadas a `main`.

No se ejecutaron aplicaciones bancarias, migración con fondos, builds Rust, escaneos de dependencias/imágenes, pruebas de intrusión ni de recuperación. No hay base para declarar una vulnerabilidad explotada, un control operativo eficaz, una certificación ni un SLA cumplido. Las protecciones de `main` siguen con la limitación de verificación documentada en [GOVERNANCE.md](GOVERNANCE.md); esta investigación no cambia permisos ni las verifica por ensayo destructivo.

### 8. Observaciones finales derivadas de los datos

1. Seleccionar perfil y primer recorrido para poder convertir fuentes y FR genéricos en un paquete con oráculos. Mantener PSAV, CUT y jurisdicciones como alcances condicionados hasta esa decisión.
2. Evaluar Rust 1.99.1 al fijar el primer toolchain y exigir evidencia por target, dependencias nativas, TLS y apagado en scratch. Conservar reproducibilidad y una política de actualización; no adoptar una versión sólo por ser la última observada.
3. Demostrar un flujo financiero pequeño, incluida carga inicial/conciliación y salida, con permisos y estados externos ambiguos. Es la evidencia que conecta arquitectura, valor comercial y calidad.
4. Retomar los 37 anexos BO y los gaps oficiales preservados. La vigilancia permanece parcial aunque haya hallazgos válidos; no declarar «sin novedades» global ni duplicar alertas sin variación material.

Las decisiones, prioridades y merges corresponden al mantenedor. La aplicación jurídica y la aceptación operativa corresponden al sujeto y funciones competentes; este informe aporta evidencia y preguntas concretas para esas decisiones.
