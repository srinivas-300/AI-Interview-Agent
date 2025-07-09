from app.services.llm_service import ask_llm
from app.utils.prompt_builder import build_interview_prompt


class InterviewAgent:
    def __init__(self, role):
        self.role = role
        self.history = []

    def ask_question(self, candidate_response):
        prompt = build_interview_prompt(self.role, candidate_response, self.history)
        llm_response = ask_llm(prompt)
        self.history.append({"candidate": candidate_response, "agent": llm_response})
        return llm_response
