"""
hospital_rag.py

This Retrieval-Augmented Generation (RAG) application simulates how a hospital can
use LangChain and vector databases (FAISS) to answer medical staff queries using
their internal protocol documents (stored in .txt files).

It loads medical guidelines, embeds them, stores in a vector DB, and retrieves relevant chunks
to generate accurate, grounded answers from a chat model like GPT-4o-mini.
"""

from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


# Step 1: Load hospital .txt records
folder_path = "hospital_guidelines"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Created missing folder: {folder_path}. Please add .txt files with hospital guidelines and rerun the script.")
    exit()

documents = []
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        path = os.path.join(folder_path, filename)
        loader = TextLoader(path)
        docs = loader.load()
        documents.extend(docs)

if not documents:
    print(f"No .txt files found in {folder_path}. Please add hospital guideline files and rerun the script.")
    exit()

print(f"Loaded {len(documents)} documents from hospital records")

# Step 2: Split into manageable chunks
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)
print(f"Split into {len(chunks)} text chunks")

# Step 3: Convert chunks into vector embeddings
embedding = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embedding)
print("Vector embeddings generated and stored in FAISS")

# Step 4: Create retriever from vector DB
retriever = vectorstore.as_retriever()
print("Retriever is ready")

# Step 5: Initialize Chat Model
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.3)

# Step 6: Build RAG chain (retriever + LLM)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Step 7: Ask a real medical query
query = "What is the recommended treatment for high blood pressure?"
print("User Query:", query)
response = qa_chain.invoke({"query": query})
print("Generated Response:\n", response["result"] if isinstance(response, dict) and "result" in response else response)