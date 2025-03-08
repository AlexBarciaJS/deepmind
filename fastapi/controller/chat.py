from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.langchain_service import preguntar_a_db

router = APIRouter()

# Define request body model
class QueryRequest(BaseModel):
    query: str

@router.post("/chat/")
def ask_question(request: QueryRequest):
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    response = preguntar_a_db(request.query)
    return {"response": response}

