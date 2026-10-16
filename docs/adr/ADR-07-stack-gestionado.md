# ADR-07: stack acotado y servicios de plataforma gestionados

**Estado:** Propuesto. **Fecha y base documental:** 15/10/2026, Argentina. **Alcance:** implementación y operación de las celdas del core. Las tecnologías nombradas son una línea base evaluable; no acreditan despliegue, homologación ni rendimiento observado.

## Contexto

La [arquitectura, secciones 3, 7–11 y 14–15](../achitecture.md) requiere módulos consistentes, asincronía durable, baja latencia y operación sostenible. El [análisis comercial, secciones 6, 8 y 12](../market_analysis.md) prioriza un producto argentino acotado, reutilización entre clientes y costo total que incluya soporte, integración, migración y salida. Incorporar motores por tendencia aumenta superficie de fallos, especialización y costos mínimos. Comprar operación de infraestructura no delega la responsabilidad financiera o regulatoria de la entidad.

## Decisión propuesta

Usar **Go** para dominio y servicios, con interfaces modulares, HTTP/JSON y OpenAPI. Fijar versiones por soporte, seguridad y capacidad del equipo. Representar dinero con tipos exactos; el lenguaje no garantiza precisión por sí solo. Adoptar **PostgreSQL 18 soportado por el proveedor elegido** como línea base financiera, con pools limitados y migraciones versionadas. Revalidar edición, parches, extensiones, soporte y compatibilidad al implementar; no convertir “la última versión” o una imagen `latest` en política.

Preferir PostgreSQL, Kafka y almacenamiento de objetos gestionados cuando jurisdicción, contrato y garantías técnicas lo permitan. Kafka distribuye hechos con esquemas versionados y envelope CloudEvents; tres zonas independientes, replicación 3, `acks=all`, `min.insync.replicas=2`, productor idempotente y elección de líder no sincronizado deshabilitada. Preservar **outbox/inbox y entrega al menos una vez**: las transacciones Kafka no hacen atómico un commit PostgreSQL ni un pago externo. El broker no sustituye al ledger o al archivo legal.

Comenzar con workers, tablas de jobs, leases y checkpoints para procesos durables. Añadir orquestador, buscador, caché o almacén analítico sólo ante necesidad medida. Una caché nunca autoriza fondos. Separar reportes y proyecciones del writer. Ejecutar contenedores en una plataforma gestionada multizona con cuotas, salud y capacidad remanente; Kubernetes es una opción condicionada a capacidad operativa del equipo, no un requisito del producto.

Consumir IAM/SSO, secretos y KMS especializados y recuperables. Implementar autorización de negocio propia sobre esas identidades; no construir identidad ni criptografía caseras. Instrumentar con OpenTelemetry, cuidando minimización, permisos y retención. Cada dependencia mantiene versión exacta, licencia, SBOM, responsable, parcheo y procedimiento de salida. Verificar responsabilidad compartida, ubicaciones, subcontratistas, acceso supervisor y custodia aplicable también para logs, backups y soporte.

## Alternativas y consecuencias

| Alternativa | Evaluación y contrapartida |
|---|---|
| Autogestionar todos los servicios | Válido si existen capacidad, evidencia y TCO favorable; aumenta guardia, parcheo, recuperación y carga del equipo inicial. |
| Sustituir Kafka por cola más simple | Puede bajar costo inicial; requiere revisar ADR-03 y demostrar durabilidad, reentrega, orden, replay y contratos necesarios. |
| Introducir múltiples motores y microservicios desde el inicio | Mayor libertad especializada; aumenta coordinación, consistencia y costo sin demanda medida. |

La selección reduce cantidad de motores operados y preserva interfaces exportables. A cambio, crea dependencia contractual y costos mínimos de plataforma. Calcular por celda base/réplicas, bus, retención, WAL, egress, observabilidad, claves, entornos, guardia, ensayos y salida. Un certificado ISO/SOC aporta evidencia de alcance concreto, no cumplimiento automático del servicio.

## Aceptación y revisión

Verificar configuración efectiva, ciclo de soporte, controles de acceso y recuperación; demostrar outbox/inbox ante duplicado y caída, y exportación/restauración fuera del servicio. Ensayar el perfil hipotético: 250.000 cuentas/contratos, 100 comandos monetarios/s sostenidos, pico de 500/s y hasta 1.000 lecturas/s. Metas: transferencia interna p95/p99 ≤100/200 ms, saldo consistente ≤50/100 ms y antigüedad ordinaria de outbox p99 ≤5 s. Son objetivos, no benchmarks de Go/PostgreSQL/Kafka. Medir contención, amplificación, carga de jobs, capacidad remanente y costo; no omitir dependencias.

Revisar ante fin de soporte, cambio contractual/regional, TCO insostenible, capacidad insuficiente o requisito no cubierto. Depende de ADR-01–ADR-04 y ADR-06. Trazabilidad: [compliant.md](../compliant.md), BCRA-T05–T07, T11–T19, T25–T34; STD01–STD12, STD14 y STD25–STD32; CTL-09–CTL-17. Usar el [skill ADR-07](../../.agents/skills/adr-07-stack-gestionado/SKILL.md).

## NFR relacionados

[NFR-02](../nfr/NFR-02-disponibilidad-recuperacion.md), [NFR-03](../nfr/NFR-03-latencia-capacidad.md), [NFR-04](../nfr/NFR-04-asincronia-durable.md), [NFR-05](../nfr/NFR-05-seguridad-accesos.md), [NFR-08](../nfr/NFR-08-interoperabilidad-portabilidad.md), [NFR-09](../nfr/NFR-09-mantenibilidad-configuracion.md), [NFR-12](../nfr/NFR-12-operabilidad-costos.md). Son cualidades y restricciones a verificar; la elección de este mecanismo no demuestra por sí sola su satisfacción.
