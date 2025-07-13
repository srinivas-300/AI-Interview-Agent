
from app.utils.prompt_builder import build_interview_prompt
import os
from app.services.interview_setup import interview_setup
from app.services.agent_service import run_tool_augmented_agent
from app.utils.evaluation_prompt_builder import evaluator_prompt_builder
from app.utils.final_score_prompt_builder import *

class InterviewAgent:
    def __init__(self, user):
        self.user = user
        self.role = user["role"]
        self.jd = user["jd"]
        self.resume = user["resume"]
        self.history = []
        self.jd_analysis,self.guidelines , self.questions = interview_setup(self.role, self.jd , self.resume).get_questions()

        

    def chat(self, message: str) -> str:
        #  Use guide questions + history to build the input
        
        evaluation_prompt = evaluator_prompt_builder(self.jd_analysis,self.guidelines , self.questions , message ,self.history)
        evaluation = run_tool_augmented_agent(evaluation_prompt)


        prompt = build_interview_prompt(
            questions=self.questions,
            evaluation = evaluation,
            role=self.role,
            last_response=message,
            history=self.history,
        )

        self.history.append({"candidate": message, "agent": ""})
        response = run_tool_augmented_agent(prompt)
        self.history[-1]["agent"] = response

        return response
    

    def get_finalscore_userfeedback(self) -> str:

        rubric_score_prompt = rubric_score_prompt_builder(self.history,self.jd_analysis, self.guidelines)
        rubric = run_tool_augmented_agent(rubric_score_prompt)

        final_score_prompt = final_score_prompt_builder(rubric , self.history)
        final_score = run_tool_augmented_agent(final_score_prompt)

        user_feedback_prompt = user_feedback_prompt_builder(final_score , self.history)
        user_feedback = run_tool_augmented_agent(user_feedback_prompt)
        return user_feedback , final_score
