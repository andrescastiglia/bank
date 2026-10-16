# ADR-07: stack acotado y servicios de plataforma gestionados

**Estado:** Propuesto. **Fecha y base documental:** 15/10/2026, Argentina. **Alcance:** implementación y operación de las celdas del core. Las tecnologías nombradas son una línea base evaluable; no acreditan despliegue, homologación ni rendimiento observado.

**Revisión 16/10/2026:** el mantenedor decidió usar Rust y runtime `FROM scratch` para imágenes propias. Esta elección de lenguaje/empaquetado queda fijada por su instrucción; el resto del ADR y la verificación operativa conservan su estado propuesto/sin evaluar.

## Contexto

La [arquitectura, secciones 3, 7–11 y 14–15](../achitecture.md) requiere módulos consistentes, asincronía durable, baja latencia y operación sostenible. El [análisis comercial, secciones 6, 8 y 12](../market_analysis.md) prioriza un producto argentino acotado, reutilización entre clientes y costo total que incluya soporte, integración, migración y salida. Incorporar motores por tendencia aumenta superficie de fallos, especialización y costos mínimos. Comprar operación de infraestructura no delega la responsabilidad financiera o regulatoria de la entidad.

## Decisión propuesta

Usar **Rust estable** para dominio y servicios, con módulos/crates e interfaces explícitas, HTTP/JSON y OpenAPI. Fijar toolchain, `Cargo.lock`, features y targets; elegir runtime asíncrono, clientes y crates por soporte, licencia y pruebas. Representar dinero con tipos exactos y controlar overflow/redondeos; la seguridad de memoria no demuestra precisión financiera, ausencia de deadlocks o atomicidad con terceros. Mantener trabajo bloqueante fuera del executor y concurrencia/pools acotados. Adoptar **PostgreSQL 18 soportado por el proveedor elegido** como línea base financiera, con pools limitados y migraciones versionadas. Revalidar edición, parches, extensiones, soporte y compatibilidad al implementar; no convertir “la última versión” o una imagen `latest` en política.

Preferir PostgreSQL, Kafka y almacenamiento de objetos gestionados cuando jurisdicción, contrato y garantías técnicas lo permitan. Kafka distribuye hechos con esquemas versionados y envelope CloudEvents; tres zonas independientes, replicación 3, `acks=all`, `min.insync.replicas=2`, productor idempotente y elección de líder no sincronizado deshabilitada. Preservar **outbox/inbox y entrega al menos una vez**: las transacciones Kafka no hacen atómico un commit PostgreSQL ni un pago externo. El broker no sustituye al ledger o al archivo legal.

Comenzar con workers, tablas de jobs, leases y checkpoints para procesos durables. Añadir orquestador, buscador, caché o almacén analítico sólo ante necesidad medida. Una caché nunca autoriza fondos. Separar reportes y proyecciones del writer. Ejecutar contenedores en una plataforma gestionada multizona con cuotas, salud y capacidad remanente; Kubernetes es una opción condicionada a capacidad operativa del equipo, no un requisito del producto.

Construir las imágenes propias del API, workers y jobs mediante etapas separadas de compilación y runtime, con **etapa final `FROM scratch`**. Usar binarios Rust Linux con enlace estático verificado para cada arquitectura, preferentemente musl; auditar crates con FFI y bibliotecas nativas. El payload contiene sólo ejecutable y recursos explícitos de confianza TLS/zonas horarias requeridos. Ejecutar como UID/GID numéricos no root, filesystem raíz de sólo lectura, capabilities eliminadas y sin escalamiento de privilegios. Exponer probes compatibles sin shell y manejar SIGTERM con drenaje y checkpoints durables. Builder y compilador no pasan al runtime; no incorporar secretos ni herramientas de diagnóstico privilegiadas. Véase el [contrato de construcción y aceptación](../deployment/rust-scratch.md). La política de imágenes propias no implica recompilar servicios gestionados o imágenes de terceros como si fueran parte del binario del core.

Consumir IAM/SSO, secretos y KMS especializados y recuperables. Implementar autorización de negocio propia sobre esas identidades; no construir identidad ni criptografía caseras. Instrumentar con OpenTelemetry, cuidando minimización, permisos y retención. Cada dependencia mantiene versión exacta, licencia, SBOM, responsable, parcheo y procedimiento de salida. Verificar responsabilidad compartida, ubicaciones, subcontratistas, acceso supervisor y custodia aplicable también para logs, backups y soporte.

## Alternativas y consecuencias

| Alternativa | Evaluación y contrapartida |
|---|---|
| Mantener Go, según la propuesta original | Sustituido por decisión explícita del mantenedor el 16/10/2026. Se conserva este antecedente; no existe código bancario Go que se dé por migrado. |
| Rust con runtime que depende de una distribución y librerías dinámicas | Requiere más componentes de runtime y no satisface el contrato `FROM scratch`/binario estático elegido. Si una dependencia no puede cumplirlo, resolver su selección o aislamiento antes de publicar la imagen propia. |
| Autogestionar todos los servicios | Válido si existen capacidad, evidencia y TCO favorable; aumenta guardia, parcheo, recuperación y carga del equipo inicial. |
| Sustituir Kafka por cola más simple | Puede bajar costo inicial; requiere revisar ADR-03 y demostrar durabilidad, reentrega, orden, replay y contratos necesarios. |
| Introducir múltiples motores y microservicios desde el inicio | Mayor libertad especializada; aumenta coordinación, consistencia y costo sin demanda medida. |

La selección reduce cantidad de motores operados y preserva interfaces exportables. A cambio, crea dependencia contractual y costos mínimos de plataforma. Calcular por celda base/réplicas, bus, retención, WAL, egress, observabilidad, claves, entornos, guardia, ensayos y salida. Un certificado ISO/SOC aporta evidencia de alcance concreto, no cumplimiento automático del servicio.

## Aceptación y revisión

Verificar configuración efectiva, ciclo de soporte, controles de acceso y recuperación; demostrar outbox/inbox ante duplicado y caída, y exportación/restauración fuera del servicio. Cada imagen propia debe acreditar etapa final scratch, ausencia de intérprete ELF/dependencias compartidas, arranque no root con raíz de sólo lectura, TLS/DNS/calendarios, probes y SIGTERM usando su digest final. Ensayar el perfil hipotético: 250.000 cuentas/contratos, 100 comandos monetarios/s sostenidos, pico de 500/s y hasta 1.000 lecturas/s. Metas: transferencia interna p95/p99 ≤100/200 ms, saldo consistente ≤50/100 ms y antigüedad ordinaria de outbox p99 ≤5 s. Son objetivos, no benchmarks de Rust/PostgreSQL/Kafka. Medir contención, amplificación, carga de jobs, capacidad remanente y costo; no omitir dependencias.

Revisar ante fin de soporte, cambio contractual/regional, TCO insostenible, capacidad insuficiente o requisito no cubierto. Depende de ADR-01–ADR-04 y ADR-06. Trazabilidad: [compliant.md](../compliant.md), BCRA-T05–T07, T11–T19, T25–T34; STD01–STD12, STD14 y STD25–STD32; CTL-09–CTL-17. Usar el [skill ADR-07](../../.agents/skills/adr-07-stack-gestionado/SKILL.md).

## NFR relacionados

[NFR-02](../nfr/NFR-02-disponibilidad-recuperacion.md), [NFR-03](../nfr/NFR-03-latencia-capacidad.md), [NFR-04](../nfr/NFR-04-asincronia-durable.md), [NFR-05](../nfr/NFR-05-seguridad-accesos.md), [NFR-08](../nfr/NFR-08-interoperabilidad-portabilidad.md), [NFR-09](../nfr/NFR-09-mantenibilidad-configuracion.md), [NFR-12](../nfr/NFR-12-operabilidad-costos.md). Son cualidades y restricciones a verificar; la elección de este mecanismo no demuestra por sí sola su satisfacción.
