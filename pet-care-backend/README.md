# 🐾 Pet Care AI - Backend (FastAPI)

This is the **backend** for the Pet Care AI application, built with **FastAPI**, **OpenAI GPT-4**, and an **LLM-RAG** pipeline for document-based question answering.

## 📌 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/pet-care-project.git
cd pet-care-project/pet-care-backend
```
### 2️⃣ Create & Activate Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
## 📌 Explanation of Each Dependency

| Dependency      | Description |
|----------------|-------------|
| **fastapi**    | Web framework for building APIs in Python. |
| **uvicorn**    | ASGI server for running FastAPI applications. |
| **pydantic**   | Data validation and serialization used in FastAPI. |
| **requests**   | HTTP requests library (useful for API calls). |
| **openai**     | Official OpenAI API library to interact with GPT-4. |
| **python-dotenv** | Loads environment variables from `.env` files. |
| **sqlalchemy** | SQL ORM (Optional, but useful if adding a database). |

### 4️⃣ Configure OpenAI API Key
1- Create a .env file in the pet-care-backend directory:
```bash
nano .env
```
2- Add the following line:
```bash
nano .env
```
## 📌 Running the Server
```bash
uvicorn main:app --reload
```
API runs on: http://127.0.0.1:8000
API Docs: http://127.0.0.1:8000/docs

## 📌 API Endpoints
### 🗨️ Chat with AI

| Method | Endpoint   | Description                         |
|--------|-----------|-------------------------------------|
| `POST` | `/api/chat` | Send a message to the AI assistant |

#### 📌 Example Request:
```bash
{
  "message": "What should I feed my dog?"
}
```
#### 📌 Example Response:
```Bash
{
  "reply": "You should feed your dog a balanced diet including proteins, healthy fats, and vegetables."
}
```
## 📌 LLM-RAG Pipeline (Retrieval-Augmented Generation)

The backend includes a **RAG (Retrieval-Augmented Generation)** pipeline to enable question answering based on uploaded PDF documents.
### 📌 How It Works
##### 1 Upload PDF Document

Extracts text from the PDF.

     =>Splits text into smaller chunks.

     =>Embeds chunks using sentence-transformers.

     =>Stores embeddings in a FAISS vector index.

#### 2 Ask Questions About Uploaded PDFs

    =>Converts the question into an embedding.

    =>Searches for the most relevant document chunks in FAISS.

    =>Sends the retrieved text chunks to OpenAI’s GPT-4 for a contextual response.

### 📌 RAG API Endpoints


| Method | Endpoint        | Description                                      |
|--------|----------------|--------------------------------------------------|
| `POST` | `/api/upload-pdf` | Upload a PDF document for processing and indexing. |
| `POST` | `/api/ask`      | Ask a question based on the uploaded document.  |

### 📌 Example Requests:

#### 📤 Upload a PDF:
```bash
curl -X 'POST' 'http://127.0.0.1:8000/api/upload-pdf' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@/path/to/document.pdf'
````
#### 📥 Ask a Question:
```bash
curl -X 'POST' 'http://127.0.0.1:8000/api/ask' \
  -H 'Content-Type: application/json' \
  -d '{"question": "What are the key points about pet care mentioned in the document?"}'
```
#### 📌 Example Response:
```bash
{
  "response": "The key points about pet care include regular vaccinations, balanced nutrition, and routine check-ups."
}
```