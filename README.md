# deepmind

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
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
🚀
uvicorn main:app --reload


📦 VueMind
donwnload https://github.com/creativetimofficial/vue-material-dashboard
cd vue-material-dashboard/
npm i
🚀 
npm run dev






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