---
name: nfr-12-operabilidad-costos
description: "Usar al diseñar, implementar o verificar operación, guardia, runbooks, dependencias de soporte y costo por celda/cliente del core, según NFR-12."
---

# Verificar operabilidad y costo sostenible

## Alcance y entrada

Aplicar [NFR-12](../../../docs/nfr/NFR-12-operabilidad-costos.md) al servicio o cambio pedido. Identificar perfil/cliente, flujos críticos, equipo/soporte, dependencias, exposición, carga, retención, presupuesto y moneda. Leer [operación de arquitectura](../../../docs/achitecture.md#operacion) y el caso económico pertinente de [mercado](../../../docs/market_analysis.md).

Los objetivos de la línea base del 15/10/2026 son propuestos. No inventar servicio desplegado, cobertura 24/7, presupuesto aprobado o mediciones. Si aún no existen, producir modelo y plan verificables y completar el trabajo reversible autorizado.

## Procedimiento

1. Enumerar servicios/flujos críticos y sus dependencias de infraestructura, identidad, claves, rieles, datos y personas. Asociar criticidad/BIA, dueño, guardia, escalamiento y runbook; distinguir proveedor y entidad responsable.
2. Diseñar o revisar detección y respuesta. Un runbook debe permitir reconocer impacto, contener, conservar evidencia, consultar estado financiero, comunicar y recuperar sin repetir egresos. Incluir tercero caído, backlog con deadline y diferencia de conciliación.
3. Fijar objetivos por perfil y fuente. Separar SLO técnico, plazo regulatorio, SLA del tercero y tiempo observado. No prometer un MTTR por disponer de autoscaling, ni usar una guardia técnica como autorización de reportes externos.
4. Construir costos desde sus fuentes: base y réplicas, bus, WAL/archivo, egreso, IAM/KMS, telemetría, entornos, soporte, licencias, localización, homologaciones y salida. Definir unidad facturable frente a comando técnico/asiento y evitar doble contar personas o componentes.
5. Calendarizar moneda, período, volumen y curva de retención. Contrastar costo por celda y contrato operado con presupuesto/margen aprobado; sin presupuesto, dejar sensibilidad y pendiente concreta, sin fabricar una aceptación económica.
6. Según pedido, implementar observabilidad/runbooks/automatización segura disponible, diseñar la operación faltante o revisar evidencia. Para una prueba autorizada, simular fallos con datos sintéticos y medir tiempos/capacidad/costo con controles activos. No desplegar una plataforma real por un pedido de análisis.
7. Documentar diferencia observada, impacto, dueño y acción. Verificar que otra persona/rol pueda seguir el procedimiento y que no dependa permanentemente del fundador. Registrar, no ocultar, la dependencia restante.

## Oráculos y límites

NFR-12-C01 a C05 requieren cobertura completa del inventario crítico, expediente de incidentes y costo reproducible. Un dashboard verde no demuestra recuperación; un costo bajo obtenido desactivando durabilidad, seguridad o retención no satisface el perfil. No eliminar controles obligatorios por margen insuficiente: revisar alcance, plataforma o precio.

Coordinar con NFR-02 para recuperación, NFR-03 para carga y NFR-07 para señales. Los ADR-01/04/07 pueden cambiarse con análisis y registro; la elección gestionada no transfiere la responsabilidad de la entidad. Consultar [core-bancario-argentina](../core-bancario-argentina/SKILL.md) sólo para determinar obligaciones o avisos afectados.

## Salida

Entregar `flujo | criticidad | responsable | runbook/guardia | indicador/objetivo | observación | costo/fuente | evidencia | brecha | acción`. Añadir modelo económico reproducible y sensibilidad cuando corresponda. Separar `no definido`, `diseñado`, `implementado sin evidencia` y `verificado`; no marcar un ensayo pendiente como operación demostrada. Reportar qué se cambió y cómo se comprobó conforme al pedido.
