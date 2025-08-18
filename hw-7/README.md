# Tarea: Chatbot con Capacidad de Búsqueda en Internet y Respuestas en Streaming

## Objetivo

Desarrollar un chatbot que funcione desde la consola, manteniendo la memoria de la conversación durante su ejecución y con la capacidad de realizar búsquedas en Internet para enriquecer sus respuestas. Este chatbot debe también proporcionar respuestas en streaming y citar las fuentes de donde extrajo la información.

## Requerimientos

1. **Interfaz de Consola:** El chatbot debe operar a través de una interfaz de consola, permitiendo a los usuarios hacer preguntas y recibir respuestas en tiempo real.

2. **Memoria de Conversación:** Durante el runtime, el chatbot debe recordar el historial de la conversación para utilizarlo como contexto en interacciones futuras.

3. **Búsqueda en Internet:** Implementar function calling para realizar búsquedas en Google usando la API de [https://serper.dev/](https://serper.dev/), que proporciona créditos gratuitos para búsquedas. El chatbot debe procesar información de los primeros 5 enlaces que resulten más relevantes para la pregunta del usuario.

4. **Respuestas en Streaming:** Las respuestas deben ser proporcionadas en tiempo real mientras se procesa la información recopilada, incluyendo una indicación de las fuentes de datos conforme se obtienen y procesan.

5. **Citar Fuentes:** Al final de cada respuesta, el chatbot debe proporcionar los enlaces o referencias de las páginas de donde ha extraído la información, asegurando la transparencia y permitiendo al usuario acceder a la fuente directamente.

## Especificaciones Técnicas

- **API de Búsqueda:** Utilizar la API de Serper.dev para realizar búsquedas en Google y obtener enlaces relevantes.
  
- **Extracción de Texto:** Desarrollar un módulo que visite cada uno de los primeros 5 enlaces recuperados y extraiga el texto principal de estas páginas.

- **Integración LLM:** Configurar la interacción con un modelo de lenguaje adecuado que pueda tomar tanto el historial de la conversación como los datos extraídos de Internet para generar respuestas coherentes y contextuales.

## Pruebas Automatizadas

Crear pruebas automatizadas que verifiquen la funcionalidad de cada componente, incluyendo la capacidad de realizar búsquedas efectivas, la extracción correcta del texto, y la generación adecuada de respuestas por parte del LLM.

## Ejemplo de Uso

```bash
> Usuario: ¿Cómo puedo plantar un árbol de manzanas?

> Chatbot: ** Búsqueda en internet **

> Chatbot: Según un artículo en GardeningKnowHow, el mejor momento para plantar árboles de manzana es al inicio de la primavera. También encontré información relevante en WikiHow y PlantingTutorial.com.

Referencias:
- [GardeningKnowHow](https://gardeningknowhow.com/apple-tree)

- [WikiHow](https://wikihow.com/plant-apple-trees)

- [PlantingTutorial.com](https://plantingtutorial.com/apple-trees).
```

## Entrega

- Código fuente completo del chatbot.
- Documentación que describa cómo opera el sistema, incluyendo instrucciones para ejecutar el chatbot y las pruebas.
- Archivo con pruebas unitarias.

## Requerimientos Técnicos de Software

Para poder realizar esta tarea en su computadora personal, los estudiantes deben asegurarse de contar con lo siguiente:

- **Python 3.10 o superior** instalado y agregado al `PATH`.  
- **Git** instalado (para clonar el repositorio y cambiar de rama).  
- **Entorno virtual** creado con `venv` o similar (`python -m venv .venv`).  
- Archivo `.env` en la raíz del proyecto con las siguientes variables:
   > SERPER_API_KEY=tu_clave_serper
   
   > OPENAI_API_KEY=tu_clave_llm
  
   > MODEL=gpt-4o-mini

## ⚙️ Requerimientos Técnicos de Software

Para poder desarrollar y ejecutar este proyecto en su computadora personal, los estudiantes deben asegurarse de tener instalado lo siguiente:

### 🛠️ Software Base
- [Node.js 18 o superior](https://nodejs.org/en/download)  
- [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) (incluido con Node.js) o [Yarn](https://classic.yarnpkg.com/lang/en/docs/install)  

### 📦 Dependencias principales  
Estas librerías se instalan automáticamente al ejecutar `npm install` en el proyecto.  

- [langchain](https://www.npmjs.com/package/langchain) → Framework para construir las cadenas y usar loaders.  
- [openai](https://www.npmjs.com/package/openai) → Cliente oficial para conectarse a la API de OpenAI.  
- [axios](https://www.npmjs.com/package/axios) o [node-fetch](https://www.npmjs.com/package/node-fetch) → Para llamadas HTTP a las fuentes de noticias.  
- [dotenv](https://www.npmjs.com/package/dotenv) → Para manejar variables de entorno.  
- (Opcional) [chalk](https://www.npmjs.com/package/chalk) o [ora](https://www.npmjs.com/package/ora) → Para mejorar la experiencia visual en la consola.  

