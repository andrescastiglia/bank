---
name: core-bancario-argentina
description: "Usar al diseñar, implementar, seleccionar o auditar un core bancario o ledger de pagos para Argentina y convertir leyes, regulaciones BCRA/UIF/AAIP/ARCA y estándares aplicables en controles y evidencia verificable."
---

# Core bancario argentino: requisitos y evidencia

## Propósito y límites

Evaluar el alcance regulatorio y convertir requisitos aplicables en decisiones de arquitectura, historias de implementación y pruebas. Servir para bancos, proveedores de servicios de pago y proveedores tecnológicos; no equiparar sus licencias ni sus obligaciones. No declarar un producto «certificado por BCRA», «cumplimiento automático» o conformidad integral por tener un certificado ISO.

La línea base fue investigada el **15 de octubre de 2026**. No tratarla como un inventario permanentemente vigente. Antes de usar un requisito para una decisión de producción, verificar fuente oficial, texto actualizado, comunicación modificatoria, destinatario y fecha de exigibilidad. Las revisiones jurídicas, contables y de cumplimiento corresponden a los responsables competentes de la entidad; el trabajo del agente consiste en aportar trazabilidad y evidencia técnica.

## Entrada mínima y avance con información incompleta

Determinar, a partir del contexto disponible:

- Sujeto y rol: entidad financiera autorizada, PSP registrado y función, proveedor no financiero de crédito, participante de infraestructura o proveedor tecnológico.
- País y entidad jurídica de cada operación, licencia o registro efectivo y servicios contratados.
- Productos: depósitos, cuenta de pago, préstamos, tarjetas, inversiones, cambios, cheques, transferencias y servicios de terceros.
- Modalidad: construcción, selección, migración, revisión de código o evaluación de proveedor; fecha de corte y salida prevista.
- Arquitectura, custodios de fondos, países de procesamiento/soporte/backup, terceros y subcontratistas; canales y datos tratados.

Consultar sólo los datos faltantes que cambien una decisión. Mientras tanto, producir una evaluación preliminar con supuestos expresos y requisitos pendientes de aplicabilidad. No considerar que una cuenta de pago es un depósito bancario ni que prestar tecnología habilita intermediación financiera. No inferir la licencia de una empresa por su marca comercial.

## Lectura progresiva

1. Leer [metodología](references/metodologia.md), que define jerarquía de fuentes y estados de verificación.
2. Para encuadre jurídico, secreto, datos, prevención de delitos financieros, consumidor y fiscalidad, leer [leyes y autoridades transversales](references/leyes.md).
3. Para productos, pagos, prudencia, reportes, TI/SI, nube, terceros e IA, leer [regulaciones BCRA](references/regulaciones-bcra.md).
4. Para certificaciones y sistemas de gestión, leer [ISO](references/iso.md).
5. Para PCI, SWIFT, NIST, OWASP, COBIT y atestaciones, leer [normas y estándares de industria](references/estandares-industria.md).
6. Para implementación o revisión técnica, aplicar [controles y criterios de aceptación](references/controles.md).

Las referencias son autónomas para iniciar el trabajo. Si se está dentro del repositorio que originó este skill, ampliar con `docs/compliant.md` y `docs/market_analysis.md`; no requerir esos documentos para usar el skill en otro repositorio.

## Procedimiento

### 1. Fijar perímetro y registro normativo

Crear una matriz por entidad jurídica y producto. Distinguir obligación directa de la entidad, obligación del proveedor derivada de un contrato y buena práctica de ingeniería. Identificar el responsable institucional y el componente que implementa cada control; un core no sustituye al oficial de cumplimiento, al gobierno corporativo ni a la licencia.

Para cada fuente guardar: organismo, identificador, título, artículo/sección verificados, URL oficial, versión o revisión, publicación, entrada en vigencia, transición/exigibilidad, sujetos, modificaciones conocidas y fecha de consulta. Si una página es sólo un índice o un catálogo, consignarlo. No inventar un artículo para completar la matriz.

Para BCRA, cotejar el texto ordenado con comunicaciones posteriores hasta el corte. Para leyes, leer el texto actualizado y su historia de modificaciones. Para UIF, separar reglas del sector de reglas transversales; no extender una resolución de otro sujeto obligado. No importar requisitos de GDPR, DORA, PSD2 u OFAC como si fueran ley argentina: evaluar el nexo jurisdiccional o contractual concreto.

### 2. Clasificar cada requisito

Usar estas categorías independientes de su prioridad:

- **LEGAL**: ley, decreto o decisión judicial/administrativa aplicable.
- **REGULATORIO**: disposición obligatoria del regulador competente para el sujeto y producto.
- **SUPERVISIÓN**: guía o expectativa de supervisión; registrar su vínculo con la norma base.
- **CONTRACTUAL**: exigencia de una red, cliente, adquirente o contrato efectivamente aplicable.
- **ESTÁNDAR**: marco voluntario adoptado por decisión documentada.
- **DISEÑO**: mecanismo técnico propuesto para satisfacer una obligación o un objetivo; no atribuirlo literalmente a una norma que no lo exige.

Aplicabilidad: `aplica`, `condicional`, `no aplica con fundamento` o `por determinar`. Verificación: `fuente primaria revisada`, `referencia localizada pendiente de texto` o `no verificado`. Implementación: `sin evaluar`, `brecha`, `parcial`, `implementado sin evidencia`, `verificado` o `excepción documentada`. Nunca convertir «no encontrado» en «no obligatorio» ni «sin evaluar» en «cumple».

### 3. Traducir a controles y contratos de datos

Usar un identificador estable por requisito y controles reutilizables. Definir responsable, módulo, datos, operación, criterio medible y evidencia esperada. Cubrir de extremo a extremo la operación, incluyendo canal, core, motor antifraude/AML, procesador, conciliación, contabilidad, reporte y tercero.

Verificar como mínimo: integridad del libro y saldos; determinismo monetario; idempotencia y estados de pagos; temporalidad y versionado de reglas; identidad y permisos; secreto y privacidad; integración AML; resiliencia y restauración; auditoría; contratos de terceros; exactitud de reportes; trazabilidad de condiciones comerciales y migración.

No fijar tasas, límites, umbrales AML, impuestos, montos de garantía, encajes o calendarios como constantes legales permanentes. Parametrizar con autoridad, producto, moneda, jurisdicción, `effective_from`, `effective_to`, versión, aprobación y motivo. Conservar la versión utilizada por cada operación.

### 4. Evaluar evidencia

Inspeccionar documentos, contratos, configuraciones y código disponibles sin solicitar datos personales de producción cuando basten ejemplos sintéticos. Revisar muestreo, alcance y fecha de pruebas; un documento de política por sí solo no demuestra efectividad operativa.

En una implementación, seleccionar pruebas proporcionales al riesgo y al cambio. Para un control financiero material, probar concurrencia, redondeo, duplicados, reversos, fallos parciales, cambios de fecha y conciliación. Para continuidad, exigir restauración observada y reconciliación posterior; la existencia de backup no demuestra recuperabilidad. Para seguridad, revisar separación de funciones, accesos privilegiados, secretos, trazas y segregación entre clientes.

No inferir cobertura de todo el servicio por un ISO/SOC del centro de datos. Verificar titular, servicios, ubicaciones, período, exclusiones, responsabilidades del cliente y subcontratistas. En PCI, definir el entorno de datos de tarjetas y dependencias que pueden afectar su seguridad antes de considerar una reducción de alcance por tokenización.

### 5. Reportar y priorizar

Entregar una matriz con estas columnas, adaptándola al tamaño del pedido:

`ID | fuente y sección | sujeto/producto | categoría | aplicabilidad | obligación | control propuesto | módulo/responsable | criterio de aceptación | evidencia observada | estado/brecha | prioridad | próxima acción`.

Cada hallazgo debe explicar el escenario que lo activa, el efecto económico u operativo y la evidencia. Priorizar: autorización y fondos de clientes; integridad financiera; secreto y datos; fraude/LA-FT-FP; disponibilidad y terceros; reportes y consumidor. Definir un plan con responsable y dependencia, sin fabricar fechas de compromiso.

Ante una contradicción normativa, dejar registro de ambas fuentes, fechas y alcance, proponer una lectura provisional y derivar la resolución al responsable competente. Una aceptación interna de riesgo no elimina una obligación legal. No suspender tareas reversibles de análisis o corrección mientras se resuelve una decisión institucional.

## Salida esperada

- Fecha de corte, alcance y supuestos.
- Dictamen técnico acotado: qué fue comprobado y qué sigue sin evidencia.
- Matriz de requisitos y trazabilidad a código, configuración, pruebas o contrato.
- Brechas priorizadas y acciones concretas.
- Fuentes oficiales y cuestiones pendientes de interpretación/aplicabilidad.

No emitir una certificación de cumplimiento jurídico. Usar formulaciones precisas como «este control satisface el criterio probado bajo el alcance y versión indicados».
