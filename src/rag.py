from langchain_huggingface import HuggingFaceEndpoint
import os

# Load HuggingFace API model (lightweight)
llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-base",
    temperature=0.5,
    max_new_tokens=256,
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

# Simple ask function
def ask_question(query):
    response = llm.invoke(query)
    return response