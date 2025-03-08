from fastapi import APIRouter, File, UploadFile, HTTPException
from services.documents.processor import process_pdf

router = APIRouter()

@router.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    # Ensure the file is a PDF
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    # Process the file (do not store it)
    result = await process_pdf(file)

    return {"filename": file.filename, "message": "File processed successfully", "data": result}
