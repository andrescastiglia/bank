---
name: adr-07-stack-gestionado
description: "Usar al seleccionar, implementar o revisar el stack Go/PostgreSQL/Kafka, servicios gestionados, contenedores, IAM/KMS y observabilidad del core; evalúa soporte, garantías reales, capacidad, TCO y portabilidad."
---

# ADR-07: plataforma acotada y operable

## Propósito y entrada mínima

Aplicar el [ADR-07](../../../docs/adr/ADR-07-stack-gestionado.md) a decisiones de plataforma, cambios de infraestructura/código y revisiones de proveedores. Ejecutar el tipo de trabajo solicitado y producir evidencia verificable. La base es del **15/10/2026**, con estado **Propuesto**; crear archivos o elegir un servicio no demuestra aprobación, operación ni cumplimiento.

Identificar perfil funcional y entidad, alcance del cambio, stack/versions actuales, experiencia del equipo, ubicaciones y terceros, volúmenes, latencia, disponibilidad, presupuestos y contratos disponibles. Obtener datos existentes antes de preguntar. Con información faltante, avanzar en diseño, implementación reversible o análisis con supuestos explícitos; señalar las dependencias que impiden afirmar aceptación. No introducir autorizaciones genéricas para tareas ya solicitadas.

Leer el ADR y [arquitectura §§3, 7–11, 14–15 y 18](../../../docs/achitecture.md), [mercado §§6, 8 y 12](../../../docs/market_analysis.md), [cumplimiento](../../../docs/compliant.md) y [skill regulatorio](../core-bancario-argentina/SKILL.md). Usar ADR-02 para SQL, ADR-03 para eventos, ADR-04 para continuidad y ADR-06 para aislamiento; este skill no reemplaza sus invariantes. Revalidar fuentes oficiales y edición cuando una obligación actual dependa de ello.

## Procedimiento aplicable

1. **Traducir negocio a requisitos.** Elegir el perfil inicial acotado y medir sus dependencias. Separar promedio, pico, hot accounts, cierres, carga inicial y crecimiento. Mapear garantías financieras y temporales antes de comparar herramientas. No convertir métricas nacionales de pagos ni transacciones facturables en comandos técnicos por segundo.
2. **Congelar una línea base soportada.** Usar Go para módulos con interfaces, contratos HTTP/JSON/OpenAPI y tipos monetarios exactos; fijar compilador y librerías. Tomar PostgreSQL 18 soportado como base propuesta y verificar parches, extensiones, política de soporte y compatibilidad efectiva. Si se sustituye, documentar motivo y probar invariantes; no adoptar `latest`, una RC o motor diferente por asumir equivalencia. Registrar versión/digest, licencia, SBOM, propietario y actualización.
3. **Verificar mensajería y procesos.** Kafka gestionado requiere tres zonas independientes, RF=3, `acks=all`, `min.insync.replicas=2`, productor idempotente y sin elección de líder no sincronizado. Contrastar configuración ofrecida con efectiva. Mantener outbox transaccional, inbox y unicidad del efecto; entrega al menos una vez, esquemas compatibles y CloudEvents con datos mínimos. Kafka no garantiza atomicidad con SQL/rieles. Usar jobs/checkpoints inicialmente; añadir motores sólo por necesidad comprobada.
4. **Configurar ejecución y seguridad.** Preferir contenedores gestionados con cuotas, scheduling, health checks y pérdida de zona tolerada. Kubernetes sólo si aporta valor y el equipo puede operarlo. Consumir IAM/SSO, gestor de secretos y KMS recuperables; implementar autorización por entidad/objeto/acción. No crear criptografía propia ni almacenar claves junto a los datos que protegen. Instrumentar con OpenTelemetry sin secretos, factores ni PII innecesaria; definir retención/acceso de métricas, logs y trazas.
5. **Evaluar contratación y salida.** Mapear servicio, región/ciudad/país, control, soporte y subcontratación, incluyendo backups y telemetría. Revisar responsabilidad compartida, incidentes, acceso de entidad/supervisor, avisos aplicables y exportación/borrado. Distinguir obligación legal, control técnico y requisito contractual. Un ISO/SOC sólo cubre su alcance/período y controles examinados; identificar brechas del usuario. Vincular BCRA-T26–T34 y CTL-16, sin asumir nube universalmente autorizada.
6. **Comparar TCO y capacidad.** Contabilizar por celda réplicas, bus, almacenamiento/WAL, retención, egress, claves, observabilidad, ambientes, guardia, pruebas, integración y salida. Separar cotización, supuesto y consumo medido; evaluar mínimos y pico. Probar carga con jobs y réplicas activas, contención, failover y amplificación por comando. Servicios gestionados trasladan tareas, no eliminan responsabilidad ni todo costo operativo.
7. **Actuar y verificar.** Al implementar, cambiar código/configuración/infraestructura autorizados con compatibilidad y reversión documentadas; ejecutar checks adecuados. Al revisar, mostrar evidencia efectiva y corrección concreta. Al diseñar, entregar componentes, contratos, límites y plan de aceptación. No cerrar con una mera propuesta cuando se pidió un cambio realizable.

## Invariantes y aceptación

- SQL conserva autoridad monetaria; cachés, proyecciones y Kafka no autorizan gasto.
- Outbox/inbox siguen siendo necesarias aunque el proveedor anuncie transacciones o “exactly once”.
- Ninguna certificación del proveedor acredita automáticamente el core o la entidad.
- Versiones, garantías, localización y costos quedan trazables; datos y evidencia tienen salida ensayada.

Ensayar duplicados, caída entre commits/publicación, pérdida de consumidor, dependencia indisponible y restauración/exportación. Rechazar configuraciones que pierdan efecto financiero, oculten atraso o rompan aislamiento. Metas iniciales del perfil hipotético: 250.000 cuentas/contratos; 100 comandos/s sostenidos y 500/s pico; hasta 1.000 lecturas/s; transferencia p95/p99 ≤100/200 ms; saldo ≤50/100 ms; outbox ordinaria p99 ≤5 s. No presentarlas como mediciones. Registrar duración, mezcla, hardware/servicio, versiones y saturación; un resultado fuera de meta es una brecha, no un benchmark aprobado.

## Salida

Entregar decisión o cambio, inventario versionado, configuración efectiva, comparación de alternativas/TCO, contratos de datos, pruebas, portabilidad y brechas priorizadas. Vincular archivos y evidencias a CTL-09–CTL-17 y BCRA/STD aplicables. Distinguir **verificado**, **brecha**, **no evaluado** y **no aplicable con fundamento**. Identificar revisión por soporte, volumen, costo, proveedor o región; no cambiar a Aceptado sin evidencia de una decisión real.
