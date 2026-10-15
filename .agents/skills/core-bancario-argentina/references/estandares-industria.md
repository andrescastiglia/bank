# Estándares de industria, redes y marcos de control

**Corte y consulta: 15/10/2026.** Referencia para determinar alcance y pedir evidencia en un core bancario argentino. Se verificaron publicaciones y páginas primarias públicas; los documentos técnicos Swift enlazados requirieron autenticación. La edición está identificada, pero no se auditó todo su contenido.

## Regla de exigibilidad

Separar ley/regulación argentina, contrato de red, guía de ingeniería, aprobación funcional y aseguramiento. Un estándar PCI puede ser exigido por una marca/adquirente/contrato; Swift por el programa de participación. NIST, OWASP, COBIT y Basilea no se convierten por sí mismos en legislación argentina. Registrar el activador y la entidad obligada. El proveedor del software debe aportar capacidades y evidencia; no hereda automáticamente la autorización bancaria de su cliente.

Prioridad **A**: desde diseño; **B**: según riesgo/contrato; **C**: sólo cuando se activa función/red. Son prioridades propuestas, no jerarquía legal.

## Inventario y evidencia

| Referencia verificada | Aplicabilidad y carácter | Evidencia / prioridad |
|---|---|---|
| [PCI DSS v4.0.1](https://www.pcisecuritystandards.org/document_library/) | Datos de cuenta y sistemas que pueden afectar el CDE; programa de validación definido por marcas/contrato | Alcance, flujos, segmentación, inventario, pruebas y ROC/SAQ/AOC que corresponda. C; A al activarse |
| [PCI PIN v3.1](https://blog.pcisecuritystandards.org/just-released-version-3-1-of-the-pci-pin-security-standard) | PIN/llaves dentro de función contratada | Ceremonias, HSM, doble control, bloques de llaves y evaluación especializada. C |
| [PTS HSM v5.0](https://blog.pcisecuritystandards.org/pci-ssc-publishes-pci-pts-hsm-v5.0), 18/05/2026; [KMO v1.0](https://blog.pcisecuritystandards.org/just-published-pci-key-management-operations-kmo-standard-v1.0), 14/09/2026 | Aprobación de módulos y seguridad operacional de llaves, respectivamente | Modelo/firmware/aprobación y vigencia; responsabilidades nube/remoto; generación, uso, rotación y destrucción. C |
| [Secure Software v2.0](https://blog.pcisecuritystandards.org/pci-ssc-releases-version-2.0-of-the-pci-secure-software-standard), 15/01/2026; [Secure SLC v2.0](https://blog.pcisecuritystandards.org/pci-ssc-releases-version-2.0-of-the-secure-software-lifecycle-standard), 28/09/2026 | SSF: evaluaciones distintas de software de pago y ciclo de desarrollo; confirmar elegibilidad | Activos sensibles, diseño/pruebas, vulnerabilidades, versión y alcance de listado validado. C |
| [PCI 3DS Core](https://www.pcisecuritystandards.org/standards/pci-3ds-core/) y [3DS SDK](https://www.pcisecuritystandards.org/standards/pci-3ds-sdk/) | Entornos ACS, DS o 3DS Server; SDK si se desarrolla. Confirmar edición numérica Core en biblioteca: página pública no la expone | Evaluación de entorno, datos sensibles y programa; SDK en sunset 01/05–31/10/2026, revisar ruta SSF v2.0. C |
| [EMVCo 3DS](https://www.emvco.com/emv-technologies/3-d-secure/) | Protocolo/aprobación funcional, según esquema. Línea publicada 2.3.1 y boletines; 2.4 se muestra como borrador al corte | Carta de aprobación, versión y pruebas de compatibilidad/challenge. Aprobación funcional no sustituye PCI. C |
| [Swift CSCF v2026](https://www.swift.com/es/node/33291?category%5B0%5D=169561&sort%5Bfield_last_updated%5D=DESC) | Programa para infraestructura Swift en alcance, según arquitectura/conectividad | Inventario/conectores, controles, evaluación independiente, remediación y atestación KYC-SA. C |
| [NIST CSF 2.0](https://www.nist.gov/cyberframework), 2024 | Guía de gobierno/riesgo cibernético | Perfil actual/objetivo, responsables, brechas y plan. No es certificación de producto. A |
| [SSDF v1.1 final](https://csrc.nist.gov/pubs/sp/800/218/final), 2022 | Recomendaciones de desarrollo seguro | Repositorios, revisión, dependencias, compilación/entrega y vulnerabilidades. A |
| [OWASP ASVS 5.0.0](https://owasp.org/projects/asvs); [API Top 10:2023](https://api-security.owasp.org/editions/2023/en/0x03-introduction/) | ASVS: requisitos verificables; API Top 10: concientización, no lista exhaustiva | Requisitos con versión e ID, pruebas negativas de permisos, sesión, validación y abuso. A |
| [NIST SP 800-63-4](https://csrc.nist.gov/pubs/sp/800/63/4/final) y volúmenes A/B/C, finales julio 2025; [800-61 Rev.3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), abril 2025 | Guías de identidad y respuesta a incidentes | Riesgo, enrolamiento, autenticadores, recuperación y ejercicios. No sustituyen KYC ni avisos locales. A |
| [COBIT 2019](https://www.isaca.org/resources/cobit) | Gobierno y gestión de información/tecnología | Objetivos, responsables, métricas y cambios/terceros. B |
| [AICPA SOC](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services); TSC 2017, puntos revisados 2022 | SOC 1: controles relevantes para información financiera; SOC 2: criterios seleccionados de servicios de confianza. Informes, no normas ISO | Informe íntegro, opinión, alcance/período, excepciones, CUEC y subproveedores. B; A en due diligence |
| [BCBS 239](https://www.bis.org/publications/201301-guidelines-principles-effective-risk-data-aggregation-and-risk-reporting), 2013; [POR](https://www.bis.org/publications/202103-guidelines-principles-operational-resilience), 2021; [terceros](https://www.bis.org/publications/202512-guidelines-principles-sound-management-third-party-risk), 2025 | Principios internacionales; justificar adopción/exigencia local | Linaje, calidad/agregación, operaciones críticas, dependencias, continuidad y salida. A como diseño |

## Fechas y límites que deben preservarse

Los requisitos de PCI DSS v4.x inicialmente futuros se hicieron efectivos el **31/03/2025**, sujetos a sus notas de aplicabilidad. [Publicación oficial](https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1). Secure SLC v2.0 anunció transición de doce meses desde habilitar capacitación prevista para Q4 2026; no inventar fecha final. Nueva edición PTS no invalida por sí sola todas las aprobaciones previas.

SSDF v1.2 / SP 800-218 Rev.1 continúa como **draft** en la [lista oficial actualizada 06/10/2026](https://csrc.nist.gov/projects/ssdf/publications); usar v1.1 como baseline final y registrar el borrador por separado.

Swift requiere identificar arquitectura, evaluación independiente y atestación anual; verificar controles en copia autorizada. La ventana ordinaria es julio–diciembre del año correspondiente. [Procedimiento oficial](https://www.swift.com/myswift/customer-security-programme/understand-controls). No asumir que una integración indirecta queda fuera sin revisar conectividad y componentes.

SOC 2 Type I considera diseño a una fecha; Type II incluye eficacia operativa durante período. Revisar controles del cliente y subproveedores excluidos. La integridad del procesamiento sólo aporta evidencia si está dentro del alcance contratado.

## Conversión a controles del core

Proponer pruebas de ledger balanceado, precisión monetaria, idempotencia, concurrencia, reversos y conciliación; autorización por cliente/cuenta/entidad/función; trazabilidad de datos a reportes; recuperación coherente de base, colas y llaves; y protección contra replay en pagos. Estas son decisiones de ingeniería, no equivalencias automáticas con un estándar.

Para cada adopción registrar referencia/edición, activador, alcance, propietario, evidencia, brecha y revalidación. Si se incorporan aceptación móvil, terminales, tokenización o emisión física, ampliar a [PCI PTS POI, P2PE, MPoC, TSP y Card Production](https://www.pcisecuritystandards.org/standards/) según función. No aplicar toda la familia a un ledger sin justificar alcance. Confirmar siempre versiones, boletines y reglas de la red antes de homologar o producir.
