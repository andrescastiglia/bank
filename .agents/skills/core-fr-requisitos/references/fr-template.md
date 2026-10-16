# Ficha y revisión de un FR

```text
ID / módulo / título:
Estado: propuesto, aceptado, reemplazado o retirado; decisión y evidencia:
Sociedad, perfil/rol, producto, moneda, canal, jurisdicción y etapa:
Actor/facultad y disparador:
Precondiciones, entradas y contrato de datos asociado:
Comportamiento y resultado observable:
Estado/confirmación que se devuelve y siguiente acción permitida:
Excepciones, concurrencia, reintento y corrección pertinentes:
Fuente, versión, aplicabilidad y naturaleza de la relación:
NFR/ADR/CTL y dependencias funcionales:
Casos de aceptación / fixture / oráculo independiente:
Implementación y evidencia: no evaluado salvo ejecución registrada:
Versión anterior / motivo / impacto / reemplazo si corresponde:
```

## Revisión mínima según cambio

| Cambio | Verificación material |
|---|---|
| Regla monetaria/tributaria | Vectores independientes, fechas/vigencias, redondeo, efecto en contrato y reporte |
| Dinero/asincronía | Duplicado de mensaje, ingresos reales distintos, concurrencia y fallo antes/después de commit/envío |
| Bulk/DR | Transacción fuente completa, aislamiento PREPARED, autoridad única y reconstrucción/conciliación |
| Identidad/datos | Acceso cruzado, revocación efectiva, independencia real de personas, secreto ROS y finalidad |
| Texto/enlace menor | Fidelidad al significado y enlaces/artefactos pertinentes; sin cargas de producto innecesarias |

El retiro debe ser rastreable en catálogos y mapas, sin reutilizar su ID. Un cambio de significado con el mismo identificador exige revisar relaciones y evidencia; no basta regenerar un JSON.
