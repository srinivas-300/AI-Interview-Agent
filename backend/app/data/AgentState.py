from typing import TypedDict, Optional

# --- LangGraph State ---
class AgentState(TypedDict):
    question: str
    decision: Optional[str]
    tool_output: Optional[str]
    final_answer: Optional[str]