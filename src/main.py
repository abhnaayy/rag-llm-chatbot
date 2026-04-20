from fastapi import FastAPI
from pydantic import BaseModel
from src.rag import ask_question

app = FastAPI()

# Request body format
class Question(BaseModel):
    query: str

# Home route
@app.get("/")
def home():
    return {"message": "RAG API is running 🚀"}

# Ask question route
@app.post("/ask")
def ask(question: Question):
    answer = ask_question(question.query)
    return {"answer": answer}