# lc_chain_SequentialChain.py

# Sequential Chains
# These chains are used to create a sequence of chains.
# Product Name
#   ↓
# [Step 1] LLM: Generates Description
#   ↓
# [Step 2] LLM: Translates it to French
#   ↓
# Output

# Importing the necessary libraries
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import SimpleSequentialChain
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize LLM
llm = ChatOpenAI(model_name="gpt-4o", temperature=0.7, api_key=api_key)

# Step 1: Generate a product description
description_prompt = PromptTemplate(
    input_variables=["product"],
    template="Write a short, creative description for a product called: {product}"
)

# Step 2: Translate the description to French
translate_prompt = PromptTemplate(
    input_variables=["text"],
    template="Translate the following English text to French:\n\n{text}"
)

# Create chains
# Step 1: Chain to generate description
step1_chain = description_prompt | llm
# Step 2: Chain to translate to French
step2_chain = translate_prompt | llm

# Combine them in sequence using RunnableSequence
from langchain_core.runnables import RunnableSequence

# The first step expects a dict with 'product', the second expects 'text'.
# We'll use a lambda to map the output of step1 to the input of step2.
chain = (
    step1_chain
    | (lambda desc: {"text": desc})
    | step2_chain
)

# Run it
product_name = "EcoSmart Water Bottle"
final_output = chain.invoke({"product": product_name})

print("\n✅ Final Output in French:\n", final_output.content)