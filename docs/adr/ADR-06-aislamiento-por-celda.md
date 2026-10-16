# ADR-06: aislamiento por celda y entidad jurídica

**Estado:** Propuesto, pendiente de aceptación institucional y validación técnica. **Línea base:** 15/10/2026. **Alcance:** diseño; no acredita controles implementados ni cumplimiento. **Skill asociado:** [adr-06-aislamiento-por-celda](../../.agents/skills/adr-06-aislamiento-por-celda/SKILL.md).

## Contexto

La [arquitectura](../achitecture.md#seguridad) ofrece un producto compartido entre clientes y perfiles regulatorios distintos. El [análisis comercial](../market_analysis.md) prioriza una cartera acotada, repetibilidad sin forks, costos operativos transparentes y salida demostrable. Una marca puede representar banco, PSP y prestamista: compartir marca o software no autoriza mezclar fondos, contratos, documentación ni reportes.

Una fuga por API, evento, exportación o soporte compromete secreto, privacidad y confianza comercial. La saturación de recursos también puede detener a otra entidad aunque sus datos estén separados. No existen todavía entidades, países, proveedores o volúmenes contratados; no se presupone una habilitación general para nube exterior.

## Decisión propuesta

Una **celda aloja inicialmente una entidad jurídica y su frontera contable**, con base y credenciales dedicadas. El código y la automatización se reutilizan; el plano de control conserva sólo los metadatos operativos necesarios. El inventario vincula celda, razón social, rol regulado, producto habilitado, custodio, países y responsables.

La frontera comprende DB, API, cachés, jobs, eventos/topics, DLQ, archivos, respaldos, exportaciones, observabilidad, soporte y KMS. Las claves y sus políticas quedan separadas por celda; cifrar todo con un administrador global irrestricto no demuestra aislamiento. Identidades de corta duración y permisos mínimos limitan tanto personas como servicios. La entidad autorizada se deriva de identidad y routing confiables; un `entity_id` suministrado por el cliente no amplía facultades. Se comprueban cuenta, objeto y acción también en reintentos y respuestas idempotentes.

No se confía exclusivamente en filtros de aplicación. ACL, roles de base, políticas del broker, objetos y claves refuerzan la frontera; RLS puede añadir defensa sin sustituir la separación inicial. Consultas y descargas sensibles dejan evidencia durable antes de entregar contenido. Soporte usa privilegios temporales y trazables; PII y casos ROS tienen permisos separados, sin exposición ordinaria a soporte o analítica.

Cada celda tiene cuotas de CPU, memoria, conexiones, almacenamiento, jobs y mensajería; los caminos financieros reservan capacidad. IAM, KMS, red y plano operativo compartidos se registran como dependencias comunes. Se mide disponibilidad y saturación por entidad.

El mapa de datos registra localización, finalidad, retención, acceso remoto, subcontratistas y mecanismos de transferencia. Se preservan originales exigidos en Argentina cuando corresponda a una EF. El CDE se delimita sólo al activar tarjetas; su aislamiento exige evaluación específica. Ninguna topología equivale por sí misma a certificación ISO, PCI o autorización BCRA.

## Alternativas y consecuencias

| Alternativa | Beneficio | Costo o riesgo |
|---|---|---|
| Base por celda, producto común; propuesta | Reduce alcance de incidentes y simplifica exportación/recuperación | Más bases, claves, respaldos y automatización; piso de costo por entidad |
| Esquemas o filas compartidos | Menor costo inicial | Mayor impacto de errores y cargas; requiere demostrar aislamiento equivalente antes de adoptarlo |
| Infraestructura completa por cliente | Aislamiento físico adicional | Mayor costo y complejidad; no elimina riesgos de soporte, IAM o cadena de proveedores |

Se evita una consulta remota al plano de control por débito; autorización y revocaciones materiales deben seguir siendo efectivas. Transferencias entre celdas requieren operaciones y conciliación explícitas, sin atomicidad contable global implícita.

## Aceptación, revisión y dependencias

Para aceptar, demostrar accesos cruzados denegados por API/DB/eventos/exportación/soporte/KMS, incluida reutilización de conexiones y revocación; saturación sin incumplir el presupuesto acordado de otra celda; restauración y salida aisladas; permisos ROS/PII y retención por clase verificados. Adjuntar matriz de países y contratos, dependencias comunes y resultados observados. Hoy esas pruebas están **sin ejecutar**.

Revisar al compartir almacenamiento o cómputo, sumar entidad/producto/CDE, cambiar región/subcontratista o encontrar interferencia material. Depende de ADR-01, ADR-02, ADR-04, ADR-05 y ADR-07; responsables de Arquitectura, Seguridad, Operaciones, Legal/Cumplimiento y entidad cliente deben quedar identificados al aceptar.

## Trazabilidad

[Arquitectura](../achitecture.md), secciones 1, 10–12, 15 y 18; [mercado](../market_analysis.md), secciones 6, 8, 11 y 12. [Cumplimiento](../compliant.md): LAW-03, DATA-01/03/04/05/06, AML-11, BCRA-T03/11/12/26–34, STD01–06/10/11/19 cuando aplique. [Controles](../../.agents/skills/core-bancario-argentina/references/controles.md): CTL-08 a CTL-14, CTL-16 y CTL-17. Son vínculos de diseño; la aplicabilidad y vigencia requieren verificación del caso concreto.

## NFR relacionados

[NFR-05](../nfr/NFR-05-seguridad-accesos.md), [NFR-06](../nfr/NFR-06-privacidad-residencia-retencion.md), [NFR-07](../nfr/NFR-07-auditoria-observabilidad.md), [NFR-12](../nfr/NFR-12-operabilidad-costos.md). Son cualidades y restricciones a verificar; la elección de este mecanismo no demuestra por sí sola su satisfacción.
