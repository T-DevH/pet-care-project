from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import openai
from config import OPENAI_API_KEY

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat_with_ai(request: ChatRequest):
    try:
        client = openai.OpenAI(api_key=OPENAI_API_KEY)  # Initialize OpenAI client
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": request.message}],
        )
        return {"reply": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
