from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

model = ChatOllama(model="mistral", temperature=0.4)

def summarize_text(text: str) -> str:
    prompt = ChatPromptTemplate.from_template("""
    You are **Auralis**, an advanced AI insight assistant. 
    Your role is to analyze and summarize text **clearly and precisely** — keeping all **important numbers, entities, and facts** intact.

    ### Instructions:
    1. **Summarize** the text into concise, meaningful paragraphs.
    2. **Extract key insights** or data points — such as numbers, statistics, entities, or named events.
    3. **Present results in a structured way**:
        - A short summary (2-3 sentences)
        - Followed by a section: **Key Insights** in bullet points.
    4. Be factual, avoid interpretation or opinion.
    5. If the text is very short, respond with one summarized paragraph and skip headings.

    ---
    **Text to analyze:**
    {text}
    """)

    chain = prompt | model
    result = chain.invoke({"text": text})
    return result.content
