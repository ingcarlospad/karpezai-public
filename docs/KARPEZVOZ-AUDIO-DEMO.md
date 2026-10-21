# KarpezVoz · Sesión real con entrada de audio sintético

Fecha: 21 de octubre de 2026. Estado: demostración acotada de la sesión de aplicación; no es una prueba de micrófono o del navegador ni una certificación de calidad.

[Ver o descargar el video de 29 segundos](../assets/voice-demo/KarpezVoz-turno-real.mp4) · [Pregunta sintética WAV](../assets/voice-demo/KarpezVoz-pregunta-sintetica.wav) · [Respuesta real WAV](../assets/voice-demo/KarpezVoz-respuesta-real.wav) · [Registro del saludo](../assets/voice-demo/KarpezVoz-evidencia.json) · [Primer intento y su limitación](../assets/voice-demo/KarpezVoz-primer-intento.json)

## Qué se ejecutó

Se copió el paquete local de KarpezVoz a una carpeta de trabajo aislada. Se usaron sus clases reales `CharlaSession`, `Engine`, `WhisperCli`, `OllamaChat` y `PiperTts`. La entrada fue un WAV sintetizado para la demo, convertido a PCM mono de 16 kHz. La sesión lo transcribió con Whisper local, generó una respuesta con `qwen3.8:latest` mediante Ollama local y devolvió el audio generado por Piper.

La prueba usó contexto de 4096 tokens y rutas automáticas desactivadas. No se cargaron el glosario personal ni la búsqueda web, no se consultó la bóveda y no se usaron credenciales ni servicios de pago. No se modificó el paquete original ni se utilizó una voz de Carlos o audio de otra persona.

## Dos intentos, ambos documentados

| Intento | Pregunta sintética y transcripción | Respuesta real del modelo | Interpretación |
| --- | --- | --- | --- |
| 1 | «En una frase, ¿qué hace un asistente de voz?» → «en una frase que hace un asistente de voz.» | «Aquí Rose, ¿en qué puedo ayudarte hoy?» | La cadena produjo audio, pero la respuesta no contestó la pregunta explicativa. |
| 2 | «Hola, ¿cómo te llamas?» → «Hola, ¿cómo te llamas?» | «Me llamo Rose.» | El saludo fue transcrito y la sesión produjo una respuesta hablada pertinente. |

El video incluye la pregunta y la respuesta del segundo intento y explica el límite observado en el primero. La narración introductoria y final también es sintética y se distingue de las secciones de pregunta y respuesta.

## Alcance

Este resultado amplía la muestra del detector: aquí sí se ejecutaron ASR, modelo y TTS reales dentro de una sesión. No se probó captura por micrófono, reproducción desde el navegador, interrupción humana en vivo, búsqueda web, cuotas, integración con el Core privado ni una conversación prolongada. No se publican cifras de latencia o precisión ni se interpreta un saludo correcto como validación general del asistente.

Los registros públicos solo contienen preguntas sintéticas, respuestas de esas sesiones y tipos de eventos. Configuración, rutas locales, glosario, bóveda, modelos, binarios y código restante permanecen privados.
