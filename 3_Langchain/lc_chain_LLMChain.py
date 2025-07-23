# lc_chain.py

# LLM Chains
#Explanation:
#	•	This is the most basic type of chain.
#	•	It directly:
#	1.	Accepts input (via a prompt template),
#	2.	Sends it to an LLM (like OpenAI),
#	3.	Returns the output.
#There’s no retrieval, no memory, and no multi-step sequence. It’s a simple:
# Prompt → LLM → Output

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import os 
from dotenv import load_dotenv

# Load environment variables 
load_dotenv()
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')

# Step 1: Define a prompt template
prompt = ChatPromptTemplate.from_template("List 3 ways LangChain helps developers be productive in {area}.")

# Step 2: Load the LLM
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)

# Step 3: Define the output parser
output_parser = StrOutputParser()

# Step 4: Create a chain using LCEL (pipe syntax)
chain = prompt | llm | output_parser

# Step 5: Run the chain
result = chain.invoke({"area": "software development"})

# Output the result
print("LLMChain Output:\n", result)