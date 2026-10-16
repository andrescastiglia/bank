# Revisión contable e impositiva del core y de su proveedor

**Fecha de revisión:** 16/10/2026. **Baseline:** `2e5d579103b94ab70c16d81debe73bf5840ba0c8`. **Fuentes regulatorias/documentales:** corte 15/10/2026, sin actualización jurídica nueva. **Estado:** revisión documental; no hay software financiero, cierres, facturas, declaraciones o pagos del caso acreditados por esta revisión.

La base define adecuadamente integridad financiera y trazabilidad. Sus principales pendientes son concretar políticas/oráculos del perfil inicial y construir el proceso contable y fiscal de la empresa que vende el software. Esto último puede resolverse mediante administración/ERP e integraciones externas: no exige ampliar el core bancario a ERP ni mezclar sus fondos con los del fabricante.

## Alcance, método y fortalezas

La lente A revisa el producto financiero: ACC, LED, CRE, INT, COL, REC, RSK, TAX y RPT, con contratos, arquitectura y NFR relacionados. La lente B revisa el negocio proveedor: suscripciones, implementación, facturación, cobros, costos, impuestos, moneda y caja. Se leyeron los documentos de materia y se inventariaron relaciones de los 32 módulos; el inventario de relaciones no equivale a una auditoría de cada FR. El [JSON de hallazgos](findings/accounting.json) contiene evidencia por sección/ID y lista exacta de archivos revisados.

Se aplicó el skill [alkimos-contador:alkimos-revisar-fiscal](skill://plugins_6abdac1c58908191885b74ca310370aa/alkimos-revisar-fiscal/SKILL.md), con sus recursos de privacidad/fuentes. Sólo se usaron documentos de diseño y cifras hipotéticas: no se incorporaron credenciales, CUIT reales, declaraciones o notas sensibles. Identidad, inscripción, jurisdicciones y documentación fiscal privada del proveedor no están acreditadas. Los roles de asistencia no sustituyen matrícula, dictamen ni decisiones de la entidad.

Fortalezas que conviene conservar:

- [LED](../functional/08-ledger-contabilidad-cierres.md), FR-LED-004/005/008/014, exige partida doble, transacción completa, efecto único y correcciones vinculadas. Una respuesta perdida no autoriza duplicar asiento.
- [INT](../functional/10-intereses-comisiones.md), FR-INT-012/014/019, distingue devengamiento económico, revisión de cálculo y medición contable; `rule_version` no crea otro devengo base.
- [RSK](../functional/23-riesgos-prudencia-exposiciones.md), FR-RSK-014/015/016, y LED-023 separan previsión prudencial de pérdida esperada contable y preservan transiciones BCRA. Respaldo PSPCP y encaje EF se diferencian en [ACC](../functional/06-cuentas-depositos.md).
- [TAX](../functional/24-tributos-recaudaciones.md), FR-TAX-002/014/015/017/018, versiona fecha/beneficio/padrón, distingue SIRCREB/SIRCUPA y separa devolución financiera de trámite fiscal; pago/intención tampoco se confunden.
- [REC](../functional/22-conciliacion-excepciones.md) y [RPT](../functional/25-reportes-localizacion.md) exigen corte completo, linaje y conciliación por titular/moneda; ticket de subida no equivale a validación/aceptación.
- El [mercado](../market_analysis.md), §§7–8, declara supuestos y exclusiones. Recalculé con `Decimal` contratos esperados, ARR e implementación de los tres escenarios, los tres subtotales/reservas TCO y el equilibrio de 13 clientes ilustrativos: coinciden con los importes publicados y redondeos indicados. Es consistencia aritmética, no validación comercial/fiscal ni medición del costo real.

## Diagnóstico por lente y estados

La lente A presenta controles especificados y pendientes institucionales reconocidos. La ausencia de ejecución se trata una sola vez en REV-ACC-04; no se presenta cada control propuesto como faltante. REV-ACC-01/03 concretan decisiones de Finanzas; REV-ACC-02 delimita el producto no bancario.

La lente B todavía es una hipótesis empresarial. El relevamiento [compliant](../compliant.md), «Fuera de una configuración genérica», deja correctamente fuera facturación del proveedor, IIBB propio y exterior hasta definir el sujeto. REV-ACC-05 a REV-ACC-11 desarrollan el trabajo que esa delimitación hace necesario. No hay conclusión de incumplimiento, deuda, inscripción debida ni exportación acreditada.

| Componente del trabajo fiscal | Situación comprobada |
|---|---|
| Sujeto/jurisdicción/período | Operador financiero por elegir y proveedor sin perfil fiscal aportado; revisión del diseño al 16/10/2026 |
| Tributos del producto | Inventariados por régimen y condicionalidad; alícuotas/beneficios reales del primer cliente pendientes |
| Tributos propios del proveedor | IVA, IIBB/ámbito territorial, retenciones sufridas/designaciones y demás obligaciones a determinar por actividad/sujeto; no se asignan regímenes universales |
| Parámetro/fuente/publicación/vigencia | La base conserva fuentes al 15/10/2026; no se verificó una actualización oficial posterior ni se agregaron tasas/plazos |
| Obligación/determinación/declaración/pago/imputación/saldo/estado oficial | No aportados para una empresa real; no evaluados, sin afirmar «al día» |
| Notificaciones y vencimientos del caso | No aportados; no se computa plazo fiscal individual ni se infiere inexistencia de avisos |

P0 significa resolver antes del hito indicado, no un incidente real ni un bloqueo a análisis, ensayos sintéticos o desarrollo independiente. Los entregables sugeridos son propuestas: esta revisión crea únicamente este reporte y su JSON.

## Hallazgos y acciones

### REV-ACC-01 — Concretar el paquete contable y los oráculos del primer perfil

**P0 · decisión pendiente · Hito:** Antes de aceptar el diseño financiero del piloto elegido o comprometer una migración de saldos.

**Observación:** LED/INT/NFR ya exigen plan, mapeos, vectores y aprobación; arquitectura §19 los declara pendientes. El repositorio no aporta todavía un catálogo contable del perfil ni valores esperados independientes. Es una decisión/entregable reconocido como pendiente, no ausencia de partida doble o de control propuesto.

**Evidencia:** [§19 — Autoridad y modelo contable](../achitecture.md): Se solicita catálogo de asientos, reservas, cuentas puente, límites y definiciones de saldo.; [FR-LED-001, FR-LED-002, FR-LED-006](../functional/08-ledger-contabilidad-cierres.md): Plan y mapeos versionados; vector aprobado requerido para exactitud.; [NFR-01-C04; Validación y evidencia](../nfr/NFR-01-integridad-financiera.md): Cero diferencia contra vector histórico aprobado y muestras sintéticas..

**Impacto:** Un ledger puede balancear y aun así imputar principal, interés, IVA, tránsito o cobranza al concepto equivocado; sin oráculo profesional la prueba puede repetir el mismo error del código.

**Acciones:**

- Elegir entidad/perfil y confeccionar matriz evento económico → contrato/concepto → débito/crédito/dimensiones → saldo → impuesto → reporte.
- Crear casos sintéticos con resultados calculados independientemente, fuente/política, responsable y aprobación; incluir pago parcial, mora, precancelación, reverso, refinanciación, migración y cierre.

**Cierre verificable:** El paquete del perfil cubre cada evento monetario habilitado, identifica cuentas/categorías y demuestra ecuación de saldos por titular y moneda. Cada vector tiene insumos, fórmula, calendario, redondeo, asientos y salida esperada, con revisor distinto del implementador; su aprobación no se presenta como prueba ejecutada.

**Dueño sugerido:** Finanzas/Contabilidad de la entidad de diseño y líder de dominio financiero. **Dependencias:** Perfil comercial inicial; Políticas fiscales/contables aplicables; Catálogo de productos y formatos del cliente.

### REV-ACC-02 — Definir medición y presentación para el prestamista no bancario

**P1 · brecha de especificación/alcance · Hito:** Antes de prometer que la ruta inicial PNFC entrega contabilidad financiera completa o estados de ese sujeto.

**Observación:** La ruta PNFC/CREDITO dispone de auxiliares y movimientos; los FR de adopción contable, valuación, inflación y publicación completos están acotados principalmente a EF/BANCA. Falta explicitar la interfaz y el paquete de política/presentación para un operador no EF, o limitar contractualmente el producto a submayor y exportación a su contabilidad externa.

**Evidencia:** [Propósito; FR-LED-022, FR-LED-025, FR-LED-026](../functional/08-ledger-contabilidad-cierres.md): PNFC/CREDITO aparece en alcance; medición NIIF BCRA, FX e inflación se especifican para EF.; [FR-RPT-017](../functional/25-reportes-localizacion.md): Estados/notas de publicación están definidos para EF bajo NIIF adoptadas por BCRA.; [§1 y §6.2](../market_analysis.md): Prestamistas y cartera acotada son una ruta de entrada comercial..

**Impacto:** Un comprador PNFC podría interpretar un submayor reconciliado como una solución de estados financieros, y recibir reglas bancarias que no corresponden a su marco.

**Acciones:**

- Precisar qué libro/auxiliar entrega el core y qué libro/ERP mantiene la contabilidad legal del PNFC.
- Registrar marco, política de reconocimiento/medición/presentación y mapeo externo efectivos del sujeto; no presumir NIIF BCRA ni un marco profesional particular.

**Cierre verificable:** La ficha PNFC distingue operación, contabilidad financiera, reporting y responsables; cada salida prometida tiene mapeo y caso de conciliación. Un caso PNFC y uno EF del mismo producto seleccionan sus políticas propias sin herencia automática; los servicios excluidos quedan expresos en oferta.

**Dueño sugerido:** Producto y Contador del cliente PNFC, con Finanzas del proveedor. **Dependencias:** Sujeto y marco contable concreto; Alcance de servicing frente a contabilidad completa; Integración ERP del cliente.

### REV-ACC-03 — Resolver la diferencia entre costo contractual y rendimiento contable

**P1 · decisión pendiente · Hito:** Antes de aceptar cálculos contables de un producto con comisiones iniciales, costos de originación, modificación o medición por costo amortizado cuando aplique.

**Observación:** INT define TNA/TEA/CFT, cargos y separación de obligación contractual/medición; LED remite a política aprobada. No está seleccionado el tratamiento de comisión/costo inicial, rendimiento contable, diferimiento y modificación para un producto real. El CFT del cliente y el ingreso devengado del acreedor no deben equipararse por compartir flujos.

**Evidencia:** [FR-INT-009, FR-INT-019, FR-INT-020](../functional/10-intereses-comisiones.md): CFT y capitalización/suspensión se condicionan a regla; refinanciación no decide baja contable.; [FR-LED-022, FR-LED-024](../functional/08-ledger-contabilidad-cierres.md): Política de reconocimiento/medición y evaluación de modificación/baja permanecen institucionales.; [BCRA-F18; Precisiones contables](../compliant.md): Adopción BCRA con excepciones y transiciones, sin NIIF puras universales..

**Impacto:** Reconocer una comisión cobrada como ingreso íntegro puede distorsionar resultado, valor del activo y conciliación de cuotas si la política efectiva requiere otro tratamiento.

**Acciones:**

- Completar ficha por concepto: obligación contractual, base de cálculo al cliente, reconocimiento contable, eventual diferimiento/amortización e incidencia tributaria.
- Cuando el marco efectivo lo exija, especificar motor o integración para interés efectivo/costo amortizado y revisión de modificaciones; conservar puentes a los flujos contractuales.

**Cierre verificable:** Un caso con cargo inicial y otro refinanciado muestran flujos, CFT, cobros, ingreso/medición y asientos diferenciados con política aprobada. La reproducción posterior conserva saldos diferidos/medición y reglas originales; no se declara universal una metodología no determinada para el sujeto.

**Dueño sugerido:** Finanzas/Contabilidad y Producto, con Fiscal y Riesgos. **Dependencias:** Marco y producto efectivos; Paquete contable inicial; Política de modificación/baja de activos.

### REV-ACC-04 — Obtener evidencia integral de cierre y del puente contable-prudencial

**P1 · evidencia pendiente · Hito:** Antes de declarar aceptado un cierre piloto, una cifra prudencial o un reporte de producción.

**Observación:** La especificación sí separa ECL/previsión regulatoria, fuentes completas, ajustes y aceptación del receptor. No hay corrida implementada acreditada ni paquete observado que atraviese contrato, devengo, cobro, clasificación, mayor, prudencia y reporte. Es falta de evidencia operativa del diseño propuesto, no un control omitido.

**Evidencia:** [FR-RSK-014, FR-RSK-015, FR-RSK-016, FR-RSK-034](../functional/23-riesgos-prudencia-exposiciones.md): Previsión y ECL separados y dataset desde corte completo.; [FR-LED-017, FR-LED-019, FR-LED-023](../functional/08-ledger-contabilidad-cierres.md): Cierre, conciliación y bases contable/prudencial diferenciadas están propuestos.; [Estado; NFR-11-C01, NFR-11-C02, NFR-11-C04](../nfr/NFR-11-calidad-datos-reportes.md): Metas no medidas: completitud, diferencias y aceptación..

**Impacto:** Un cuadre técnico no prueba cifra prudencial correcta, población completa ni presentación aceptada; una diferencia puede reaparecer después de refinanciar, castigar o rectificar.

**Acciones:**

- Preparar guion integrado y, al existir prototipo/entorno, ejecutar cierre con saldos iniciales, cartera, intereses, impuestos, mora, provisiones, recupero y reporte del perfil.
- Conservar puente por posición entre valor contractual, medición contable, previsión regulatoria y base prudencial, con fuentes/exclusiones explicadas y revisión independiente.

**Cierre verificable:** Paquete esperado/observado versionado concilia por entidad, titular, moneda y concepto; fuente faltante deja cierre pendiente. Se demuestra rectificación/reapertura sin reemplazo silencioso y estados recibido/validado/aceptado separados; mientras no se ejecute permanece no evaluado.

**Dueño sugerido:** Finanzas y QA financiero, con Riesgos, Fiscal y responsable de RPT. **Dependencias:** Prototipo y entorno de prueba; Oráculos aprobados; Perímetro y diseños regulatorios efectivos.

### REV-ACC-05 — Determinar el perfil fiscal propio de la empresa proveedora

**P0 · decisión pendiente · Hito:** Antes de emitir la primera factura, presentar una oferta tributariamente cerrada o contratar servicios exteriores con impacto fiscal.

**Observación:** La documentación fiscal se concentra en operadores financieros y expresamente deja fuera de la configuración genérica la facturación del proveedor, IIBB propio y exterior. No se aportan sujeto, inscripción, actividad, domicilios/jurisdicciones, forma jurídica ni documentación fiscal del proveedor; no se puede concluir su tratamiento ni que esté al día.

**Evidencia:** [Impuestos; Fuera de una configuración genérica](../compliant.md): Facturación operador/proveedor, Sellos, IIBB propio y beneficiarios del exterior requieren delimitación.; [FR-TAX-030; Dependencias y validación pendiente](../functional/24-tributos-recaudaciones.md): Regímenes locales/especiales se remiten a regla/dictamen efectivos; designaciones/jurisdicciones siguen pendientes.; [Perfiles y activación — PROVEEDOR](../functional/scope.md): Perfil tecnológico y contractual no identifica una situación fiscal concreta..

**Impacto:** Precio neto, comprobante, percepción/retención, costo de compras y obligación provincial pueden presupuestarse de manera incorrecta si se confunde tributo del core con tributo de su fabricante.

**Acciones:**

- Abrir legajo fiscal empresarial mínimo con sujeto, actividad, forma jurídica, jurisdicciones y evidencia fechada; completar matriz nacional/provincial/municipal sin presumir inscripciones.
- Separar rol de agente de retención del cliente financiero, impuestos propios del proveedor y retenciones sufridas; validar normas vigentes sólo una vez determinado el sujeto/período.
- Si hay cliente/proveedor exterior, documentar residencia, prestación, utilización, moneda y nexo para evaluar exportación/importación de servicios y requisitos aplicables; no presumir exportación por facturar en USD.

**Cierre verificable:** Contador/Legal registran aplicable, condicional o no aplicable fundado por tributo/régimen y jurisdicción, con fuente efectiva y documentos pendientes. Obligación, determinación, declaración, pago, imputación y estado oficial quedan separados; los no acreditados figuran pendientes, sin afirmar cumplimiento.

**Dueño sugerido:** Contador del proveedor y representante/administración de la sociedad, con Legal para exterior. **Dependencias:** Identidad y actividad del proveedor; Localización real de operaciones/clientes/servicios; Documentos fiscales autorizados.

### REV-ACC-06 — Especificar medición de consumo y facturación B2B del proveedor

**P1 · brecha de especificación/alcance · Hito:** Antes de vender una suscripción por cuenta, contrato o consumo y liquidar su primer período.

**Observación:** Mercado pide definir unidades cobrables, mínimos/bandas y simulador de factura; OPS mide costo por unidad técnica. El catálogo no desarrolla un ciclo propio del proveedor que concilie contrato comercial, consumo cobrable, cierre de factura y comprobante fiscal. TAX-030 menciona facturación en forma condicional, sin ese contrato operativo.

**Evidencia:** [§8.1; §12.1](../market_analysis.md): Se distinguen cuentas/contratos y reintentos/rechazos; se recomienda simulador de factura y consumo trazable.; [FR-OPS-027](../functional/30-operacion-continuidad-terceros.md): Calcula costo técnico y de servicio; no define qué consumo se factura al comprador.; [FR-TAX-030](../functional/24-tributos-recaudaciones.md): Facturación aplicable remite a definición por régimen..

**Impacto:** Duplicados técnicos, cuentas inactivas o cambio de tarifa pueden incrementar la factura sin base contractual o impedir reproducir un ingreso.

**Acciones:**

- Especificar workflow B2B o integración con sistema de facturación/ERP: contrato/tarifa, identidad del evento cobrable, bandas/mínimos, moneda/indexación, corte, validación, factura y nota correctiva.
- Definir tratamiento de retries, rechazos, consultas, reversos, sandbox, promociones y créditos de servicio; no reutilizar automáticamente el ledger de clientes para la caja propia del proveedor.

**Cierre verificable:** Un lote sintético con reintentos, cuenta cerrada, cambio de banda y corrección tardía genera unidades e importe reproducibles desde contrato y fuentes. Simulador, factura propuesta y consumo conciliado coinciden; emisión fiscal se efectúa sólo por interfaz/proceso efectivo y sujeto habilitado.

**Dueño sugerido:** Finanzas/Administración comercial del proveedor y Producto. **Dependencias:** Contrato/tarifario comercial; Perfil fiscal empresarial; Fuente independiente de consumo cobrable.

### REV-ACC-07 — Separar ingreso devengado, facturación y cobro de contratos de software

**P1 · decisión pendiente · Hito:** Antes de aprobar presupuesto o estados del proveedor con diagnósticos, pilotos, implementación y suscripción.

**Observación:** Mercado separa ARR/ACV de implementación y advierte que no equivalen a ingreso/caja. No hay política empresarial de reconocimiento para anticipos, hitos, aceptación del cliente, soporte, variable por consumo, descuentos o créditos SLA. La expresión ingreso de implementación del modelo no resuelve cuándo se devenga contablemente.

**Evidencia:** [§7.1, §7.2 y §12.1](../market_analysis.md): ARR de salida, cobro único e hitos de implementación se distinguen; su calendarización se deja pendiente.; [Propósito; FR-CON-003, FR-CON-018](../functional/05-contratos-documentos.md): CON conserva contrato financiero y versión económica, no política de ingresos del contrato de venta de software..

**Impacto:** Un anticipo o ARR de salida tratado como ingreso inmediato sobreestima rentabilidad y oculta obligaciones de implementación/soporte pendientes.

**Acciones:**

- Crear matriz de contratos del proveedor que separe cobros/anticipos, facturas, prestaciones/hitos, aceptación, devengo e ingresos diferidos cuando corresponda al marco efectivo.
- Asignar precio/criterio de medición a diagnóstico, piloto, implementación, licencia/suscripción, mantenimiento y consumo; resolver principal/agente para servicios de terceros si corresponde.

**Cierre verificable:** Un contrato sintético con anticipo, aceptación diferida y suscripción muestra tres cronologías reconciliadas: ingreso, facturación y caja. Contador documenta marco y juicio aplicado sin imponer NIIF 15 a un sujeto no determinado; descuentos/bonificaciones quedan vinculados a su período/contrato.

**Dueño sugerido:** Contador y Dirección financiera del proveedor, con Comercial y Legal. **Dependencias:** Marco contable empresarial; Modelo contractual y evidencia de aceptación; Tarifario y política de créditos comerciales.

### REV-ACC-08 — Conciliar cobros netos y retenciones sufridas del proveedor

**P1 · brecha de especificación/alcance · Hito:** Antes de cobrar facturas propias de bancos/PSP u otros clientes que descuenten retenciones, comisiones o diferencias de cambio.

**Observación:** TAX define funciones de agente que retiene a terceros y REC concilia flujos financieros del producto. No se especifica la cuenta por cobrar empresarial del proveedor con factura bruta, transferencia neta, certificados de retención sufrida, notas de crédito, diferencias y crédito tributario propio.

**Evidencia:** [FR-TAX-011, FR-TAX-013, FR-TAX-018](../functional/24-tributos-recaudaciones.md): Retener, emitir certificado y liquidar obligación del agente están previstos.; [FR-REC-019; Propósito](../functional/22-conciliacion-excepciones.md): Conciliación de régimen/comisiones/certificados del producto; no es un submayor de facturas propias del fabricante.; [§12.3 — Economía](../market_analysis.md): Incluye caja y demora de cobro como indicadores del proveedor..

**Impacto:** Registrar sólo el depósito neto como venta subestima ingresos o da de baja saldos incorrectos; certificado faltante puede dejar crédito fiscal sin soporte o duplicarlo.

**Acciones:**

- Definir workflow en administración/ERP del proveedor para imputación de cobro parcial, certificado sufrido, comisión bancaria y diferencia en moneda, por factura y tributo/jurisdicción.
- Conciliar bruto facturado con neto bancario, retenciones/percepciones acreditables y saldo pendiente; validar autenticidad/período de certificados y llevar excepciones.

**Cierre verificable:** Una factura cobrada neta de deducciones concilia ingreso, cuenta por cobrar, banco, gasto y crédito fiscal según política sin tratar todo descuento como gasto ni toda retención como pago definitivo. Pago/certificado duplicado no extingue dos veces saldo ni crea doble crédito; faltante conserva responsable y estado pendiente.

**Dueño sugerido:** Tesorería/Administración y Contador del proveedor. **Dependencias:** Facturación B2B; Regímenes de retenciones sufridas aplicables; Extractos/certificados autorizados.

### REV-ACC-09 — Resolver costeo por cliente y política de desarrollo capitalizable

**P1 · decisión pendiente · Hito:** Antes de fijar margen/precio sostenible o utilizar un presupuesto de desarrollo como valor de activo.

**Observación:** NFR-12/OPS ya exigen costo por celda y fuentes; mercado distingue producto común/integración y advierte que inversión frente a gasto necesita análisis. Faltan reglas de imputación de horas/costos comunes, ociosidad, implementación, soporte y evolución, y política del marco propio para capitalizar/gastar y eventualmente amortizar/deteriorar desarrollo.

**Evidencia:** [NFR-12-C03, NFR-12-C04](../nfr/NFR-12-operabilidad-costos.md): Costos mensuales y contraste con presupuesto están propuestos, sin medición.; [FR-OPS-027, FR-OPS-028](../functional/30-operacion-continuidad-terceros.md): Incluye componentes de servicio/capacidad; no fija política contable ni bases de reparto.; [§7.3, §8.3 y §12.1](../market_analysis.md): Evitar doble conteo de personas; inversión/gasto requiere análisis; producto común e integración separados..

**Impacto:** Puede aparentar margen por trasladar soporte a desarrollo o sobrevalorar un activo; el mismo personal/costo puede contarse en proyecto y plataforma.

**Acciones:**

- Definir centros de costo y bases verificables de reparto entre producto, cliente, implantación, operación y administración; incluir costos compartidos y capacidad ociosa explícitos.
- Aprobar política de gasto/activo y costos elegibles bajo marco real, con evidencias de fase, horas, entregables y revisión posterior; no inferir capitalización por llamarlo desarrollo propio.
- Separar impuestos recuperables de costos no recuperables y de efectos transitorios de caja en cada escenario.

**Cierre verificable:** Una muestra de horas/facturas se imputa una vez y concilia al mayor/presupuesto; margen por cliente mantiene bases/moneda y muestra subsidios cruzados. Cada importe activado tiene fundamento y soporte; lo no elegible se trata según política, y presupuesto de inversión no se confunde con activo contable.

**Dueño sugerido:** Dirección financiera/Contador del proveedor y líderes de Entrega/Operaciones. **Dependencias:** Marco contable empresarial; Registro de horas/consumo y contratos; Tratamiento fiscal de compras.

### REV-ACC-10 — Definir moneda e inflación del negocio proveedor por separado del módulo bancario

**P1 · decisión pendiente · Hito:** Antes de consolidar presupuesto, cierre o precio en varias monedas del proveedor.

**Observación:** El modelo de mercado está en USD constantes; LED prevé FX e inflación para EF. Esa funcionalidad del producto no determina moneda de registración/presentación, conversión de facturas/cobros, exposición monetaria ni ajuste aplicable del proveedor. Tampoco debe copiarse sin análisis al PNFC.

**Evidencia:** [Versión; §4.3; §8.2](../market_analysis.md): Modelos en USD constantes; moneda/indexación y descalce deben validarse; tasas/flujos deben ser consistentes.; [FR-LED-025, FR-LED-026](../functional/08-ledger-contabilidad-cierres.md): FX y ajuste por inflación del catálogo están definidos para EF..

**Impacto:** Un precio USD con costo ARS puede verse rentable en moneda constante y perder caja; mezclar resultados nominales, convertidos y reexpresados altera margen y patrimonio.

**Acciones:**

- Documentar monedas de contrato/factura/cobro/contabilidad/presentación y fuentes/fechas de conversión para cada evento del proveedor.
- Determinar marco y tratamiento inflacionario efectivo, separando modelo real comercial, registración nominal y ajustes contables/fiscales que correspondan; especificar conciliación mediante ERP o proceso externo.

**Cierre verificable:** Caso sintético entre contratación, factura, cierre y cobro a cotizaciones distintas explica toda diferencia y separa resultado, impuesto y caja. El presupuesto identifica moneda/base temporal y escenario de devaluación/inflación; no usa la funcionalidad EF como evidencia del cierre empresarial propio.

**Dueño sugerido:** Contador y Tesorería del proveedor. **Dependencias:** Marco contable y fiscal empresarial; Condiciones de moneda/indexación del contrato; Fuentes de cotización/índices efectivas.

### REV-ACC-11 — Calendarizar el modelo económico con impuestos y capital de trabajo

**P0 · brecha de especificación/alcance · Hito:** Antes de aprobar financiación, estructura fija o propuesta a precio cerrado usando los modelos ilustrativos como presupuesto de caja.

**Observación:** Las sumas de ARR/TCO y equilibrio son consistentes; el modelo declara que excluye impuestos/retenciones/financiación y que debe calendarizar anticipos, aceptación y cobros. Aún no existe un presupuesto empresarial mensual integrado de resultados y caja con esos efectos y sensibilidad por demora.

**Evidencia:** [§7.2, §7.3 y §8.2–8.4](../market_analysis.md): ARR de salida no es ingreso acumulado; equilibrio excluye financiamiento/impuestos; TCO excluye impuestos y necesita otro cronograma para caja.; [§12.3 — Entrega/Economía](../market_analysis.md): Horas hasta aceptación, caja y demora de cobro son indicadores expresos.; [NFR-12-C04](../nfr/NFR-12-operabilidad-costos.md): Límite económico debe fijarse por caso aprobado, sin umbral universal..

**Impacto:** Puede financiarse una estructura fija con ARR esperado al mes 36 aunque faltan meses de caja, anticipo suficiente o cobertura de impuestos/costos previos a cobrar.

**Acciones:**

- Construir calendario por contrato/escenario con hitos, probabilidad, reconocimiento, facturación, cobro, pagos de equipo/nube y tributos aplicables, sin reemplazar datos faltantes por tasas legales supuestas.
- Separar EBITDA/resultado u otra medida elegida, caja, créditos fiscales recuperables, retenciones, capital de trabajo y financiación; usar escenarios de atraso/cancelación y salida.
- Aprobar supuestos/base de moneda y presupuesto por puerta de inversión, conservando el TCO comparativo original como escenario de alcance limitado.

**Cierre verificable:** Modelo mensual reproduce ARR de salida e ingresos/caja de cada contrato sin equivalerlos; apertura más entradas menos salidas concilia saldo final. Muestra necesidad máxima de caja y sensibilidad a atraso, impuestos recuperables/no recuperables, FX y costo de soporte, con supuestos y responsable; no se fija solvencia por una cifra sin fondos acreditados.

**Dueño sugerido:** Dirección financiera/Contador y Dirección del proveedor. **Dependencias:** Hitos comerciales/contratos y plazos de cobro; Costeo por cliente; Perfil fiscal y moneda del proveedor.

## Relaciones del resto del inventario

| Módulos | Relación contable/fiscal que debe preservarse |
|---|---|
| ENT, IAM, CLI, CFG, CON | Sociedad/actividad, situación fiscal y facultades; regla vigente y evidencia contractual. Contrato financiero del cliente y contrato de venta de software del proveedor son documentos distintos. |
| ACC, BAL, LED, CRE, INT, GAR, COL | Obligaciones/fondos, consumo y reservas, valoración de garantía, devengos, prioridades de cobro y baja; puente entre deuda contractual y saldo contable. |
| PAY, CHQ, CRD, CSH | Fuente independiente para acreditación/liquidación, clearing, caja física, reversos, comisiones e impuestos. La aceptación técnica no demuestra cobro o entrega. |
| TRE, FXT, INV | Moneda/unidad, cotización, custodia propia/terceros, liquidación y resultados de valuación; no mezclar posición de cliente con ingreso/tesorería del proveedor. |
| AML, FRD, REC, RSK, TAX, RPT | Calidad/secretos, pérdidas/recuperaciones, conciliación, clasificación, tributo y reporte; no confundir reporte sistemático, declaración fiscal y pago/imputación. |
| CST, DAT, ASY, MIG | Explicación de cobros, soporte probatorio, retención/hold, secuencias y unicidad; apertura/historia y PREPARED no duplican mayor ni resultado. |
| OPS, AIG, COR | Costos fuente y continuidad, decisiones de modelos, precio/mandato/responsabilidades BaaS/corresponsal/plataforma; ingreso propio y fondos administrados se concilian separadamente. |

## Orden de trabajo y decisiones institucionales

Primero elegir perfil/cliente y cerrar el paquete contable (REV-ACC-01); la ampliación no EF y la ficha de rendimiento se resuelven según la oferta (REV-ACC-02/03). El cierre observado requiere prototipo y datos aprobados (REV-ACC-04). En paralelo puede prepararse el perímetro empresarial sin datos sensibles y luego validarlo con documentación mínima autorizada (REV-ACC-05).

El circuito empresarial recomendado es contrato/consumo → factura → cuenta por cobrar/cobro neto → créditos fiscales/obligaciones → mayor/resultado/caja. Facturación y reconocimiento se concretan con REV-ACC-06/07/08; costos y moneda con REV-ACC-09/10; el modelo mensual de REV-ACC-11 integra los resultados antes de comprometer financiación. El ERP o servicio contable elegido puede ejecutar ese circuito fuera del core.

Quedan a cargo de los responsables reales: designación de entidad y marco, firma de políticas/vectores, determinación fiscal por jurisdicción, aprobación de estados y presentación/pago autorizado. No se modificaron requisitos base, skills, parámetros ni fuentes normativas. Los próximos cambios documentales propuestos y su impacto en skills están enumerados por hallazgo en [accounting.json](findings/accounting.json).
