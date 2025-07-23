# Create your first Interaction with an LLM using LangChain
# 
from langchain_openai import ChatOpenAI
import os 
from dotenv import load_dotenv

# Load environment variables
 
load_dotenv()
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')

# Initialize a chat model
model=ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7, api_key=OPENAI_API_KEY)

# Invoke the model
response=model.invoke("How can LangChain help developers improve their efficiency in a list of ways?")
print("Response from model:", response.content)
