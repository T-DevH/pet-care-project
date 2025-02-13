from fastapi import APIRouter, File, UploadFile, HTTPException, Depends
from pydantic import BaseModel
import shutil
import os
from rag_pipeline import add_pdf_to_vector_store, generate_response

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the folder exists


class QueryModel(BaseModel):
    question: str


@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    """Upload and process a PDF file."""
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    try:
        # Debugging logs
        print(f"📂 Uploading file: {file.filename}")
        print(f"📍 Saving to path: {file_path}")

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        if os.path.exists(file_path):
            print(f"✅ File successfully saved: {file_path}")
        else:
            print(f"❌ ERROR: File not found after writing: {file_path}")

        message = add_pdf_to_vector_store(file_path)
        return {"message": message, "file_path": file_path}

    except Exception as e:
        print(f"❌ Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Upload error: {str(e)}")


@router.post("/ask")
async def ask_question(query: QueryModel):
    """Retrieve knowledge from the uploaded PDFs and generate an AI response."""
    try:
        print(f"🧐 Received question: {query.question}")

        answer = generate_response(query.question)

        if not answer:
            raise HTTPException(status_code=404, detail="No relevant information found in the uploaded documents.")

        print(f"✅ AI Response: {answer}")
        return {"response": answer}

    except Exception as e:
        print(f"❌ Error in ask endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
