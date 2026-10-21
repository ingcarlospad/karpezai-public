# KarpezAI · Ingeniería de un runtime de agentes

Proyecto técnico de Carlos Padilla / Karpeztec. **En desarrollo; runtime principal privado.** Este repositorio contiene documentación y una muestra de código real de KarpezVoz, derivado del trabajo de voz de KarpezAI. No es una distribución completa del runtime ni una afirmación de madurez comercial.

KarpezAI explora cómo conservar contexto y estado de trabajo al cambiar modelos, proveedores y herramientas, con decisiones de permisos y evidencia verificable bajo control del runtime.

| Evidencia | Alcance |
| --- | --- |
| [Estado](docs/STATUS.md) | Implementación observada, planes y límites de verificación |
| [Arquitectura](docs/ARCHITECTURE.md) | Separación entre Core, adaptadores y herramientas |
| [Decisiones](docs/adr/0001-public-boundaries.md) | Límites de publicación y continuidad |
| [Especificación educativa](docs/spec/demo.md) | Contrato reproducible con datos sintéticos |
| [KarpezVoz: código real, demo y pruebas](examples/karpezvoz/README.md) | Detector original de fin de turno, sin dependencias; entradas sintéticas |
| [Decisión de publicación del componente](docs/adr/0002-karpezvoz-source-sample.md) | Procedencia, revisión y alcance de lo publicado |
| [Ejemplo conceptual anterior](demo.py) | Adaptadores falsos; no es implementación del runtime |
| [Trabajo con Codex](docs/CODEX.md) | Atribución honesta, dirección humana y evidencia disponible |

## Ejecutar el componente real publicado

Python 3.12 o superior. Desde esta carpeta:

```sh
python examples/karpezvoz/demo.py
python -m unittest discover -s examples/karpezvoz/tests -v
```

No requiere claves, red, modelos, bases de datos, micrófono ni cuentas. Ejecuta el detector real sobre secuencias artificiales: cierre por silencio, descarte de sonido breve y límite de duración. **No valida ASR, LLM, TTS ni el Core privado.** Consulte [los resultados y sus límites](VALIDATION.md).

## Dos proyectos, evidencias diferentes

[Karpeztec showcase](https://github.com/ingcarlospad/karpeztec-showcase) presenta Bloom como caso de uso real, según Carlos. KarpezAI muestra un proyecto técnico en evolución. No se publican métricas de adopción, rendimiento o ahorro ni se afirma que el runtime esté desplegado comercialmente.

La documentación no implica afiliación, selección ni respaldo de OpenAI u otros proveedores. Derechos reservados; véase [NOTICE](NOTICE.md).
