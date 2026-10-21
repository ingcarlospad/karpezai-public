# Validación del ejemplo público

Fecha: 21 de octubre de 2026. Entorno: Python 3.14 en Windows.

Se ejecutó `python demo.py`: Fake A recibe la primera tarea, Fake B recibe la continuación y observa un mensaje previo; se conservan cuatro eventos.

Se ejecutó `python -m unittest -v`: tres pruebas aprobadas. Cubren conservación del historial y contexto al cambiar adaptador, rechazo de adaptador desconocido sin mutaciones y estabilidad del snapshot inmutable.

Estos resultados corresponden exclusivamente al ejemplo educativo nuevo. No validan las suites, seguridad, rendimiento ni integraciones del KarpezAI privado. Python 3.12 no se ejecutó en esta preparación.
