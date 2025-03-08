# services/pinecone_service.py
from pinecone import Pinecone, ServerlessSpec
from config import settings

# Initialize the Pinecone client and create the index if it does not exist
pinecone_client = Pinecone(api_key=settings.PINECONE_API_KEY)
index_name = settings.PINECONE_INDEX

if index_name not in pinecone_client.list_indexes().names():
    pinecone_client.create_index(
        name=index_name,
        dimension=1536,  # Adjust the dimension according to the embedding model used
        metric="cosine",
        spec=ServerlessSpec(
            cloud=settings.PINECONE_CLOUD,
            region=settings.PINECONE_REGION
        )
    )

# Connect to the Pinecone index
index = pinecone_client.Index(index_name)

def upsert_vectors(vectors):
    """
    Inserts or updates a list of vectors in the Pinecone index.
    Each vector is a tuple (id, embedding, metadata).
    """
    index.upsert(vectors=vectors)
