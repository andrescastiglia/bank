# NFR-08 — Interoperabilidad y portabilidad

**Estado:** Propuesto. **Línea base:** 15 de octubre de 2026. **Responsables propuestos:** Integraciones, Plataforma y Seguridad; el responsable institucional determina las obligaciones aplicables. Los objetivos requieren verificación; no representan homologaciones obtenidas.

## Alcance y motivación

Contratos de API/eventos, adaptadores de rieles y salida del proveedor, incluyendo datos, documentos, historial, metadatos y recuperación de claves. La composición modular y la salida comprobable sostienen la propuesta comercial y evitan omitir integración, coexistencia y egreso en el TCO. Este NFR define resultados verificables; las decisiones sobre módulos y mecanismos pertenecen a los ADR.

## Criterios medibles

| ID | Métrica y unidad | Ventana/escenario | Objetivo propuesto | Fuente |
|---|---|---|---|---|
| NFR-08-C01 | Casos contractuales compatibles, % | Cada cambio de API/evento; combinaciones productor/consumidor soportadas | 100% de casos aprobados; cero rupturas sin versión y transición acordadas | Arquitectura §§7, 14–15; CTL-15 |
| NFR-08-C02 | Resultados semánticos correctos, %; plazos, ms/s según riel | Cada versión/perfil de adaptador; éxito, duplicado, timeout, estado ambiguo, rechazo y reverso | 100% de casos aprobados conserva estados, importes, identidad, autorización y plazo contractual del riel | Arquitectura §§4–8; PAY-01–05; STD17 |
| NFR-08-C03 | Objetos autorizados exportados/importados, %; diferencias inexplicadas, cantidad | Ensayo de salida previo a producción y cambio material | 100% del inventario acordado; cero diferencias por titular, producto, entidad y moneda; historial reconstruible | CTL-05, CTL-16; BCRA-T28 |
| NFR-08-C04 | Restauraciones independientes satisfactorias, %; duración, horas | Cada ensayo de salida, fuera de la cuenta/servicio administrado por el proveedor saliente | 100% del escenario aprobado recupera datos, esquemas documentados, versiones y referencias; claves recuperables por canal protegido | Arquitectura §§10, 14; CTL-10, CTL-13, CTL-16 |
| NFR-08-C05 | Exportaciones no autorizadas o campos prohibidos, cantidad | Cada exportación; casos negativos multientidad y de roles | Cero; autorización por finalidad/destinatario y exclusión de secretos, PAN completo innecesario y ROS fuera del circuito reservado | Arquitectura §12; CTL-08–12, CTL-17 |
| NFR-08-C06 | Tiempo total de salida, horas; costo, moneda/base | Ensayo representativo por volumen y retención | Medidos contra ventana y presupuesto aprobados, incluyendo egreso, claves, archivo y coexistencia; sin umbral universal inventado | Mercado §§8–9; CTL-16 |

## Aceptación y evidencia

Conservar matriz de versiones soportadas, pruebas de contrato, resultados de contraparte, manifiestos con hashes, diccionario de datos, conciliación y acta del ensayo de salida con costos. Separar simulación de homologación efectiva: una prueba local no acredita autorización de una red. Sin ventana, presupuesto o acceso al destino independiente, registrar evaluación pendiente y su dependencia; no declarar portabilidad demostrada.

## Dependencias y trazabilidad

[Arquitectura: módulos](../achitecture.md#modulos), [asincronía](../achitecture.md#asincronia), [operación](../achitecture.md#operacion); [ADR-01](../adr/ADR-01-nucleo-modular.md), [ADR-05](../adr/ADR-05-configuracion-versionada.md); [mercado y TCO](../market_analysis.md); [cumplimiento](../compliant.md#estandares). CTL-04, CTL-05, CTL-08–13, CTL-15–17 y BCRA-T28 requieren evidencia del alcance concreto.

Skill operativo: [nfr-08-interoperabilidad-portabilidad](../../.agents/skills/nfr-08-interoperabilidad-portabilidad/SKILL.md).
