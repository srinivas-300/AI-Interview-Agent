import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("prompt_builder")

def build_interview_prompt(role: str, last_response: str, history: list) -> str:
    history_str = ""
    for exchange in history:
        history_str += f"Candidate: {exchange['candidate']}\nAgent: {exchange['agent']}\n"

    log.info(f"The past history_str -------\n{history_str}\n")
    
    prompt = (
        f"You are conducting a job interview for a {role} role.\n"
        f"This is the history so far \n{history_str}"
        f"Candidate just said: \"{last_response}\"\n"
        f"What is your next question?"
    )
    return prompt
