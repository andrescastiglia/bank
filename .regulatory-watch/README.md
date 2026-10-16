# Estado del agente de vigilancia normativa

Rama operativa independiente; no fusionar automáticamente a main. Sólo @andrescastiglia realiza merges a main. Proyecto conforme a GNU GPL v2 existente.

sources.json registra fuentes y scope; state.json se inicia sin corridas ni cobertura acreditada. initial_backfill_from solicita comenzar desde 15/10/2026 inclusive; no es un checkpoint verificado. Persistir aquí bitácoras en runs/<run_id>.json, gaps, agenda y referencias de propuestas. No guardar datos personales, secretos o textos restringidos.

Cada ejecución recupera cobertura por fuente, consulta textos oficiales y anexos, deduplica por identidad y contenido, separa publicación/vigencia/exigibilidad, conserva revisiones y prepara propuestas en regulatory/... con PR. Nunca hacer push/merge/auto-merge a main. Las propuestas no acreditan implementación ni cumplimiento.

Retomar gaps desde último checkpoint completo con solapamiento; página, anexo o fuente incompletos no permiten declarar sin novedades global ni avanzar corte. Guardar actualizaciones por SHA/versionado; ante conflicto recargar, sin force-push. Consultar protocolo actualizado en main cuando el mantenedor integre la PR de gobierno y vigilancia. Hasta entonces aplica el protocolo completo de la automatización autorizada.
