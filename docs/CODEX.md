# Cómo se usa Codex y qué evidencia existe

## Bloom: declaración de Carlos

Carlos confirma que Bloom fue construido enteramente con Codex y ChatGPT mediante la extensión Roo Code, mientras él dirigía el desarrollo, probaba y corregía el producto. Esta es una declaración del propietario; no una medición de autoría por commit ni un reparto porcentual entre herramientas. El producto se utiliza en un negocio real, según su confirmación. El código y los datos siguen privados. Roo Code se identifica como la extensión utilizada; no se presenta como un producto de OpenAI.

## KarpezAI: atribución limitada

La documentación local contempla varios agentes y herramientas. No se atribuye todo KarpezAI a Codex ni se atribuyen a Codex cambios cuyo autor y sesión no fueron comprobados. La presencia de integración con Codex no demuestra que Codex haya creado el componente.

## Caso verificable de esta preparación

Carlos pidió organizar las evidencias públicas, separar producción de experimentos y revisar privacidad. Codex recuperó el contexto autorizado, examinó documentación y un archivo de pruebas local, detectó la diferencia entre el README inicial y el avance posterior y redactó este repositorio público sin copiar implementación privada. También creó una demo pedagógica y pruebas independientes. El resultado de ejecución se registra en `VALIDATION.md`.

Después, Carlos pidió aprovechar KarpezVoz. Codex seleccionó un componente real sin I/O, cotejó su hash con el original, preparó un lanzador y ocho pruebas públicas y ejecutó la muestra. La copia exacta y su procedencia están documentadas; esto no atribuye retrospectivamente a Codex la creación del detector original.

Para Bloom, Codex preparó una copia local aislada, una base nueva con datos ficticios y desactivó el asistente y los procesos periódicos en el entorno de demo. Comprobó creación de citas e ingresos y rechazo de solapamientos, además de ejecutar las trece pruebas existentes del piloto con Claude simulado y SQLite temporal. Esto verifica comportamientos acotados del código local, no una llamada real a Claude ni resultados comerciales.

Esto demuestra un flujo de revisión y documentación con Codex. No demuestra que se haya depurado un defecto del runtime privado durante esta sesión.

## Guía para publicar una próxima sesión real

1. Carlos define el problema, restricciones y criterio de aceptación con datos ficticios.
2. Codex propone el diagnóstico o cambio; Carlos revisa el alcance.
3. Se registra una prueba de regresión que falla antes y pasa después, si corresponde.
4. Se documentan decisiones de arquitectura, alternativas y limitaciones.
5. Carlos revisa el resultado y decide su integración.
6. Se publica un resumen sanitizado con enlaces verificables y sin conversaciones privadas completas.

Este flujo es una propuesta educativa; no se presenta como una cronología histórica ya comprobada. No hay cifras de productividad ni porcentajes de código generado.
