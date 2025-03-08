from pinecone import Pinecone
from config import settings

# ✅ Create Pinecone client instance
pinecone_client = Pinecone(api_key=settings.PINECONE_API_KEY)
index_name = settings.PINECONE_INDEX

async def check_pinecone():
    """
    Runs at FastAPI startup to check Pinecone index status and fetch a stored vector.
    """
    try:
        # ✅ Ensure the index exists
        existing_indexes = [idx.name for idx in pinecone_client.list_indexes()]
        if index_name not in existing_indexes:
            print(f"⚠️ Pinecone index '{index_name}' not found.")
            return

        index = pinecone_client.Index(index_name)

        # ✅ Fetch index statistics
        response = index.describe_index_stats()
        print(f"✅ Pinecone Index Status: {response}")

        # ✅ Retrieve a stored vector (Modify ID if necessary)
        vector_id = "1"  # Change this to a valid stored vector ID
        vector_data = index.fetch([vector_id])

        # ✅ Correct way to access the vector
        if vector_data and vector_id in vector_data.vectors:
            vector_info = vector_data.vectors[vector_id]
            metadata = vector_info.metadata if hasattr(vector_info, "metadata") else {}

            print(f"✅ Retrieved stored vector {vector_id}:")
            print(f"   ➡️ Embedding Length: {len(vector_info.values)}")
            print(f"   ➡️ Metadata: {metadata}")

            # ✅ Print extracted text (if available)
            text_content = metadata.get("text", "⚠️ No text found in metadata.")
            print(f"   ➡️ Extracted Text: {text_content}")

        else:
            print(f"⚠️ Vector {vector_id} not found in Pinecone.")

    except Exception as e:
        print(f"❌ Error connecting to Pinecone: {e}")
