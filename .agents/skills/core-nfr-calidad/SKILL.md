---
name: core-nfr-calidad
description: "Usar para crear, mantener, especificar, medir o revisar Non-Functional Requirements (NFR), atributos de calidad y restricciones verificables, y relacionarlos con ADR, controles y evidencia del proyecto."
---

# Crear y verificar Non-Functional Requirements

## Significado y propósito

Un **NFR — Non-Functional Requirement** define una condición de calidad o restricción verificable bajo un escenario, alcance y entorno. No describe por sí solo una función ni prescribe necesariamente una tecnología. «Importar cartera» es funcional; «importarla dentro de la ventana aprobada, sin diferencias ni duplicados, manteniendo el servicio» es NFR; «usar COPY hacia staging y publicar una cohorte» es un Architectural Decision Record.

Este skill permite crear requisitos nuevos, mantener los existentes y aplicar sus criterios al diseño, implementación o verificación. Los trece NFR de la línea base son familias con criterios propios; no se interpretan como trece certificaciones o cualidades ya logradas.

## Entrada y lectura progresiva

Identificar objetivo de negocio, perfil/entidad, función/servicio, usuarios, carga, estímulo/fallo, entorno y trabajo autorizado. Leer [índice NFR](../../../docs/nfr/README.md), [arquitectura](../../../docs/achitecture.md) y la fuente comercial o regulatoria pertinente. Usar [core-adr-arquitectura](../core-adr-arquitectura/SKILL.md) para decisiones motivadas por esos requisitos y [core-bancario-argentina](../core-bancario-argentina/SKILL.md) para encuadre legal.

La documentación del 15/10/2026 propone objetivos; no hay pruebas de la aplicación por la sola existencia del documento. Si faltan datos, definir el escenario y registrar la dependencia; no inventar un umbral, contrato, aprobación o medición. Avanzar en análisis/correcciones independientes ya autorizadas.

## Procedimiento

1. **Separar función y calidad.** Nombrar la función o dato al que aplica el atributo. Convertir adjetivos como rápido, seguro, disponible o configurable en resultados observables, sin sustituirlos por «usar Kafka/Kubernetes» o «tener ISO».
2. **Crear identidad estable.** Buscar requisitos existentes antes de duplicar. Una familia usa `NFR-XX`; cada criterio `NFR-XX-CYY`. Una ampliación del mismo atributo conserva su historia; una familia nueva recibe el siguiente ID libre. No reutilizar IDs retirados.
3. **Definir escenario completo.** Registrar sujeto/estímulo, servicio/artefacto, entorno normal/degradado, respuesta esperada, población/carga, métrica/unidad, ventana, umbral y oráculo. Utilizar [la plantilla](references/plantilla-nfr.md). Condiciones binarias también son medibles si se conocen población y resultado.
4. **Clasificar origen del objetivo.** Distinguir obligación aplicable, contrato, objetivo de negocio, supuesto de arquitectura y propuesta nueva. Conservar fuente/versión/período. No transformar valores propuestos en límites legales; un parámetro por acordar es un pendiente que impide afirmar aceptación, no una licencia para omitir la calidad.
5. **Resolver relaciones y conflictos.** Mapear NFR a funciones, ADR, CTL y componentes. Evaluar disponibilidad frente a persistencia/latencia, privacidad frente a conservación, costo frente a capacidad, y carga inicial frente al servicio activo. Una compensación interna no elimina una obligación aplicable.
6. **Seleccionar los skills de atributo.** Leer los NFR específicos afectados. Para cambios de dinero/colas revisar integridad y asincronía; topología requiere recuperación, seguridad y residencia; bulk requiere migración, integridad y reportes; configuración requiere mantenibilidad, integridad y experiencia.
7. **Actuar según el pedido.** Diseñar el mecanismo, realizar cambios autorizados en código/configuración existente o verificar evidencia. Elegir pruebas materiales por riesgo; no agregar pruebas que sólo repliquen el texto del requisito. Usar datos sintéticos y no cargar producción para un pedido documental.
8. **Medir correctamente.** Distinguir objetivo, configuración y resultado. Medir latencia extremo a extremo con percentiles/errores, sin sumar percentiles. Separar disponibilidad por solicitudes de equivalencia por tiempo; objetivo de lag no prueba RPO regional. Comparar población y entorno con lo contratado y registrar exclusiones, muestras y límites de inferencia.
9. **Mantener historia.** Actualizar registro, índice, arquitectura y skills afectados; conservar motivo/versión y pruebas previas. No cambiar un umbral después del ensayo para ocultar una brecha ni reducir un control material sin fundamento. La aceptación y la evidencia observada se registran por separado.

## Familias y aplicación

El [índice NFR](../../../docs/nfr/README.md) enlaza los trece skills: integridad; disponibilidad/recuperación; latencia/capacidad; asincronía durable; seguridad; privacidad/residencia/retención; auditoría/observabilidad; interoperabilidad/portabilidad; mantenibilidad/configuración; migración; calidad de datos/reportes; operabilidad/costos; accesibilidad/experiencia.

No ejecutar todas las familias para cualquier cambio menor. Si se usa IA o se activa un producto especializado, ampliar el alcance de calidad y normativa correspondiente sin asumir que el catálogo inicial lo verifica automáticamente.

## Salida y estados

Entregar `ID criterio | atributo | servicio/perfil | escenario/entorno | métrica/unidad | población/ventana | objetivo y origen | oráculo | evidencia observada | estado | brecha/acción | ADR/CTL`.

Separar estado del requisito —`Propuesto`, `Aceptado`, `Reemplazado`, `Descartado`— de evaluación —`no evaluado`, `diseñado`, `implementado sin evidencia`, `verificado`, `brecha`, `no aplica con fundamento`. Un ensayo verificado acredita sólo su alcance y versión; no prueba todas las cargas/fallas futuras ni certifica el sistema. Informar cambios realizados, comprobaciones y dependencias concretas.
