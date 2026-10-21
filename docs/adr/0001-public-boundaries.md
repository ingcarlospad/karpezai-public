# ADR público 0001 · Continuidad y límites de publicación

Fecha: 2026-10-21. Estado: decisión para esta documentación pública.

Ampliación posterior: [ADR 0002](0002-karpezvoz-source-sample.md) autoriza la muestra seleccionada de KarpezVoz. El runtime principal y su historial siguen privados.

## Contexto

Existe un repositorio privado con implementación, historia de desarrollo y material operativo. Publicarlo completo no es necesario para explicar el proyecto y puede exponer información o propiedad intelectual.

## Decisión

Mantener la implementación privada y preparar un repositorio público independiente con textos nuevos y un ejemplo sintético. No trasladar historial, configuraciones de proveedores, registros, prompts privados ni fuentes de terceros. Conservar el principio arquitectónico existente de estado canónico en el Core y proveedores reemplazables.

## Consecuencias

La demo puede reproducirse sin servicios externos, pero no acredita el funcionamiento del producto privado. La revisión pública del Core queda limitada. Cada nueva evidencia exige identificar origen, autoría, permiso de publicación y alcance probado.
