import os
import faiss
import numpy as np
import openai
import re
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from PyPDF2 import PdfReader
from config import OPENAI_API_KEY

# ✅ Initialize OpenAI API Key
openai.api_key = OPENAI_API_KEY

# ✅ Load sentence transformer model for embeddings
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# ✅ Create FAISS Index for vector search
dimension = 384  # Dimensionality of embeddings
index = faiss.IndexFlatL2(dimension)

# ✅ Store text chunks and their mapping
doc_store = []


def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text.strip()


def chunk_text(text, chunk_size=500):
    """Break text into meaningful chunks, preserving full sentences."""
    sentences = re.split(r'(?<=[.!?])\s+', text)  # ✅ Split only at sentence boundaries
    chunks, current_chunk = [], ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) < chunk_size:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "

    if current_chunk:
        chunks.append(current_chunk.strip())

    print(f"📑 Chunked text into {len(chunks)} meaningful segments.")
    return chunks


def add_pdf_to_vector_store(pdf_path):
    """Process and store PDF content in FAISS vector database."""
    global doc_store, index

    # ✅ Clear FAISS index & document store before adding a new PDF
    doc_store = []
    index.reset()

    text = extract_text_from_pdf(pdf_path)
    chunks = chunk_text(text)

    doc_store.extend(chunks)
    embeddings = embedding_model.encode(chunks)
    index.add(np.array(embeddings, dtype=np.float32))

    print(f"📄 Extracted {len(chunks)} chunks & stored {len(chunks)} embeddings in FAISS.")
    return f"Processed {len(chunks)} chunks from {pdf_path}."


def retrieve_relevant_chunks(query, top_k=10, distance_threshold=1.8):
    """Retrieve the most relevant text chunks from FAISS, allowing slightly higher distances."""
    query_embedding = embedding_model.encode([query])
    distances, indices = index.search(np.array(query_embedding, dtype=np.float32), top_k)

    relevant_chunks = []
    print(f"🔍 FAISS Search Query: {query}")
    print(f"📌 Retrieved Indices: {indices}")
    print(f"📏 Distances: {distances}")

    for i, idx in enumerate(indices[0]):
        if 0 <= idx < len(doc_store):
            if distances[0][i] < distance_threshold:  # ✅ Allow slightly higher distances
                relevant_chunks.append(doc_store[idx])
                print(f"✅ Selected chunk {idx}: {doc_store[idx]}")
            else:
                print(f"⚠ Skipped chunk {idx} due to high distance ({distances[0][i]}).")

    if not relevant_chunks:
        print("❌ No relevant chunks found after filtering.")
        return "No relevant information found."

    print(f"✅ Retrieved {len(relevant_chunks)} relevant chunks.")
    return " ".join(relevant_chunks[:5])  # ✅ Use up to 5 best results


def generate_response(question: str):
    """Retrieve relevant knowledge and generate a response using LLM."""
    try:
        retrieved_docs = retrieve_relevant_chunks(question)  # Get similar chunks

        if retrieved_docs == "No relevant information found":
            print("❌ No relevant documents found for query.")
            return "I'm sorry, but I couldn't find relevant information in the uploaded documents."

        print(f"🔍 Retrieved {len(retrieved_docs)} relevant chunks.")

        # ✅ Construct better prompt for OpenAI
        llm_prompt = f"""
        You are an AI assistant that answers questions based on the provided document.

        Document Context:
        {retrieved_docs}

        Question:
        {question}

        Provide a concise, relevant answer.
        """

        # ✅ Updated OpenAI API Call (for versions >=1.0.0)
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": llm_prompt}
            ]
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"❌ Error in generate_response: {str(e)}")
        return f"An error occurred: {str(e)}"
