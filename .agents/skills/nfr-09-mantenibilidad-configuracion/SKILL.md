---
name: nfr-09-mantenibilidad-configuracion
description: "Usar al diseñar, implementar o verificar evolución modular, configuración acotada y versionada, activaciones, migraciones de esquema y reversión del core argentino, con evidencia histórica y objetivos de cambio medibles."
---

# NFR-09: mantenibilidad y configuración

## Aplicación y entradas mínimas

Leer [NFR-09](../../../docs/nfr/NFR-09-mantenibilidad-configuracion.md), arquitectura y ADR enlazados. Aplicar [core bancario argentino](../core-bancario-argentina/SKILL.md) cuando cambien reglas financieras, condiciones o controles. Distinguir el atributo medible del mecanismo decidido en un ADR y la obligación aplicable. La existencia de documentación no demuestra implementación.

Identificar el cambio pedido, módulo/entidad/producto, regla o esquema, versión actual y destino, período afectado, actores y evidencia disponible. Obtener objetivos de tiempo/costo por tipo de cambio y combinaciones de versiones soportadas cuando sean necesarios. Preguntar sólo por faltantes materiales; preparar análisis o correcciones reversibles con supuestos explícitos. No exigir un formulario completo para una revisión pequeña.

## Flujo operativo

1. **Clasificar el cambio.** Vincular NFR-09-C01 a C06 pertinentes con riesgo y alcance. Separar parámetro soportado, perfil habilitado, nueva fórmula/algoritmo y cambio de invariante. Un algoritmo nuevo requiere código, revisión y pruebas financieras. No introducir scripts genéricos o SQL arbitrario como configuración del producto. Mantener una base de producto compartida; registrar adaptadores específicos y su costo sin crear forks permanentes por cliente.
2. **Diseñar el contrato temporal.** Determinar vigencia de negocio y fecha en que se registró/aprobó cada versión; guardar identificador exacto en operaciones. Definir estados y permisos de crear, simular, revisar, aprobar y activar; impedir ambigüedad de intervalos. Evaluar fecha/hora/zona, activaciones futuras y correcciones retroactivas. La aprobación institucional corresponde al responsable; preparar evidencia y cambios autorizados sin inventar permisos.
3. **Implementar si se solicitó.** Inspeccionar código, migraciones y configuración existentes. Modificar la superficie mínima con validadores, trazabilidad y pruebas proporcionales. Preservar interfaces de módulos; usar evolución de esquema compatible con las versiones coexistentes aprobadas. La activación debe ser atómica y comprobada al ejecutar, sin fallback silencioso ante versión faltante. Ante caída del plano administrativo, sólo seguir con versiones aprobadas válidas.
4. **Verificar oráculos y fallos.** Comparar cálculos con vectores contractuales/financieros aprobados y reconstruir operaciones históricas con su versión original. Probar límites de vigencia, zona horaria, regla futura/vencida, scheduler caído, activación concurrente, paquete alterado y rol sin facultades. Probar flags intentando omitir autorización, aislamiento, partida doble o auditoría: deben fallar. Los controles legales aplicables tampoco son desactivables.
5. **Ensayar entrega y reversión.** Probar releases soportadas, migración de esquema y rollback con operaciones antes/después del cambio. Para imágenes propias, aplicar [Rust/scratch](../../../docs/deployment/rust-scratch.md): toolchain/lockfile/features/targets, enlace estático, SBOM y promoción del digest probado, incluyendo CA/zonas horarias y pruebas de terminación. Conservar cálculo y operación originales. Volver de software/configuración sólo afecta comportamiento futuro permitido; no borra contratos ni revierte pagos liquidados. Si se requiere rectificación, formular ajustes trazables y autorizados, conservando historia.
6. **Medir mantenibilidad.** Registrar horas desde solicitud hasta activación, trabajo por cliente, costo y causas de demora. Comparar con el objetivo aprobado para el tipo de cambio y TCO; no inventar una meta universal ni usar número de módulos como sustituto. Incluir al menos un caso representativo del cambio solicitado; no crear suites que sólo reflejen la implementación.

## Salida y estado

Entregar decisión de alcance, cambios realizados o diseño, matriz criterio–prueba–observado–evidencia, historial efectivo/registrado y brechas priorizadas. Identificar versiones, responsables y objetivo pendiente cuando corresponda. Marcar `sin evaluar` cuando falten pruebas; `implementado sin evidencia` cuando sólo exista código; `verificado` únicamente para el escenario observado. Una reversión técnica exitosa no demuestra conciliación financiera.
