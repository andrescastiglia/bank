# Requisitos funcionales del core bancario argentino

Los **Functional Requirements (FR)** especifican comportamientos verificables por módulo, incluyendo aceptación, excepciones, perfiles regulatorios y trazabilidad. Se desarrolla la biblioteca completa documentada: núcleo, crédito, pagos, banca y extensiones por rol, además de la ruta comercial inicial.

**Estado: Propuesto. Implementación y evidencia: sin evaluar. Base documental: 15/10/2026.** La cobertura se refiere al inventario existente, con sus condiciones y pendientes; no acredita cumplimiento legal, licencia, homologación ni certificación.

Leer primero [alcance y contrato común](scope.md). Consultar la [matriz de cobertura](coverage.md), los [flujos integrados de aceptación](flows.md) y el [catálogo estructurado](catalog.json). Las columnas de trazabilidad remiten a [cumplimiento](../compliant.md), [controles técnicos](../../.agents/skills/core-bancario-argentina/references/controles.md), [ADR](../adr/README.md) y [NFR](../nfr/README.md). La [arquitectura](../achitecture.md) define autoridad y fronteras; el [mercado](../market_analysis.md) orienta producto, integración, costos y secuencia comercial.

## Módulos

<!-- catalog:start -->
**1016 FR en 32 módulos.** Los conteos se extraen de las filas de requisitos.

| Nº | Código | Módulo | FR |
|---:|---|---|---:|
| 01 | ENT | [Entidades, perímetro y organización](01-entidades-perimetro.md) | 31 |
| 02 | IAM | [Identidad y accesos](02-identidad-accesos.md) | 30 |
| 03 | CLI | [Personas, clientes y KYC](03-personas-clientes-kyc.md) | 31 |
| 04 | CFG | [Productos, parámetros y reglas](04-productos-configuracion.md) | 30 |
| 05 | CON | [Contratos, documentos y consentimientos](05-contratos-documentos.md) | 27 |
| 06 | ACC | [Cuentas y depósitos](06-cuentas-depositos.md) | 30 |
| 07 | BAL | [Saldos, reservas y restricciones](07-saldos-reservas-restricciones.md) | 30 |
| 08 | LED | [Ledger, contabilidad y cierres](08-ledger-contabilidad-cierres.md) | 30 |
| 09 | CRE | [Originación y administración de crédito](09-originacion-administracion-credito.md) | 33 |
| 10 | INT | [Intereses, comisiones y liquidación de conceptos](10-intereses-comisiones.md) | 30 |
| 11 | GAR | [Garantías, avales y compromisos](11-garantias-avales.md) | 26 |
| 12 | COL | [Cobranzas, mora y recupero](12-cobranzas-mora-recupero.md) | 28 |
| 13 | PAY | [Pagos y transferencias](13-pagos-transferencias.md) | 31 |
| 14 | CHQ | [Cheques, ECHEQ, CEDIP e instrumentos documentales](14-cheques-echeq-cedip.md) | 30 |
| 15 | CRD | [Tarjetas, procesamiento y adquirencia](15-tarjetas-adquirencia.md) | 34 |
| 16 | CSH | [Caja, sucursales y efectivo](16-caja-sucursales-efectivo.md) | 30 |
| 17 | TRE | [Tesorería y liquidez](17-tesoreria-liquidez.md) | 30 |
| 18 | FXT | [Exterior, cambios y comercio internacional](18-exterior-cambios-comercio.md) | 37 |
| 19 | INV | [Inversiones, custodia y fondos](19-inversiones-custodia-fondos.md) | 34 |
| 20 | AML | [Prevención LA/FT/FP](20-prevencion-la-ft-fp.md) | 31 |
| 21 | FRD | [Prevención y gestión de fraude](21-prevencion-fraude.md) | 28 |
| 22 | REC | [Conciliación y excepciones](22-conciliacion-excepciones.md) | 31 |
| 23 | RSK | [Riesgos, prudencia y exposiciones](23-riesgos-prudencia-exposiciones.md) | 35 |
| 24 | TAX | [Tributos, recaudaciones e intercambio fiscal](24-tributos-recaudaciones.md) | 32 |
| 25 | RPT | [Localización y reportes regulatorios](25-reportes-localizacion.md) | 38 |
| 26 | CST | [Canales, atención y protección de usuarios](26-canales-atencion-usuarios.md) | 32 |
| 27 | DAT | [Auditoría, privacidad y archivo](27-auditoria-privacidad-archivo.md) | 30 |
| 28 | ASY | [Integraciones, eventos y trabajos](28-integraciones-eventos-trabajos.md) | 32 |
| 29 | MIG | [Carga inicial, migración y salida](29-carga-inicial-migracion-salida.md) | 33 |
| 30 | OPS | [Operación, continuidad y terceros](30-operacion-continuidad-terceros.md) | 42 |
| 31 | AIG | [Gobierno de modelos e inteligencia artificial](31-gobierno-modelos-ia.md) | 32 |
| 32 | COR | [Corresponsalía, BaaS y plataformas](32-corresponsalia-baas-plataformas.md) | 38 |
<!-- catalog:end -->

## Cómo convertirlos en una entrega verificable

1. Registrar en ENT sociedad, perfil/rol, productos, monedas, países, canales y fecha. Fundamentar lo aplicable, condicional o excluido.
2. Seleccionar módulos y dependencias de la ruta inicial; los controles de un producto activo se aplican desde su primer uso.
3. Derivar casos de aceptación de cada FR y de los flujos integrados: escenario permitido, denegado, concurrencia, fallo y reparación pertinentes. Asociar los criterios NFR sin sustituir sus métricas/oráculos.
4. Implementar y probar contra versiones de reglas, redes y contratos efectivas. Conservar datos de prueba, resultado esperado/observado y evidencia por entidad/versión.
5. Registrar por separado implementación, verificación y aprobación institucional. Una exclusión requiere fundamento; un archivo no cambia un requisito a «cumplido».

Las etapas BASE, CREDITO, PAGOS, BANCA y EXT se definen en [scope.md](scope.md). Los estados `202`, confirmado local, enviado, incierto y liquidado tienen significados distintos. El cierre de un módulo depende también de sus excepciones y contratos operativos; no basta implementar el camino feliz de sus filas.

## Catálogo y verificación reproducible

[coverage_map.json](coverage_map.json) mantiene la relación revisada entre módulos lógicos, necesidades comerciales, capacidades descritas en prosa y FR concretos. [tools/build_catalog.py](tools/build_catalog.py) extrae las tablas de los 32 módulos y el inventario vigente de los documentos fuente; genera el catálogo, la matriz y el índice con sus conteos y huellas SHA-256. No instala dependencias ni modifica documentos de negocio.

Desde la raíz del repositorio:

```sh
python3 docs/functional/tools/build_catalog.py
python3 docs/functional/tools/build_catalog.py --check
```

La verificación controla inventario, secuencias, unicidad, cinco columnas, fuentes existentes, cobertura referenciada, relaciones manuales, enlaces locales y reproducción exacta de los artefactos. No interpreta leyes ni sustituye la revisión semántica, pruebas del software o una auditoría. Al modificar un FR o una fuente, revisar primero el impacto y después regenerar; no agregar referencias ajenas al comportamiento para elevar un porcentaje.
