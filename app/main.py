from fastapi import FastAPI, UploadFile, File
from app.resume_parser import extract_text
from app.chatgpt import ask_gpt

app = FastAPI()

@app.post("/upload_resume/")
async def upload_resume(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text(content)
    return {"parsed_resume": text}

@app.post("/ask/")
async def ask_question(text: str, question: str):
    answer = ask_gpt(text, question)
    return {"response": answer}
