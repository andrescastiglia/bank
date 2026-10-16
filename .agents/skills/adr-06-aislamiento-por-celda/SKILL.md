---
name: adr-06-aislamiento-por-celda
description: "Usar al diseñar, implementar o revisar aislamiento entre entidades jurídicas del core: celdas, autorización, DB, eventos, claves, soporte, privacidad y recursos compartidos conforme ADR-06."
---

# ADR-06: aislamiento entre entidades del core

## Propósito y lectura

Convertir la frontera de celda en diseño, cambios autorizados y evidencia verificable. Aplicar este skill cuando se agregue una entidad, cambie la topología compartida, se implementen permisos/exportaciones o se investigue acceso cruzado e interferencia de carga. Una celda contiene inicialmente una entidad jurídica; compartir producto de software permite reutilización sin forks, sin mezclar contabilidad ni fondos.

Leer [ADR-06](../../../docs/adr/ADR-06-aislamiento-por-celda.md), [arquitectura](../../../docs/achitecture.md#seguridad), secciones 10–12, 15 y 18, y [skill regulatorio](../core-bancario-argentina/SKILL.md). Para controles usar su [catálogo](../core-bancario-argentina/references/controles.md), especialmente CTL-08 a CTL-14, CTL-16 y CTL-17. Consultar [mercado](../../../docs/market_analysis.md), secciones 6, 8 y 12, para ponderar repetibilidad, TCO y portabilidad. La base es **15/10/2026**: fuente y aplicabilidad actuales se verifican al decidir producción; no atribuir una certificación a este diseño.

## Entrada mínima

Reconstruir del pedido y repositorio: modo `DISEÑAR`, `IMPLEMENTAR` o `REVISAR`; entidades/roles/productos y custodios; fronteras existentes; identidades; DB/broker/archivo/KMS; recursos compartidos; países de ejecución, control y soporte; alcance del cambio y presupuesto operativo. Distinguir hechos, supuestos y pendientes. Si falta un dato material, avanzar con las partes independientes y señalar qué decisión queda condicionada; no inventar una licencia ni detener trabajo reversible ya autorizado.

## Procedimiento adaptable

1. **Mapear la frontera.** Vincular `deployment_cell → legal_entity → regulated_role → product_version`. Enumerar flujos por API, DB, caché, workers, jobs, topics, DLQ, documentos, respaldos, trazas, soporte y exportaciones. Identificar dependencias comunes que puedan comprometer varias celdas: IAM, KMS, DNS, red, administradores y plano de control. Separar fondos operativos, fondos de clientes y cuentas de custodia según el perfil.
2. **Trazar identidad a objeto.** Derivar entidad autorizada de principal y routing confiables; verificar permisos por cuenta/objeto/acción. Diseñar roles mínimos, expiración, revocación y elevación temporal registrada. Una cabecera o parámetro `entity_id` no concede acceso. Incluir respuestas previas de idempotencia, consultas históricas, callbacks y descargas; limpiar/probar el contexto de conexiones reutilizadas y trabajos encolados.
3. **Materializar la separación.** Mantener inicialmente base y credenciales por celda. Definir ACL, roles SQL, claves y políticas KMS, namespaces de objetos, permisos de broker/consumidores y destinos de copia. Añadir RLS cuando proceda, sin presentarla como sustitución automática. Delimitar acceso a PII y ROS: investigar AML no habilita al CRM, soporte ordinario ni analítica general. Auditoría de acceso/entrega sensible debe ser durable antes de completar la entrega.
4. **Regular datos y recursos.** Registrar por flujo finalidad, país, subencargado, acceso remoto, retención y disposición/hold. Considerar backups, observabilidad y soporte exterior aunque la base primaria esté en Argentina. Para EF cotejar originales y responsables locales; aplicar BCRA-T26–34 y DATA-04–06 según alcance. Definir cuotas/pools y capacidad reservada por celda; observar SLO y saturación individual. Delimitar CDE sólo si se activan tarjetas y evaluar sus dependencias; tokenizar no elimina automáticamente PCI.
5. **Ejecutar según el modo.** En `DISEÑAR`, producir topología, matriz de acceso/datos/recursos, amenazas, costos y criterios medibles. En `IMPLEMENTAR`, inspeccionar código/IaC/configuración y cambiar el alcance autorizado, incluyendo políticas y contratos de interfaz; verificar compatibilidad y preparar recuperación. En `REVISAR`, contrastar configuración efectiva y rutas reales con el ADR y reportar escenarios explotables o fallos de aislamiento con evidencia. No sustituir implementación solicitada por una opinión. Si cambia la decisión propuesta, registrar alternativa y consecuencias en el ADR.
6. **Verificar y cerrar brechas.** Elegir ensayos proporcionales al cambio con datos sintéticos. Registrar versiones, escenario, resultado esperado/observado y responsable. Mantener separado «configurado» de «verificado». Las aprobaciones institucionales, contratos y avisos dependen de roles reales y exigibilidad; no crear pedidos de permiso ficticios para análisis o correcciones autorizadas.

## Invariantes y fallos de aceptación

- Ninguna celda puede leer, modificar, consumir, descifrar o exportar otra usando su identidad ordinaria. Probar API, DB, broker, objetos, soporte y KMS, tanto lectura como escritura y respuestas idempotentes.
- Revocación y cambio de roles no conservan accesos sensibles mediante cachés, sesiones, workers o conexiones reutilizadas. Privilegios temporales expiran y dejan evidencia.
- Una carga intensa no agota recursos de otra entidad por encima del presupuesto definido. Medir CPU, I/O, conexiones, backlog y capacidad de dependencias compartidas; no prometer aislamiento sólo con namespaces.
- Restauración, exportación y salida mantienen entidad, claves, reglas e historia sin contaminar otras celdas. No se mezclan libros ni se compensa una diferencia entre sociedades.
- PII/ROS no aparecen en trazas, soporte o reportes generales. Retención y derechos conservan evidencia exigible sin retención infinita indiscriminada.

## Salida y estado de evidencia

Entregar cambios/diseño, matriz `frontera | entidad/principal | recurso/acción | control | prueba | evidencia | estado`, riesgos comunes, impacto en costo/latencia, brechas y siguiente acción con responsable cuando conste. Usar estados `propuesto`, `sin evaluar`, `parcial`, `implementado sin evidencia` o `verificado` según lo observado; nunca convertir ausencia de prueba en conformidad. Vincular archivos, configuración y resultados reproducibles, evitando secretos/datos personales. El ADR continúa propuesto hasta una decisión institucional documentada; ejecutar un ensayo no lo acepta automáticamente.
