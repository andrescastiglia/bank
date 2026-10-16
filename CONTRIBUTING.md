# Contribuir al core bancario

El proyecto sigue [GNU GPL v2](LICENSE) y el [gobierno del mantenedor](GOVERNANCE.md). Conservar autoría/procedencia y aportar únicamente material que pueda incorporarse de forma compatible. Las fuentes normativas y los estándares se citan; no subir textos comerciales/restringidos completos, datos personales o secretos.

## Flujo

1. Leer los documentos y skills afectados; delimitar problema, sociedad/rol, producto y fecha cuando corresponda.
2. Crear una rama o fork. Para propuestas normativas usar `regulatory/<identificador-descriptivo>`; evitar una rama/PR nueva para el mismo cambio ya abierto.
3. Hacer un cambio acotado con evidencia, impacto y aceptación. Mantener IDs e historia; conservar reglas anteriores y vigencias futuras.
4. Ejecutar las comprobaciones pertinentes y abrir una PR a `main` con la [plantilla](.github/PULL_REQUEST_TEMPLATE.md).
5. Responder observaciones. **El merge lo realiza exclusivamente `@andrescastiglia`.** No publicar directamente en `main`, fusionar mediante APIs o activar auto-merge.

```sh
python3 docs/functional/tools/build_catalog.py --check
python3 docs/review/tools/check_review.py
python3 docs/regulatory-watch/tools/check_watch.py
python3 docs/regulatory-watch/tools/test_check_watch.py
```

Los checks documentales usan las dependencias fijadas en [requirements.txt](docs/review/tools/requirements.txt). Si cambian fuentes del catálogo, regenerar con `python3 docs/functional/tools/build_catalog.py` y revisar el diff. Una implementación debe además ejecutar sus pruebas materiales; la sintaxis de documentos no verifica dinero, seguridad, disponibilidad ni interpretación jurídica.

## Propuestas normativas

Adjuntar autoridad, norma/edición, URL oficial, texto/anexos revisados, publicación, vigencia/exigibilidad y transición, perfiles afectados, relaciones con reglas previas, FR/NFR/ADR/skills, pruebas y pendientes de interpretación. Señalar fuentes inaccesibles y ventanas sin cobertura. Un aviso de prensa o estándar voluntario no se convierte en una obligación general por aparecer en una PR.

Usar el [procedimiento de vigilancia](docs/regulatory-watch/README.md). Las bitácoras de consulta pueden persistirse en `automation/regulatory-state` sin tocar `main`; los cambios funcionales/documentales se revisan en PR separadas. Crear una propuesta no habilita su ejecución productiva, no implica que el mantenedor la haya aceptado y no cambia la fecha histórica de una evaluación.
