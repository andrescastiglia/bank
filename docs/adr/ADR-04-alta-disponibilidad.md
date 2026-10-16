# ADR-04: alta disponibilidad multizona y recuperación regional activa/pasiva

**Estado:** Propuesto. **Fecha y base documental:** 15/10/2026, Argentina. **Alcance:** cada celda financiera y sus dependencias. No registra una aprobación institucional, infraestructura desplegada ni recuperación ya demostrada.

## Contexto

La [arquitectura, secciones 10–12 y 15](../achitecture.md#disponibilidad) combina baja latencia, continuidad e integridad monetaria. El [análisis comercial, secciones 6, 8 y 9](../market_analysis.md) exige medir recuperación, costo total y salida: multiplicar componentes sin una operación sostenible no aporta una ventaja verificable. Replicar aplicaciones tampoco recupera identidad, claves, pagos en vuelo o evidencia. El BIA debe determinar tolerancias por servicio y entidad; las metas arquitectónicas no constituyen valores universales exigidos por BCRA.

## Decisión propuesta

Operar una región primaria con tres zonas o sitios realmente independientes, capacidad remanente para perder una zona y **un escritor PostgreSQL por celda**. Mantener `fsync=on`, `synchronous_commit=on` y standby síncrono en otro dominio, o garantías gestionadas equivalentes verificables. Confirmar éxito sólo después del commit durable bajo esa política. La promoción requiere réplica elegible que preserve commits reconocidos, quorum de control y fencing efectivo del escritor anterior. Sin standby elegible se suspenden las escrituras afectadas; no se degrada silenciosamente la durabilidad.

Mantener una región secundaria pasiva con replicación asíncrona. Su lag objetivo de ≤60 segundos ayuda a operar, pero **no garantiza RPO regional ≤60 segundos**: pueden faltar commits informados al cliente. El RPO regional observado corresponde al último WAL durable recuperado y a la evidencia independiente conciliable. Un requisito de RPO regional cero obliga a revisar esta decisión, con persistencia síncrona entre sitios adecuados y el costo de RTT, disponibilidad y operación correspondiente. No habilitar dos escritores regionales.

Incluir DNS, balanceadores, IAM, KMS, certificados, red, objetos, configuración, jobs, broker y monitoreo en la continuidad. Tres instancias dentro de un único datacenter no prueban tolerancia a pérdida de sitio. Mantener respaldos cifrados, recuperación puntual y copias protegidas e independientes; la réplica no sustituye una copia limpia.

El runbook debe aislar el primario anterior, determinar el punto autoritativo y reconciliar SQL, outbox, inbox, offsets, jobs y estados externos antes de reabrir. Un broker puede conservar eventos posteriores a la base restaurada; una inbox puede ser anterior al offset consumido. Aislar hechos huérfanos y reconstruir con identidades originales, sin replay indiscriminado de pagos históricos. Un lease local no impide por sí solo que un proceso antiguo vuelva a llamar a un riel.

## Alternativas y consecuencias

| Alternativa | Evaluación y contrapartida |
|---|---|
| Activo/activo regional sin consenso financiero | Rechazado: una partición permite escrituras incompatibles y doble gasto. |
| Persistencia síncrona entre regiones | Considerar si el negocio exige RPO regional cero; añade latencia, costo y decisiones de disponibilidad durante particiones. |
| Un solo sitio con backups | Menor costo inicial; no satisface la tolerancia propuesta ante pérdida del sitio y exige otro perfil explícito. |

La topología elegida reduce RTT monetario frente a consenso interregional, a cambio de pérdida regional potencial y un procedimiento de recuperación material. Financia capacidad ociosa, copias y ensayos; debe reflejarse en el costo por celda y contrato. Residencia, transferencia, subcontratación, acceso supervisor y custodia de originales aplicables alcanzan también al DR y sus claves.

## Aceptación y revisión

Ensayar partición, caída de writer/zona, pérdida regional, corrupción, pérdida de IAM/KMS y restauración con desfase DB/broker. Demostrar escritor único, conservación de commits locales reconocidos, conciliación monetaria y resolución de intentos externos ambiguos. Registrar carga, versión, topología, punto recuperado y tiempos. Metas iniciales: redistribución de proceso ≤30 s; failover local ≤120 s; DR regional ≤60 min; copia limpia del piloto ≤4 h; API local 99,95 % mensual. Son objetivos por validar; un ensayo de failover no prueba disponibilidad mensual.

Revisar ante cambios de BIA, región, proveedor, volumen, contrato, independencia de sitios o exigencia de RPO. Depende de ADR-02, ADR-03, ADR-06 y ADR-07. Trazabilidad: [compliant.md](../compliant.md), BCRA-T15–T19 y T26–T34; STD04, STD07–STD12 y STD32; CTL-04, CTL-05, CTL-10 y CTL-13–CTL-16. Aplicar el [skill ADR-04](../../.agents/skills/adr-04-alta-disponibilidad/SKILL.md).

## NFR relacionados

[NFR-02](../nfr/NFR-02-disponibilidad-recuperacion.md), [NFR-03](../nfr/NFR-03-latencia-capacidad.md), [NFR-06](../nfr/NFR-06-privacidad-residencia-retencion.md), [NFR-12](../nfr/NFR-12-operabilidad-costos.md). Son cualidades y restricciones a verificar; la elección de este mecanismo no demuestra por sí sola su satisfacción.
