from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

model = ChatOllama(model="mistral", temperature=0.4)

def summarize_text(text: str) -> str:
    prompt = ChatPromptTemplate.from_template("""
    You are Auralis, a helpful text insight assistant, You are expected to give insights as a summarization.
    Summarize the following text and extract key insights.
    Text:
    {text}
    """)
    chain = prompt | model
    result = chain.invoke({"text": text})
    return result.content
