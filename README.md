# Core bancario para Argentina

Proyecto de software libre conforme a **[GNU GPL v2](LICENSE)**. Las contribuciones se proponen mediante ramas/PR y **sólo [@andrescastiglia](https://github.com/andrescastiglia) realiza merges a `main`**. Ver [gobierno](GOVERNANCE.md) y [contribuciones](CONTRIBUTING.md).

Proyecto en etapa de diseño y validación de producto. El repositorio reúne investigación de mercado, cumplimiento, arquitectura, requisitos y workflows locales; todavía no contiene una implementación bancaria ni evidencia de operación productiva.

El stack elegido usa **Rust** para dominio y servicios, e imágenes propias con runtime **`FROM scratch`** para Kubernetes. El [contrato de construcción y ejecución](docs/deployment/rust-scratch.md) concreta binarios estáticos, dependencias de runtime, seguridad y pruebas requeridas.

- [Documentación general](docs/README.md): mercado, normativa y arquitectura modular.
- [Requisitos funcionales](docs/functional/README.md): 1.016 FR organizados en 32 módulos.
- [ADR](docs/adr/README.md) y [NFR](docs/nfr/README.md): decisiones propuestas y calidad verificable.
- [Revisión integral y plan de mejoras](docs/review/README.md): análisis comercial, contable, legal, técnico, QA, seguridad, rentabilidad y operaciones.
- [Skills locales](docs/skills.md): workflows reutilizables para desarrollar y revisar el proyecto.
- [Vigilancia normativa diaria](docs/regulatory-watch/README.md): agente de IA, fuentes oficiales, cobertura, agenda y propuestas sin merge automático.
- [Plan de implementación por fases](PLAN_DE_IMPLEMENTACION_BANK.md): actualización legal, mercado, tecnología y seguridad, con propuestas trazables, esfuerzo y cobertura real de fuentes.

La cobertura documental no acredita implementación, licencia, homologación o cumplimiento efectivo. Los documentos distinguen perfil jurídico, fuentes verificadas, supuestos, decisiones y evidencia pendiente. El corte normativo original es 15/10/2026; la revisión integral corresponde al 16/10/2026.

La decisión del mantenedor conserva la licencia existente y la orientación libre del proyecto. La procedencia/compatibilidad de aportes y las obligaciones de quien preste servicios financieros reales se revisan en su alcance; ni una PR ni la licencia acreditan cumplimiento operativo.
