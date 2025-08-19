# LLM Chat Completion Mock Server

Este proyecto es un servidor muy simple escrito en Python que emula el endpoint de chat completion de OpenAI. Su objetivo es facilitar el desarrollo y pruebas de integraciones que dependen de la API de OpenAI, sin necesidad de conectarse a los servicios reales.

## Características

- Emulación básica del endpoint `/v1/chat/completions` de OpenAI.
- Respuestas mock configurables o predefinidas.
- Fácil de ejecutar y modificar.

## Uso

1. Clona este repositorio.
2. Instala las dependencias (ver sección de instalación próximamente).
3. Ejecuta el servidor Python.
4. Realiza peticiones HTTP al endpoint mock para probar tu integración.

## Estado

En desarrollo inicial. Próximamente se agregarán instrucciones detalladas y ejemplos de uso.

## Instalación y ejecución

1. Crea un entorno virtual (recomendado):

   ```bash
   python3 -m venv venv
   ```

2. Activa el entorno virtual:

   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - En Windows:
     ```cmd
     venv\Scripts\activate
     ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta el servidor:

   ```bash
   uvicorn main:app --reload
   ```
