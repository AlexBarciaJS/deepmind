from fastapi import APIRouter, HTTPException
from services.ia.openai_service import generate_embedding
from services.vector.pinecone_service import query_pinecone
from pydantic import BaseModel
from services.langchain_service import preguntar_a_db
import openai
import time

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


MAX_RETRIES = 3  # ✅ Retry up to 3 times
WAIT_TIME = 5  # ✅ Wait 5 seconds before retrying

MAX_TOKENS_RESPONSE = 800  # ✅ Reduce max tokens to stay within limits

@router.post("/ask-ai/")
async def ask_ai(request: QueryRequest):
    """
    Queries Pinecone and sends relevant information to OpenAI.
    """
    try:
        query_vector = await generate_embedding(request.query)
        retrieved_texts = await query_pinecone(query_vector)

        if not retrieved_texts or "No relevant information found" in retrieved_texts[0]:
            return {"query": request.query, "response": "No relevant information found in the database."}

        # ✅ Ensure context is within token limits
        context = "\n".join(retrieved_texts)

        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI assistant answering based only on provided information."},
                {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {request.query}"}
            ],
            max_tokens=MAX_TOKENS_RESPONSE,  # ✅ Reduce response token limit
            temperature=0.7,
        )

        return {"query": request.query, "response": response.choices[0].message.content}

    except openai.RateLimitError as e:
        return {"error": "OpenAI API rate limit exceeded. Try again later."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

