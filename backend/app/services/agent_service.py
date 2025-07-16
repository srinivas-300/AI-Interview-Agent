from langgraph.graph import StateGraph, END
from typing import Literal
from app.services.llm_service import ask_llm
from app.services.tavily_service import tavily_search
from app.data.AgentState import AgentState
from app.utils.agent_service_prompt_builder import *

from judgeval.tracer import Tracer
from judgeval.scorers import AnswerRelevancyScorer

judgment = Tracer(project_name="InterviewAgentTracing")

@judgment.observe(span_type="decision")
def decision_node(state: AgentState) -> AgentState:
    prompt = requires_tool_prompt(state["question"])
    decision = ask_llm(prompt)
    return {**state, "decision": decision.strip()}

def tool_needed(state: AgentState) -> Literal["tool", "llm"]:
    return "tool" if state["decision"].upper().startswith("YES") else "llm"

@judgment.observe(span_type="tool")
def tool_node(state: AgentState) -> AgentState:
    # Ask LLM which tool to use
    tool_prompt = selection_tool_prompt(state["question"])
    selected_tool = ask_llm(tool_prompt).strip().lower()

    # Use selected tool
    if selected_tool == "tavily_search":
        output = tavily_search(state["question"])
    else:
        output = f"Error: Unknown tool '{selected_tool}' selected by LLM."

    return {**state, "tool_output": output, "tool_selected": selected_tool}


@judgment.observe(span_type="llm")
def llm_node(state: AgentState) -> AgentState:
    prompt = final_response_prompt(state["question"], state.get("tool_output"))
    answer = ask_llm(prompt)
    
    # Real-time Evaluation
    judgment.async_evaluate(
        scorers=[AnswerRelevancyScorer(threshold=0.5)],
        input=state["question"],
        actual_output=answer,
        model="gpt-4.1"
    )

    return {**state, "final_answer": answer}

@judgment.observe(span_type="function")
def run_tool_augmented_agent(question: str):
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
