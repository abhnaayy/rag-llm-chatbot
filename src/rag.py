from langchain_huggingface import HuggingFaceEndpoint
import os

# Load model from Hugging Face API
llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-base",
    temperature=0.5,
    max_new_tokens=256,
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

def ask_question(query):
    return llm.invoke(query)