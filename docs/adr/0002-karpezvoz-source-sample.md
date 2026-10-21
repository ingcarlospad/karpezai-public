# ADR público 0002 · Publicar un componente real de KarpezVoz

Fecha: 2026-10-21. Estado: aplicado a esta publicación, bajo la solicitud de Carlos de usar KarpezVoz como parte de la evidencia de KarpezAI.

## Problema

La demo inicial de adaptadores falsos explicaba una idea, pero no permitía inspeccionar código de los proyectos reales. Carlos pidió aprovechar KarpezVoz, que deriva del trabajo de voz de KarpezAI.

## Decisión

Publicar únicamente `turns.py`, un componente determinista sin I/O ni dependencias externas. Conservar sus bytes y registrar SHA-256 para distinguir el código original del lanzador y los tests nuevos. Publicar pruebas reproducibles sobre secuencias sintéticas de niveles y duraciones.

## Revisión de límites

Se leyó el archivo completo. Contiene reglas, tipos, configuración genérica y comentarios técnicos; no contiene credenciales, datos de clientes, grabaciones, glosarios personales, rutas de usuario ni datos de dispositivos. No se copian configuración operativa, servidor, bóveda, bridges, modelos, binarios ni archivos de terceros. La procedencia se basa en el componente y la documentación locales; no se certifica un análisis completo de la cadena histórica de propiedad intelectual.

## Consecuencias

El repositorio ahora incluye una muestra de implementación real además de documentación. El runtime completo sigue privado. La publicación de este componente no implica que toda KarpezVoz o KarpezAI sea código abierto ni prueba una conversación de voz de extremo a extremo. La atribución histórica a Codex no se verificó; los tests y el lanzador públicos sí se prepararon con Codex.
