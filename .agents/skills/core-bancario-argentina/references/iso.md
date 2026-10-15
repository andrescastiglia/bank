# Referencia ISO para core bancario argentino

**Corte y consulta: 15/10/2026.** Esta referencia es autónoma para identificar estándares y pedir evidencia. Sólo se consultaron catálogos, metadatos y descripciones públicas de ISO; no se realizó una auditoría del texto íntegro de pago. No reproducir cláusulas ni asignar números de control no cotejados con una copia autorizada.

## Reglas de uso

1. Clasificar cada estándar como norma de gestión, guía o especificación técnica. No convertirlo automáticamente en ley argentina. Registrar qué norma local, contrato, licitación o decisión interna lo vuelve exigible y para quién.
2. Separar implementación de certificación. Un certificado de gestión cubre una organización, servicios y sitios definidos; comprobar vigencia, edición, alcance, certificador y acreditación. No inferir que certifica el producto o todas las instalaciones del cliente. [ISO/CASCO](https://casco.iso.org/attestations-of-conformity.html).
3. Solicitar la edición y enmiendas pactadas. Una revisión publicada no cambia por sí sola contratos ni protocolos homologados. Documentar transición con contraparte/certificador.
4. Para conformidad por cláusula, usar el texto autorizado y evidencia concreta. Si falta, informar “alcance/edición identificados; conformidad no evaluada”. Nunca declarar un core “100 % compliant” por una lista de ISO.

## Inventario verificado

Prioridad **A**: evaluar desde diseño; **B**: según riesgo/contrato; **C**: al activarse la función. La prioridad es recomendación de ingeniería, no obligatoriedad legal.

| Referencia | Naturaleza y aplicación | Evidencia y prioridad |
|---|---|---|
| [ISO/IEC 27001:2022](https://www.iso.org/standard/27001) + [Amd 1:2024](https://www.iso.org/standard/88435.html) | SGSI certificable; voluntario o contractual | Alcance desarrollo/operación, riesgos, tratamiento, aplicabilidad, auditorías y seguimiento. A |
| [27002:2022](https://www.iso.org/standard/75652.html) y [27005:2022](https://www.iso.org/standard/80585.html) | Guías de controles y riesgos | Mapeo de medidas a amenazas; dueño y riesgo residual. A |
| [27017:2026](https://www.iso.org/standard/27017) | Guía de seguridad de nube; edición 2 publicada 27/07/2026, reemplaza 2015 | Responsabilidades compartidas, aislamiento y configuración. A si nube |
| [27018:2025](https://www.iso.org/standard/27018) | Guía para datos personales en nube pública cuando proveedor es encargado | Instrucciones, subencargados, acceso, devolución/eliminación. A si aplica |
| [27701:2025](https://www.iso.org/standard/27701) | Sistema independiente de gestión de privacidad; no describirlo sólo como extensión de 27001 | Roles, tratamientos, finalidades, riesgos, derechos y alcance evaluado. A |
| [22301:2019 y Amd 1:2024](https://www.iso.org/standard/75106.html) | Gestión de continuidad certificable | BIA, operaciones críticas, tolerancias y ejercicios. A |
| [27031:2025](https://www.iso.org/standard/27031) | Guía de preparación TIC para continuidad; reemplaza 2011 | Restauración de datos, colas, llaves, identidades y conciliación. A |
| [27035-1:2023](https://www.iso.org/standard/78973.html), [-2:2023](https://www.iso.org/standard/78974.html), [-3:2020](https://www.iso.org/standard/74033.html), [-4:2024](https://www.iso.org/standard/80973.html) | Serie de gestión de incidentes; partes con edición propia | Escalamiento, operación, coordinación y preservación de evidencia. A |
| [27036-2:2022](https://www.iso.org/standard/82060.html), [-3:2023](https://www.iso.org/standard/82890.html) | Seguridad de proveedores/cadena de suministro | Due diligence, subcontratación, integridad de entregas, acceso remoto y salida. A |
| [27040:2024](https://www.iso.org/standard/80194.html) | Seguridad de almacenamiento | Respaldos, medios, accesos, llaves y retiro. A |
| [20000-1:2018](https://www.iso.org/standard/70636.html) + [Amd 1:2024](https://www.iso.org/standard/88434.html) | Gestión de servicios certificable | SLA/SLO, cambios, incidentes, problemas y capacidad. B |
| [9001:2026](https://www.iso.org/standard/9001) | Calidad certificable; edición 6 publicada 16/09/2026, ya no borrador | Entrega, aceptación, defectos y mejora; comprobar transición de certificados legados. B |
| [25010:2023](https://www.iso.org/standard/78176.html) | Modelo de calidad del producto | Requisitos medibles y pruebas de fiabilidad, rendimiento y mantenibilidad. A |
| [37301:2021](https://www.iso.org/standard/75080.html) + [Amd 1:2024](https://www.iso.org/standard/88422.html); [37001:2025](https://www.iso.org/standard/37001) | Gestión de compliance y antisoborno | Obligaciones, responsables, controles, formación y seguimiento. B |
| [42001:2023](https://www.iso.org/standard/42001), [23894:2023](https://www.iso.org/standard/77304.html) | Gestión de IA certificable y guía de riesgos, respectivamente | Inventario/modelos/datos, impacto, desempeño, supervisión y reversión. C |
| ISO 20022; [parte 1:2026](https://www.iso.org/standard/20022-1) y [7:2026](https://www.iso.org/standard/20022-7) | Mensajería; definir perfil y versión de mensaje | Esquema, semántica, correlación y pruebas de contraparte. C |
| [8583:2023](https://www.iso.org/standard/79451.html), [11568:2023](https://www.iso.org/standard/73993.html) | Mensajes de tarjetas y llaves de pagos minoristas | Perfil de red, reversos, homologación y ciclo de llaves/HSM. C |

ISO 20022 no tiene una autoridad oficial de certificación del core. La interoperabilidad se verifica por mensajes, versiones y reglas de la comunidad; no equivale a corrección contable. [Autoridad de registro: FAQ](https://www.iso20022.org/faq).

## Traducción a trabajo verificable

Crear una fila por requisito con `referencia + edición + activador + alcance + responsable + evidencia + estado + fecha de revisión`. Clasificar estado como aplicable, no aplicable justificado, pendiente de alcance o no verificado.

Proponer, identificándolo como ingeniería propia: ledger balanceado, dinero con precisión exacta, idempotencia y reversos trazables; pruebas de concurrencia y conciliación; acceso mínimo y segregación; registros resistentes a alteración; recuperación integral medida; y trazabilidad requisito→prueba→release. Asociar cada medida con riesgos y disposiciones argentinas concretas. No atribuir estos patrones a una cláusula ISO no leída.

RTO/RPO, retención, avisos de incidentes y bases legales de tratamiento deben provenir del negocio y las obligaciones aplicables, no de cifras inventadas como “mandato ISO”. Conciliar borrado y privacidad con deberes de conservación y legal hold. El SGSI de la nube no cubre automáticamente configuración, aplicación y usuarios del banco.

Si el alcance incorpora PIN, ampliar a la parte específica de ISO 9564: [9564-1:2017 sigue como edición a reemplazar por un CD en desarrollo](https://www.iso.org/standard/90849.html) y [9564-5:2025](https://www.iso.org/standard/86132.html). Un borrador no reemplaza un estándar publicado. Revalidar catálogo y boletines antes de licitar o salir a producción.
