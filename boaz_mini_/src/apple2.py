from fastapi import FastAPI
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# API 애플리케이션 생성
app = FastAPI()

# 모델 및 토크나이저 로드
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

@app.get("/generate/")
def generate(text: str):  # URL 쿼리 파라미터로부터 텍스트를 받습니다.
    inputs = tokenizer.encode(text, return_tensors="pt")
    outputs = model.generate(inputs, max_length=50, num_return_sequences=1)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": text}

@app.get("/")
def a():
    return {"response": '안녕'}