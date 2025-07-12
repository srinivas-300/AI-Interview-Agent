 
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("evaluation_prompt")

def evaluator_prompt_builder(jd_analysis, guidelines, questions, last_response, history):
    formatted_history = "\n".join(
        [f"Candidate: {turn['candidate']}\nInterviewer: {turn['agent']}" for turn in history]
    )

    prompt = f"""
You are an AI interviewer assistant helping evaluate a candidate's response during a live job interview for the role of:

{jd_analysis}

INTERVIEW GUIDELINES:
{guidelines}

INTERVIEW CONTEXT:
These are the interview questions prepared so far:
{questions}

Recent conversation history:
{formatted_history}

Candidate's latest response:
"{last_response}"

---

YOUR EVALUATION TASK:
Carefully evaluate the candidate’s latest response along the following soft-skill dimensions:

1. **Body Language**  
   - If body posture or behavioral indicators are described (e.g., "I usually keep eye contact", "I smile when..."), assess for confidence, professionalism, and composure.
   - If not mentioned explicitly, infer possible posture based on tone or choice of words.

2. **Tone of the Interview**  
   - Assess whether the candidate is confident, collaborative, defensive, open, respectful, evasive, etc.
   - Is the tone appropriate for a professional interview?

3. **Communication Skills**  
   - Evaluate clarity, articulation, logical flow, conciseness, and ability to explain technical or strategic points clearly.
   - Note if they answered the question directly or went off-topic.

4. **Diversity and Inclusion Awareness**  
   - Look for signs of inclusive thinking, openness to collaboration, or mention of equitable practices.
   - If nothing is explicitly stated, infer their stance based on phrasing and values reflected.

Please return a structured response in this format:

- Body Language:
- Tone:
- Communication Skills:
- Diversity and Inclusion Awareness:
"""

    log.info(f"\n--------evaluation_prompt--------\n{prompt}\n------------")

    return prompt
