from app.services.agent_service import run_tool_augmented_agent
from app.utils.interview_setup_prompt_builder import *

class interview_setup:
    def __init__(self, role, jd, resume):
        self.role = role
        self.jd = jd
        self.resume = resume

    def get_questions(self):

        jd_prompt = jd_prompt_builder(self.role , self.jd)

        jd_analysis = run_tool_augmented_agent(jd_prompt)

        resume_prompt = resume_prompt_builder(self.role , self.resume)

        resume_analysis = run_tool_augmented_agent(resume_prompt)

        guidelines_prompt = guidelines_prompt_builder(self.role , resume_analysis , jd_analysis)

        guidelines = run_tool_augmented_agent(guidelines_prompt)

        questions_prompt = questions_prompt_builder(guidelines)

        questions = run_tool_augmented_agent(questions_prompt)

        return jd_analysis,guidelines ,questions