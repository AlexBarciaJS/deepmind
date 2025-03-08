from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller.chat import router as chat_router

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Allow Vue frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Include brain.py in router
app.include_router(chat_router, prefix="/chat", tags=["Chat"])

@app.get("/")
def read_root():
    return {"message": "API con FastAPI, LangChain y PostgreSQL"}
