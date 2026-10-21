# Decreto 1228/2026: prórroga FAL y cómputo de carencia

**Estado:** cambio primario verificado; interpretación operativa y aplicación individual pendientes. Identidad `PEN|DECRETO|1228|2026|AR`.

## Hechos, fechas y relaciones

Se leyó el [BO20, Decreto 1228](https://www.boletinoficial.gob.ar/detalleAviso/primera/349294/20261020), emitido **19/10**, publicado y vigente **20/10/2026** (art.3). No se anuncia anexo. Modifica el [Decreto 408/2026](https://www.argentina.gob.ar/normativa/nacional/norma-426272/texto), arts.15 y27:

- **Art.1:** carencia mínima de **doce períodos mensuales completos y consecutivos de devengamiento y pago**, contados desde el mes calendario en que se registre ante ARCA la **efectiva integración de la primera contribución del empleador**. No contar desde publicación, apertura de cuenta o creación del sistema.
- **Art.2:** entrada del régimen del título II FAL de Ley27.802 pasa del antecedente **1/11 al 1/12/2026**. Distinguir vigencia del decreto (20/10), comienzo del régimen (1/12) y carencia individual cuyo disparador todavía no se conoce.

Se releyó [RG 5907](https://www.argentina.gob.ar/normativa/nacional/norma-430768/texto), especialmente art.19: su texto recuperado aún menciona vigencia 1/11, devengado noviembre y versión48 para presentaciones posteriores de períodos anteriores. **La prórroga del régimen no prueba por sí sola que todo plazo procedimental, sistema o registro de esa RG se haya movido un mes.** Falta armonización y revisión de disposiciones complementarias vigentes por responsable fiscal/legal antes de parametrizar.

## Aplicabilidad y brecha detectada

La sociedad operadora/proveedora puede estar alcanzada **como empleador privado**, según relaciones excluidas y su encuadre. Un rol distinto es instrumentar, administrar, custodiar o invertir FAL mediante vehículos/actores habilitados. Ser banco o aportar software no habilita todos esos roles. Los considerandos identifican FCI abiertos/fideicomisos y normas CNV1167, ARCA5907 y UIF109; no se verificó integralmente ese marco en esta corrida.

docs/LEGAL_TAX.md §11 conserva el antecedente de noviembre y necesita esta actualización fechada. Faltan sociedad, rol, primera integración registrada y mecanismo probado de conciliación. No se inventa un vencimiento individual o fecha final de carencia. La prórroga no demuestra derogación ni suspensión del tratamiento prudencial de inversiones A8490 ni elimina contribuciones por estar en carencia.

## Propuesta y aceptación

Mapear docs/LEGAL_TAX.md §11, docs/compliant.md según producto/rol, FR-ENT-031 (extensión que requiere encuadre), FR-TAX-001/002/018/030/031, FR-RPT-001/007/009/010/038, módulos INV/TRE/CON/OPS cuando se activen; NFR-01/04/07/09/11/12, ADR-05, CTL-02/05/06/14/19. Skills de cumplimiento, configuración, reportes y kickoff existentes; no crear un módulo universal FAL a partir de una prórroga.

Preparar matriz por rol con versión, fecha, obligación y evidencia de integración; mantener agenda del 1/12 y el disparador individual pendiente. Casos propuestos: publicación frente a comienzo; contribución ordenada/pagada/registrada; registro tardío; períodos discontinuos; cambio de empleador o cuenta; regla RG 5907 pendiente; recepción de reporte sin aceptación. Bloquear la declaración de «carencia cumplida» si falta la secuencia probada. **Sin simulación financiera, nómina, presentación fiscal, pago o intervención institucional ejecutados.**

Consulta y evidencia: [RUN-20261021T014755Z, URLs finales, fechas y SHA-256](https://github.com/andrescastiglia/bank/blob/659cbd9220d4d93960d03c5889013959f2b57657/.regulatory-watch/evidence/RUN-20261021T014755Z.json). Ver [informe integral](../INFORME_ANALISIS_BANK.md) para cobertura y validación documental; no acredita implementación.
