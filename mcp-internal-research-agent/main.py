import warnings
warnings.filterwarnings("ignore")

import requests
from langchain.agents import initialize_agent, Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain_chroma import Chroma
#from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config import GEMINI_API_KEY
from rag.loader import load_policies
from web.websearch import google_search

import os
os.environ["PYTHONWARNINGS"] = "ignore"

# 1. Load & index your HR policies
docs = load_policies()

# 2. Create a retriever + QA chain
embeddings = GoogleGenerativeAIEmbeddings(google_api_key=GEMINI_API_KEY, model="models/embedding-001")
vectorstore = Chroma(
    persist_directory=".chromadb",
    embedding_function=embeddings,
    collection_name="hr-policies"
)

# Add documents to the vectorstore
texts = [doc["text"] for doc in docs]
metadatas = [{"source": doc["source"]} for doc in docs]
vectorstore.add_texts(texts=texts, metadatas=metadatas)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
policy_qa = RetrievalQA.from_chain_type(
    llm=ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=GEMINI_API_KEY
    ),
    retriever=retriever,
    return_source_documents=True
)

# 3. Define your LangChain tools
tools = [
    Tool(
        name="HRPolicyQA",
        func=lambda q: policy_qa.invoke({"query": q})["result"],
        description="Answer questions based on the actual HR policy document content. Use this to find specific policies, rules, and guidelines from the company's HR document."
    ),
    Tool(
        name="WebSearch",
        func=lambda q: google_search(q),
        description="Fetch industry benchmarks & regulatory updates."
    ),
]

# 4. Initialize the agent
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    google_api_key=GEMINI_API_KEY
)
agent = initialize_agent(
    tools, llm,
    agent="zero-shot-react-description",
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=3,
    early_stopping_method="generate"

)

def run_query(query: str):
    enhanced_query = f"Based on the company's HR policy document, {query}"
    result = agent.run(enhanced_query)
    return result

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:]).strip()
        print(f"❓ Question: {question}")
        try:
            answer = run_query(question)
            print(f"✅ Answer: {answer}")
        except Exception as e:
            print(f"❌ Error: {e}")
    else:
        print("Usage: python3 main.py 'Your question here'")
        print("Or import and use run_query() in your own code.")