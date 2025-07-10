

def build_interview_guide_prompt(jd,role,resume):


    prompt = (
        f"You are GUIDE conducting a job interview for a {role} role.\n"
        f"These are the candidate details {resume}\n"
        f"This is the job description {jd}\n"
        f"Read the resume and jd and provide informative "
    )

    return prompt