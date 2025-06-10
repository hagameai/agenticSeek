# AgenticSeek: Alternativa Privada y Local a Manus.

<p align="center">
<img align="center" src="./media/agentic_seek_logo.png" width="300" height="300" alt="Agentic Seek Logo">
<p>

  [English](./README.md) | [中文](./README_CHS.md) | [繁體中文](./README_CHT.md) | [Français](./README_FR.md) | [日本語](./README_JP.md) | [Português (Brasil)](./README_PTBR.md) | [Español](./README_ES.md)

*Una **alternativa 100% local a Manus AI**, este asistente de IA con capacidad de voz navega autónomamente por la web, escribe código y planifica tareas mientras mantiene todos los datos en tu dispositivo. Diseñado para modelos de razonamiento local, funciona completamente en tu hardware, garantizando privacidad total y cero dependencia de la nube.*

[![Visit AgenticSeek](https://img.shields.io/static/v1?label=Website&message=AgenticSeek&color=blue&style=flat-square)](https://fosowl.github.io/agenticSeek.html) ![License](https://img.shields.io/badge/license-GPL--3.0-green) [![Discord](https://img.shields.io/badge/Discord-Join%20Us-7289DA?logo=discord&logoColor=white)](https://discord.gg/8hGDaME3TC) [![Twitter](https://img.shields.io/twitter/url/https/twitter.com/fosowl.svg?style=social&label=Update%20%40Fosowl)](https://x.com/Martin993886460) [![GitHub stars](https://img.shields.io/github/stars/Fosowl/agenticSeek?style=social)](https://github.com/Fosowl/agenticSeek/stargazers)

### ¿Por qué AgenticSeek?

* 🔒 Totalmente Local y Privado - Todo se ejecuta en tu máquina — sin nube, sin compartir datos. Tus archivos, conversaciones y búsquedas permanecen privados.

* 🌐 Navegación Web Inteligente - AgenticSeek puede navegar por internet por sí mismo — buscar, leer, extraer información, llenar formularios web — todo sin intervención manual.

* 💻 Asistente de Código Autónomo - ¿Necesitas código? Puede escribir, depurar y ejecutar programas en Python, C, Go, Java y más — todo sin supervisión.

* 🧠 Selección Inteligente de Agentes - Tú preguntas, él determina el mejor agente para el trabajo automáticamente. Como tener un equipo de expertos listos para ayudar.

* 📋 Planifica y Ejecuta Tareas Complejas - Desde planificación de viajes hasta proyectos complejos — puede dividir grandes tareas en pasos y completarlas usando múltiples agentes de IA.

* 🎙️ Habilitado por Voz - Voz y texto a voz limpios, rápidos y futuristas que te permiten hablar con él como si fuera tu IA personal de una película de ciencia ficción. (En progreso)

### **Demo**

> *¿Puedes buscar el proyecto agenticSeek, aprender qué habilidades se requieren, luego abrir el CV_candidates.zip y decirme cuáles coinciden mejor con el proyecto?*

https://github.com/user-attachments/assets/b8ca60e9-7b3b-4533-840e-08f9ac426316

Descargo de responsabilidad: Esta demo, incluyendo todos los archivos que aparecen (ej: CV_candidates.zip), son completamente ficticios. No somos una corporación, buscamos contribuidores de código abierto, no candidatos.

> 🛠⚠️️ **Trabajo Activo en Progreso**

> 🙏 Este proyecto comenzó como un proyecto secundario y no tiene hoja de ruta ni financiamiento. Ha crecido mucho más allá de lo que esperaba al terminar en GitHub Trending. Las contribuciones, comentarios y paciencia son profundamente apreciados.

## Prerrequisitos

Asegúrate de tener instalado chrome driver, docker y python3.10.

Para problemas relacionados con chrome driver, consulta la sección **Chromedriver**.

### 1. **Clonar el repositorio y configuración**

```sh
git clone https://github.com/Fosowl/agenticSeek.git
cd agenticSeek
mv .env.example .env
```

### 2. Cambiar el contenido del archivo .env

```sh
SEARXNG_BASE_URL="http://127.0.0.1:8080"
REDIS_BASE_URL="redis://redis:6379/0"
WORK_DIR="/Users/mlg/Documents/workspace_for_ai"
OLLAMA_PORT="11434"
LM_STUDIO_PORT="1234"
CUSTOM_ADDITIONAL_LLM_PORT="11435"
OPENAI_API_KEY='opcional'
DEEPSEEK_API_KEY='opcional'
OPENROUTER_API_KEY='opcional'
TOGETHER_API_KEY='opcional'
GOOGLE_API_KEY='opcional'
ANTHROPIC_API_KEY='opcional'
```

**Las API Keys son totalmente opcionales para usuarios que elijan ejecutar LLM localmente. Este es el propósito principal de este proyecto. Déjalas vacías si tienes hardware suficiente**

Las siguientes variables de entorno configuran las conexiones y claves API de tu aplicación.

Actualiza el archivo `.env` con tus propios valores según sea necesario:

- **SEARXNG_BASE_URL**: Déjalo sin cambios
- **REDIS_BASE_URL**: Déjalo sin cambios
- **WORK_DIR**: Ruta a tu directorio de trabajo en tu máquina local. AgenticSeek podrá leer e interactuar con estos archivos.
- **OLLAMA_PORT**: Número de puerto para el servicio Ollama.
- **LM_STUDIO_PORT**: Número de puerto para el servicio LM Studio.
- **CUSTOM_ADDITIONAL_LLM_PORT**: Puerto para cualquier servicio LLM personalizado adicional.

Todas las variables de entorno de API key a continuación son **opcionales**. Solo necesitas proporcionarlas si planeas usar APIs externas en lugar de ejecutar LLMs localmente.

### 3. **Iniciar Docker**

Asegúrate de que Docker esté instalado y ejecutándose en tu sistema. Puedes iniciar Docker usando los siguientes comandos:

- **En Linux/macOS:**  
    Abre una terminal y ejecuta:
    ```sh
    sudo systemctl start docker
    ```
    O inicia Docker Desktop desde el menú de aplicaciones si está instalado.

- **En Windows:**  
    Inicia Docker Desktop desde el menú de inicio.

Puedes verificar que Docker está ejecutándose ejecutando:
```sh
docker info
```
Si ves información sobre tu instalación de Docker, está ejecutándose correctamente.

---

## Configuración para ejecutar LLM localmente en tu máquina

**Requisitos de Hardware:**

Para ejecutar LLMs localmente, necesitarás hardware suficiente. Como mínimo, se requiere una GPU capaz de ejecutar Qwen/Deepseek 14B. Consulta la sección FAQ para recomendaciones detalladas de modelos/rendimiento.

**Configura tu proveedor local**  

Inicia tu proveedor local, por ejemplo con ollama:

```sh
ollama serve
```

Consulta más abajo la lista de proveedores locales soportados.

**Actualiza el config.ini**

Cambia el archivo config.ini para establecer provider_name a un proveedor soportado y provider_model a un LLM soportado por tu proveedor. Recomendamos modelos de razonamiento como *Qwen* o *Deepseek*.

Consulta la sección **FAQ** al final del README para los requisitos de hardware.

```sh
[MAIN]
is_local = True # Si estás ejecutando localmente o con proveedor remoto.
provider_name = ollama # o lm-studio, openai, etc..
provider_model = deepseek-r1:14b # elige un modelo que se ajuste a tu hardware
provider_server_address = 127.0.0.1:11434
agent_name = Jarvis # nombre de tu IA
recover_last_session = True # si quieres recuperar la sesión anterior
save_session = True # si quieres recordar la sesión actual
speak = False # texto a voz
listen = False # Voz a texto, solo para CLI, experimental
jarvis_personality = False # Si quieres usar una personalidad más tipo "Jarvis" (experimental)
languages = en zh # La lista de idiomas, Text to speech usará por defecto el primer idioma de la lista
[BROWSER]
headless_browser = True # déjalo sin cambios a menos que uses CLI en el host.
stealth_mode = True # Usa selenium no detectado para reducir la detección del navegador
```

**Advertencia**:

- El formato del archivo `config.ini` no soporta comentarios.
No copies y pegues la configuración de ejemplo directamente, ya que los comentarios causarán errores. En su lugar, modifica manualmente el archivo `config.ini` con tus configuraciones deseadas, excluyendo cualquier comentario.

- NO establezcas provider_name como `openai` si estás usando LM-studio para ejecutar LLMs. Establécelo como `lm-studio`.

- Algunos proveedores (ej: lm-studio) requieren que tengas `http://` antes de la IP. Por ejemplo `http://127.0.0.1:1234`

**Lista de proveedores locales**

| Proveedor  | ¿Local? | Descripción                                               |
|-----------|--------|-----------------------------------------------------------|
| ollama    | Sí    | Ejecuta LLMs localmente con facilidad usando ollama como proveedor LLM |
| lm-studio  | Sí    | Ejecuta LLM localmente con LM studio (establece `provider_name` como `lm-studio`)|
| openai    | Sí     |  Usa API compatible con openai (ej: servidor llama.cpp)  |

Siguiente paso: [Iniciar servicios y ejecutar AgenticSeek](#Iniciar-servicios-y-ejecutar)  

*Consulta la sección **Problemas conocidos** si tienes problemas*

*Consulta la sección **Ejecutar con una API** si tu hardware no puede ejecutar deepseek localmente*

*Consulta la sección **Config** para una explicación detallada del archivo de configuración.*

---

## Configuración para ejecutar con una API

**Ejecutar con una API es opcional, consulta arriba para ejecutar localmente.**

Establece el proveedor deseado en el `config.ini`. Consulta más abajo la lista de proveedores de API.

```sh
[MAIN]
is_local = False
provider_name = google
provider_model = gemini-2.0-flash
provider_server_address = 127.0.0.1:5000 # no importa
```
Advertencia: Asegúrate de que no haya espacios al final en la configuración.

Exporta tu API key: `export <<PROVIDER>>_API_KEY="xxx"`

Ejemplo: export `TOGETHER_API_KEY="xxxxx"`

**Lista de proveedores de API**
  
| Proveedor  | ¿Local? | Descripción                                               |
|-----------|--------|-----------------------------------------------------------|
| openai    | Depende  | Usa API de ChatGPT  |
| deepseek  | No     | API de Deepseek (no privada)                            |
| huggingface| No    | API de Hugging-Face (no privada)                            |
| togetherAI | No    | Usa API de together AI (no privada)                         |
| google | No    | Usa API de google gemini (no privada)                         |

Ten en cuenta que la codificación/bash podría fallar con gemini, parece ignorar nuestro prompt para respetar el formato, que están optimizados para deepseek r1. Modelos como gpt-4 también parecen tener un rendimiento deficiente con nuestro prompt.

Siguiente paso: [Iniciar servicios y ejecutar AgenticSeek](#Iniciar-servicios-y-ejecutar)

*Consulta la sección **Problemas conocidos** si tienes problemas*

*Consulta la sección **Config** para una explicación detallada del archivo de configuración.*

---

## Iniciar servicios y ejecutar

Inicia los servicios requeridos. Esto iniciará todos los servicios del docker-compose.yml, incluyendo:
    - searxng
    - redis (requerido por searxng)
    - frontend
    - backend (si usas `full`)

```sh
./start_services.sh full # MacOS
start ./start_services.cmd full # Windows
```

**Advertencia:** Este paso descargará y cargará todas las imágenes de Docker, lo que puede tomar hasta 30 minutos. Después de iniciar los servicios, espera hasta que el servicio backend esté completamente ejecutándose (deberías ver backend: <info> en el log) antes de enviar cualquier mensaje. Los servicios backend pueden tardar más en iniciar que otros.

Ve a `http://localhost:3000/` y deberías ver la interfaz web.

**Opcional:** Ejecutar con la interfaz CLI:

Para ejecutar con la interfaz CLI tendrías que instalar el paquete en el host:

```sh
./install.sh
./install.bat # windows
```

Inicia los servicios:

```sh
./start_services.sh # MacOS
start ./start_services.cmd # Windows
```

Luego ejecuta: `python3 cli.py` 

## Uso

Asegúrate de que los servicios estén funcionando con `./start_services.sh full` y ve a `localhost:3000` para la interfaz web.

También puedes usar el reconocimiento de voz configurando `listen = True` en el config. Solo para modo CLI.

Para salir, simplemente di/escribe `goodbye`.

Aquí hay algunos ejemplos de uso:

> *¡Haz un juego de serpiente en python!*

> *Busca en la web los mejores cafés en Rennes, Francia, y guarda una lista de tres con sus direcciones en rennes_cafes.txt.*

> *Escribe un programa en Go para calcular el factorial de un número, guárdalo como factorial.go en tu espacio de trabajo*

> *Busca en mi carpeta summer_pictures todos los archivos JPG, renómbralos con la fecha de hoy, y guarda una lista de archivos renombrados en photos_list.txt*

> *Busca en línea películas populares de ciencia ficción de 2024 y elige tres para ver esta noche. Guarda la lista en movie_night.txt.*

> *Busca en la web los últimos artículos de noticias sobre IA de 2025, selecciona tres, y escribe un script de Python para extraer sus títulos y resúmenes. Guarda el script como news_scraper.py y los resúmenes en ai_news.txt en /home/projects*

> *Viernes, busca en la web una API gratuita de precios de acciones, regístrate con supersuper7434567@gmail.com luego escribe un script de Python para obtener usando la API los precios diarios de Tesla, y guarda los resultados en stock_prices.csv*

*Ten en cuenta que las capacidades de llenado de formularios son aún experimentales y podrían fallar.*

Después de escribir tu consulta, AgenticSeek asignará el mejor agente para la tarea.

Debido a que este es un prototipo temprano, el sistema de enrutamiento de agentes podría no asignar siempre el agente correcto según tu consulta.

Por lo tanto, debes ser muy explícito en lo que quieres y cómo la IA podría proceder, por ejemplo, si quieres que realice una búsqueda web, no digas:

`¿Conoces algunos buenos países para viajar solo?`

En su lugar, pregunta:

`Haz una búsqueda web y averigua cuáles son los mejores países para viajar solo`

---

## **Configuración para ejecutar el LLM en tu propio servidor**

Si tienes una computadora potente o un servidor que puedes usar, pero quieres usarlo desde tu laptop, tienes la opción de ejecutar el LLM en un servidor remoto usando nuestro servidor llm personalizado.

En tu "servidor" que ejecutará el modelo de IA, obtén la dirección IP

```sh
ip a | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | cut -d/ -f1 # ip local
curl https://ipinfo.io/ip # ip pública
```

Nota: Para Windows o macOS, usa ipconfig o ifconfig respectivamente para encontrar la dirección IP.

Clona el repositorio y entra en la carpeta `server/`.

```sh
git clone --depth 1 https://github.com/Fosowl/agenticSeek.git
cd agenticSeek/llm_server/
```

Instala los requisitos específicos del servidor:

```sh
pip3 install -r requirements.txt
```

Ejecuta el script del servidor.

```sh
python3 app.py --provider ollama --port 3333
```

Tienes la opción de usar `ollama` y `llamacpp` como servicio LLM.

Ahora en tu computadora personal:

Cambia el archivo `config.ini` para establecer `provider_name` a `server` y `provider_model` a `deepseek-r1:xxb`.
Establece `provider_server_address` a la dirección IP de la máquina que ejecutará el modelo.

```sh
[MAIN]
is_local = False
provider_name = server
provider_model = deepseek-r1:70b
provider_server_address = x.x.x.x:3333
```

Siguiente paso: [Iniciar servicios y ejecutar AgenticSeek](#Iniciar-servicios-y-ejecutar)

---

## Voz a Texto

Advertencia: la voz a texto solo funciona en modo CLI por el momento.

Ten en cuenta que actualmente la voz a texto solo funciona en inglés.

La funcionalidad de voz a texto está deshabilitada por defecto. Para habilitarla, establece la opción listen a True en el archivo config.ini:

```
listen = True
```

Cuando está habilitada, la función de voz a texto escucha una palabra clave de activación, que es el nombre del agente, antes de comenzar a procesar tu entrada. Puedes personalizar el nombre del agente actualizando el valor `agent_name` en el archivo *config.ini*:

```
agent_name = Friday
```

Para un reconocimiento óptimo, recomendamos usar un nombre común en inglés como "John" o "Emma" como nombre del agente.

Una vez que veas que comienza a aparecer la transcripción, di el nombre del agente en voz alta para activarlo (por ejemplo, "Friday").

Habla tu consulta claramente.

Termina tu solicitud con una frase de confirmación para indicar al sistema que proceda. Ejemplos de frases de confirmación incluyen:
```
"do it", "go ahead", "execute", "run", "start", "thanks", "would ya", "please", "okay?", "proceed", "continue", "go on", "do that", "go it", "do you understand?"
```

## Config

Ejemplo de configuración:
```
[MAIN]
is_local = True
provider_name = ollama
provider_model = deepseek-r1:32b
provider_server_address = 127.0.0.1:11434
agent_name = Friday
recover_last_session = False
save_session = False
speak = False
listen = False
jarvis_personality = False
languages = en zh
[BROWSER]
headless_browser = False
stealth_mode = False
```

**Explicación**:

- is_local -> Ejecuta el agente localmente (True) o en un servidor remoto (False).

- provider_name -> El proveedor a usar (uno de: `ollama`, `server`, `lm-studio`, `deepseek-api`)

- provider_model -> El modelo usado, ej., deepseek-r1:32b.

- provider_server_address -> Dirección del servidor, ej., 127.0.0.1:11434 para local. Establece a cualquier cosa para API no local.

- agent_name -> Nombre del agente, ej., Friday. Usado como palabra de activación para TTS.

- recover_last_session -> Reinicia desde la última sesión (True) o no (False).

- save_session -> Guarda datos de la sesión (True) o no (False).

- speak -> Habilita salida de voz (True) o no (False).

- listen -> escucha entrada de voz (True) o no (False).

- jarvis_personality -> Usa una personalidad tipo JARVIS (True) o no (False). Esto simplemente cambia el archivo de prompt.

- languages -> La lista de idiomas soportados, necesaria para que el router llm funcione correctamente, evita poner demasiados o idiomas demasiado similares.

- headless_browser -> Ejecuta el navegador sin una ventana visible (True) o no (False).

- stealth_mode -> Hace más difícil la detección de bots. El único inconveniente es que tienes que instalar manualmente la extensión anticaptcha.

- languages -> Lista de idiomas soportados. Requerido para el sistema de enrutamiento de agentes. Cuanto más larga sea la lista de idiomas, más modelos se descargarán.

## Proveedores

La tabla a continuación muestra los proveedores disponibles:

| Proveedor  | ¿Local? | Descripción                                               |
|-----------|--------|-----------------------------------------------------------|
| ollama    | Sí    | Ejecuta LLMs localmente con facilidad usando ollama como proveedor LLM |
| server    | Sí    | Aloja el modelo en otra máquina, ejecuta tu máquina local |
| lm-studio  | Sí    | Ejecuta LLM localmente con LM studio (`lm-studio`)             |
| openai    | Depende  | Usa API de ChatGPT (no privada) o API compatible con openai  |
| deepseek-api  | No     | API de Deepseek (no privada)                            |
| huggingface| No    | API de Hugging-Face (no privada)                            |
| togetherAI | No    | Usa API de together AI (no privada)                         |
| google | No    | Usa API de google gemini (no privada)                         |

Para seleccionar un proveedor cambia el config.ini:

```
is_local = True
provider_name = ollama
provider_model = deepseek-r1:32b
provider_server_address = 127.0.0.1:5000
```
`is_local`: debe ser True para cualquier LLM ejecutándose localmente, de lo contrario False.

`provider_name`: Selecciona el proveedor a usar por su nombre, ver la lista de proveedores arriba.

`provider_model`: Establece el modelo a usar por el agente.

`provider_server_address`: puede establecerse a cualquier cosa si no estás usando el proveedor server.

# Problemas conocidos

## Problemas con Chromedriver

**Error conocido #1:** *incompatibilidad de chromedriver*

`Exception: Failed to initialize browser: Message: session not created: This version of ChromeDriver only supports Chrome version 113
Current browser version is 134.0.6998.89 with binary path`

Esto ocurre si hay una incompatibilidad entre tu navegador y la versión de chromedriver.

Necesitas navegar para descargar la última versión:

https://developer.chrome.com/docs/chromedriver/downloads

Si estás usando Chrome versión 115 o más nueva ve a:

https://googlechromelabs.github.io/chrome-for-testing/

Y descarga la versión de chromedriver que coincida con tu SO.

![alt text](./media/chromedriver_readme.png)

Si esta sección está incompleta por favor crea un issue.

## Problemas con adaptadores de conexión

```
Exception: Provider lm-studio failed: HTTP request failed: No connection adapters were found for '127.0.0.1:11434/v1/chat/completions'
```

Asegúrate de tener `http://` antes de la dirección IP del proveedor:

`provider_server_address = http://127.0.0.1:11434`

## Se debe proporcionar la URL base de SearxNG

```
raise ValueError("SearxNG base URL must be provided either as an argument or via the SEARXNG_BASE_URL environment variable.")
ValueError: SearxNG base URL must be provided either as an argument or via the SEARXNG_BASE_URL environment variable.
```

¿Quizás no moviste `.env.example` como `.env`? También puedes exportar SEARXNG_BASE_URL: 

`export  SEARXNG_BASE_URL="http://127.0.0.1:8080"`

## FAQ

**P: ¿Qué hardware necesito?**  

| Tamaño del Modelo  | GPU  | Comentario                                               |
|-----------|--------|-----------------------------------------------------------|
| 7B        | 8GB Vram | ⚠️ No recomendado. El rendimiento es pobre, alucinaciones frecuentes, y los agentes planificadores probablemente fallarán. |
| 14B        | 12 GB VRAM (ej. RTX 3060) | ✅ Usable para tareas simples. Puede tener dificultades con la navegación web y tareas de planificación. |
| 32B        | 24+ GB VRAM (ej. RTX 4090) | 🚀 Éxito con la mayoría de las tareas, aún puede tener dificultades con la planificación de tareas |
| 70B+        | 48+ GB Vram (ej. mac studio) | 💪 Excelente. Recomendado para casos de uso avanzados. |

**P: ¿Por qué Deepseek R1 sobre otros modelos?**  

Deepseek R1 sobresale en razonamiento y uso de herramientas para su tamaño. Creemos que es una buena opción para nuestras necesidades, otros modelos funcionan bien, pero Deepseek es nuestra elección principal.

**P: Obtengo un error al ejecutar `cli.py`. ¿Qué hago?**  

Asegúrate de que local esté ejecutándose (`ollama serve`), tu `config.ini` coincida con tu proveedor, y las dependencias estén instaladas. Si nada funciona, no dudes en crear un issue.

**P: ¿Realmente puede ejecutarse 100% localmente?**  

Sí, con proveedores Ollama, lm-studio o server, todos los modelos de voz a texto, LLM y texto a voz se ejecutan localmente. Las opciones no locales (OpenAI u otras API) son opcionales.

**P: ¿Por qué debería usar AgenticSeek cuando tengo Manus?**

Esto comenzó como un Proyecto Secundario que hicimos por interés en los agentes de IA. Lo especial es que queremos usar modelos locales y evitar APIs.
Nos inspiramos en Jarvis y Friday (películas de Iron man) para hacerlo "genial" pero para la funcionalidad tomamos más inspiración de Manus, porque eso es lo que la gente quiere en primer lugar: una alternativa local a manus.
A diferencia de Manus, AgenticSeek prioriza la independencia de sistemas externos, dándote más control, privacidad y evitando costos de API.

## Contribuir

¡Buscamos desarrolladores para mejorar AgenticSeek! Revisa los issues o discusiones abiertas.

[Guía de contribución](./docs/CONTRIBUTING.md)

[![Star History Chart](https://api.star-history.com/svg?repos=Fosowl/agenticSeek&type=Date)](https://www.star-history.com/#Fosowl/agenticSeek&Date)

## Mantenedores:

 > [Fosowl](https://github.com/Fosowl) | Hora de París 

 > [antoineVIVIES](https://github.com/antoineVIVIES) | Hora de Taipei 

 > [steveh8758](https://github.com/steveh8758) | Hora de Taipei 

## Agradecimientos Especiales:

 > [tcsenpai](https://github.com/tcsenpai) y [plitc](https://github.com/plitc) Por ayudar con la dockerización del backend

