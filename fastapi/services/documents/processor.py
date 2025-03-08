from fastapi import UploadFile
from services.nosql.mongo import check_pdf_exists, insert_pdf_record
from services.documents.chunker import chunk_text
import fitz  # PyMuPDF for PDF processing
from datetime import datetime
from services.vector.pinecone_service import upsert_vectors
from services.ia.openai_service import create_embeddings

async def process_pdf(file: UploadFile):
    """
    Processes a PDF file:
    - Checks if the file already exists in MongoDB based on filename and size.
    - Extracts text from the PDF.
    - Chunks the text for better storage and retrieval.
    - Stores metadata and chunked content in MongoDB.
    """
    try:
        # Read file into memory
        pdf_content = await file.read()
        file_size = len(pdf_content)
        filename = file.filename
        
        # Extract metadata (modification date)
        pdf_document = fitz.open(stream=pdf_content, filetype="pdf")
        metadata = pdf_document.metadata
        modification_date = metadata.get("modDate", None)  # Extract modification date

        # Convert modification date format
        modification_date = format_pdf_date(modification_date)

        # Use current timestamp if modification date is not found
        creation_date = datetime.utcnow().isoformat() if not modification_date else modification_date



        # Check if file already exists in MongoDB
        existing_file = await check_pdf_exists(filename, file_size, creation_date, modification_date)
        if existing_file:
            return {"message": "File already exists in DataBase"}

        # Extract text from PDF
        pdf_text = extract_text_from_pdf(pdf_content)

        # Chunk the extracted text
        text_chunks = chunk_text(pdf_text, chunk_size=1500, chunk_overlap=100)

        # Generate embeddings using OpenAI
        embeddings = create_embeddings(text_chunks)
    
        # Prepare vectors for Pinecone
        vectors = [
            (str(i), embeddings[i], {"text": text_chunks[i]})
            for i in range(len(text_chunks))
        ]
    
        # Upsert vectors to Pinecone index
        upsert_vectors(vectors)


        # Prepare document for MongoDB
        pdf_document = {
            "file_name": filename,
            "file_size": file_size,
            "creation_date": creation_date,
            "modification_date": modification_date,
            # "chunks": text_chunks  # Store the chunked text
        }

        # Insert document into MongoDB
        result = await insert_pdf_record(pdf_document)

        return {"message": "File processed and stored successfully", "file_id": result}

    except Exception as e:
        return {"error": str(e)}

def extract_text_from_pdf(pdf_content: bytes) -> str:
    """
    Extracts text from a PDF file using PyMuPDF.
    """
    pdf_document = fitz.open(stream=pdf_content, filetype="pdf")
    text = ""
    for page in pdf_document:
        text += page.get_text("text") + "\n"
    return text


def format_pdf_date(pdf_date: str) -> str:
    """
    Converts PDF metadata date format (D:YYYYMMDDHHmmSS) to ISO format.
    """
    if not pdf_date or not pdf_date.startswith("D:"):
        return None  # Return None if the date is missing or incorrectly formatted
    
    try:
        # Extract timestamp and convert to datetime
        date_str = pdf_date[2:16]  # Removes "D:" prefix
        formatted_date = datetime.strptime(date_str, "%Y%m%d%H%M%S").isoformat()
        return formatted_date
    except ValueError:
        return None  # Return None if parsing fails