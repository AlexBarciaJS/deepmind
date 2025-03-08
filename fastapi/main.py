from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller.brain import router as brain_router  # Importar el router

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Allow Vue frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Incluir el router de brain.py
app.include_router(brain_router, prefix="/brain", tags=["Brain"])

@app.get("/")
def read_root():
    return {"message": "API con FastAPI, LangChain y PostgreSQL"}
