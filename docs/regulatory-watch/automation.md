# Programación y estado inicial

**Verificación de configuración:** 16/10/2026 UTC. La herramienta de automatizaciones confirmó la creación y activación de **«Vigilancia normativa del core»**, con frecuencia diaria, modo de vigilancia condicional y zona personal **`America/Buenos_Aires`**. No se impuso una hora de entrega que el mantenedor no hubiera solicitado.

El acceso al conector GitHub se comprobó leyendo `main` y creando/leyendo el estado inicial en la rama [`automation/regulatory-state`](https://github.com/andrescastiglia/bank/tree/automation/regulatory-state). Los checkpoints, agenda y cambios se iniciaron vacíos/sin cobertura acreditada. La automatización usa ese destino durable y no depende del filesystem de esta sesión.

El prompt programado contiene el protocolo esencial, las fuentes, el backfill desde 15/10/2026 inclusive, los gaps y el silencio ante ventanas completas sin cambios. También establece GPL v2 y la prohibición explícita de merge, auto-merge o push a `main`. Puede empezar la investigación aunque el mantenedor todavía no haya integrado la PR con estos documentos; en ese caso usa el protocolo embebido y la rama de propuesta como referencia.

## Qué acredita esta configuración

- Existe una automatización activa con el mandato y frecuencia indicados.
- Hay acceso observado a GitHub y un destino de estado separado de `main`.
- Las propuestas se preparan para revisión del mantenedor; ninguna integración está autorizada para el agente.

La creación no acredita una primera corrida, cobertura completa de las fuentes, descubrimiento de todas las normas ni implementación de cambios. Esos resultados deben constar en bitácoras posteriores con ventana, evidencia y limitaciones. La validación documental del repositorio tampoco prueba la ejecución del servicio de automatizaciones.

## Operación de la programación

El mantenedor puede localizar la tarea por su título en las automatizaciones de su cuenta para modificar horario, pausar o reanudar. No crear una segunda programación al cambiar una preferencia: consultar la tarea existente y actualizarla. Su configuración pertenece a la cuenta; cambiar este Markdown o invocar el skill no modifica la tarea activa.

Si se cambian el repositorio, las fuentes, el protocolo o los permisos, actualizar también el prompt/configuración y comprobar el acceso necesario. Si faltan herramientas o acceso durante una corrida, registrar la falla y notificarla cuando sea material; no dar por realizada una consulta o una PR. Las notificaciones son para el usuario, sin correos o presentaciones a terceros.

La exclusividad técnica del merge aún requiere verificar/configurar los controles de GitHub descritos en [GOVERNANCE.md](../../GOVERNANCE.md). La integración de esta sesión devolvió 403 al consultar protección y al intentar crear el ruleset restrictivo; se conserva una plantilla revisable. La automatización no tiene autorización para eludir la limitación o alterar permisos.
