# Cómo se usa Codex y qué evidencia existe

## Bloom: declaración de Carlos

En el contexto aportado, Carlos declara: «Codex escribió el código y yo dirigí el desarrollo, probé y corregí el producto». Esta es una declaración del propietario; no un análisis de autoría por commit. El producto se utiliza en un negocio real, según su confirmación. El código y los datos siguen privados.

## KarpezAI: atribución limitada

La documentación local contempla varios agentes y herramientas. No se atribuye todo KarpezAI a Codex ni se atribuyen a Codex cambios cuyo autor y sesión no fueron comprobados. La presencia de integración con Codex no demuestra que Codex haya creado el componente.

## Caso verificable de esta preparación

Carlos pidió organizar las evidencias públicas, separar producción de experimentos y revisar privacidad. Codex recuperó el contexto autorizado, examinó documentación y un archivo de pruebas local, detectó la diferencia entre el README inicial y el avance posterior y redactó este repositorio público sin copiar implementación privada. También creó una demo pedagógica y pruebas independientes. El resultado de ejecución se registra en `VALIDATION.md`.

Esto demuestra un flujo de revisión y documentación con Codex. No demuestra que se haya depurado un defecto del runtime privado durante esta sesión.

## Guía para publicar una próxima sesión real

1. Carlos define el problema, restricciones y criterio de aceptación con datos ficticios.
2. Codex propone el diagnóstico o cambio; Carlos revisa el alcance.
3. Se registra una prueba de regresión que falla antes y pasa después, si corresponde.
4. Se documentan decisiones de arquitectura, alternativas y limitaciones.
5. Carlos revisa el resultado y decide su integración.
6. Se publica un resumen sanitizado con enlaces verificables y sin conversaciones privadas completas.

Este flujo es una propuesta educativa; no se presenta como una cronología histórica ya comprobada. No hay cifras de productividad ni porcentajes de código generado.
