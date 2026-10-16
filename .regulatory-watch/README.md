# Estado del agente de vigilancia normativa

Rama operativa independiente; no fusionar automáticamente a main. Sólo @andrescastiglia realiza merges a main. Proyecto conforme a GNU GPL v2 existente.

sources.json registra fuentes y scope; state.json se inicia sin corridas ni cobertura acreditada. initial_backfill_from solicita comenzar desde 15/10/2026 inclusive; no es un checkpoint verificado. Persistir aquí bitácoras en runs/<run_id>.json, gaps, agenda y referencias de propuestas. No guardar datos personales, secretos o textos restringidos.

Cada ejecución recupera cobertura por fuente, consulta textos oficiales y anexos, deduplica por identidad y contenido, separa publicación/vigencia/exigibilidad, conserva revisiones y prepara propuestas en regulatory/... con PR. Nunca hacer push/merge/auto-merge a main. Las propuestas no acreditan implementación ni cumplimiento.

Retomar gaps desde último checkpoint completo con solapamiento; página, anexo o fuente incompletos no permiten declarar sin novedades global ni avanzar corte. Guardar actualizaciones por SHA/versionado; ante conflicto recargar, sin force-push. Consultar protocolo actualizado en main cuando el mantenedor integre la PR de gobierno y vigilancia. Hasta entonces aplica el protocolo completo de la automatización autorizada.

## Recuperación y primera corrida observada

El 16/10/2026 UTC se confirmó que la rama operativa no existía tras la integración del seed en main mediante PR #2. Se recuperó desde el commit remoto 6a784b1af7f3aafffc4a87d3c4315bfabf090341, conservando el blob state.json da1bf4d579e746dfc7e360993a6b19c4d4c8b802 como estado anterior. Ese seed tenía checkpoints y last_run_id nulos; no se atribuye cobertura previa.

La corrida RUN-20261016T014713Z consulta la ventana del 15/10/2026 en America/Buenos_Aires y registra resultado PARTIAL. Su evidencia, estado anterior, cambios, agenda y propuesta PR #3 se conservan en esta rama. Mantenerla como destino operativo separado: la vigilancia no abre una PR para fusionar bitácoras a main ni elimina esta rama tras una propuesta documental. Sólo el mantenedor decide los merges.
