# COMARB Disposición de Presidencia 11/2026: calendario específico

**Estado:** texto primario recuperado; análisis propuesto, aplicabilidad individual pendiente. Identidad `COMARB|DP|11|2026|AR-CM`. No confundir con DTR11 del RPI.

## Datos verificados

El [Boletín Oficial del 19/10](https://www.boletinoficial.gob.ar/detalleAviso/primera/349247/20261019) publica el texto completo emitido **16/10/2026**. Se leyeron considerandos y arts. 1–4; no se anuncia anexo en ese aviso. Se recupera así el candidato pendiente, aunque el sitio COMARB/SIRCREB/SIRCUPA continúa devolviendo 500. Fuente alternativa oficial recuperada no significa cobertura completa de esos sistemas.

| Régimen, período y población | Cambio literal del dispositivo |
|---|---|
| SIRCAR, segunda quincena octubre 2026, vencimientos previstos 9 y 10/11 | Ambos pasan al **13/11/2026 inclusive** (art. 1). |
| SIRTAC, segunda quincena octubre, agentes con dígito verificador CUIT 5–9, fecha previa 11/11 | **13/11/2026** (art. 2). No extender a los demás dígitos sin fuente. |
| SIFERE, anticipo octubre 2026, contribuyentes Convenio Multilateral | **17, 18, 19 y 20/11**, según distribución del calendario aplicable (art. 3). Este texto no basta para inventar la asignación CUIT→día. |

El art. 4 ordena publicación e incorporación al ordenamiento. No fija una fecha general de entrada en vigencia independiente: `effective_at=null`, con fechas de obligación por régimen/población. Faltan designación/inscripción, CUIT y encuadre de la sociedad para asignar vencimiento individual.

## Interpretación, brecha y propuesta

Es un cambio de **plazos**, no de alícuotas, bases o padrones. No modifica SIRCREB/SIRCUPA ni todos los regímenes de IIBB. El fundamento sobre feriados no habilita extrapolar un calendario universal: para feriado bancario se verificó por separado [A8487](BCRA-A8487-2026.md); otros feriados/jurisdicciones necesitan sus propias fuentes y alcance.

Mapear docs/LEGAL_TAX.md, docs/compliant.md TAX-01/03/09, FR-TAX-001/002/018/028/030/031, FR-RPT-001/007/009/010/011/014/015/038, FR-OPS-003; ADR-05, NFR-04/09/11/12 y CTL-02/14/19. Los skills existentes de cumplimiento, configuración y reportes proporcionan el procedimiento. Falta un paquete de calendario específico, versionado y revisado para cada sociedad; una fecha en documentación no demuestra que sus jobs se hayan reprogramado.

Proponer calendario con procedencia, período, sistema, perfil y versión; conservar fecha anterior y posterior para reconstrucción. Casos: SIRTAC dígito 4 frente a 5; segunda quincena frente a primera; octubre frente a noviembre; SIRCAR frente a SIRCREB; contribuyente CM sin distribución CUIT resuelta. Deben mantenerse excepción y revisión, nunca completar un día o extender una prórroga por semejanza. La caída de la fuente o DLQ no suspende una obligación.

**Sin pruebas fiscales materiales ni presentaciones/pagos.** Confirmar calendario base y asignación concreta con responsable fiscal antes de configurar vencimientos.

Trazabilidad de consulta: [RUN-20261020T010802Z, URLs finales, fechas y SHA-256](https://github.com/andrescastiglia/bank/blob/ffa061ece43df870aab46a3ba185154c2f411c55/.regulatory-watch/evidence/RUN-20261020T010802Z.json). Validación documental descrita en el [informe integral](../INFORME_ANALISIS_BANK.md); no acredita implementación.
