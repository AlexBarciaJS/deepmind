# ✅ Run Pinecone debugging at module load
import asyncio
from pinecone import Pinecone, ServerlessSpec
from config import settings
from services.vector.pinecone_debug import check_pinecone  # ✅ Correct import

# ✅ Initialize the Pinecone client
pinecone_client = Pinecone(api_key=settings.PINECONE_API_KEY)
index_name = settings.PINECONE_INDEX

# ✅ Check if the index exists, otherwise create it
existing_indexes = [index.name for index in pinecone_client.list_indexes()]
if index_name not in existing_indexes:
    print(f"Creating Pinecone index: {index_name}")
    pinecone_client.create_index(
        name=index_name,
        dimension=1536,  # Adjust according to embedding model
        metric="cosine",
        spec=ServerlessSpec(
            cloud=settings.PINECONE_CLOUD,
            region=settings.PINECONE_REGION
        )
    )

# ✅ Connect to the Pinecone index
index = pinecone_client.Index(index_name)
print(f"Connected to Pinecone index: {index.describe_index_stats()}")


# ✅ Use `asyncio.create_task()` to run `check_pinecone()` in the background
async def startup_task():
    await check_pinecone()

asyncio.create_task(startup_task())

def upsert_vectors(vectors):
    """
    Inserts or updates a list of vectors in the Pinecone index.
    Each vector must be a tuple (id, embedding, metadata).
    """
    if not isinstance(vectors, list) or not vectors:
        print("❌ Error: `upsert_vectors` received an empty or invalid vector list.")
        return

    # Validate metadata
    for vector in vectors:
        if not isinstance(vector, tuple) or len(vector) != 3:
            print(f"❌ Invalid vector format: {vector}")
            continue

        vector_id, embedding, metadata = vector

        if not isinstance(metadata, dict) or "text" not in metadata:
            print(f"⚠️ Warning: Skipping vector {vector_id} - Missing 'text' in metadata")
            continue

    index.upsert(vectors=vectors)
    print(f"✅ {len(vectors)} vectors inserted into Pinecone.")

MAX_CONTEXT_LENGTH = 4000  # ✅ Limit total context size

MAX_CONTEXT_TOKENS = 4000  # ✅ Adjust based on OpenAI limits

async def query_pinecone(query_vector, top_k=5):
    """
    Queries Pinecone for relevant vectors while limiting token usage.
    """
    try:
        response = index.query(
            vector=query_vector,
            top_k=top_k,
            include_metadata=True
        )

        matches = response.matches  # ✅ Access matches directly

        if not matches:
            print("⚠️ No relevant vectors found in Pinecone.")
            return []

        # ✅ Extract metadata text
        retrieved_texts = [match.metadata.get("text", "") for match in matches if match.metadata]

        print(f"✅ Extracted {len(retrieved_texts)} texts from Pinecone.")
        return retrieved_texts if retrieved_texts else ["⚠️ No relevant information found in the database."]

    except Exception as e:
        print(f"❌ Error querying Pinecone: {e}")
        return []
