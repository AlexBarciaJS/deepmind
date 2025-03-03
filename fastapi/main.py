from fastapi import FastAPI
from controller.brain import router as brain_router  # Importar el router

app = FastAPI()

# Incluir el router de brain.py
app.include_router(brain_router, prefix="/brain", tags=["Brain"])

@app.get("/")
def read_root():
    return {"message": "API con FastAPI, LangChain y PostgreSQL"}
