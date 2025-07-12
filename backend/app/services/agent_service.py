from langgraph.graph import StateGraph, END
from typing import Literal
from app.services.llm_service import ask_llm
from app.services.tavily_service import tavily_search
from app.data.AgentState import AgentState
from app.utils.agent_service_prompt_builder import *



# Node 1: Decide whether to use a tool
def decision_node(state: AgentState) -> AgentState:
    temp = requires_tool_prompt(state["question"])
    print("\n----tool check prompt-----\n",temp,"\n-------------")
    decision = ask_llm(temp)
    print("\n---decision------\n",decision,"\n-------------\n")
    return {**state, "decision": decision.strip()}

# Router: Decide next path
def tool_needed(state: AgentState) -> Literal["tool", "llm"]:
    return "tool" if state["decision"].upper().startswith("YES") else "llm"

# Node 2: Use tavily_search tool
def tool_node(state: AgentState) -> AgentState:
    output = tavily_search(state["question"])
    print("\n----tool_output-----\n",output,"-------------\n")
    return {**state, "tool_output": output}

# Node 3: Final LLM Answer
def llm_node(state: AgentState) -> AgentState:

    temp = final_response_prompt(state["question"], state.get("tool_output"))
    print("\n------final prompt-------\n",temp,"\n-----------")
    final_answer = ask_llm(temp)
    print("\n----final_answer-----\n",final_answer,"\n-------------\n")
    return {**state, "final_answer": final_answer}



# --- Callable Agent Function ---
def run_tool_augmented_agent(question: str):

    # --- LangGraph Builder ---
    builder = StateGraph(AgentState)
    builder.add_node("decide", decision_node)
    builder.add_node("tool", tool_node)
    builder.add_node("llm", llm_node)

    builder.set_entry_point("decide")
    builder.add_conditional_edges("decide", tool_needed, {"tool": "tool", "llm": "llm"})
    builder.add_edge("tool", "llm")
    builder.add_edge("llm", END)

    graph = builder.compile()

    state = {
        "question": question,
        "decision": None,
        "tool_output": None,
        "final_answer": None
    }
    result = graph.invoke(state)
    
    return result["final_answer"]
