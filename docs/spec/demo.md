# Contrato del ejemplo público

El ejemplo educativo debe conservar una conversación al alternar Fake A y Fake B. Cada mensaje conserva secuencia, emisor y contenido. Un adaptador recibe una copia inmutable de la historia disponible y produce una respuesta determinista. Un adaptador desconocido se rechaza antes de añadir eventos.

Criterios: alternar proveedores conserva eventos anteriores; el adaptador puede ver contexto anterior; el historial entregado no permite modificar el estado interno; una selección inválida no modifica el historial. Las pruebas cubren estos casos con datos sintéticos.

Fuera de alcance: persistencia durable, red, LLM, permisos reales, caché KV, seguridad de procesos, integración del runtime y rendimiento. No debe usarse como implementación de producción.
