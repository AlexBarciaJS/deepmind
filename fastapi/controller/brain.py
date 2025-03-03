from fastapi import APIRouter
from services.langchain_service import preguntar_a_db

router = APIRouter()

@router.get("/preguntar/")
def hacer_pregunta(query: str):
    respuesta = preguntar_a_db(query)
    return {"respuesta": respuesta}
