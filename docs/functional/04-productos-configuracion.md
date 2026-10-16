# Módulo 04 — Productos, parámetros y reglas (CFG)

**Estado:** Propuesto; implementación y evidencia sin evaluar. **Base:** 15/10/2026. La configuración representa capacidades soportadas y no reemplaza autorización jurídica ni validación financiera.

## Propósito, actores y datos

Administrar catálogo de productos, reglas y calendarios con historia, ámbito y activación controlados. Actores: Producto, Finanzas, Fiscal, Riesgos, Cumplimiento, revisores independientes y operadores autorizados. Entradas: perfil, fórmula soportada, parámetros, fuente, vigencia, moneda, jurisdicción, mapeos y condiciones contractuales. Salidas: paquete validado, versiones instaladas, simulaciones, decisiones y evidencia de activación/corrección.

## Requisitos funcionales

| ID | Requisito funcional | Ámbito / etapa | Criterio de aceptación y excepciones | Trazabilidad |
|---|---|---|---|---|
| FR-CFG-001 | Registrar familias y versiones de productos con capacidades, entidades, segmentos, monedas y canales admitidos. | COMUN / BASE | Una versión nueva no habilita un producto excluido del perfil ENT; los contratos previos conservan su versión. | ADR-01, ADR-05, BCRA-F01 |
| FR-CFG-002 | Definir el esquema y catálogo cerrado de fórmulas/parámetros soportados por cada tipo de producto. | COMUN / BASE | Una fórmula desconocida o SQL/script suministrado como parámetro se rechaza; un algoritmo nuevo sigue cambio de código. | BCRA-T25, NFR-09-C04, CTL-15 |
| FR-CFG-003 | Crear una versión de regla con identidad, ámbito, fuente y motivo sin sobrescribir la anterior. | COMUN / BASE | La consulta histórica conserva la regla previa y quién registró el cambio. | BCRA-T06, CTL-06, CTL-12 |
| FR-CFG-004 | Registrar validez de negocio y tiempo de registro/conocimiento/aprobación como dimensiones distintas. | COMUN / BASE | Un corte anterior no utiliza una regla conocida después sin una corrección explícita y trazable. | ADR-05, NFR-09-C02, CTL-06 |
| FR-CFG-005 | Validar vigencias, jerarquía de ámbito y ausencia de solapamientos ambiguos. | COMUN / BASE | Dos reglas candidatas igualmente prioritarias impiden aprobación/uso y muestran conflicto; no se elige arbitrariamente la última. | NFR-09-C02, NFR-09-C03, CTL-02 |
| FR-CFG-006 | Gestionar borrador, simulación, revisión, aprobación, programación, activación y retiro de una versión. | COMUN / BASE | Actor incompatible no aprueba su propio cambio; retirar una versión no elimina su uso histórico. | BCRA-T03, BCRA-T17, NFR-05-C03 |
| FR-CFG-007 | Simular el efecto de una versión sobre contratos/datos autorizados y comparar el resultado anterior. | COMUN / BASE | La simulación explica cambios en cuotas, intereses, cargos, impuestos, asientos y reportes sin aplicar efectos reales. | CTL-02, CTL-15, NFR-09-C06 |
| FR-CFG-008 | Asociar vectores monetarios y resultados esperados revisados a fórmula/producto/regla. | COMUN / BASE | La versión no se declara validada sin los casos materiales definidos; el resultado observado permanece separado del esperado. | CTL-02, NFR-01-C04 |
| FR-CFG-009 | Configurar moneda, escala, precisión intermedia y redondeo por concepto. | COMUN / BASE | Un cálculo conserva importe exacto y regla; no combina monedas para cuadrar ni usa una escala de presentación como cálculo por defecto. | BCRA-T21, CTL-01, CTL-02 |
| FR-CFG-010 | Mantener calendarios, zonas, feriados, bases de días y tratamiento de vencimiento por producto. | COMUN / BASE | Un día no hábil y cambio de año usan la versión pactada; la fecha de negocio no se deduce de UTC sin zona/calendario. | CTL-06, NFR-01-C04 |
| FR-CFG-011 | Registrar tasas fijas/variables, índices, márgenes y reglas de renovación/cambio de tasa admitidas. | EF/PNFC/PSCPP / CREDITO | El contrato referencia índice, publicación y condición; un dato ausente no activa una tasa inventada. | BCRA-F05, BCRA-F07, CTL-02 |
| FR-CFG-012 | Definir la fuente y vigencia de unidades UVA/CER y UVI/ICC sin intercambiarlas. | EF/rol autorizado / BANCA | El cálculo guarda unidad/serie/fecha; atraso/corrección produce excepción o ajuste previsto, no conversión silenciosa. | LAW-16, BCRA-F06, CTL-02 |
| FR-CFG-013 | Configurar comisiones, bonificaciones y gratuidades por producto/cliente/período con fundamento contractual. | COMUN / BASE | Un cargo excluido por la modalidad no se cobra; una bonificación vencida sigue las condiciones históricas comunicadas. | LAW-08, BCRA-F03, BCRA-F08 |
| FR-CFG-014 | Vincular reglas tributarias, padrones y condición fiscal a conceptos de producto sin duplicar el motor TAX. | COMUN / BASE | Una operación selecciona versión fiscal efectiva y conserva cálculo/desglose; falla si no existe regla requerida. | TAX-01, TAX-03, CTL-02 |
| FR-CFG-015 | Definir plantillas de imputación y cuentas permitidas por evento, entidad y moneda. | COMUN / BASE | Una plantilla no balanceada, cuenta no admitida o moneda incompatible impide su publicación. | BCRA-F18, CTL-01, NFR-01-C01 |
| FR-CFG-016 | Configurar límites, sobregiro, facultades y condiciones de disponibilidad permitidos por producto. | COMUN / BASE | Caja de ahorro no recibe sobregiro por copiar una plantilla de cuenta corriente; BAL/RSK revalidan límites al ejecutar. | BCRA-F03, BCRA-F04, BCRA-F15, CTL-03 |
| FR-CFG-017 | Configurar estados y transiciones de contrato/operación dentro de la máquina soportada y sus controles. | COMUN / BASE | Un estado que omite autorización o transforma pendiente en liquidado sin evidencia se rechaza. | CTL-04, NFR-13-C02 |
| FR-CFG-018 | Registrar plazos/deadlines, calendarios y responsables por tarea, riel, reclamo o presentación. | COMUN / BASE | Cada reloj conserva hecho disparador y fuente; no se usa el plazo de notificación técnica para sustituir el de otro régimen. | BCRA-T46, AML-10, NFR-04-C04 |
| FR-CFG-019 | Incorporar versiones regulatorias futuras y transiciones por sujeto/período sin aplicarlas antes de exigibilidad. | COMUN / BASE | Se prueban períodos anteriores/nuevos y reglas por etapa; un texto consolidado con vigencia futura no cambia el período actual. | RPT-08, BCRA-T48, BCRA-T49, BCRA-T50, BCRA-T51, BCRA-T52 |
| FR-CFG-020 | Construir paquetes de configuración con esquema, versiones, dependencias y comprobación de integridad. | COMUN / BASE | Paquete alterado, parcial o incompatible queda rechazado con diagnóstico; no instala una selección incompleta. | BCRA-T17, BCRA-T25, CTL-15 |
| FR-CFG-021 | Instalar las versiones aprobadas en el ámbito local del núcleo y activar la referencia de forma atómica. | COMUN / BASE | Operaciones concurrentes usan una versión coherente completa; el plano remoto caído no impone consultas por cada débito. | ADR-05, NFR-09-C03, NFR-03-C02 |
| FR-CFG-022 | Resolver la regla efectiva al ejecutar con perfil, contrato y fecha aplicables y guardar su referencia. | COMUN / BASE | No se usa una versión futura/vencida/no aprobada, aun si falló el scheduler; la ausencia genera estado explícito permitido. | NFR-09-C02, NFR-09-C03, CTL-06 |
| FR-CFG-023 | Diferenciar condiciones contractuales pactadas de valores de catálogo para nuevas contrataciones. | COMUN / BASE | Cambiar el catálogo no reescribe una cuota o cargo de contratos anteriores sin cláusula/proceso válido. | LAW-06, CTL-18, NFR-13-C03 |
| FR-CFG-024 | Gestionar excepciones contractuales permitidas con autoridad, motivo, límites y evidencia de aceptación. | COMUN / BASE | Una excepción fuera de facultades o contraria a control aplicable no se publica como simple override. | BCRA-F08, BCRA-T03, CTL-09 |
| FR-CFG-025 | Ejecutar recálculos comparativos y generar propuestas de ajustes vinculadas, con fechas contables permitidas. | COMUN / BASE | No crea otro devengamiento base por cambiar rule_version; el ajuste preserva el original y requiere la aprobación aplicable. | ADR-02, CTL-02, CTL-04, NFR-01-C02 |
| FR-CFG-026 | Revertir una activación seleccionando una versión válida para decisiones futuras y documentando consecuencias. | COMUN / BASE | El rollback no elimina pagos liquidados, contratos ni reportes; las diferencias ya ejecutadas se corrigen por su procedimiento. | NFR-09-C05, CTL-15 |
| FR-CFG-027 | Restringir feature flags y habilitaciones para que no omitan controles invariantes o legales del perfil. | COMUN / BASE | Ninguna flag habilita saltar doble partida, aislamiento, autorización o auditoría; los intentos quedan registrados. | NFR-09-C04, CTL-01, CTL-09, CTL-17 |
| FR-CFG-028 | Exportar la configuración histórica y referencias necesarias para reproducir un contrato o reporte fuera del proveedor. | COMUN / BASE | La exportación autorizada incluye esquemas/versiones y excluye secretos; la reconstrucción identifica datos de origen requeridos. | CTL-16, NFR-08-C03, NFR-08-C04 |
| FR-CFG-029 | Mantener trazabilidad requisito/fuente, cambio, simulación, revisión, artefacto y activación de una versión. | COMUN / BASE | Un auditor reconstruye el cambio sin reemplazar la evidencia anterior; materiales sin prueba figuran pendientes. | BCRA-T22, BCRA-T25, NFR-09-C01 |
| FR-CFG-030 | Registrar tiempos, costos y trabajo específico de una solicitud de cambio para evaluar repetibilidad del producto. | PROVEEDOR/entidad / BASE | Se mide solicitud a activación y se compara con el objetivo acordado, separando hipótesis de costo observado. | NFR-09-C06, NFR-12-C03, NFR-12-C04 |

## Operaciones, estados y excepciones

Comandos: crear versión, validar, simular, revisar, aprobar, instalar, activar, retirar, recalcular y revertir activación. Consulta efectiva de reglas es inmediata; simulaciones y despliegue de paquetes pueden ser asíncronos con ID/estado. `202` de una simulación no activa reglas. La activación informa versión efectivamente instalada y punto de cambio.

Errores: regla ausente, rango solapado, fórmula no soportada, parámetro inválido, contrato fuera de ámbito, firma/hash alterado, aprobación incompatible y referencia concurrente cambiada. La falla no produce fallback silencioso. Auditoría captura valores relevantes anteriores/posteriores, versiones, actores y motivo; eventos no distribuyen credenciales.

## Escenarios integrados

1. Cambio de comisión: FR-CFG-003 a FR-CFG-008 y FR-CFG-013/023 simulan e instalan sin alterar contratos que no admiten el cambio.
2. Caída del scheduler: FR-CFG-019/021/022 seleccionan la versión por vigencia al ejecutar; nunca anticipan o demoran silenciosamente una regla normativa.
3. Corrección retroactiva de interés: FR-CFG-025 preserva identidad económica y genera diferencias/ajustes; FR-CFG-026 no borra dinero ejecutado.
4. Paquete de otro cliente o flag de bypass: FR-CFG-001/020/027 rechazan la instalación y preservan el perfil anterior válido.

## Dependencias y fuentes

[ENT](01-entidades-perimetro.md), [CON](05-contratos-documentos.md), [LED](08-ledger-contabilidad-cierres.md), [INT](10-intereses-comisiones.md), [TAX](24-tributos-recaudaciones.md), [RPT](25-reportes-localizacion.md), [ASY](28-integraciones-eventos-trabajos.md). Fuentes: [arquitectura](../achitecture.md#configuracion), [ADR-05](../adr/ADR-05-configuracion-versionada.md), [cumplimiento](../compliant.md), [NFR](../nfr/README.md), [mercado](../market_analysis.md).
