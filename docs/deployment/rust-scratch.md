# Contrato de construcción y ejecución: Rust y scratch

**Decisión del mantenedor:** 16/10/2026. **Alcance:** imágenes propias del API, workers, jobs e importador del core, destinadas a Kubernetes o plataforma equivalente. **Estado de implementación:** pendiente; el repositorio documenta el producto y todavía no contiene un workspace Cargo, un binario bancario o una imagen de aplicación construida. Este contrato concreta [ADR-07](../adr/ADR-07-stack-gestionado.md) y [arquitectura §14](../achitecture.md).

En este proyecto, *distroless* significa una **etapa final `FROM scratch`**, con ejecutable y recursos de runtime explícitos. La elección de lenguaje e imagen fue indicada por el mantenedor; los componentes de plataforma de terceros se seleccionan y evalúan en su propio alcance. No se presupone que PostgreSQL, Kafka, un proxy o un agente de observabilidad puedan sustituirse por el binario del core.

## 1. Rust como línea base

- Usar Rust estable y fijar la versión exacta del compilador, componentes y targets en `rust-toolchain.toml`; versionar `Cargo.lock` y features de cada artefacto. No usar toolchain flotante en una release.
- Organizar dominio, persistencia, adaptadores y procesos en módulos/crates con contratos explícitos. Elegir runtime asíncrono, framework HTTP, clientes PostgreSQL/Kafka/TLS y telemetría por soporte, compatibilidad, licencia y pruebas. Tokio y otros crates son candidatos a evaluar, no dependencias ya incorporadas por este documento.
- Dinero usa representación exacta, escala/unidad y redondeo explícitos, con overflow controlado. Ownership y tipos no prueban partida doble, idempotencia o corrección fiscal. Mantener los oráculos e invariantes de ADR-02/03.
- Limitar tareas concurrentes, pools, colas y trabajo CPU/I/O bloqueante; no bloquear el executor ni asumir que cancelar una tarea revierte una transacción o un efecto externo. Los jobs aceptados tienen estado/checkpoint durable.
- Revisar y justificar `unsafe`/FFI; las dependencias también pueden contenerlos. Las fronteras nativas requieren inventario y pruebas. No afirmar ausencia de `unsafe` en todo el árbol por prohibirlo sólo en un módulo propio.

## 2. Construcción por arquitectura

1. **Builder separado.** Fijar imagen de compilación por digest, toolchain, linker, librerías nativas, CA públicas, fuentes y lockfile. No incorporar tokens en instrucciones, argumentos, capas o cachés publicadas; usar mecanismos de secretos de build cuando sean necesarios.
2. **Target y enlace.** Compilar para la arquitectura Linux elegida, preferentemente `x86_64-unknown-linux-musl` o `aarch64-unknown-linux-musl` cuando su soporte efectivo esté verificado. Un target GNU o una compilación Rust ordinaria no garantiza enlace estático. Cross-compilation requiere linker y dependencias nativas correctos; declarar un target no los instala.
3. **Dependencias nativas.** Si un cliente Kafka/TLS u otro crate enlaza C/C++, comprobar el enlace estático de esas bibliotecas y sus dependencias transitivas, licencias y soporte. Si no cumple el contrato, resolver la selección/configuración o separar la integración antes de publicar una imagen propia; no ocultar un cargador dinámico faltante con una copia parcial de librerías.
4. **Artefacto.** Ejecutar build release con lockfile (`cargo build --locked --release --target <target> --bin <binario>`) en el workspace real. Registrar flags, target, features y versión del código. No existe todavía un nombre de binario de producto aprobado en este repositorio.
5. **Comprobar el ELF.** Fuera de la imagen final, inspeccionar el ejecutable con herramientas como `readelf`: arquitectura correcta, ausencia de segmento `PT_INTERP` y de entradas `DT_NEEDED`. Un static PIE puede tener otros segmentos dinámicos; el criterio es no depender de un intérprete o bibliotecas compartidas. Verificar también carga de plugins/datos en runtime: inspeccionar ELF no los detecta por sí solo.
6. **Publicar por digest.** Construir la imagen scratch por arquitectura, inventariar payload y producir SBOM/procedencia/firma. Un índice multiarch sólo incluye plataformas compiladas y probadas; no etiquetar un binario amd64 como arm64. Promover el mismo digest probado entre entornos.

El runtime final no contiene compilador, Cargo, shell, gestor de paquetes, clientes administrativos o herramientas de depuración. Las herramientas de inspección se ejecutan en builder/CI o en un entorno diagnóstico autorizado separado. No se necesita añadir shell para implementar probes o terminar el proceso.

## 3. Payload y dependencias de runtime

| Recurso | Contrato verificable |
|---|---|
| Ejecutable | Rust Linux estático por arquitectura, con entrypoint directo al proceso; sin script de shell ni supervisor que oculte señales |
| Confianza TLS | Bundle de CA públicas versionado dentro de la imagen o trust store montado por el mecanismo autorizado. El cliente TLS debe cargarlo efectivamente, validar cadena/nombre y respetar rotación; no desactivar verificación para que funcione scratch |
| Zonas horarias | Instantes en UTC y calendarios de negocio con IANA explícita. Incluir tzdata mínima versionada, incorporarla mediante la biblioteca elegida o montarla; probar conversión y cierres en `America/Argentina/Buenos_Aires`. El archivo de zona no proporciona por sí solo el calendario de feriados bancarios |
| DNS y red | Probar resolución de servicios y destinos autorizados con la configuración de red del pod y el resolver usado por el binario; no depender de utilitarios de shell o de bibliotecas ausentes |
| Usuario | `USER` numérico no root, por ejemplo `65532:65532`; no requiere `/etc/passwd` si la aplicación/bibliotecas no lo necesitan. Verificar permisos de archivos y volúmenes reales |
| Escrituras | Raíz de sólo lectura; logs por stdout/stderr. Cuando haga falta un directorio temporal o spool, declararlo como volumen con límites, permisos y política de conservación. Un `emptyDir` no sustituye estado durable aceptado |
| Secretos | Credenciales, claves privadas y certificados cliente por mecanismo externo autorizado, con mínimo acceso/rotación; no copiarlos al build context o imagen. CA pública y secreto TLS tienen tratamientos diferentes |

Este **fragmento de etapa final** muestra el contrato; requiere una etapa `build` real que produzca y verifique los archivos indicados. No constituye un Dockerfile de aplicación ejecutado o desplegado:

```dockerfile
FROM scratch AS runtime
COPY --from=build --chown=65532:65532 /out/core /core
COPY --from=build /out/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
USER 65532:65532
ENTRYPOINT ["/core"]
```

`/out/core` es un nombre ilustrativo. El ejemplo usa CA públicas copiadas; el diseño concreto debe elegir bundle, trust store montado o raíces incorporadas según su cliente TLS y contrato. Copiar un bundle o definir una variable como `SSL_CERT_FILE` no garantiza que un cliente Rust lo utilice: comprobar la configuración efectiva. Añadir los datos de zona si la biblioteca no los incorpora. Un `COPY` desde builder no debe arrastrar su root filesystem, archivos de credenciales o utilidades.

## 4. Ejecución en Kubernetes

Definir requests/limits, cuotas por celda, política de red, disponibilidad multizona y presupuesto de terminación según los NFR y el BIA. El contexto de seguridad de los contenedores propios debe incluir el equivalente de:

```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 65532
  runAsGroup: 65532
  readOnlyRootFilesystem: true
  allowPrivilegeEscalation: false
  capabilities:
    drop: ["ALL"]
  seccompProfile:
    type: RuntimeDefault
```

Este fragmento corresponde al contenedor, no a todo el manifiesto de un servicio. Ajustar permisos de volúmenes sin conceder root o capabilities por comodidad. Usar puertos no privilegiados. Configurar credenciales y acceso al API de Kubernetes sólo para cargas que lo necesiten y con facultades mínimas; el montaje automático del token de ServiceAccount se deshabilita cuando no corresponda.

Probes HTTP, TCP o gRPC nativas de Kubernetes, según el servicio y soporte del cluster, evitan `exec` con `sh`/`curl`. Readiness indica admisión de trabajo; liveness no debe provocar reinicios en cascada por una dependencia temporalmente indisponible. StartupProbe, si corresponde, diferencia arranque lento de proceso bloqueado.

Al recibir SIGTERM, el proceso inicia drenaje, deja de admitir nuevo trabajo y hace observable la pérdida de readiness; termina o revierte transacciones locales dentro del presupuesto, persiste checkpoints y estados externos ambiguos y detiene workers ordenadamente. No confirma éxito por abortar un future ni vuelve a enviar un pago sólo por terminar el pod. La política de terminación debe contemplar el tráfico en vuelo y `terminationGracePeriodSeconds`; no depender de un hook `preStop` de shell. Si llega SIGKILL, la recuperación por outbox/inbox, leases y evidencia durable conserva las invariantes. Ensayar caída abrupta además del cierre limpio.

## 5. Evidencia de aceptación pendiente

| Escenario | Oráculo / resultado necesario | Trazabilidad |
|---|---|---|
| Build/imagen por arquitectura | Toolchain/lockfile/features/builder identificados; etapa final scratch, payload permitido, ELF sin intérprete/dependencias compartidas; digest e índice coherentes | FR-OPS-025/026, NFR-09-C01, ADR-07 |
| Arranque endurecido | API/worker arranca como usuario no root con raíz de sólo lectura y sin capabilities/escalamiento; escrituras sólo en volúmenes declarados; probes sin shell | FR-OPS-026, NFR-05-C01, ADR-06/07 |
| TLS, DNS y calendarios | Conecta a dependencias sintéticas/autorizadas con confianza válida, rechaza CA/nombre incorrectos, resuelve servicios y calcula fechas/cierres con zona/calendario versionados | NFR-05-C04, NFR-08-C01, CTL-06/10 |
| Terminación/fallo | SIGTERM y caída abrupta no pierden trabajo aceptado ni duplican efectos; estado ambiguo conserva su referencia, lease y reconciliación | NFR-01/04, FR-OPS-023, ADR-03/04 |
| Entrega y actualización | Promoción del digest probado, SBOM de crates y bibliotecas nativas/payload, licencias compatibles con GPL v2, revisión de avisos y reconstrucción por parche de código/CA/tzdata | FR-OPS-024/025/026, NFR-09-C01/C05, CTL-15 |
| Rendimiento | Ensayo del mismo perfil, durabilidad, seguridad y arquitectura real; percentiles/errores/costo medidos. Elegir Rust o reducir la imagen no demuestra el SLO | NFR-02/03/12, ADR-07 |

No hay pruebas de imagen o aplicación ejecutadas por escribir este contrato. Al existir implementación, `cargo fmt --check`, Clippy con el toolchain/features soportados, pruebas de dominio/contratos y revisión de dependencias/licencias formarán parte del pipeline de producto; los checks Python documentales siguen cumpliendo su función. Scratch reduce componentes disponibles, pero siguen existiendo vulnerabilidades en binario, crates, bibliotecas nativas, datos de confianza y kernel del host. No se declara una imagen «sin CVE» por carecer de una distribución.

## 6. Fuentes técnicas y mantenimiento

Referencias técnicas para la implementación: [targets Rust y plataformas](https://doc.rust-lang.org/rustc/platform-support.html), [Rust musl](https://doc.rust-lang.org/rustc/platform-support/x86_64-unknown-linux-musl.html), [configuración de toolchain](https://rust-lang.github.io/rustup/overrides.html#the-toolchain-file), [Cargo lockfile](https://doc.rust-lang.org/cargo/guide/cargo-toml-vs-cargo-lock.html), [Docker scratch](https://docs.docker.com/build/building/base-images/#create-a-minimal-base-image-using-scratch), [build multietapa](https://docs.docker.com/build/building/multi-stage/), [contexto de seguridad Kubernetes](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/), [probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) y [terminación de pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination).

Fijar versiones reales antes de compilar y revisar soporte, cambios de cliente y compatibilidad nativa; estas referencias no son una validación de versiones que aún no fueron seleccionadas. Mantener el [skill ADR-07](../../.agents/skills/adr-07-stack-gestionado/SKILL.md), NFR y catálogo funcional alineados cuando cambien los criterios.
