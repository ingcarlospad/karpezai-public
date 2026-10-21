# KarpezVoz · Componente real y ejecutable

`turns.py` es una copia sin cambios del detector de fin de turno presente en la instalación local de KarpezVoz de Carlos al 21 de octubre de 2026. Su documentación de origen lo vincula con las reglas de conversación M23 de KarpezAI. Esta muestra reemplaza a la demo de adaptadores falsos como evidencia técnica principal de este repositorio.

La aplicación KarpezVoz deriva de la función «Charla» de KarpezAI y puede ejecutarse aparte. La muestra pública contiene **un componente**, no toda la aplicación: detecta el inicio y el fin de un turno a partir de niveles de señal y duraciones. Descarta sonidos breves y aplica un límite temporal. Las secuencias de entrada de esta demo son sintéticas.

## Ejecutar desde la raíz del repositorio

```sh
python examples/karpezvoz/demo.py
python -m unittest discover -s examples/karpezvoz/tests -v
```

Python 3.12 o superior; sin dependencias, red, claves, micrófono ni modelos. La ejecución comprobada se registra en [VALIDATION](../../VALIDATION.md).

## Qué demuestra

Permite inspeccionar y probar código real usado por KarpezVoz: cuándo cerrar una intervención y cuándo descartar un sonido demasiado corto. La demo no simula resultados de pruebas del detector; ejecuta el código extraído sobre entradas artificiales.

## Qué no demuestra

No prueba reconocimiento de voz, calidad de audio, latencia, cancelación del modelo, síntesis de voz, búsqueda web, seguridad del servidor ni integración con el Core. No es una demo de voz de extremo a extremo. Los umbrales y el detector son una heurística de energía y duración, no un sistema de detección de voz basado en un modelo.

## Procedencia y atribución

El hash SHA-256 del archivo publicado se compara con el original en `PROVENANCE.json`. Los tests y el lanzador públicos son nuevos y fueron preparados con Codex para esta publicación. No se atribuye a Codex la autoría histórica de `turns.py`: no se verificó la sesión que lo creó.

Se excluyen configuraciones, glosarios privados, dispositivos emparejados, bóvedas, puentes de proveedores y archivos de datos. Derechos reservados según el aviso del repositorio; no se anuncia una licencia de código abierto.
