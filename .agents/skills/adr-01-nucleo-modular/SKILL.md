---
name: adr-01-nucleo-modular
description: "Usar al diseñar, implementar o revisar límites de módulos, dependencias, propiedad de datos o extracción de servicios del núcleo financiero de este proyecto según ADR-01."
---

# Aplicar ADR-01: núcleo modular

## Alcance y decisión de referencia

Preservar un núcleo financiero modular con transacciones locales para los invariantes de dinero. Separar responsabilidades en código y datos; desplegar servicios independientes cuando lo justifiquen aislamiento, carga, conectividad o entrega. La decisión es **propuesta en la línea base del 15/10/2026**; no convertirla en una prohibición inmutable ni declarar que ya fue implementada.

Usar para fronteras de dominio y topología de despliegues. Para la transacción financiera detallada consultar ADR-02; para el transporte asíncrono, ADR-03. La frontera modular no concede licencias ni prueba cumplimiento.

## Entrada y lectura

Identificar el cambio autorizado, perfil/producto, módulos afectados, datos, flujos y motivo comercial u operativo. Leer el [registro ADR-01](../../../docs/adr/ADR-01-nucleo-modular.md), las secciones pertinentes de [arquitectura](../../../docs/achitecture.md#modulos) y el [análisis de mercado](../../../docs/market_analysis.md). Inspeccionar el código, contratos y esquema existentes; si sólo hay documentos, entregar diseño y backlog sin inventar servicios, repositorios o pruebas ejecutadas.

Avanzar con supuestos explícitos si falta una métrica secundaria. Pedir sólo información que cambie la decisión; no detener análisis o correcciones reversibles por falta de una aceptación institucional del ADR.

## Procedimiento

1. **Nombrar responsabilidades.** Dibujar el flujo desde el canal hasta contrato, disponibilidad, ledger, outbox y proyecciones. Asignar a cada tabla/evento/operación un dueño. Identificar decisiones preventivas y tareas que pueden demorarse.
2. **Localizar invariantes.** Marcar qué estado debe cambiar junto: reservas, límites, restricciones, posiciones y asientos. Mantener esa unidad en una transacción del núcleo. No descomponerla en varias bases porque coincida con nombres de módulos.
3. **Diseñar contratos.** Explicitar comandos, resultados, errores, datos y dependencias permitidas. Evitar ciclos de escritura, consultas indiscriminadas a tablas ajenas y lógica monetaria duplicada en API, worker o adaptador.
4. **Seleccionar despliegues.** Partir de API, núcleo/workers, adaptadores y consumidores periféricos. Justificar cada proceso adicional mediante carga, riesgo, seguridad o equipo; reservar capacidad de conexión/CPU para la operación crítica.
5. **Evaluar la extracción.** Comparar mantener el módulo, separar su proceso conservando transacción y extraer servicio/base. Para la última opción describir autoridad, coordinación, ambigüedad, idempotencia, conciliación, retorno y costo de operación. Un llamado remoto no conserva automáticamente una transacción local.
6. **Ejecutar según pedido.** Si se pidió implementar/refactorizar, realizar cambios acotados y compatibles en el código disponible, actualizar contratos y correr las verificaciones relevantes. Si se pidió diseñar o revisar, entregar el mapa/alternativas o hallazgos sin desplegar componentes por ese solo motivo.
7. **Cerrar trazabilidad.** Vincular decisión y criterios con evidencia. Si cambia la línea base, registrar contexto y consecuencias en el ADR y sus relaciones; no modificar silenciosamente el significado de otro ADR.

## Invariantes y escenarios de verificación

- Sólo el núcleo autorizado puede alterar fondos. Reportes, proyecciones y conciliación solicitan comandos para ajustes; no actualizan saldos directamente.
- API y workers comparten semántica financiera. Reintentar por un camino distinto conserva identidad, permisos y efecto.
- Cada contrato tiene una autoridad durante coexistencia/migración. Separar servicios no permite que dos sistemas lo modifiquen a la vez.
- Las funciones activadas corresponden al producto/licencia; un tenant PSP no obtiene depósitos por importar el módulo de una EF.

Con código disponible, verificar dependencias, rutas de escritura y escenarios de concurrencia, reintento y saturación por reportes. Antes de extraer, simular caída y respuesta perdida entre los futuros servicios. Seleccionar pruebas materiales; no agregar pruebas que sólo repitan nombres de paquetes o el texto del ADR.

## Salida

Entregar mapa de módulos/datos, cambio o hallazgos, alternativas evaluadas y matriz `flujo | invariante | propietario | contrato | despliegue | criterio | evidencia | estado`. Separar `diseñado`, `implementado sin evidencia` y `verificado`. Los NFR de rendimiento, entrega y operabilidad se verifican por separado: la modularidad por sí sola no acredita baja latencia ni alta disponibilidad.

Ante alcance regulatorio afectado, aplicar las referencias pertinentes de [core-bancario-argentina](../core-bancario-argentina/SKILL.md), en especial CTL-01, CTL-03, CTL-04, CTL-15 y CTL-17.
