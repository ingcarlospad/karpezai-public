# Estado y calidad de evidencia · 21 de octubre de 2026

| Área | Estado | Qué se comprobó en esta preparación |
| --- | --- | --- |
| Bloom | En uso en un salón, según Carlos | Declaración del propietario; sin acceder a producción ni a datos del negocio |
| KarpezAI | Implementación privada en desarrollo | Existen Core, contratos, API, clientes, adaptadores y pruebas locales |
| Core independiente de proveedor | Decisión de arquitectura | README, ADR-0001 y criterios M0 consultados; no se ejecutó la suite privada |
| Herramientas y permisos | Código de prueba presente | Se leyó una prueba M9 que rechaza herramientas desconocidas y trata resultados como datos no confiables; presencia no equivale a ejecución aprobada |
| Fachada compatible e imágenes | Integradas en el historial local observado | Commit de checkout `69e70a76`, con merges de PR #49 y #50; no se reprodujeron las pruebas vivas |
| Voz natural | Experimental | Rama de trabajo local; no se anuncia completada |
| M28/M29/M30 | Estado no consolidado aquí | Las notas locales y el checkout consultado describen estados distintos; no se publica un resumen de hitos completados |
| Demo de este repositorio | Ejemplo educativo nuevo | Adaptadores falsos y datos sintéticos; no representa una sesión real del runtime |

El README privado describe el bootstrap M0 y no basta para resumir el avance posterior. Las especificaciones son objetivos de aceptación, no certificados de cumplimiento. No se trasladan cifras de suites ni benchmarks sin ejecución y procedencia reproducible.

Pendiente para ampliar evidencia pública: exportar un caso real sanitizado con objetivo, revisión humana, cambio concreto, prueba de regresión y resultado reproducible. También falta una demostración pública del runtime privado libre de información confidencial.
