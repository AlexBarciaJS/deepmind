import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.chains import create_sql_query_chain
from langchain_community.utilities import SQLDatabase
from sqlalchemy import text
from db.database import engine  # Importamos la conexión a la BD

# Cargar variables de entorno
load_dotenv()

# Configurar la base de datos en LangChain
db = SQLDatabase(engine)

# Configurar OpenAI
llm = OpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0  # 0 para respuestas más deterministas
)

# Crear la cadena de generación de SQL
db_chain = create_sql_query_chain(llm, db)

def ejecutar_consulta(consulta_sql: str):
    """Ejecuta una consulta SQL en PostgreSQL y devuelve el resultado"""
    try:
        with engine.connect() as conn:
            result = conn.execute(text(consulta_sql))
            return [row._asdict() for row in result]  # Convertir resultados a lista de diccionarios
    except Exception as e:
        return {"error": str(e)}

def preguntar_a_db(pregunta: str):
    """Genera y ejecuta la consulta SQL basada en la pregunta"""
    consulta_sql = db_chain.invoke({"question": pregunta})
    
    # Ejecutar la consulta SQL en la base de datos
    resultado = ejecutar_consulta(consulta_sql)
    
    return {"consulta_sql": consulta_sql, "resultado": resultado}
