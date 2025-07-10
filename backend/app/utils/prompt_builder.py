import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("prompt_builder")

def build_interview_prompt(analysis:str, role: str, last_response: str, history: list) -> str:
    history_str = ""
    for exchange in history[-9:]:
        history_str += f"Candidate: {exchange['candidate']}\nAgent: {exchange['agent']}\n"

    log.info(f"The past history_str -------\n{history_str}\n")
    

    prompt = (
        f"You are conducting a professional interview for a {role} role.\n\n"
        f"These are the candidate insights and interview plan you must follow:\n{analysis}\n\n"
        f"Here is the past conversation:\n{history_str}\n"
        f"The candidate just responded: \"{last_response}\"\n\n"
        f"Based on this context, generate the next interview question only.\n"
        f"Do NOT include any rationale, reasoning, commentary, or explanation.\n"
        f"Your tone should be concise, neutral, and professional.\n"
        f"Keep your response under 40 words."
    )

    log.info(f"The prompt -------\n{history_str}\n------------")
    return prompt
