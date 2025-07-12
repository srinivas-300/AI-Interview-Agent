def jd_prompt_builder(role, jd):
    return f"""
You are an expert interviewer preparing to evaluate a candidate for the position of **{role}**.

Analyze the following job description from the perspective of a hiring manager:

JOB DESCRIPTION:
{jd}

Your task:
1. Extract the core responsibilities, technical skills, tools, and soft skills required for this role.
2. Identify both explicit and implicit expectations (e.g., leadership, deployment experience, scalability understanding).
3. Infer how a strong candidate should align with this description.

Output format:
- Core Responsibilities
- Required Technical Skills
- Required Soft Skills & Traits
- Implicit Expectations
- What to look for in a strong candidate
"""


def resume_prompt_builder(role, resume):
    return f"""
You are an interviewer assessing a candidate for the **{role}** role.

Here is the candidate's resume:
{resume}

Your task:
1. Evaluate how well the candidate aligns with the requirements and expectations of a typical {role}.
2. Identify strengths in their experience, skills, and projects that indicate suitability for this role.
3. Detect any potential red flags or missing experience.
4. Make note of interesting points to probe during the interview.

Output format:
- Summary of Candidate Strengths
- Role Alignment Assessment
- Red Flags or Concerns
- Key Follow-up Topics for Interview
"""

def guidelines_prompt_builder(role, resume_analysis, jd_analysis):
    return f"""
You are an AI interviewer preparing to conduct an interview for the **{role}** position.

You have the following two analyses:
1. Job Description Analysis:
{jd_analysis}

2. Candidate Resume Analysis:
{resume_analysis}

Your task:
Based on the above, create a detailed interview plan that:
1. Focuses on evaluating the most critical skills and competencies for this role.
2. Includes follow-up areas to probe further based on the candidate’s profile.
3. Suggests what a good answer vs. a weak answer would look like in those areas.

Structure your output as:
- Interview Focus Areas
- Candidate-Specific Follow-Up Areas
- Ideal Answer Characteristics (per topic)
- Red Flag Indicators
"""

def questions_prompt_builder(guidelines):
    return f"""
You are conducting a technical and behavioral interview for a candidate applying for a role.

You have the following interviewer preparation notes:
{guidelines}

Your task:
1. Generate a set of **6–8 in-depth interview questions** based on the guidelines.
2. Questions should include:
    - Deep technical problem-solving
    - Role-specific scenario questions
    - Behavioral/leadership questions based on resume red flags or strengths
    - One or two domain-oriented "thinking" questions to test analytical reasoning

Format:
1. [Technical] ...
2. [Behavioral] ...
3. [Scenario-based] ...
4. [Follow-up on Resume: <topic>] ...
...
"""
