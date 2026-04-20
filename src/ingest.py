from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

# Load dataset
with open("data/docs.txt") as f:
    text = f.read()

# Split into chunks
splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=50)
docs = splitter.split_text(text)

# Create embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Create FAISS DB
db = FAISS.from_texts(docs, embeddings)

# Save index
db.save_local("faiss_index")

print("FAISS index created successfully!")