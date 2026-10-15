# Regulaciones BCRA para el core bancario argentino

## BCRA: perímetro, productos, prudencia, pagos y reportes

Referencia operativa para revisar cambios en un core financiero argentino. Corte de las fuentes base: **15/10/2026**. Revalidar la fuente y su vigencia para cada evaluación posterior. Los requisitos se asignan a la entidad alcanzada y al proveedor según su función/contrato; el software no recibe una licencia bancaria por satisfacer esta lista.

### 1. Resolver el perímetro

Registrar entidad legal, autorización/registro, clase/grupo BCRA, productos, monedas, clientes, canales y terceros. Dibujar flujo de fondos con responsable de cada cuenta y asiento.

- **EF:** autorización conforme Ley 21.526 y [TO de autorización](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-ayccef.pdf); productos sujetos a operaciones admitidas por clase.
- **PSP:** clasificar funciones en [TO PSP, 1.1–1.4 y 2.1](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-snp-psp.pdf). No asumir que todos ofrecen cuentas ni que un registro habilita cualquier función.
- **PSPCP:** cuentas de pago en pesos; saldo individualizado, inmediato y respaldo del 100 % en cuentas a la vista locales; cuenta operativa separada; inversión solicitada expresamente y diferenciada. No son depósitos bancarios ni tienen su garantía: TO PSP, 4.1–4.2.
- **PSPCP como Servicio:** revisar alta/habilitación del tercero, identificación del PSPCP en interfaz, contratos y controles del tercero; responsabilidad permanece en PSPCP: TO PSP, 2.2.2.11.i y 4.5.
- **PNFC:** [TO PNFC, 1.1–1.3](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-apnf.pdf), crédito no bancario y registro según alcance; sin licencia para captar depósitos.
- **PSCPP:** [TO PSCPP, 1.1–1.4](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-pscpp.pdf), préstamos entre particulares en pesos, prohibición de asumir/garantizar riesgo y separación patrimonial; individualizar inversor/tomador/operación.
- **Proveedor técnico:** distinguir software de provisión de cuentas, administración de esquema o ejecución de una función regulada. Registrar responsabilidades contractuales y controles exigidos al prestador.

### 2. Inventariar normas según las capacidades modificadas

Comenzar por el [índice oficial de TO/RI](https://www.bcra.gob.ar/ordenamiento-y-resumenes/); abrir cada documento y sus hojas, no usar sólo el resumen semestral. Revisar comunicaciones posteriores y anotar fecha de publicación y entrada en vigor por separado.

| Capacidad | Textos primarios |
|---|---|
| Cuentas y depósitos | [Ahorro/sueldo/especiales](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-depaho.pdf), [cuenta corriente](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-ctacte.pdf), [plazo/UVA/UVI](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-depinv.pdf) |
| Crédito y usuario | [Tasas y CFT](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-tasint.pdf), [PUSF](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-pusf.pdf), [política de crédito](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-polcre.pdf), [clasificación](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-cladeu.pdf), [previsiones](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-prevmi.pdf) |
| Prudencia | [Seguro de depósitos](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-seggar.pdf), [encajes](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-efemin.pdf), [capital](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-capmin.pdf), [grandes exposiciones/vinculados](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-gerc.pdf), [LCR](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-ratio.pdf), [NSFR](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-ratiofn.pdf), [apalancamiento](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-raapal.pdf) |
| Identificadores y pagos | [Servicios de pago](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-snp-spd.pdf), [transferencias](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-SNP-tr.pdf), [normas complementarias](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-snp-tr-nc.pdf), [DEBIN](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-snp-debin.pdf), [débitos directos](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-snp-dd.pdf), [cheques/ECHEQ/CEDIP](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-snp-cheq.pdf) |
| Cambios y tesorería | [Exterior y cambios](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-excbio.pdf), [MEP](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-snp-mep.pdf), [CRyL](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-cryl.pdf), [derivados/FCI](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-opefci.pdf); CNV si presta actividades de valores |
| Contabilidad y RI | [RI-DCPC](https://www.bcra.gob.ar/archivos/Pdfs/Texord/RI-DCPC.pdf), [plan de cuentas](https://www.bcra.gob.ar/archivos/Pdfs/Texord/plandecuentas.pdf), [estados NIIF](https://www.bcra.gob.ar/archivos/Pdfs/Texord/RI-NIIF.pdf), [presentación](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-optico.pdf), [instrucciones generales de envío/validación](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-so-s01.pdf) |

Añadir familias institucionales de gobierno/riesgo/auditoría, controles internos, supervisión consolidada, conservación, secreto financiero, LA/FT/FP y tecnología; y familias de producto como garantías, graduación/evaluación crediticia, MiPyME, corresponsalía, moneda extranjera, ANSES, cuentas especiales y sector público cuando correspondan.

### 3. Convertir obligaciones en controles y evidencia

Para cada cambio producir fila: `ID | norma y apartado | vigencia | sujeto/condición | obligación | control core/integración/entidad | dueño | evidencia | prueba | estado/brecha`.

Comprobaciones mínimas según alcance:

1. **Productos:** distinguir cuenta de pago y depósito; impedir sobregiro en caja de ahorro; gratuidades por producto; titulares/poderes/menores; límites/monedas; cierre y estados de cuenta.
2. **Cálculo:** precisión decimal, base y redondeo explícitos, TNA/TEA/CFT coherentes, UVA-CER separada de UVI-ICC, cronogramas, mora, precancelación y renovación. Reconciliar contrato, simulación, asiento y liquidación.
3. **Usuario:** versión aceptada y entregada, avisos, tarifas, revocación/rescisión y devoluciones; registro de reclamos con responsable, plazos y respuesta trazable. PUSF 1.1.2 determina los sujetos, incluidos PSPCP/PSI con billetera.
4. **Prudencia:** saldos diarios y promedios; atributos para capital/encaje; garantías/vinculaciones/grupos; provisión regulatoria separada de deterioro NIIF; alcance individual/consolidado.
5. **Pagos:** identificar esquema/rol/instrumento; CBU/CVU/alias y titular; consentimiento vigente y revocable; comprobante e identificador único; efecto monetario único ante reintentos; conciliación; homologación del operador.
6. **Contabilidad:** partida doble y cuadre auxiliar-mayor-RI; NIIF adoptadas por BCRA y sus excepciones/transiciones. Registros y cierres históricos reproducibles.
7. **Reportes:** matriz por sujeto/registro, campo y fuente; calendario y unidades; “opera/no opera”; archivo/descriptor; validación completa y corrección. Ticket de carga o recepción no demuestra cumplimiento.

Probar bordes de fecha, feriado, ausencia de índice, cuenta bloqueada, duplicado, timeout, pago por otro canal, reversión y reproceso histórico según el cambio. Usar datos sintéticos y conciliaciones independientes. No inventar un plazo universal de conservación o respuesta para todos los eventos.

### 4. Evitar errores de vigencia conocidos al corte

- Seguro: [A8407 incorporada en TO, 5.3 y 6](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-seggar.pdf) fija $50.000.000 desde 01/04/2026; agregado por persona, prorrateo de cotitulares y exclusiones. Revalidar antes de usarlo en otro período; parametrizarlo.
- [LCR](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-ratio.pdf) y [NSFR](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-ratiofn.pdf), 1.1, A8445 desde 05/06/2026: D-SIB y sucursales/subsidiarias G-SIB; Grupo A restante con RI correspondiente. No exigir automáticamente los mismos ratios a toda EF.
- [CEDIP, 3.6.5](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-snp-cheq.pdf): emisión optativa, gestión obligatoria para emisor CEDIP/gestor ECHEQ y cobro obligatorio para toda EF. Verificar activación normativa/operativa de fraccionamiento y transmisión para negociación: 3.6.7.4 las exceptúa de la vigencia general.
- [A8492 del 15/10/2026](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8492.pdf): posición diaria de efectivo mínimo y validación; **entra en vigor 01/11/2026**. Preparar versión futura, conservar la anterior para períodos anteriores.
- [RI-DCPC sección 6](https://www.bcra.gob.ar/archivos/Pdfs/Texord/RI-DCPC.pdf): NIIF 18 figura con vigencia 01/01/2027. La aparición en un listado no convierte su entrada futura en obligación activa.

Cerrar la evaluación con cumplimiento demostrado, brechas y pendientes explícitos. Una recomendación CIMPRA, estándar de marca y ley no tienen la misma fuerza; registrar su naturaleza. No declarar “core certificado por BCRA”, “cumplimiento total” ni exhaustividad sin evidencia y alcance cerrado. La decisión institucional y profesional se informa con evidencia concreta; no se sustituye por una validación automatizada del repositorio.

---

## BCRA: tecnología, seguridad, terceros e IA

**Consulta base: 15/10/2026.** Este catálogo ayuda a ejecutar la revisión; no certifica que una entidad, un proveedor o un core cumpla. Antes de cada revisión descargar TO vigente, revisar su última comunicación y buscar comunicaciones posteriores aún no consolidadas.

### Fuentes primarias y selección

- [TI/SI, t-rmgcti.pdf](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-rmgcti.pdf): TO 13/02/26, última A 8401. Base A 7724/A 7777; A 7783 complementa y amplía IMF; A 8398 reemplaza sección 10 e incorpora PSP del Registro; sección 12 fija PSP desde **04/08/26**. Sujetos1.1: EF, IMF INTERBANKING/COELSA/LINK/NEWPAY y PSP del Registro.
- [Servicios financieros digitales, t-rmrtsd.pdf](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-rmrtsd.pdf): TO 02/06/23, A 7783, vigente 29/11/23. EF/PSP con servicios digitales. **A 7784 es depósitos; no usar como norma digital.**
- [RRCI, t-rrci.pdf](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-rrci.pdf): TO17/07/25, A 8280 sobre baseA7266. Sección2 buena práctica con adopción fundada; sección 3 notificación obligatoria. EF/PSP Registro/IMF sistémicas.
- [Expansión EF](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-expaef.pdf): TO13/02/26, A 8401, sección 2 tercerización y originales en Argentina.
- [Riesgos EF](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-lingeef.pdf): TO31/07/26, A 8463; secciones 6 y12, A 8249 (vigente 01/09/25), complementadas por [A 8471](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8471.pdf) y [A 8473](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8473.pdf).
- [Guías oficiales de supervisión](https://www.bcra.gob.ar/guias-de-supervision-bcra/): IA junio2026 y guías TI/continuidad/DLP/ciberresiliencia/identidad. Clasificar como guías y contrastar contra obligaciones del TO; no llamarlas leyes.
- [Régimen disciplinario BCRA](https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-rdbcra.pdf): TO 27/03/26, A 8415 sobre A 8411; 2.2.1.2 sujetos Grupo A, 11.15 infracciones TI/SI/SFD. Conservar evidencia de controles, decisiones y remediaciones; no estimar multa sin revisar caso y procedimiento.

### Procedimiento de verificación

1. Identificar persona regulada y función: EF, PSPCP, otra funciónPSP, IMF, proveedor tecnológico. Ser PSP no impone automáticamente todo requisito prudencial de un banco. El proveedor soporta requisitos técnicos/contractuales del cliente y no hereda por defecto su licencia.
2. Registrar estado temporal: publicación, divulgación, vigencia, implementación transitoria y fecha/disparador del caso. Nunca mezclar «emitida» con «ya exigible».
3. Para cada control registrar fuente/sección, aplicabilidad/fundamento, obligación o recomendación, propietario, diseño, evidencia, prueba, brecha y fecha. Aplicabilidad: aplica, condicional, no aplica con fundamento o por determinar. Implementación: sin evaluar, brecha, parcial, implementado sin evidencia, verificado o excepción documentada. No marcar conforme sin evidencia.
4. Probar controles sobre arquitectura, código/configuración, contratos y operación. La matriz de documentos no basta para demostrar efectividad.

### Controles imprescindibles

| Bloque | Verificar | Evidencia exigida por la revisión |
|---|---|---|
| Gobierno/riesgo | TI/SI 2 y3: Directorio, comité, responsables, segregación, riesgos residuales, evaluación previa de producto/tercero y funciones locales. | RACI, organigrama, actas, riesgos aprobados y pruebas de incompatibilidades. |
| Datos/activos | TI/SI 4.4–4.5: dueño, clasificación, calidad, linaje, inventario, retención/borrado y dependencias. | Catálogo y reconciliación de inventario, pruebas de calidad y eliminación; resolver conservación legal antes de borrar. |
| Identidad/accesos | TI/SI 5.7: identidad única, mínimo privilegio, bajas, recertificación, protección de factores y accesos de terceros. | Pruebas negativas de permisos, bajas, bloqueo/revocación, privilegios temporales y trazabilidad. |
| Operación/seguridad | TI/SI 5.8 y7: monitoreo, vulnerabilidades, cambios autorizados, procesamiento/reinicio, comunicaciones y respaldos. | Configuración efectiva, hallazgos/remediación, cambio/rollback y restauración. Al menos dos copias de datos clientes/contable-financieros/transaccionales, controles anti corrupción y offline según clasificación. |
| Continuidad | TI/SI 6 y Riesgos EF 12: BIA, RTO/RPO por servicio, amenazas conjuntas, dependencias, sitio/proveedor y ejercicios anuales con escenario máximo crítico. | Resultados medidos, participantes, conciliación de operaciones y planes correctivos. No inventar RTO/RPO universal. |
| Ledger/auditoría | TI/SI 9.1: integridad, límites a edición/borrado de operaciones/saldos, consistencia operativa-contable, cliente único y auditoría completa. | Concurrencia, duplicados, redondeo, reversión y cierre; evento/fecha/usuario/canal/antes-después parámetro. Soporte contable y auditoría mínimo 6 años recuperable, inmediato para SEFYC; respetar plazos mayores concurrentes. |
| Reportes/SDLC | TI/SI 9.1.1–9.2: RI automatizados y ajustes controlados; requisitos, amenazas, dependencias, integridad versiones y QA independiente. | Reconciliación/linaje de RI, pruebas y aprobaciones; vulnerabilidades por tercero independiente en apps con datos clientes/transaccionales/financieros. |
| Terceros/nube | TI/SI 10 vigenteA8398/A 8401: evaluación aprobada, catálogo cadena/regiones/controles; aviso crítico ≥ 60 días; contrato, auditoríaSEFYC toda cadena, incidentes, SLA, continuidad, fuentes/datos/documentación y salida. | Contratos/subcontratos y evidencia de aviso, prueba de salida y revisión de coberturaSOC/ISO. Cambios naturaleza/ubicación/subcontratista requieren nuevo proceso10.1. Informes externos son complementarios. |
| Exterior/documentación | TI/SI 10.1/10.6 y Expansión EF 2.1–2.3. | Para EF, Expansión2.1 exige aviso ≥ 60 días de actividades tercerizadas sin atención clientes/público: no presumir exención para servicios no críticos por leer solo TI/SI 10.1. Países/supervisión intragrupo certificada cuando aplica; mantener Argentina originales/documentos2.2.6. Validar régimen digital; ni nube exclusivamente local ni traslado irrestricto se presumen. |
| IA | TI/SI 4.6,3,9.2; guíaIA junio26 complementaria. | Propósito, inventario/versiones/datos/modelos, roles, umbrales, validación, privacidad, sesgos, explicabilidad, monitoreo, comunicación cliente y salida/continuidad. La guía no impone por sí misma certificaciónISO 42001. |
| Canales digitales | SFD 1.2/3/4: aviso nuevo producto/servicio ≥ 60 días, autenticación, confirmación de acciones críticas, sesión/dispositivo, identidad digital, fraude. | Pruebas de cambio contacto/beneficiario/crédito/factor, suplantación y replay; MFA o identificación digital para acciones críticas según3.1.1. Validar reglas del autenticador: secreto ≥ 8 caracteres y composición; OTP≥ 6 dígitos/≤ 120 s; PIN tarjeta ≥ 4 dígitos, no iguales/consecutivos y validación online. |
| Incidentes | RRCI 3: clasificación críticos/importantes incluida cadena de terceros; inicial primera hora de ocurrido/detectado, actualizaciones frecuentes, cierre ≤ 5 días corridos tras resolución. | Simulacro de expediente3.6 y envío autorizado a audext.incidente@bcra.gob.ar; IDúnico, datos disponibles, impacto, causa raíz, medidas. No enviar comunicaciones reales sin autorización de la tarea. |

### Calendario antifraude publicado antes del corte

- A 8471 EF puntos 1–4: **01/12/26**; programa antifraude, función, base central denuncias, vinculación riesgo/PUSF, CPF y reporte trimestral al Directorio.
- A 8471 PSPCP: etapa1 **01/09–31/12/26**, etapa2 **01/01–31/05/27**, etapa3 **01/06–31/08/27**, plena **01/09/27**. Dos informes de etapa y final máxima autoridad+auditor externo. A15/10/26 revisar etapa1; no anticipar plena exigibilidad.
- A 8471 demásPSP: función/autoevaluación/mitigación/TI desde **01/01/27**.
- A 8473 administradores transferencias: **120 días desde publicación**; EF/PSPCP **60 días desde recepción de documentación técnica** para altas/aperturas/revisión padrón y **90 días** para monitoreo ordenante/receptor. Documentar disparador. Score no decide solo: conservar contexto, versión, uso y acceso; integrar a mecanismos propios, con fines y seguridad de norma. Auditoría internaEF/equivalentePSPCP mínimo anual; revisión independiente del modelo administrador mínimo semestral.

### Criterios para impedir conclusiones falsas

- No declarar «core certificado BCRA» por una ISO, un SOC o cumplir una lista.
- No presentar ledger inmutable, HSM, microservicios, nube local, un cifrado concreto o un RTO específico como mandato universal sin disposición que lo funde. Identificarlos como decisión de diseño cuando corresponda.
- No usar A 6354 histórica como reemplazo de sección 10 actual ni A 7784 como seguridad digital.
- No asumir todas las seccionesRRCI obligatorias: diferenciar prácticassección 2, fundamentación de adopción y notificaciónsección 3.
- No reemplazar retenciones concurrentes por el mínimo 6 años de TI/SI 9.1.
- No prometer exhaustividad normativa futura: anexar fuentes, fechas y pendientes y revisar normas posteriores antes del despliegue.
