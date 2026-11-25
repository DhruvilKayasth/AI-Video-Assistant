
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

llm = ChatGroq(
    model=os.getenv("GROQ_MODEL", "openai/gpt-oss-20b"),
    temperature=0.3,
    max_tokens=200
)

response = llm.invoke("Explain RAG in simple words.")

print(response.content)
