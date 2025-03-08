# services/openai_service.py
import openai
from openai import OpenAI
from config import settings

# Initialize OpenAI client
openai_client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_embedding(text):
    """Generates an embedding for the given text using the OpenAI API."""
    client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )
    print(f"Generated text embedding: {text[:50]}...", response.data[0].embedding[:10])
    return response.data[0].embedding

def create_embeddings(chunks):
    """
    Generate embeddings for a list of text chunks using OpenAI.
    Returns a list of embeddings.
    """
    response = openai_client.embeddings.create(model="text-embedding-3-small", input=chunks)
    # Assuming response.data is a list of objects with an 'embedding' attribute
    embeddings = [item.embedding for item in response.data]
    return embeddings