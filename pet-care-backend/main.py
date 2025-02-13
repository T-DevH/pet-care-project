from fastapi import FastAPI
from routes.chat import router as chat_router
from routes.pet import router as pet_router
from fastapi.middleware.cors import CORSMiddleware
from routes.rag import router as rag_router
import uvicorn

app = FastAPI(title="Pet Care AI API")

# Include routers
app.include_router(chat_router, prefix="/api")
app.include_router(pet_router, prefix="/api")
app.include_router(rag_router, prefix="/api")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow frontend to communicate with backend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Pet Care AI Backend"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
