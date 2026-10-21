# De una muestra local a una prueba pública: el fallo que encontró CI

Esta nota documenta un problema real de publicación encontrado y corregido durante la preparación con Codex del 21 de octubre de 2026. El problema pertenece al empaquetado de la muestra, no al reconocimiento de voz ni al Core privado.

## Objetivo definido por Carlos

Mostrar código real de KarpezVoz como evidencia de KarpezAI, con pruebas que otros puedan ejecutar, conservando privados el resto del runtime, configuraciones y datos. Codex preparó la selección, documentación, lanzador y tests. No se verificó quién escribió históricamente el detector.

## Lo que falló

El archivo `turns.py` se copió de la instalación local y su SHA-256 coincidía con el original. Los ocho tests de comportamiento pasaron en Windows. Sin embargo, la [primera ejecución pública](https://github.com/ingcarlospad/karpezai-public/actions/runs/39554715081) falló en la comprobación de huella tanto en Python 3.12 como en 3.14, antes de llegar a los tests del detector.

Eso no demostraba un defecto de su lógica. Mostraba que los bytes del archivo entregado a CI no eran los bytes registrados en la procedencia.

## Diagnóstico

Codex comparó el objeto guardado por Git con los bytes locales. La normalización de finales de línea había convertido el archivo CRLF de Windows a LF dentro de Git. El texto ejecutable era equivalente para Python, pero el hash de bytes era diferente.

La prueba de procedencia era útil precisamente porque detectó la diferencia: una afirmación de «copia exacta» necesita comprobar el artefacto publicado, además del archivo antes del commit.

## Corrección

Se añadió una regla específica para el archivo extraído:

```gitattributes
/examples/karpezvoz/turns.py -text whitespace=cr-at-eol
```

`-text` conserva los bytes de este componente. `whitespace=cr-at-eol` permite reconocer su final de línea al comprobar espacios. El resto de los archivos mantiene el comportamiento habitual de Git. La [corrección publicada](https://github.com/ingcarlospad/karpezai-public/commit/abe594c4d3e08341a57004344c0b55c4ec631ea1) preservó el original sin alterar la lógica del detector.

## Resultado verificable

La [ejecución posterior](https://github.com/ingcarlospad/karpezai-public/actions/runs/39554760961) pasó: huella de procedencia, demo y ocho tests de comportamiento en Python 3.12 y 3.14 sobre Linux. El hash publicado volvió a coincidir con el original local.

Es un caso acotado de dirección humana y trabajo con Codex: objetivo y límites de publicación, preparación de pruebas, fallo observable, diagnóstico, corrección y nueva verificación. No mide productividad, no prueba calidad de voz y no convierte la muestra en una auditoría del runtime completo.

## Qué puede reutilizar otro builder

Si publicas una extracción exacta desde Windows, decide si necesitas identidad de texto o identidad de bytes. Para identidad de bytes, registra la huella antes de publicar y compruébala después del checkout en CI. Mantén separados los tests del comportamiento y los de procedencia: pueden fallar por razones distintas.
