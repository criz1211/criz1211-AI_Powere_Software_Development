# lc_FAIS.py

# FAISS
# FAISS is a vector store that is used to store and retrieve vectors.
#What is FAISS?

#FAISS (Facebook AI Similarity Search) is an open-source library developed by Meta AI (Facebook) designed to:
#	•	Search large sets of high-dimensional vectors quickly and efficiently
#	•	Perform similarity search, such as finding the most similar document, image, or text snippet to a given query
#	•	Run locally (no internet needed) and is super fast, even with millions of records

#When you convert text into embeddings (high-dimensional vectors), you need a smart way to search for the “closest” match (similar meaning) — that’s what FAISS does best.
#Instead of brute-force searching every vector (which is slow), FAISS indexes them for fast approximate nearest neighbor (ANN) search.
#   1.	Text is split into chunks (100 characters).
#	2.	Embeddings are created using OpenAI.
#	3.	FAISS stores the embeddings.
#	4.	Query is embedded and similar chunks retrieved.
#	5.	Retrieved context is passed to GPT for answering.

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

from dotenv import load_dotenv
import os

# Load environment variables (make sure .env has OPENAI_API_KEY)
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print("[INFO] Environment variables loaded.")

# Step 1: Sample document
document = """LangChain is a framework for building applications with LLMs. 
It helps developers structure complex workflows involving language models, 
retrievers, prompts, memory, and more."""

print("[STEP 1] Loaded sample document:")
print(document)
print(f"Type of document: {type(document)}")
print("This is a simple string containing the text to be processed.")
print("-" * 60)

# Step 2: Split the document into chunks
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=10)
print(f"[STEP 2] Initialized text splitter: {text_splitter}")
print(f"Type of text_splitter: {type(text_splitter)}")
print("The text splitter will break the document into smaller chunks for embedding and retrieval.")
chunks = text_splitter.split_text(document)
print(f"Document split into {len(chunks)} chunk(s):")
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk}")
print(f"Type of chunks: {type(chunks)} (list of strings)")
print("-" * 60)

# Step 3: Create Embeddings
embedding_model = OpenAIEmbeddings()
print("[STEP 3] OpenAI embedding model initialized.")
print(f"Type of embedding_model: {type(embedding_model)}")
print("This model converts text chunks into numerical vectors for similarity search.")
print("-" * 60)

# Step 4: Create FAISS Vector Store
vector_store = FAISS.from_texts(chunks, embedding_model)
print("[STEP 4] FAISS vector store created with embeddings.")
print(f"Type of vector_store: {type(vector_store)}")
print("The vector store holds the embeddings and allows for efficient similarity search.")
print("-" * 60)

# Step 5: Create Retriever
retriever = vector_store.as_retriever()
print("[STEP 5] Retriever created from FAISS store.")
print(f"Type of retriever: {type(retriever)}")
print("The retriever is an object that can search the FAISS vector store for relevant chunks based on a query.")
print("-" * 60)

# Step 6: Load LLM
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
print("[STEP 6] ChatOpenAI model initialized.")
print(f"Type of llm: {type(llm)}")
print("This is the language model that will answer questions using retrieved context.")
print("-" * 60)

# Step 7: Build QA Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)
print("[STEP 7] RetrievalQA chain constructed.")
print(f"Type of qa_chain: {type(qa_chain)}")
print("This chain combines retrieval and LLM to answer questions with supporting context.")
print("-" * 60)

# Step 8: Ask a question
query = "What is LangChain used for?"
print(f"[STEP 8] User Query: {query}")
print(f"Type of query: {type(query)}")
print("This is the question that will be answered using the QA chain.")

response = qa_chain.invoke({"query": query})
print("[STEP 9] Response from RetrievalQA Chain:")
print(f"Type of response: {type(response)}")
print("This is a dictionary containing the answer and source documents.")
print("Answer:", response["result"])

# Optional: show sources
print("-" * 60)
print("[INFO] Retrieved Source Document(s):")
for doc in response['source_documents']:
    print(doc.page_content)
print(f"Type of each source document: {type(doc)}")