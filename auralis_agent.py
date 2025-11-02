from langgraph.graph import StateGraph
from typing import TypedDict
from tools.ocr_tool import ocr_tool
from tools.insight_tool import summarize_text

class AuralisState(TypedDict):
    input_type: str  
    content: str

def process_input(state: AuralisState):
    if state["input_type"] == "image":
        text = ocr_tool(state["content"])
    else:
        text = state["content"]

    summary = summarize_text(text)
    return {"input_type": state["input_type"], "content": summary}

graph = StateGraph(AuralisState)
graph.add_node("process", process_input)
graph.set_entry_point("process")
graph.set_finish_point("process")

auralis = graph.compile()
