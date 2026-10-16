# Caso de negocio y caja del proveedor

**Plantilla de trabajo, sin cifras reales.** Completar con fuentes y fechas; separar observación, cotización, supuesto y decisión. El TCO del banco comprador y la rentabilidad del proveedor son modelos distintos.

## Entradas y unidades

| Entrada | Unidad y desglose requerido | Fuente/valor/estado |
|---|---|---|
| Clientes/cohortes | Segmento, fecha probable de firma, inicio de implantación, aceptación, facturación y cobro | Por completar |
| Precio recurrente | Moneda, unidad, mínimo, bandas, consumo incluido, índice/FX, impuestos y revisión | Por completar |
| Implantación | Ingreso por hitos y costo directo por cliente; separar alcance común/específico | Por completar |
| Infraestructura | Por celda/entorno/región; HA, DR, bus, DB, red, egreso, llaves, logs y retención | Por completar |
| Personal | Capacidad real, costo total, guardia, vacaciones, reemplazos y funciones incompatibles | Por completar |
| Terceros/control | IAM, KYC, fraude, firma, redes, licencias, auditorías, asesoría y actualización normativa | Por completar |
| Cobranza fiscal | Calendario de factura/cobro, IVA/IIBB y otros tratamientos aplicables, retenciones/percepciones, recuperabilidad y mora | Por completar con revisión profesional |
| Capital de trabajo | Caja inicial, pagos, anticipo, créditos fiscales, financiación, contingencia y caja mínima acordada | Por completar |
| Salida/concentración | Costo de egreso/transición/archivo, pérdida de cliente o proveedor y tiempo de sustitución | Por completar |

## Modelo mensual por cohorte

Mantener columnas separadas para ingresos reconocidos, facturas, cobros netos, impuestos/retenciones, costos devengados, pagos y saldo de caja. Calendarizar retrasos y capacidad de entregar; una oportunidad adjudicada no está necesariamente activa y facturando. No usar ARR de salida como ingresos acumulados.

```text
Ingreso recurrente mensual = cargos devengados del período por la prestación,
                            conforme política contable aprobada, separados
                            del calendario de facturación y cobro
Margen bruto recurrente = ingreso recurrente − costos directos del servicio
Margen de implantación = ingreso por implantación − costo directo de entrega
Caja final del mes = caja inicial + cobros + financiación
                    − pagos operativos/inversión excluidos los egresos fiscales
                    − egresos fiscales
Equilibrio recurrente = costos fijos / contribución recurrente por cliente equivalente
Payback de adquisición (meses) = costo de adquisición / contribución mensual del cliente
```

Las fórmulas de equilibrio/adquisición sólo son útiles con contribución positiva y mezcla comparable; no dividir por un promedio que oculta clientes deficitarios. El umbral de margen/caja y el horizonte de financiación los fija el caso de negocio aprobado, no una norma ni esta plantilla. Evitar doble contar personas, anticipos, IVA recuperable y costos comunes.

## Sensibilidad y decisión

Comparar conservador, base y expansión con supuestos explícitos de demoras, volumen, cliente perdido, descuento, costo de soporte, incidentes, variación de moneda, cambio normativo y salida. Analizar costo mínimo con baja ocupación de una celda y costo marginal al escalar. No aceptar un precio recurrente deficitario porque un anticipo mejora temporalmente la caja.

Registrar quién decide invertir, asociarse/comprar, reducir alcance, cambiar precio o detener. Adjuntar cotizaciones y validación de disposición a pagar antes de presentar el escenario como rentable o financiado. No confundir una tabla completada con contratación, factura emitida o declaración fiscal presentada.
