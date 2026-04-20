from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline
from langchain.prompts import PromptTemplate
import os

# Load embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Fix path issue (IMPORTANT)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
index_path = os.path.join(BASE_DIR, "faiss_index")

# Load FAISS index
db = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)

# Create retriever
retriever = db.as_retriever()

# Load LLM (better model)
qa_pipeline = pipeline(
    task="text2text-generation",
    model="google/flan-t5-base"
)

llm = HuggingFacePipeline(pipeline=qa_pipeline)

# Prompt template (NEW ADDITION)
prompt_template = """
You are an AI assistant.

Answer the question in a complete and clear sentence using the given context.
Do not give short phrases. Always give a full explanation.

Context:
{context}

Question:
{question}

Answer:
"""

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

# Create QA chain (UPDATED)
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type_kwargs={"prompt": PROMPT}
)

# Function to ask question (UPDATED)
def ask_question(query):
    return qa.invoke({"query": query})["result"]