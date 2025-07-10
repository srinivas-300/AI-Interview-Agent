import logging
from app.services.llm_service import ask_llm

log = logging.getLogger("interview_guide_agent")
logging.basicConfig(level=logging.INFO)

class InterviewGuideAgent:
    def __init__(self, jd, role, resume):
        self.jd = jd
        self.role = role
        self.resume = resume

    def guide_agent(self):
        
        prompt1 = (
            f"You are preparing to conduct a technical interview for a {self.role} position.\n\n"
            f"Here is the job description:\n{self.jd}\n\n"
            f"Please extract the following:\n"
            f"1. Key technical skills required\n"
            f"2. Key soft skills required\n"
            f"3. Major responsibilities the candidate must handle\n"
            f"4. Traits or behaviors that define a strong candidate\n\n"
            f"Provide your answer in clearly labeled bullet points."
        )
        log.info(f"\n{prompt1}\n")
        response1 = ask_llm(prompt1)

        log.info(f"\n{response1}\n")
        
        prompt2 = (
            f"Using the analysis from the job description, design a structured interview for the {self.role} role.\n\n"
            f"Include the following in your answer:\n"
            f"- 3 to 5 core evaluation themes (e.g., problem-solving, system design, communication)\n"
            f"- The type of questions under each theme (coding, scenario-based, behavioral)\n"
            f"- Guidelines to differentiate strong vs weak responses\n\n"
            f"Present the output as a clear plan the interview agent can follow."
        )
        log.info(f"\n{prompt2}\n")
        response2 = ask_llm(prompt2)
        log.info(f"\n{response2}\n")
        
        prompt3 = (
            f"Now, consider the following candidate resume:\n{self.resume}\n\n"
            f"Based on this resume and the {self.role} role:\n"
            f"1. Identify the strengths and relevant experiences of the candidate\n"
            f"2. Point out any unclear areas or gaps that should be clarified\n"
            f"3. Suggest a few personalized questions tailored to this candidate\n\n"
            f"Respond in bullet points under each section."
        )
        log.info(f"\n{prompt3}\n")
        response3 = ask_llm(prompt3)
        log.info(f"\n{response3}\n")
        
        final_analysis = (
            f"--- JD Analysis ---\n{response1.strip()}\n\n"
            f"--- Interview Plan ---\n{response2.strip()}\n\n"
            f"--- Resume Analysis ---\n{response3.strip()}"
        )

        log.info("Completed guide_agent with structured analysis.")
        return final_analysis
