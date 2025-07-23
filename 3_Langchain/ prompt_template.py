from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 1. Define a prompt template
template = """
You are an expert assistant.
Answer the following question clearly and concisely.

Question: {question}
"""

prompt = PromptTemplate(
    input_variables=["question"],
    template=template
)

# 2. Format the prompt with input
final_prompt = prompt.format(question="What are the benefits of using LangChain with OpenAI GPT?")
#
#final_prompt = prompt.format(question="Capital of the UK?")

# 3. Create an LLM instance
llm = ChatOpenAI(
    model_name="gpt-4o-mini",
    temperature=0.7,
    api_key=OPENAI_API_KEY
)

# 4. Get response
response = llm.invoke(final_prompt)
print("LLM Response:", response.content)