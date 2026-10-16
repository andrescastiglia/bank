---
name: nfr-01-integridad-financiera
description: "Usar al diseñar, implementar o verificar exactitud monetaria, partida doble, unicidad de efectos, reservas y límites concurrentes del core bancario argentino conforme a NFR-01."
---

# NFR-01: integridad financiera

## Resultado y entrada mínima

Aplicar [NFR-01](../../../docs/nfr/NFR-01-integridad-financiera.md) como contrato de calidad medible. La línea base es 15/10/2026 y su estado es propuesto. Determinar la acción autorizada: especificar, implementar o evaluar. El skill no convierte una solicitud documental en autorización para operar fondos, migrar producción ni efectuar cambios externos.

Identificar entidad, producto, moneda/escala, operación, versión de reglas, autoridad de saldo, frontera transaccional y efectos externos. Recoger código/configuración disponibles, vectores aprobados, volumen y comportamiento contractual del riel. Si faltan, explicitar supuestos y continuar el análisis independiente; dejar sin evaluar el comportamiento que requiere ejecución. Consultar [cumplimiento](../core-bancario-argentina/SKILL.md) para aplicabilidad de obligaciones, sin atribuirles estos mecanismos literalmente.

## Procedimiento por acción

1. **Diseñar:** enumerar invariantes por NFR-01-C01 a C05 y definir estados observables antes/después del commit. Separar fecha de evento, valor, contabilización y período. Precisar identidad económica, no sólo clave de transporte; conservar unicidad material durante vida y retención aplicables. Documentar redondeo, reverso, aprobación y conciliación por titular/moneda.
2. **Implementar:** dentro del alcance solicitado, identificar cada ruta que cambia fondos, reservas, congelamientos, mandatos y exposición. Comprobar protección común frente a inserciones concurrentes: una fila guardiana o mecanismo equivalente debe proteger también la ausencia previa de restricciones. El agregado de grupo/línea no puede depender de una proyección atrasada. Usar la autoridad financiera definida por ADR-02; proponer ADR sólo si se pretende cambiar la decisión.
3. **Verificar:** elegir escenarios materiales para el cambio: dos débitos sobre disponibilidad insuficiente, embargo concurrente, límite compartido, pérdida de respuesta, callback tardío, reverso y fallo de persistencia. Comparar resultado financiero esperado con diario, posiciones, reserva, exposición y evidencia externa. Ejecutar pruebas proporcionales sólo cuando exista implementación y entorno adecuado; si el pedido es documental, entregar especificación y oráculos.

## Oráculos y fallos que deben buscarse

Exigir cero operaciones desbalanceadas por entidad/moneda, efectos económicos adicionales, sobregiros no autorizados y diferencias contra vectores aprobados. No compensar diferencias entre titulares ni monedas. Reproducir interés, impuestos y comisiones con reglas históricas y calendarios; probar bisiesto y cierre cuando corresponda.

Separar éxito financiero de aceptación durable: `202` o acuse no declara liquidación. El éxito local exige su commit durable; una confirmación final externa exige además evidencia del riel correspondiente. No exigir evidencia externa a una operación puramente interna ni confundir un estado pendiente válido con una confirmación incorrecta.

Devengar una vez por entidad/contrato/tipo/período: la versión de regla describe el cálculo y no habilita otro devengamiento base. Una corrección conserva el original y genera ajuste aprobado. Perder una respuesta externa no significa rechazo: conservar estado ambiguo y no liberar fondos ni reenviar sin resolución segura. Una prueba aislada de idempotencia de transporte no acredita efecto único de negocio.

## Medición, evidencia y salida

Registrar criterio, alcance, semilla/datos sintéticos, versión, escenario concurrente, fallo inyectado, esperado, observado y conciliación. Revisar el universo completo del ensayo y conservar muestras explicables de operaciones y cambios históricos. No utilizar datos personales reales si bastan ejemplos sintéticos.

Entregar `ID | criterio | escenario | métrica/unidad | objetivo | observado | evidencia | estado | brecha/responsable`. Usar `no evaluado` si falta implementación, vector aprobado o ejecución; `no satisface` ante diferencia y `satisface en escenario probado` únicamente con evidencia. Separar hipótesis, hallazgo y recomendación. No declarar conformidad jurídica ni aprobación institucional. Revisar tras cambios en fórmulas, concurrencia, producto, migración o autoridad financiera.
