# KarpezAI · Ingeniería de un runtime de agentes

Proyecto técnico de Carlos Padilla / Karpeztec. **En desarrollo; implementación privada.** Este repositorio público contiene documentación y un ejemplo educativo independiente. No es una distribución del runtime ni una afirmación de madurez comercial.

KarpezAI explora cómo conservar contexto y estado de trabajo al cambiar modelos, proveedores y herramientas, con decisiones de permisos y evidencia verificable bajo control del runtime.

| Evidencia | Alcance |
| --- | --- |
| [Estado](docs/STATUS.md) | Implementación observada, planes y límites de verificación |
| [Arquitectura](docs/ARCHITECTURE.md) | Separación entre Core, adaptadores y herramientas |
| [Decisiones](docs/adr/0001-public-boundaries.md) | Límites de publicación y continuidad |
| [Especificación educativa](docs/spec/demo.md) | Contrato reproducible con datos sintéticos |
| [Demo](demo.py) y [pruebas](test_demo.py) | Ejemplo nuevo, sin dependencias ni proveedores reales |
| [Trabajo con Codex](docs/CODEX.md) | Atribución honesta, dirección humana y evidencia disponible |

## Ejecutar el ejemplo público

Python 3.12 o superior. Desde esta carpeta:

```sh
python demo.py
python -m unittest -v
```

No requiere claves, red, modelos, bases de datos ni cuentas. Prueba la idea de conservar un historial al alternar dos adaptadores falsos. **No ejecuta ni valida el Core privado de KarpezAI.**

## Dos proyectos, evidencias diferentes

[Karpeztec showcase](https://github.com/ingcarlospad/karpeztec-showcase) presenta Bloom como caso de uso real, según Carlos. KarpezAI muestra un proyecto técnico en evolución. No se publican métricas de adopción, rendimiento o ahorro ni se afirma que el runtime esté desplegado comercialmente.

La documentación no implica afiliación, selección ni respaldo de OpenAI u otros proveedores. Derechos reservados; véase [NOTICE](NOTICE.md).
