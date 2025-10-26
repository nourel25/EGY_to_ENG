from fastapi import FastAPI, HTTPException as HttpException
from pydantic import BaseModel
from transformers import pipeline
import torch


device = 0 if torch.cuda.is_available() else -1

app = FastAPI(title="LLM Inference API")

MODEL_NAME = "NEldin10/marian-finetuned-ArzEn-MultiGenre-egy-to-en"

try:
    print("🔹 Loading model... please wait.")
    llm = pipeline("translation", model=MODEL_NAME)
    print("✅ Model loaded successfully!")
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}")



class Query(BaseModel):
    text: str

@app.post("/translate")
def translate(query: Query):
    if not query.text:
        raise HttpException(status_code=400, detail="Input text cannot be empty")
    try:
        result = llm(query.text)
        return {"translation": result[0]["translation_text"]}
    except Exception as e:
        raise HttpException(status_code=500, detail=str(e))


