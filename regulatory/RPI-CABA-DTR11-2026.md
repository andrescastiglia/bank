# RPI Capital Federal DTR11/2026: impacto condicionado en documentos inmobiliarios

**Estado:** análisis de alcance para revisión competente; no se activa jurisdicción local del operador. Identidad `RPI-CABA|DTR|11|2026|CABA`.

## Hechos

Se leyó el [texto BO del 19/10](https://www.boletinoficial.gob.ar/detalleAviso/primera/349248/20261019?anexos=1) y **ambos anexos**: I, actividades específicas; II, formulario modelo de beneficiario final. Emisión **16/10**; vigencia explícita **8/11/2026**, art. 9. El art. 1 deroga DTR1/2014, 19/2016, 7/2020 y 7/2024. Se conserva relación, no se borra documentación histórica.

La disposición instrumenta el marco UIF93/2026 para el **Registro de la Propiedad Inmueble de Capital Federal**, sujeto obligado propio. Art. 2 delimita documentos notariales/administrativos cuando el profesional autorizante/solicitante es sujeto obligado y solicita una actividad específica del anexo I. Art. 3 exige CUIT profesional/solicitante, condición PEP e información BF cuando corresponda. Art. 4 delimita transmisión de dominio autorizada desde 8/11 y adquirente persona/estructura jurídica comprendida; no exige el mismo formulario para cualquier hipoteca o trámite. Art. 5 prevé excepción de personas jurídicas públicas con constancia. Arts. 6–8 regulan generación electrónica, suscripción y observaciones por omisión.

Anexo I distingue compraventas por umbral en SMVM y otros actos con condiciones particulares: dación en pago, aporte fiduciario, escisión, fusión y aportes de inmuebles. No transformar todos sus actos en una obligación BF indiferenciada. Anexo II es modelo ilustrativo; no se copiaron datos de personas ni se presenta como formulario ya válido para un expediente real. No se recalculó aquí un umbral monetario SMVM.

## Interpretación y brecha

La norma del Registro **no sustituye** el régimen UIF propio de EF, PSP u otros sujetos, ni habilita trasladar deberes del registrador al proveedor de software. Puede afectar expedientes inmobiliarios/garantías, adquisición o dación en pago que efectivamente lleguen a ese Registro bajo las condiciones citadas. No prueba alcance nacional ni activa por sí sola todas las jurisdicciones.

Falta identificar operación, profesional, plaza, actividad y documentación exigible. UIF93 y sus antecedentes/modificatorias no fueron objeto de revisión integral en esta corrida: se conserva esa dependencia antes de cerrar interpretación. No se propone automatizar PEP/BF sólo a partir de los considerandos.

## Propuesta verificable

Mapear docs/compliant.md AML/DATA/LAW-10/PAY-11 según perfil, FR-TAX-030 para perímetro local, y módulos CLI/AML/GRN/CON/DAT/RPT; NFR-05/06/07/09/11, ADR-05 y CTL-07/09/11/18/19. Revisar con skills de cumplimiento, privacidad y configuración. La función propuesta es un expediente condicionado, con versión de formulario y procedencia, no una nueva regla AML universal.

Casos pendientes: documento anterior/posterior al 8/11; profesional sujeto/no sujeto; acto incluido/excluido; compraventa respecto del umbral con SMVM efectivamente vigente; adquirente pública/privada; minuta con múltiples actos; firmante y facultad; datos BF restringidos; documento observado y corrección preservada. No almacenar CUIT, BF, notas firmadas o claves reales en el repositorio público. **No se consultó ni presentó ningún trámite registral.**

Trazabilidad de consulta: [RUN-20261020T010802Z, URLs finales, fechas y SHA-256](https://github.com/andrescastiglia/bank/blob/ffa061ece43df870aab46a3ba185154c2f411c55/.regulatory-watch/evidence/RUN-20261020T010802Z.json). Validación documental descrita en el [informe integral](../INFORME_ANALISIS_BANK.md); no acredita implementación.
