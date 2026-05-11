from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
 
app = FastAPI(title="LLM API")
 
class ChatRequest(BaseModel):
    message: str
    model: str = "llama3"
 
class ChatResponse(BaseModel):
    reply: str
    tokens_used: int
 
@app.get("/health")
async def health():
    return {"status": "ok"}
 
@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": req.model, "prompt": req.message, "stream": False}
        )
        data = response.json()
        return ChatResponse(
            reply=data["response"],
            tokens_used=data.get("eval_count", 0)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))