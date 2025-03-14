# deepmind

📦 Ubuntu
sudo apt update && sudo apt install -y libpq-dev python3-dev build-essential



🐳 Postgres Docker

/
docker-compose up -d

📝 Link Pgadmin to Postgres

📌 1. Accede a pgAdmin
Abre tu navegador y ve a http://localhost:5050
Inicia sesión con:
Email: admin@example.com
Contraseña: admin
📌 2. Agregar un nuevo servidor
En pgAdmin, en la barra lateral izquierda, haz clic derecho en "Servers" → "Create" → "Server".
Pestaña "General":
Name: PostgreSQL (o cualquier nombre)
Pestaña "Connection":
Host: postgres-db (nombre del servicio en Docker Compose)
Port: 5432
Username: myuser
Password: mypassword
Save password? Yes
Haz clic en "Save" y ya estarás conectado.


📦 FastApi

fastapi/
sudo apt update && sudo apt install python3-venv -y
sudo apt install python3-poetry
poetry init
poetry add fastapi uvicorn psycopg2-binary
poetry env use python3
poetry install

🚀
poetry run uvicorn main:app --reload


📦 VueMind
donwnload https://github.com/creativetimofficial/vue-material-dashboard
cd vue-material-dashboard/
npm i
🚀 
npm run dev


📌 ## Setting up the Llama 3.2 Model

1. Make sure Docker and Docker Compose are installed.
2. Run the following command to download the Llama 3.2 model:

```bash
docker compose exec ollama ollama pull llama3.2
```

3. Execute the following command to download the embedding model:
```bash
 docker compose exec ollama ollama pull mxbai-embed-large
```



🚀 Inicio rápido
🐳 Docker & Containers
🗄️ Base de Datos
🛠️ Configuración
🔗 Conexión
⚙️ Comandos útiles
📦 Instalación
🎯 Objetivo
📌 Pasos a seguir
📝 Notas
🔥 Ejemplo en acción
🌍 Acceder a pgAdmin
🔑 Credenciales
✨ Starts