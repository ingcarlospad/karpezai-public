# Validación de las muestras públicas

Fecha: 21 de octubre de 2026. Entorno: Python 3.14 en Windows.

## KarpezVoz · componente real

`python examples/karpezvoz/demo.py`: se ejecutó `turns.py`, copiado sin cambios del proyecto real. Resultados sobre entradas sintéticas: ruido corto → `start, drop`; voz suficiente y silencio → `start, end`; silencio solo → ningún evento; duración máxima → `start, max`.

`python -m unittest discover -s examples/karpezvoz/tests -v`: **8 pruebas aprobadas**. Comprueban descarte de sonido breve, cierre tras silencio, ausencia de turnos ante silencio, límite de duración, reinicio del silencio cuando se retoma la voz, reinicio del detector, rechazo de configuración inválida y distinción entre etiquetas de ruido y palabras.

El SHA-256 del archivo publicado coincide con el original local; véase `examples/karpezvoz/PROVENANCE.json`. No se ejecutaron micrófono, reconocimiento, LLM ni síntesis de audio.

### Ejecución pública independiente

[GitHub Actions: ejecución aprobada](https://github.com/ingcarlospad/karpezai-public/actions/runs/39554760961), commit `abe594c4d3e08341a57004344c0b55c4ec631ea1`: comprobación de huella, demo y ocho pruebas en **Python 3.12 y Python 3.14 sobre Ubuntu**. Ambos trabajos terminaron correctamente. El workflow se conserva en `.github/workflows/public-voice-sample.yml`.

La primera ejecución detectó que Git había normalizado los saltos de línea del archivo original de Windows. Se corrigió conservando sus bytes mediante `.gitattributes`; la ejecución enlazada valida esa corrección. No se modificó la lógica del detector para obtener el resultado.

## Ejemplo conceptual de continuidad

Se ejecutó `python demo.py`: Fake A recibe la primera tarea, Fake B recibe la continuación y observa un mensaje previo; se conservan cuatro eventos.

Se ejecutó `python -m unittest -v`: tres pruebas aprobadas. Cubren conservación del historial y contexto al cambiar adaptador, rechazo de adaptador desconocido sin mutaciones y estabilidad del snapshot inmutable.

Los tres tests de esta sección corresponden exclusivamente al ejemplo conceptual nuevo. No validan las suites, seguridad, rendimiento ni integraciones del KarpezAI privado. Python 3.12 no se ejecutó localmente; su ejecución pública corresponde al componente de KarpezVoz descrito arriba.
