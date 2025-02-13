# 🐾 Pet Care AI - Complete Project

Welcome to **Pet Care AI**, an AI-powered platform that provides intelligent assistance for pet owners. This project integrates **LLM-RAG** (Retrieval-Augmented Generation) with **FastAPI** for the backend and **Next.js** for the frontend, enabling document-based AI chat functionalities.

## 📂 Project Structure

| Path                   | Description                              |
|------------------------|------------------------------------------|
| `pet-care-project/`    | Root directory of the project           |
| ├── `pet-care-backend/` | Backend (FastAPI, RAG, OpenAI API)      |
| ├── `pet-care-ai/`      | Frontend (Next.js, React, MUI)         |
| ├── `.gitignore`        | Git ignore file                        |
| ├── `README.md`         | Main repository documentation          |


Each folder contains a `README.md` file with detailed installation steps.

---

## 🏗️ **Backend (FastAPI & RAG)**
📌 **Tech Stack**:  
- **FastAPI** – Web framework for API development  
- **FAISS** – Vector search for document-based AI chat  
- **OpenAI API** – Chat-based AI responses  
- **PyPDF2** – PDF document processing  
- **Sentence Transformers** – Text embedding for document search  

📌 **Key Features**:  
- ✅ **LLM-RAG Implementation**  
- ✅ **PDF Upload & Processing**  
- ✅ **Vector Search with FAISS**  
- ✅ **AI Chat with Retrieval-Augmented Generation (RAG)**  

🔗 **[Backend Documentation & Setup](./pet-care-backend/README.md)**  

---

## 🎨 **Frontend (Next.js & React)**
📌 **Tech Stack**:  
- **Next.js** – React framework for SSR & client-side rendering  
- **Material UI (MUI)** – Responsive UI components  
- **Axios** – API communication with backend  
- **React Hooks** – State management  

📌 **Key Features**:  
- ✅ **Chat Interface** – AI-powered chat  
- ✅ **PDF Upload UI** – Upload documents for AI analysis  
- ✅ **Modern UI** – MUI-powered responsive design  

🔗 **[Frontend Documentation & Setup](./pet-care-ai/README.md)**  

---

## 🚀 **Installation & Running the Project**
1️⃣ **Clone the Repository**
```bash
git clone https://github.com/T-DevH/pet-care-project.git
cd pet-care-project
```

2️⃣ 🚀 **Set Up the Backend**
```bash
cd pet-care-backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```
🚀 Backend is now running at: http://127.0.0.1:8000

3️⃣ 🚀 **Set Up the Frontend**
```bash
cd ../pet-care-ai
npm install
npm run dev
```
🚀 Frontend is now running at: http://localhost:3000

## 📌 Key API Endpoints

| Method | Endpoint          | Description                          |
|--------|------------------|--------------------------------------|
| `POST` | `/api/upload-pdf` | Upload a PDF for AI processing      |
| `POST` | `/api/ask`        | Ask questions about the uploaded PDF |
| `POST` | `/api/chat`       | Chat with AI assistant              |


## 📚  LLM-RAG Implementation & Blog Series

This project is part of a[ 6-blog series]() covering LLM-RAG implementation from exploration to enterprise deployment, 
including AI agents and agentic AI.

📌 **Next Steps**:
-  **Upgrade to NVIDIA NeMo + NIMs** for optimized cost-effective deployment
- **Scale** with GPU acceleration

Stay tuned for updates in the blog series!