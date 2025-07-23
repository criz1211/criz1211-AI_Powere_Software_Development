from langchain_openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key=os.getenv("OPENAI_API_KEY")


if openai_api_key:   
    llm=OpenAI(openai_api_key=openai_api_key)
    output=llm.invoke("What is the capital of France?")
    print(output)
else:
    print("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
