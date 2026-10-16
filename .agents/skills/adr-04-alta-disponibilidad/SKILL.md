---
name: adr-04-alta-disponibilidad
description: "Usar al diseñar, implementar o revisar alta disponibilidad, replicación PostgreSQL, failover, respaldos y recuperación regional del core; incluye quorum, fencing, RTO/RPO y conciliación de base, eventos y pagos externos."
---

# ADR-04: continuidad con una autoridad financiera

## Propósito, alcance y entrada

Aplicar el [ADR-04](../../../docs/adr/ADR-04-alta-disponibilidad.md) y la [arquitectura](../../../docs/achitecture.md#disponibilidad) para producir un diseño, cambio implementado o revisión verificable, según el pedido. La base documental es del **15/10/2026** y la decisión está **Propuesta**. No atribuir aprobación, disponibilidad o ensayos a un sistema sin evidencia. Este skill trata continuidad; conservar la autoridad SQL, idempotencia y aislamiento definidos por los ADR relacionados.

Identificar celda/entidad, servicio y alcance solicitado; topología y dominios independientes; mecanismo gestionado o propio; versiones; carga, dependencias, sitios de datos/soporte; BIA, RTO/RPO, contratos y evidencia disponible. Obtener del contexto lo ya conocido. Si falta información, avanzar con supuestos y marcar qué decisión depende de ella; pedir sólo datos que cambian materialmente la solución. No detener análisis, documentación o correcciones reversibles por una aprobación imaginada.

Leer progresivamente el ADR, arquitectura §§10–12, 15, 18 y 19, [mercado §§6, 8 y 9](../../../docs/market_analysis.md), [cumplimiento](../../../docs/compliant.md) y el [skill regulatorio](../core-bancario-argentina/SKILL.md). Consultar su catálogo CTL-13–CTL-16 y las fuentes oficiales cuando una decisión actual de producción dependa de vigencia normativa. No convertir este documento en certificación jurídica.

## Procedimiento

1. **Delimitar fallos y objetivos.** Separar proceso, zona, región, corrupción, ransomware y pérdida de identidad/claves. Mapear operación crítica hasta rieles, DNS, red y terceros. Distinguir objetivo, compromiso contractual y resultado medido. El BIA aporta tolerancias; no inventar un RTO legal universal. Verificar independencia física y capacidad al perder una zona: tres procesos en un sitio no equivalen a tres sitios.
2. **Verificar persistencia local.** Inspeccionar configuración efectiva, no sólo plantillas: escritor único, `fsync`, `synchronous_commit`, standbys síncronos y política del proveedor. Explicar qué fallo cubre el commit reconocido. Elegir sólo un standby que conserve esos commits. Sin réplica elegible, mantener detenidas las escrituras afectadas; una opción de continuidad asíncrona constituye un cambio de decisión explícito.
3. **Diseñar o corregir promoción.** Comprobar quorum y fencing del primario anterior antes de enrutar escrituras al nuevo. Revisar partición de control y red, credenciales y procesos antiguos. Un timeout o lease vencido no demuestra aislamiento. En implementaciones, modificar infraestructura/configuración y runbooks dentro del alcance autorizado; acompañar la modificación con validación proporcional y reversión operativa.
4. **Separar recuperación regional.** Mantener el destino pasivo asíncrono. Registrar lag, WAL durable recuperado, operaciones reconocidas ausentes y fuentes independientes para reconciliarlas. Lag objetivo ≤60 s no es RPO garantizado. Si se exige RPO regional cero, proponer y documentar persistencia síncrona adecuada con RTT/costo medidos; no etiquetar la solución asíncrona como suficiente.
5. **Recuperar todo el sistema.** Inventariar copias y restaurar SQL, objetos, documentos, configuración, jobs, identidad y claves. Comparar outbox/inbox restauradas con retención y offsets del broker. Aislar eventos posteriores al punto autoritativo; reconstruir proyecciones y consultar referencias externas. No avanzar offsets arbitrariamente ni reenviar históricos para “alcanzar” al broker. Resolver cada intento potencialmente enviado según el riel; preservar identificadores originales.
6. **Cubrir contratos y residencia.** Trazar ubicación/control/soporte de DR, backups, observabilidad y KMS; verificar subcontratistas, acceso supervisor y salida. Relacionar evidencia con BCRA-T26–T34 y obligaciones de datos aplicables, con el responsable correspondiente. Distinguir notificación de autorización. Un certificado de nube no demuestra configuración ni continuidad del core.
7. **Ejecutar y registrar aceptación.** Preparar datos sintéticos y escenarios representativos. Cuando se solicita implementar, efectuar los cambios y ensayos autorizados disponibles; cuando se solicita revisar, entregar hallazgos reproducibles con correcciones concretas. No limitarse a recomendar otra revisión.

## Invariantes y criterios de fallo

- Nunca dos escritores financieros de una misma celda, ni reapertura sin aislar el anterior y conciliar.
- No desactivar persistencia síncrona, WAL o controles para mejorar un benchmark.
- Copias recuperables y protegidas frente al administrador productivo; replicar corrupción no constituye backup limpio.
- Ninguna restauración SQL implica por sí sola deshacer un efecto externo; reconciliar antes de actuar.
- Recuperar IAM/KMS sin exportar secretos o claves a una ubicación no autorizada.

Probar pérdida de writer/zona, partición, standby inelegible, región, copia corrupta y desfase de SQL/inbox/broker; incluir intento externo ambiguo. Fallar aceptación si hay commits locales reconocidos perdidos bajo el modelo declarado, dos primarios, doble efecto, diferencia contable inexplicada o dependencia crítica irrecuperable. Las metas iniciales son ≤30 s proceso, ≤120 s failover local, ≤60 min DR y ≤4 h copia limpia del piloto; medirlas bajo carga declarada. Verificar por separado el SLO mensual propuesto de 99,95 %.

## Salida y evidencia

Entregar topología y configuración/versiones, cambios realizados, runbook, escenarios, RTO/RPO observados, puntos WAL/offset relevantes, conciliación y costos por celda. Vincular cada hallazgo a archivo/configuración, prueba o contrato y CTL/BCRA/STD aplicable. Marcar **verificado**, **brecha**, **no evaluado** o **no aplicable con fundamento**; una meta sin ensayo queda no evaluada. Registrar dependencias y condiciones para revisar el ADR, sin presentar su estado como Aceptado por haber creado documentos.
