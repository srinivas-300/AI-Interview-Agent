from typing import Optional

# --- Prompt Templates ---
def requires_tool_prompt(question: str) -> str:
    return f"""
You're an intelligent AI interviewer. Determine if this question needs web search using the Tavily tool.

Question: "{question}"

Respond only with:
- NO — if the LLM can answer without external info.
- YES — if web search (tavily_search) is required.
"""

def final_response_prompt(question: str, tool_output: Optional[str] = None) -> str:
    if tool_output:
        return f"""Use the tool output below to answer the question.

Question: {question}

Tool Output: {tool_output}

Your final answer:"""
    else:
        return f"""Answer the following question:

Question: {question}
"""