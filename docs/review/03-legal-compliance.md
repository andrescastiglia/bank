# Revisión legal y de cumplimiento del proyecto

**Revisión:** 16/10/2026 UTC. **Repositorio revisado:** `2e5d579103b94ab70c16d81debe73bf5840ba0c8`. **Base normativa documental:** 15/10/2026. **Objeto:** preparación jurídica de un proveedor de core y de sus posibles clientes regulados. **Estado observado:** documentación propuesta, sin aplicación bancaria, contratación firmada, piloto con datos/fondos reales ni controles operativos acreditados en el repositorio.

La biblioteca distingue adecuadamente el software, el operador regulado y la evidencia institucional. La principal brecha jurídica está entre esa especificación y un servicio concreto que pueda ofrecerse y contratarse: perímetro del primer caso, derechos de IP, términos de venta, datos, cadena de proveedores y obligaciones de operación todavía no están cerrados. Los diez hallazgos siguientes son decisiones, especificaciones contractuales o evidencias pendientes; no representan diez infracciones observadas.

**P0** exige resolver la condición antes del compromiso o piloto específicamente afectado; permite seguir investigando, diseñando y desarrollando con datos sintéticos. **P1** exige preparación antes de la entrega/ampliación correspondiente. El detalle estructurado, responsables y entregables sugeridos se conserva en [findings/legal.json](findings/legal.json).

## Fortalezas comprobadas

- [Perímetro y FR-ENT-004](../functional/01-entidades-perimetro.md) distinguen EF, PSPCP, otra función PSP, PNFC, PSCPP y proveedor; [COR](../functional/32-corresponsalia-baas-plataformas.md) identifica cliente del PSPCP, interfaz del tercero y separación de fondos. No se atribuye una licencia al software.
- [CON](../functional/05-contratos-documentos.md) separa oferta, aceptación, formalización, habilitación y entrega; distingue firma electrónica de digital y preserva versiones económicas. Es una base útil para evidencia contractual del operador.
- [DAT](../functional/27-auditoria-privacidad-archivo.md), [NFR-06](../nfr/NFR-06-privacidad-residencia-retencion.md) y [ADR-06](../adr/ADR-06-aislamiento-por-celda.md) incluyen finalidad, países, subencargados, secreto, derechos y conservación por categoría; evitan TTL universal, anonimización presumida y exposición de ROS.
- [OPS](../functional/30-operacion-continuidad-terceros.md) distingue avisos de nuevo servicio, outsourcing e incidente, acceso supervisor y salida. [NFR-02](../nfr/NFR-02-disponibilidad-recuperacion.md) reconoce metas propuestas y pérdida regional posible; no promete RPO cero por replicación asíncrona.
- [Cumplimiento](../compliant.md) y [alcance funcional](../functional/scope.md) no equiparan ISO/SOC/PCI/Swift con ley ni llaman cumplimiento al 100 % de relaciones del catálogo. Mantienen destinatarios, condiciones, transiciones y límites de lectura de fuentes.

## Diagnóstico por lente

| Lente | Resultado documental | Decisión pendiente |
|---|---|---|
| Proveedor frente a operador | Perfiles y responsabilidades bien separados en diseño | Sociedad, producto, cliente y rol reales; no decidir desde la marca BaaS |
| Venta y responsabilidad | Mercado propone alcance y aceptación; CON cubre contratos financieros | MSA/SOW, aceptación, remedios, IP y obligaciones comerciales del proveedor |
| Propiedad intelectual | Existe LICENSE GNU GPL v2 e inventario de dependencias propuesto | Alcance, titulares, contribuciones y compatibilidad del modelo de entrega |
| Datos y consumidor | Funciones de consentimiento, secreto, derechos, entrega/baja y reclamos especificadas | DPA, países, plantillas y plazos del producto seleccionado |
| Terceros y operación | Requisitos de cadena, aviso, supervisión y salida especificados | Contratos, evidencias y calendario del proveedor/servicio concreto |
| Normas y aseguramiento | Base fechada y distinciones de exigibilidad explícitas | Perfil contratado, texto autorizado cuando corresponda y dueño del mantenimiento |

## Hallazgos y acciones

| ID | Prioridad | Hallazgo | Activador |
|---|---|---|---|
| REV-LEG-01 | P0 | Falta cerrar el perímetro jurídico del primer caso de uso | Antes de comprometer un piloto que contrate clientes, trate datos reales o mueva fondos. |
| REV-LEG-02 | P0 | La oferta carece de paquete contractual proveedor–cliente | Antes de emitir una oferta vinculante, aceptar un piloto remunerado o asumir operación productiva. |
| REV-LEG-03 | P0 | GPL v2 no está integrada en la estrategia de IP y distribución | Antes de ofrecer derechos exclusivos, una licencia incompatible o entregar software/artefactos a un cliente o tercero. |
| REV-LEG-04 | P1 | No está definido qué estándares y aseguramiento se contratarán | Antes de responder una licitación o prometer una certificación, validación de red o conformidad por cláusula. |
| REV-LEG-05 | P0 | El tratamiento de datos aún no tiene un DPA y mapa de países aplicado | Antes de recibir datos personales reales, habilitar soporte externo o replicar datos/telemetría a un destino internacional. |
| REV-LEG-06 | P0 | La contratación de terceros no tiene cadena de derechos y calendario aplicados | Antes de cerrar proveedor/fecha de piloto con tercerización regulada o cambiar una ubicación/subcontratista en alcance. |
| REV-LEG-07 | P0 | Falta convertir los relojes regulatorios en un SLA proveedor–entidad | Antes de asumir guardia/operación de un servicio alcanzado o firmar su SLA. |
| REV-LEG-08 | P0 | El primer producto aún no tiene condiciones y plazos legales concretos | Antes de ofrecer/contratar el primer préstamo, cuenta u otro producto a usuarios reales. |
| REV-LEG-09 | P0 | El archivo legal y la equivalencia del soporte no están resueltos para la migración | Antes de migrar/destruir originales, llevar libros oficiales en el nuevo soporte o terminar el servicio con datos reales. |
| REV-LEG-10 | P1 | El mantenimiento regulatorio carece de dueño y compromiso de servicio aplicados | Antes de fijar precio/alcance de localización mantenida y, en todo caso, antes del piloto alcanzado por una transición. |

### REV-LEG-01 — Falta cerrar el perímetro jurídico del primer caso de uso

**P0 · missing_decision · Responsable sugerido:** Legal/Cumplimiento de la entidad y dirección del proveedor.

ENT/COR especifican correctamente perfiles y responsabilidades, pero no existe un expediente aplicado a una sociedad, licencia, producto, custodio y canal reales. La biblioteca no permite decidir todavía si el proveedor sólo vende tecnología o ejecutará una función regulada propia. No se observó intermediación ilegal ni se afirma que falten FR de habilitación.

**Consecuencia:** Una propuesta puede asignar al proveedor obligaciones que no puede cumplir, ocultar al PSPCP responsable o incluir productos fuera de la licencia del cliente; el costo de corregir contrato y arquitectura aparece después de vender.

**Evidencia:**
- [docs/functional/01-entidades-perimetro.md](../functional/01-entidades-perimetro.md), FR-ENT-002, FR-ENT-003, FR-ENT-004 y FR-ENT-021: Exigen permisos y relación institucional; son especificaciones propuestas, sin sociedad/caso instanciado.
- [docs/functional/32-corresponsalia-baas-plataformas.md](../functional/32-corresponsalia-baas-plataformas.md), FR-COR-001, FR-COR-002, FR-COR-004, FR-COR-006 y Dependencias y límites: Distingue software, PSPCP como Servicio y cliente del proveedor regulado; las habilitaciones/contratos siguen pendientes.
- [docs/functional/scope.md](../functional/scope.md), Perfiles y activación: La aplicabilidad por sociedad, perfil, producto, canal y fecha está exigida, no resuelta para un operador.

**Acción concreta:** Preparar un expediente jurídico del cliente de diseño con personas legales, licencias/registros y alcance de operaciones. Dibujar titularidad de fondos y cuentas, acreedor contractual, KYC/AML, atención, reportes, terceros y fronteras del proveedor. Obtener decisión fundada por función y registrar aplicabilidad/exclusión y condiciones de activación; no inferir habilitación desde BaaS o la marca.

**Cierre verificable:** Matriz aplicada al primer producto con evidencia de autorización/registro y responsable de cada flujo. Prueba de mesa de alta, cobro, restitución y cierre con una única entidad responsable; exclusiones y dependencias aprobadas.

### REV-LEG-02 — La oferta carece de paquete contractual proveedor–cliente

**P0 · specification_gap · Responsable sugerido:** Dirección comercial, Legal y responsable de entrega.

CON cubre contratos de productos financieros y OPS/COR permiten registrar contratos de terceros; no hay borrador de contrato marco de venta tecnológica, SOW, orden de servicio o anexo de aceptación para este proveedor. El análisis comercial propone diagnóstico, piloto, implementación y suscripción, pero no distribuye jurídicamente entregables, dependencia del cliente, garantía, reparación de errores, límites/excepciones de responsabilidad, propiedad de mejoras y finalización.

**Consecuencia:** Alcance abierto, aceptación discutible, pago ligado a dependencias ajenas y exposición no presupuestada por dinero incorrecto, datos o indisponibilidad; garantías publicitarias pueden superar lo construido.

**Evidencia:**
- [docs/market_analysis.md](../market_analysis.md), §§8.1, 11.1 y 12.1: Identifica unidades facturables, IP y responsabilidades como materias contractuales sin aportar términos del proveedor.
- [docs/functional/05-contratos-documentos.md](../functional/05-contratos-documentos.md), Propósito y FR-CON-001, FR-CON-022 a FR-CON-025: Especifica documentación de los productos del operador; no equivale al contrato de comercialización del core.
- [docs/functional/30-operacion-continuidad-terceros.md](../functional/30-operacion-continuidad-terceros.md), FR-OPS-030 y FR-OPS-036: Registrar un contrato y un plan de salida no fija sus condiciones comerciales/jurídicas.

**Acción concreta:** Preparar MSA/SOW y anexos de alcance, aceptación, precios, cambios, datos, seguridad, soporte y salida, con jerarquía documental. Separar producto común, localización común, integración específica y servicios; fijar entregables del piloto y qué depende del cliente/tercero. Negociar responsabilidad y remedios por clase de riesgo, preservando obligaciones imperativas aplicables; no copiar el descargo GPL como contrato de servicio.

**Cierre verificable:** Paquete revisable aprobado por dirección/Legal con ejemplos de rechazo, subsanación y aceptación de un hito. Matriz cláusula–FR/NFR–evidencia y exclusiones comerciales coherentes con el producto realmente disponible.

### REV-LEG-03 — GPL v2 no está integrada en la estrategia de IP y distribución

**P0 · missing_decision · Responsable sugerido:** Legal de propiedad intelectual y dirección del proveedor.

LICENSE contiene GNU GPL versión 2. Los documentos comparan SaaS/licencia/operación propia y prevén mejoras comunes/exportación, pero no delimitan qué obras quedan licenciadas, titularidad/contribuciones, avisos por artefacto, componentes de terceros ni derechos que se prometerán al banco. No se identificó infracción: GPL permite cobrar y el mero acceso a un servicio remoto no se equipara automáticamente a distribución bajo GPL v2. Tampoco puede presumirse titularidad suficiente para relicenciar.

**Consecuencia:** Prometer exclusividad, restricciones adicionales o entrega/escrow sin derechos compatibles puede impedir cumplir el contrato o forzar rediseño de la oferta. El copyright de la licencia de FSF no identifica a los titulares del proyecto.

**Evidencia:**
- [LICENSE](../../LICENSE), GNU GENERAL PUBLIC LICENSE v2, §§0–3, 6 y 11–12: Distingue distribución, código fuente, derechos y descargos; existe licencia, no un repositorio sin licencia.
- [docs/market_analysis.md](../market_analysis.md), §§8.1, 11.1 y 12.1: Contempla licencia, IP y mejoras comunes sin una decisión de licenciamiento aplicable a este repositorio.
- [docs/adr/ADR-07-stack-gestionado.md](../adr/ADR-07-stack-gestionado.md), Decisión propuesta: Exige inventariar licencia/SBOM de dependencias; no resuelve IP del producto, documentos y contribuciones.

**Acción concreta:** Inventariar obras, autores/cesiones o permisos y dependencias; definir alcance de GPL para software, documentación y skills. Acordar modelos de SaaS/distribución/on-premise y política de mejoras, integraciones y contribuciones con sus avisos/licencias. Revisar obligaciones por combinación y distribución concretas y cualquier promesa de exclusividad, fuentes o escrow; no cambiar unilateralmente derechos ajenos.

**Cierre verificable:** Decisión escrita de IP/licenciamiento con titularidad/procedencia suficiente y avisos consistentes por artefacto. Ejemplo de entrega SaaS/on-premise con materiales/obligaciones identificados y términos MSA compatibles, sin inferir obligaciones AGPL inexistentes.

### REV-LEG-04 — No está definido qué estándares y aseguramiento se contratarán

**P1 · missing_decision · Responsable sugerido:** Seguridad/GRC, Legal y dirección comercial.

La biblioteca distingue correctamente ISO, SOC, PCI, EMVCo, Swift y ley, pero sólo releva metadatos/descripciones públicas de ISO y no acredita certificados/informes ni textos completos autorizados. El catálogo de 100 % mide relaciones. Falta un perfil contractual de adopción y evidencia que diga qué edición/servicio/sitio debe demostrarse por el proveedor, el cliente y cada tercero. No se halló una certificación falsamente declarada.

**Consecuencia:** Un comprador puede incorporar por referencia una obligación mucho mayor que el producto presupuestado; una certificación de nube no cubre app, controles del cliente o auditoría supervisora.

**Evidencia:**
- [docs/compliant.md](../compliant.md), Estándares ISO; Cómo interpretar su exigibilidad: Declara acceso al catálogo, no auditoría del texto íntegro ni conformidad por cláusula.
- [docs/functional/30-operacion-continuidad-terceros.md](../functional/30-operacion-continuidad-terceros.md), FR-OPS-035, FR-OPS-038 y FR-OPS-042: Son funciones propuestas de evaluación y registro de alcance, CUEC y programa de validación.
- [docs/functional/coverage.md](../functional/coverage.md), Denominadores y resultado: El porcentaje expresa trazabilidad documental y conserva pendientes, sin informe de auditoría.

**Acción concreta:** Definir perfil de estándares por función/cliente con edición, contrato activador, alcance, dueño y forma de evaluación. Obtener acceso autorizado a los textos que se comprometerán y evaluar por cláusula cuando corresponda. Preparar política de afirmaciones comerciales y expediente de certificados/informes completos, exclusiones, controles del usuario y períodos sin cobertura.

**Cierre verificable:** Anexo de adopción sin PCI/Swift universales ni ISO de producto por analogía. Cada afirmación de certificado/validación se vincula a evidencia íntegra vigente del servicio/sitio/versión contratado o se conserva como pendiente.

### REV-LEG-05 — El tratamiento de datos aún no tiene un DPA y mapa de países aplicado

**P0 · evidence_gap · Responsable sugerido:** Responsable de datos/Legal de la entidad y privacidad del proveedor.

DAT/NFR-06/ADR-06 especifican inventario, roles, finalidades y transferencias, incluidos DR, KMS y soporte; faltan el mapa aplicado y los instrumentos de encargo/transferencia de una cadena real. No se puede deducir país adecuado, finalidad autorizada, acceso de soporte o habilitación de entrenamiento de IA de la contratación del core. No se observó transferencia real de datos en el repositorio.

**Consecuencia:** Procesamiento fuera de instrucciones/finalidad, secreto o transferencias sin mecanismo aplicable; un despliegue primario local puede ocultar exportación por logs, soporte, backups o modelos.

**Evidencia:**
- [docs/functional/27-auditoria-privacidad-archivo.md](../functional/27-auditoria-privacidad-archivo.md), FR-DAT-006, FR-DAT-007, FR-DAT-008, FR-DAT-026 y FR-DAT-028: Las capacidades están definidas; no incluyen DPA firmado o destinos/subencargados seleccionados.
- [docs/functional/31-gobierno-modelos-ia.md](../functional/31-gobierno-modelos-ia.md), FR-AIG-005, FR-AIG-006 y FR-AIG-023: El uso secundario de datos y países del modelo exige decisión/contrato, no permiso implícito.
- [docs/nfr/NFR-06-privacidad-residencia-retencion.md](../nfr/NFR-06-privacidad-residencia-retencion.md), C01 y C05; pendientes: Registra finalidad/rol/país/destinatario y ausencia de cambios no habilitados, aún sin evidencia.

**Acción concreta:** Cerrar inventario de tratamientos por flujo y rol de responsable/encargado/subencargado, incluyendo retorno y copias. Preparar DPA e instrumentos de transferencia que correspondan al destino/operación, con instrucciones y cadena completa. Ensayar con datos sintéticos y denegar datos reales/destinos pendientes hasta disponer del expediente del flujo.

**Cierre verificable:** Mapa aplicado con países, accesos remotos, finalidades, conservación y mecanismo fundado; DPA/contratos exigibles formalizados antes del flujo real. Revisión de configuración/contrato que incluya telemetría, DLQ, KMS, DR y terceros de IA, sin exposición general de ROS.

### REV-LEG-06 — La contratación de terceros no tiene cadena de derechos y calendario aplicados

**P0 · evidence_gap · Responsable sugerido:** Compras/Legal, responsable TI/SI de la entidad y gestión de terceros.

OPS/COR y el TO relevado prevén due diligence, contratos, acceso supervisor, salida y avisos; no existe proveedor seleccionado con contratos de toda la cadena ni expediente de notificación. Una cláusula de auditoría genérica o SOC no permite presumir acceso exigible a SEFYC. El aviso depende de sujeto/servicio, no es una autorización universal; una corresponsalía no se clasifica automáticamente como outsourcing TI/SI.

**Consecuencia:** Comprometer una fecha sin plazo de aviso o aceptar términos estándar que limiten auditoría, fuentes/documentación y salida puede dejar sin vía de habilitación al servicio ya vendido.

**Evidencia:**
- [docs/functional/30-operacion-continuidad-terceros.md](../functional/30-operacion-continuidad-terceros.md), FR-OPS-029 a FR-OPS-036: Define evaluación, contrato, derechos, aviso y salida, pero no acredita un expediente de contratación concreto.
- [docs/compliant.md](../compliant.md), Tercerización; BCRA-T27, BCRA-T29, BCRA-T32 y BCRA-T34: Distingue 60 días/servicio crítico, cambios de proceso, cadena supervisora y reglas propias de EF; no se verificó un servicio real.
- [docs/functional/32-corresponsalia-baas-plataformas.md](../functional/32-corresponsalia-baas-plataformas.md), FR-COR-020, FR-COR-021 y FR-COR-022: Preserva separación de figuras y derechos/salida como condición de activación.

**Acción concreta:** Clasificar servicios/terceros por figura y criticidad con el régimen del cliente. Comparar contratos y subcontratos con matriz de derechos de entidad/supervisor, incidentes, cambio de país, continuidad y salida. Construir cronograma por disparador real y conservar notificación por responsable cuando corresponda, sin inventar una aprobación regulatoria.

**Cierre verificable:** Contratos de la cadena cerrados sin bloqueos materiales de auditoría/salida y con brechas decididas de forma compatible con obligaciones. Fecha de servicio viable frente a avisos aplicables, constancias antes del inicio y ejercicio de pedido de evidencia/exportación.

### REV-LEG-07 — Falta convertir los relojes regulatorios en un SLA proveedor–entidad

**P0 · specification_gap · Responsable sugerido:** Legal, SRE/Seguridad y responsable de incidentes de la entidad.

OPS registra los relojes y responsables de incidentes y NFR-02 conserva metas propuestas, pero no hay presupuesto contractual entre detección del proveedor, escalamiento, clasificación propia del cliente y envío autorizado. Tampoco se han pactado cobertura de guardia, información mínima temprana, contingencia del presentante ni remedios por indisponibilidad. Un SLO de API local de 99,95 % no sustituye el aviso RRCI en la primera hora ni garantiza pagos de punta a punta.

**Consecuencia:** El banco puede recibir tarde o incompleto el incidente de su proveedor y perder capacidad de cumplir su propio aviso, aunque el ticket interno cumpla el SLA elegido; exposición contractual por garantías no ensayadas.

**Evidencia:**
- [docs/functional/30-operacion-continuidad-terceros.md](../functional/30-operacion-continuidad-terceros.md), FR-OPS-016, FR-OPS-017, FR-OPS-018, FR-OPS-019 y FR-OPS-021: Exige hitos, envío autorizado y crisis, sin SLA operativo de una cadena contratada.
- [docs/nfr/NFR-02-disponibilidad-recuperacion.md](../nfr/NFR-02-disponibilidad-recuperacion.md), C01 a C06 y Validación: Los objetivos son hipótesis y no contratos ni medidas; RPO regional asíncrono no es cero.
- [docs/compliant.md](../compliant.md), BCRA-T45 y BCRA-T46; Incidentes y plazos: RRCI y plazos contractuales/datos son circuitos separados; no se importa AAIP 72 horas universal.

**Acción concreta:** Descomponer cada reloj en hitos proveedor–entidad–responsable autorizado y pactar márgenes internos compatibles con el plazo aplicable, sin inventar minutos legales. Acordar guardia/suplencia, contenido temprano, acuses, actualizaciones, comunicaciones y evidencia ante caída de canales. Mantener SLA de servicio, NFR/BIA y notificaciones con denominadores/alcance propios y hacer un simulacro de mesa previo al servicio.

**Cierre verificable:** SLA/anexo de incidentes aprobado con contactos/cobertura y presupuesto compatible con obligaciones por sujeto. Simulacro demuestra escalamiento y borrador/envío de prueba a responsable autorizado a tiempo; no se envía comunicación regulatoria real por esta revisión.

### REV-LEG-08 — El primer producto aún no tiene condiciones y plazos legales concretos

**P0 · missing_decision · Responsable sugerido:** Legal de producto, responsable de atención y Finanzas.

CON/CST describen avisos, costo financiero, firma, revocación, bajas y reclamos con selección por régimen. No se eligió un producto contractual ni una matriz de contenido, canal, disparador, plazo, excepción y autoridad aplicada a sus recorridos. Esa parametrización pendiente no es una función ausente ni implica que deba aplicarse un único plazo a todos los productos.

**Consecuencia:** Oferta/contrato puede no coincidir con cargos, omitirse una comunicación o impedirse baja/reintegro por una regla genérica; OTP puede ofrecerse con presunciones de firma digital que no tiene.

**Evidencia:**
- [docs/functional/05-contratos-documentos.md](../functional/05-contratos-documentos.md), FR-CON-003, FR-CON-006, FR-CON-007, FR-CON-010, FR-CON-012, FR-CON-016 y FR-CON-017: Separa contenido, firma electrónica/digital, entrega, cambios y baja, pendientes de plantillas/condiciones aprobadas.
- [docs/functional/26-canales-atencion-usuarios.md](../functional/26-canales-atencion-usuarios.md), FR-CST-009, FR-CST-010, FR-CST-015 a FR-CST-023 y FR-CST-026: Contiene recorridos y excepciones, pero no perfil/plazos legales concretos para un operador/producto.
- [docs/nfr/NFR-13-accesibilidad-experiencia.md](../nfr/NFR-13-accesibilidad-experiencia.md), C01, C03, C04 y C05: Perfil de accesibilidad, contenido y evidencias permanecen pendientes.

**Acción concreta:** Preparar anexos/plantillas del producto seleccionado con tablas económicas, fuentes, advertencias y recorridos de firma/entrega/cambio/baja. Cerrar matriz de derechos/plazos por producto/canal, incluyendo reglas particulares de teléfono/mensajería y reclamos de tarjetas sólo al activarse. Revisar ejemplos completos contrato–cálculo–asiento–extracto y mensajes de rechazo/accesibilidad con responsables institucionales.

**Cierre verificable:** Plantillas y reglas aprobadas que reproducen casos permitidos, excepciones y vías de revisión del producto. Pruebas de mesa muestran costo contractual igual al calculado/debitado, plazos desde recepción y entrega fiel sin ROS/datos ajenos.

### REV-LEG-09 — El archivo legal y la equivalencia del soporte no están resueltos para la migración

**P0 · missing_decision · Responsable sugerido:** Legal/Archivo, Finanzas y responsable de datos de la entidad.

DAT/MIG prevén retención por categoría, originales locales y evidencia, pero no existe cuadro aplicado que asigne custodio, país, soporte legal, disparadores y autorización registral cuando corresponda. Los mínimos de seis años TI/SI y diez años de otros regímenes no forman un único TTL; un hash, WORM o PDF no concede por sí solo equivalencia legal al original o a un título.

**Consecuencia:** Pérdida de fuerza probatoria/disponibilidad supervisora o destrucción ilícita; en el sentido opuesto, archivo indefinido o difundido sin finalidad. El cierre de un contrato de nube puede dejar archivos obligatorios inaccesibles.

**Evidencia:**
- [docs/functional/27-auditoria-privacidad-archivo.md](../functional/27-auditoria-privacidad-archivo.md), FR-DAT-009 a FR-DAT-014, FR-DAT-024 y FR-DAT-026: Originales, retención, hold, disposición y salida están diseñados, sin autorización/contrato de custodia aplicado.
- [docs/functional/29-carga-inicial-migracion-salida.md](../functional/29-carga-inicial-migracion-salida.md), FR-MIG-015, FR-MIG-016, FR-MIG-028 y FR-MIG-030: Los modos de historia y aborto/salida conservan evidencia; la decisión sobre originales y soporte sigue siendo institucional.
- [docs/compliant.md](../compliant.md), Conservación; LAW-05, BCRA-T23 y BCRA-T34: Exige distinguir categoría/disparador, plazos concurrentes, originales EF y medios electrónicos autorizados.

**Acción concreta:** Preparar cuadro de conservación por clase, entidad y régimen, con disparadores, concurrencias, hold, custodio y destino de fin de servicio. Resolver soporte de libros/documentos/títulos y autorizaciones pertinentes antes de reemplazar o destruir originales; preservar lo no resuelto. Incluir pruebas de legibilidad, verificación temporal/firma cuando corresponda, recuperación local/supervisora y reaplicación de disposición tras restauración.

**Cierre verificable:** Cuadro aplicado y decisión documentada de soporte/residencia por clase material, con permisos/autorizaciones exigibles. Ensayo sintético de requerimiento, salida y restauración demuestra integridad, búsqueda y no borrado/reintroducción indebidos.

### REV-LEG-10 — El mantenimiento regulatorio carece de dueño y compromiso de servicio aplicados

**P1 · missing_decision · Responsable sugerido:** Responsable de cumplimiento/localización del proveedor y de la entidad.

CFG/RPT y el skill regulatorio especifican versiones, fuentes y análisis de cambios; no hay servicio aplicado que asigne quién releva, interpreta, aprueba y entrega cada cambio, con plazo por exigibilidad, presupuesto, sustitución y responsabilidad contractual. Las huellas del catálogo y los 173 vínculos no demuestran seguimiento de nuevas normas, todos los anexos o cada obligación de un producto.

**Consecuencia:** Vender actualizaciones incluidas sin dueño/capacidad puede dejar un período con reglas incorrectas o una transición fuera de plazo; el costo de cambio se discute después de asumir obligación frente al cliente.

**Evidencia:**
- [docs/functional/04-productos-configuracion.md](../functional/04-productos-configuracion.md), FR-CFG-019 y FR-CFG-030: Se puede registrar transición/costo; falta asignación contractual y operativa del servicio de localización.
- [docs/functional/25-reportes-localizacion.md](../functional/25-reportes-localizacion.md), FR-RPT-002 y FR-RPT-038: Diseños y cambios necesitan fuentes completas y responsables, no sólo una fila de inventario.
- [.agents/skills/core-bancario-argentina/references/metodologia.md](../../.agents/skills/core-bancario-argentina/references/metodologia.md), Actualización y Alcance de las afirmaciones: Ordena revalidar antes de producción y asignar seguimiento; no crea por sí mismo una operación de vigilancia.
- [docs/research/bcra_sources.json](../research/bcra_sources.json), metodo, no_cubierto y fuentes: URLs y hashes identifican snapshots, sin demostrar custodia de toda fuente ni lectura integral de anexos.

**Acción concreta:** Asignar RACI y rutina de revisión con fuentes, edición/anexo, estado de lectura e interpretación, impacto, prueba y fecha efectiva. Definir qué cambios están incluidos, quién aporta dictamen/formato/regla y cómo se presupuestan urgencias o productos nuevos. Conservar versiones recuperables de fuentes permitidas y probar una transición vigente/futura y una rectificativa histórica sin reescribir pasado.

**Cierre verificable:** Servicio de mantenimiento con dueño/suplente, fuente verificable, flujo y obligaciones comerciales explícitos. Ejercicio sobre A8492 o transición A8471/A8473 demuestra detección, aplicabilidad, versión por período, revisión institucional y evidencia de entrega; sin declarar exhaustividad futura.

## Plan de resolución por dependencia

| Orden | Trabajo | Evidencia de salida |
|---|---|---|
| 1 | Elegir cliente/producto/rol y resolver REV-LEG-01; revisar IP REV-LEG-03 al definir entrega | Expediente de perímetro y decisión de derechos compatibles |
| 2 | Preparar el paquete MSA/SOW REV-LEG-02, con datos REV-LEG-05 y cadena de terceros REV-LEG-06 | Documentos concretos revisables; negociación y formalización antes de comprometer el flujo real |
| 3 | Pactar SLA/incidentes REV-LEG-07 y anexos de usuario REV-LEG-08; resolver custodia/soporte REV-LEG-09 para migración | Matriz aplicada de obligación–responsable–plazo–contrato–prueba y ensayos de mesa con datos sintéticos |
| 4 | Cerrar estándares comprometidos REV-LEG-04 y servicio de mantenimiento REV-LEG-10 al presupuestar localización | Perfil de aseguramiento, corpus autorizado, dueño/suplente y control de cambios por exigibilidad |
| 5 | Antes de actividad real, contrastar implementación/evidencia y decisiones de la entidad | Gates del perfil con evidencia efectiva; los FR propuestos no cambian a verificados por este reporte |

No se exige que estén firmados hoy todos los contratos de una futura suite universal. Cada condición se resuelve para el compromiso, producto, dato o tercero que se vaya a activar. Las especialidades condicionadas de FX, valores, tarjetas o IA conservan sus requisitos propios; las excluidas por FR-ENT-031 no se declaran listas. Ninguna aceptación de riesgo interna elimina una obligación aplicable.

## Contraste independiente de fuentes oficiales

Se hicieron solicitudes HTTPS oficiales durante esta revisión y lectura acotada del texto recuperado. Todas las fuentes de la muestra respondieron HTTP 200. Se confirmó lo indicado abajo; no se actualizó íntegramente la base jurídica al 16/10/2026 ni se revisaron todas las hojas, anexos, contratos privados o ediciones completas de estándares. La sola respuesta HTTP 200 no demuestra aplicabilidad o vigencia integral.

| Fuente | Comprobación realizada | Límite |
|---|---|---|
| [BCRA A8398](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8398.pdf) | Identificador, fecha 05/02/2026, inclusión PSP del Registro, plazo anunciado y sustitución de sección 10; hash coincide con research | No auditoría de todo anexo ni encuadre de un servicio específico |
| [BCRA A8471](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8471.pdf) | Identificador, fecha 27/08/2026 y objeto de fraude/riesgos/gobierno; hash coincide con research | No revalidación integral del calendario por sujeto y modificatorias posteriores |
| [BCRA A8492](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8492.pdf) | Fecha 15/10/2026, vigencia 01/11/2026 y cambios de posición diaria/partida/control; hash coincide con research | No prueba de que un generador de RI implemente los cambios |
| [BCRA RRCI](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-rrci.pdf) | Sección 3.3: aviso inicial primera hora; actualizaciones; cierre posterior a contención, recuperación y resolución dentro de 5 días corridos; canal prescrito | No prueba de guardia o aviso real ni relectura de todo TI/SI |
| [Ley 27826](https://www.argentina.gob.ar/normativa/nacional/norma-431078/texto) | Identidad de la ley, texto original oficial y publicación 09/10/2026 | No se da por cerrada su reglamentación/UIF/API posterior |
| [ISO 9001](https://www.iso.org/standard/9001) y [ISO/IEC 27017](https://www.iso.org/standard/27017) | Metadatos públicos: 9001:2026 edición 6 publicada y 27017:2026 edición 2 publicada | No acceso/auditoría por cláusula de textos íntegros ni certificados |
| [AAIP transferencias](https://www.argentina.gob.ar/transferencias-internacionales) | Guía oficial mantiene adecuación del destino, excepciones y mecanismos; consistente con el enfoque condicional del proyecto | No evaluación de ningún país/contrato/flujo efectivo |

Huellas de las comunicaciones contrastadas: A8398 `7b4252e3535ea02d4519eb86d6941329f0dcf16ddb319340342b60eaaec92af5`; A8471 `c49a6502384a99f2399e130fc42a3c2a9f8c9da31382440563f83201f24838bd`; A8492 `e85ae416dc44931c4a35da3d172ac656aa21abe887f34328ea28e6268b719d40`. Coinciden con [el registro BCRA existente](../research/bcra_sources.json). Los TO/HTML son mutables; esta muestra no reemplaza conservar fuentes autorizadas ni analizar modificaciones.

No se encontraron en la muestra contradicciones que justifiquen declarar falsas esas referencias. Las actividades, obligaciones y números no muestreados permanecen como línea base documental que debe revalidar la función competente antes del uso material. No se importa un deber AAIP general de 72 horas ni un mandato universal PCI/Swift.

## Cuestiones institucionales todavía abiertas

- Sociedad que comercializará/desarrollará/operará y titularidad de derechos aportados; facultades para firmar y asumir garantías.
- Cliente de diseño, producto, licencia/rol, custodios, canales, países y fecha prevista de uso real.
- Aceptación de riesgos, recursos/guardia, autorizaciones/delegaciones y revisión profesional contable/fiscal/jurídica del producto.
- Contratos y contraparte real de nube, identidad, KYC, AML, fraude, redes y archivo; informes/certificados con su alcance efectivo.
- Política de origen y uso de datos, soporte y modelos; conservación y salida al finalizar el servicio.

Estas decisiones competen a sus responsables. La revisión puede continuarse con borradores y datos sintéticos sin atribuir licencias, firmas, presentaciones o certificaciones inexistentes.

## Documentos consultados

Se revisó íntegramente el material legal/transversal y sus referencias, y se contrastaron los apartados pertinentes de mercado, arquitectura, ADR/NFR y módulos de producto para evaluar obligaciones y contratos. El listado incluye consultas parciales por materia; no implica auditoría integral de cada actividad bancaria o de los 1.016 FR. Los documentos normativos/arquitectónicos anteriores a FR no cambiaron entre el commit fuente `ec0ef12` y la baseline revisada. La lista estructurada exacta se conserva también en el JSON.

- [.agents/skills/adr-05-configuracion-versionada/SKILL.md](../../.agents/skills/adr-05-configuracion-versionada/SKILL.md)
- [.agents/skills/adr-06-aislamiento-por-celda/SKILL.md](../../.agents/skills/adr-06-aislamiento-por-celda/SKILL.md)
- [.agents/skills/adr-07-stack-gestionado/SKILL.md](../../.agents/skills/adr-07-stack-gestionado/SKILL.md)
- [.agents/skills/core-adr-arquitectura/SKILL.md](../../.agents/skills/core-adr-arquitectura/SKILL.md)
- [.agents/skills/core-bancario-argentina/SKILL.md](../../.agents/skills/core-bancario-argentina/SKILL.md)
- [.agents/skills/core-bancario-argentina/references/controles.md](../../.agents/skills/core-bancario-argentina/references/controles.md)
- [.agents/skills/core-bancario-argentina/references/estandares-industria.md](../../.agents/skills/core-bancario-argentina/references/estandares-industria.md)
- [.agents/skills/core-bancario-argentina/references/iso.md](../../.agents/skills/core-bancario-argentina/references/iso.md)
- [.agents/skills/core-bancario-argentina/references/leyes.md](../../.agents/skills/core-bancario-argentina/references/leyes.md)
- [.agents/skills/core-bancario-argentina/references/metodologia.md](../../.agents/skills/core-bancario-argentina/references/metodologia.md)
- [.agents/skills/core-bancario-argentina/references/regulaciones-bcra.md](../../.agents/skills/core-bancario-argentina/references/regulaciones-bcra.md)
- [.agents/skills/core-nfr-calidad/SKILL.md](../../.agents/skills/core-nfr-calidad/SKILL.md)
- [.agents/skills/nfr-06-privacidad-residencia-retencion/SKILL.md](../../.agents/skills/nfr-06-privacidad-residencia-retencion/SKILL.md)
- [.agents/skills/nfr-08-interoperabilidad-portabilidad/SKILL.md](../../.agents/skills/nfr-08-interoperabilidad-portabilidad/SKILL.md)
- [.agents/skills/nfr-12-operabilidad-costos/SKILL.md](../../.agents/skills/nfr-12-operabilidad-costos/SKILL.md)
- [.agents/skills/nfr-13-accesibilidad-experiencia/SKILL.md](../../.agents/skills/nfr-13-accesibilidad-experiencia/SKILL.md)
- [LICENSE](../../LICENSE)
- [docs/README.md](../README.md)
- [docs/achitecture.md](../achitecture.md)
- [docs/adr/ADR-01-nucleo-modular.md](../adr/ADR-01-nucleo-modular.md)
- [docs/adr/ADR-02-autoridad-sql.md](../adr/ADR-02-autoridad-sql.md)
- [docs/adr/ADR-03-outbox-inbox.md](../adr/ADR-03-outbox-inbox.md)
- [docs/adr/ADR-04-alta-disponibilidad.md](../adr/ADR-04-alta-disponibilidad.md)
- [docs/adr/ADR-05-configuracion-versionada.md](../adr/ADR-05-configuracion-versionada.md)
- [docs/adr/ADR-06-aislamiento-por-celda.md](../adr/ADR-06-aislamiento-por-celda.md)
- [docs/adr/ADR-07-stack-gestionado.md](../adr/ADR-07-stack-gestionado.md)
- [docs/adr/ADR-08-carga-inicial-masiva.md](../adr/ADR-08-carga-inicial-masiva.md)
- [docs/adr/README.md](../adr/README.md)
- [docs/compliant.md](../compliant.md)
- [docs/functional/01-entidades-perimetro.md](../functional/01-entidades-perimetro.md)
- [docs/functional/02-identidad-accesos.md](../functional/02-identidad-accesos.md)
- [docs/functional/03-personas-clientes-kyc.md](../functional/03-personas-clientes-kyc.md)
- [docs/functional/04-productos-configuracion.md](../functional/04-productos-configuracion.md)
- [docs/functional/05-contratos-documentos.md](../functional/05-contratos-documentos.md)
- [docs/functional/06-cuentas-depositos.md](../functional/06-cuentas-depositos.md)
- [docs/functional/09-originacion-administracion-credito.md](../functional/09-originacion-administracion-credito.md)
- [docs/functional/12-cobranzas-mora-recupero.md](../functional/12-cobranzas-mora-recupero.md)
- [docs/functional/13-pagos-transferencias.md](../functional/13-pagos-transferencias.md)
- [docs/functional/14-cheques-echeq-cedip.md](../functional/14-cheques-echeq-cedip.md)
- [docs/functional/15-tarjetas-adquirencia.md](../functional/15-tarjetas-adquirencia.md)
- [docs/functional/18-exterior-cambios-comercio.md](../functional/18-exterior-cambios-comercio.md)
- [docs/functional/19-inversiones-custodia-fondos.md](../functional/19-inversiones-custodia-fondos.md)
- [docs/functional/20-prevencion-la-ft-fp.md](../functional/20-prevencion-la-ft-fp.md)
- [docs/functional/21-prevencion-fraude.md](../functional/21-prevencion-fraude.md)
- [docs/functional/25-reportes-localizacion.md](../functional/25-reportes-localizacion.md)
- [docs/functional/26-canales-atencion-usuarios.md](../functional/26-canales-atencion-usuarios.md)
- [docs/functional/27-auditoria-privacidad-archivo.md](../functional/27-auditoria-privacidad-archivo.md)
- [docs/functional/29-carga-inicial-migracion-salida.md](../functional/29-carga-inicial-migracion-salida.md)
- [docs/functional/30-operacion-continuidad-terceros.md](../functional/30-operacion-continuidad-terceros.md)
- [docs/functional/31-gobierno-modelos-ia.md](../functional/31-gobierno-modelos-ia.md)
- [docs/functional/32-corresponsalia-baas-plataformas.md](../functional/32-corresponsalia-baas-plataformas.md)
- [docs/functional/README.md](../functional/README.md)
- [docs/functional/catalog.json](../functional/catalog.json)
- [docs/functional/coverage.md](../functional/coverage.md)
- [docs/functional/coverage_map.json](../functional/coverage_map.json)
- [docs/functional/flows.md](../functional/flows.md)
- [docs/functional/scope.md](../functional/scope.md)
- [docs/market_analysis.md](../market_analysis.md)
- [docs/nfr/NFR-01-integridad-financiera.md](../nfr/NFR-01-integridad-financiera.md)
- [docs/nfr/NFR-02-disponibilidad-recuperacion.md](../nfr/NFR-02-disponibilidad-recuperacion.md)
- [docs/nfr/NFR-05-seguridad-accesos.md](../nfr/NFR-05-seguridad-accesos.md)
- [docs/nfr/NFR-06-privacidad-residencia-retencion.md](../nfr/NFR-06-privacidad-residencia-retencion.md)
- [docs/nfr/NFR-07-auditoria-observabilidad.md](../nfr/NFR-07-auditoria-observabilidad.md)
- [docs/nfr/NFR-08-interoperabilidad-portabilidad.md](../nfr/NFR-08-interoperabilidad-portabilidad.md)
- [docs/nfr/NFR-09-mantenibilidad-configuracion.md](../nfr/NFR-09-mantenibilidad-configuracion.md)
- [docs/nfr/NFR-10-migracion-carga-masiva.md](../nfr/NFR-10-migracion-carga-masiva.md)
- [docs/nfr/NFR-11-calidad-datos-reportes.md](../nfr/NFR-11-calidad-datos-reportes.md)
- [docs/nfr/NFR-12-operabilidad-costos.md](../nfr/NFR-12-operabilidad-costos.md)
- [docs/nfr/NFR-13-accesibilidad-experiencia.md](../nfr/NFR-13-accesibilidad-experiencia.md)
- [docs/nfr/README.md](../nfr/README.md)
- [docs/research/bcra_sources.json](../research/bcra_sources.json)
- [docs/skills.md](../skills.md)

Sólo se agregaron este reporte y sus hallazgos estructurados. No se modificaron documentos fuente, contratos, skills ni configuración productiva; no se emitió un dictamen jurídico ni se declaró eficacia de controles.
