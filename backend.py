from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import requests
import json

app = FastAPI()

# Allow CORS for all origins (for development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request and response models
class ChatRequest(BaseModel):
    message: str
    language: Optional[str] = "english"

class ChatResponse(BaseModel):
    response: str

def chat_with_ollama(prompt: str, language: str) -> str:
    payload = {
        "model": "llama3",
        "messages": [
            {"role": "system", "content": f"You are a helpful farming assistant. Reply only in {language}."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("http://localhost:11434/api/chat", json=payload, stream=True)
    response_text = ""

    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            try:
                json_data = json.loads(decoded_line)
                part = json_data.get("message", {}).get("content", "") if "message" in json_data else json_data.get("response", "")
                response_text += part
            except json.JSONDecodeError:
                continue

    return response_text

@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="No input message provided")

    try:
        response_text = chat_with_ollama(request.message, request.language.lower())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return ChatResponse(response=response_text)
