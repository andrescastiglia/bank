---
name: core-fr-requisitos
description: "Usar para crear, mantener, revisar o retirar Functional Requirements del core bancario por módulo, con identidad estable, aceptación, excepciones, aplicabilidad y trazabilidad a casos y evidencia."
---

# Ciclo de vida de Functional Requirements

## Alcance y lectura

Un FR especifica comportamiento observable. Un NFR define calidad/restricción y un ADR registra una elección. Leer [alcance funcional](../../../docs/functional/scope.md), [catálogo](../../../docs/functional/README.md), módulos afectados, [flujos integrados](../../../docs/functional/flows.md) y los hallazgos de [calidad](../../../docs/review/05-quality-skills.md). Usar los coordinadores de [NFR](../core-nfr-calidad/SKILL.md), [ADR](../core-adr-arquitectura/SKILL.md) y [cumplimiento](../core-bancario-argentina/SKILL.md) cuando corresponda.

## Procedimiento

1. Identificar actor, sociedad/rol, producto, disparador, precondición, datos, facultad, resultado y excepción. Delimitar si es comportamiento del core, integración o decisión institucional. No transformar «cumplir ISO/BCRA» en un FR sin conducta verificable.
2. Buscar el requisito vigente antes de duplicarlo. Asignar siguiente ID libre por módulo; conservar IDs publicados. Si se retira/sustituye, mantener su registro, motivo, versión y reemplazo. **Nunca renumerar los posteriores para satisfacer un verificador.** El generador de la línea base exige contigüidad y no interpreta retiros: evolucionar su contrato/manifiesto de estados antes de afirmar que el catálogo soporta el retiro. Conservar el registro histórico, excluirlo de cobertura activa y reasignar fuentes/capacidades/casos al reemplazo o dejar una brecha visible. Un tombstone que la herramienta sigue contando no resuelve el problema.
3. Escribir las cinco columnas del catálogo: ID, comportamiento, ámbito/etapa, aceptación/excepciones y trazabilidad. Aplicar [la ficha](references/fr-template.md). Evitar combinar funciones sin un resultado de negocio común; concretar campos/esquemas en el contrato de interfaz asociado.
4. Definir casos permitidos, denegados y de fallo/concurrencia material, resultado esperado y oráculo independiente. Relacionar FR → caso → fixture/oráculo → ejecución/evidencia → versión. Si sólo existe el caso propuesto, dejar la ejecución sin evaluar.
5. Validar la fuente y su aplicabilidad, no sólo el ID. Una relación a norma puede ser soporte de evidencia, integración o función directa; no transmite por sí sola obligación ni prueba cumplimiento. Revisar ediciones, vigencia, perfil y transiciones.
6. Revisar el cambio semántico: ¿se suprimió un caso, una excepción, un dato o un control aunque el ID siga presente? Propagar impacto a dependencias, operaciones, reportes, NFR, ADR, capacidades comerciales y skills. Un porcentaje idéntico no demuestra equivalencia.
7. Mantener fronteras monetarias y estados: commit local, recepción durable y liquidación externa no equivalen; reintento de mensaje y dos ingresos reales son hechos distintos; correcciones preservan originales; datos PREPARED no se publican operativamente. No autorizar efectos externos por replay o vencimiento de lease.
8. Ejecutar el generador/check documental y verificaciones pertinentes. Sus controles cubren tablas/referencias/artefactos, no semántica total, metadatos de todos los skills ni pruebas del producto. Registrar las limitaciones encontradas y corregirlas en su alcance, sin ocultarlas renombrando requisitos.

## Salida

Entregar FR creados/cambiados/retirados, motivo, aplicabilidad, diferencias funcionales, relaciones y casos, verificación efectuada y pendientes. Separar estado del requisito, implementación, evidencia y aceptación institucional. Un pedido de requisitos no autoriza datos productivos, contactos, despliegues ni movimientos financieros.
