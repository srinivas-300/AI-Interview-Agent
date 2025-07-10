from app.services.llm_service import ask_llm
from app.utils.prompt_builder import build_interview_prompt
from app.services.db_service import  get_user
from app.agents.interview_guide_agent import InterviewGuideAgent


class InterviewAgent:
    def __init__(self,user_id):
        self.history = []
        self.user = get_user(user_id)
        self.role = self.user["role"]
        self.jd = self.user["jd"]
        self.resume = self.user["resume"]
        self.analysis = InterviewGuideAgent(self.jd , self.role ,self.resume).guide_agent()

    def ask_question(self, candidate_response):
        prompt = build_interview_prompt(self.analysis , self.role, candidate_response, self.history)
        llm_response = ask_llm(prompt)
        self.history.append({"candidate": candidate_response, "agent": llm_response})
        return llm_response
