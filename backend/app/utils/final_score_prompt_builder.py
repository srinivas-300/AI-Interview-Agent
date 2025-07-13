

def rubric_score_prompt_builder(history, jd_analysis, guidelines):
    questions_only = "\n".join([f"- {turn['agent']}" for turn in history])

    prompt = f"""
You are an expert AI interview architect. Your job is to create a custom **evaluation rubric** for a candidate interview session.

This rubric should be derived purely from:
- The **job description analysis**
- The **interview guidelines**
- The **interview questions asked** (without considering the candidate’s answers)

---

JOB DESCRIPTION ANALYSIS:
{jd_analysis}

INTERVIEW GUIDELINES:
{guidelines}

INTERVIEW QUESTIONS:
{questions_only}

---

YOUR TASK:

1. Based on the job description and the nature of the interview questions, identify 5–7 core evaluation dimensions (e.g., Communication, Technical Depth, Problem Solving, Domain Knowledge, Leadership, DEI Awareness, etc.).

2. For each dimension, define:
   - A clear **description** of what is being measured and why it matters for this role.
   - A **scoring rubric** from 1 to 5 with explicit anchor points.

3. End with a **short rationale** explaining how the questions and rubric were aligned with the job role and expectations.

---

OUTPUT FORMAT:

Evaluation Rubric:

1. Category Name
   - Description: [What it measures and why]
   - Scoring Scale:
     - 1 = ...
     - 2 = ...
     - ...
     - 5 = ...

...

Rubric Design Rationale:
[Explain why these dimensions were selected based on the questions and job description]

Do not evaluate or score the candidate yet. Just return the rubric.
"""

    return prompt



def final_score_prompt_builder(rubric, history):
    full_conversation = "\n\n".join(
        [f"Interviewer: {turn['agent']}\nCandidate: {turn['candidate']}" for turn in history]
    )

    prompt = f"""
You are an AI interview evaluator.

Below is the **rubric** that defines the scoring dimensions and criteria for evaluating the candidate:

RUBRIC:
{rubric}

And here is the **complete conversation transcript** between the interviewer and the candidate:

INTERVIEW TRANSCRIPT:
{full_conversation}

---

YOUR TASK:

1. Carefully evaluate the candidate's responses across each rubric dimension.
2. For each dimension:
   - Assign a **score from 1 to 5**
   - Justify the score with **brief evidence** from the candidate’s responses.

3. Provide an overall **Goodness of Fit score (1–5)** that reflects the candidate’s suitability for the role.

4. Analyze the conversation structure and flow to determine if:
   - The interview ended **abruptly** (e.g., cutoff, missing closing, dropped midway)
   - The interview was **too short or prematurely ended** (e.g., not all questions answered)
   - If so, note this as a structural issue in the final recommendation

5. Conclude with a **recommendation summary** stating:
   - Whether the candidate is a strong fit, potential fit with gaps, or not suitable
   - Mention any interview flow issues (e.g., early end, short responses, disengagement) **only if they materially affect the evaluation**

---

OUTPUT FORMAT:

Final Evaluation:

1. Category Name: Score = X/5  
   - Justification: ...

...

Overall Goodness of Fit: X/5

Recommendation:
[Strong Fit / Potential Fit / Not Suitable]  
[1-2 lines summarizing your reasoning — include structural issues only if impactful]
"""

    return prompt




def user_feedback_prompt_builder(final_score, history):
    full_conversation = "\n\n".join(
        [f"Interviewer: {turn['agent']}\nCandidate: {turn['candidate']}" for turn in history]
    )

    prompt = f"""
You are an AI interview coach. Your task is to provide **constructive, professional feedback** to a candidate who just completed an interview.

You are given:
- A private final evaluation summary (NOT to be shown or referenced directly)
- The complete interview transcript between the interviewer and the candidate

---

FINAL EVALUATION SUMMARY:
{final_score}

---

INTERVIEW TRANSCRIPT:
{full_conversation}

---

YOUR TASK:

1. Review the candidate’s responses and overall conversation style.
2. Write a short feedback message **addressed to the candidate** that:
    - Is encouraging and respectful
    - Highlights general areas of strength (e.g., clarity, communication, relevant experience)
    - Offers **constructive suggestions** for improvement (e.g., provide examples, improve structure, elaborate more)
    - **Does not disclose or hint at any scores, scoring logic, rubric criteria, or evaluation decisions**

3. Speak like a human interviewer who wants to help the candidate grow. Avoid generic filler.

4. Be specific in your comments **based only on the conversation**, not on the rubric or score text.

Length: Keep the feedback message concise — ideally 1–2 paragraphs.

Do NOT include:
- Any mention of scores
- Any direct insight from the evaluation summary
- Any rubric terminology

Output only the final feedback message.
"""

    return prompt
