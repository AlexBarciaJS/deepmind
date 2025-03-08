# config.py
import os
import json
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from typing import ClassVar, List

# Load environment variables
load_dotenv()

class Settings(BaseSettings):
    MONGO_URI: str = os.getenv("MONGO_URI")
    MONGO_DB_NAME: str = os.getenv("MONGO_DB_NAME")
    PINECONE_API_KEY: str = os.getenv("PINECONE_API_KEY")
    PINECONE_INDEX: str = os.getenv("PINECONE_INDEX")
    PINECONE_CLOUD: str = os.getenv("PINECONE_CLOUD")
    PINECONE_REGION: str = os.getenv("PINECONE_REGION")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    # The list of sites to scan is loaded and marked as ClassVar so that Pydantic ignores it in validation.

settings = Settings()
