import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from langchain.sql_database import SQLDatabase

# Cargar variables de entorno
load_dotenv()

# Configurar conexión a PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# Inicializar LangChain con la base de datos
db = SQLDatabase(engine)
