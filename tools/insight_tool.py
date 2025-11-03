from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
#model = ChatOllama(model="mistral", temperature=0.4)
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  
    temperature=0.4
)
def summarize_text(text: str) -> str:
    prompt = ChatPromptTemplate.from_template("""
You are Auralis, an AI that extracts insights from documents concisely.

Analyze this text and respond in the most appropriate format:

**If it's a receipt/invoice:**
"Receipt from [Business] on [Date] at [Time] of [Total Amount] for [Person] 
- [Item 1]: [Price]
- [Item 2]: [Price]
- Payment method: [if mentioned]
- Tax: [if found]"

**If it's an article/document:**
"[One-two sentence summary of main topic]

Key points:
- [Point 1]
- [Point 2]
- [Point 3]
- And so on... "

**If it's data/statistics:**
"[What the data shows in one sentence]
- [Key metric 1]
- [Key metric 2]
- [Key metric 3]
- And so on... "

Keep responses under 100 words. Use bullet points (•) not asterisks. Be direct and factual.

Text to analyze:
{text}
""")

    chain = prompt | model
    result = chain.invoke({"text": text})
    return result.content
