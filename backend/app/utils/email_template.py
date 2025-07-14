import os


def interview_id_template(id :str ) -> str:

    frontend_url = f'{os.getenv("frontend_url")}'

    return (f"You are selected for the interview!\n"
            f"Please use the following id and URL to start the interview:\n"
            f"ID : {id} \n"
            f"URL : {frontend_url}/interview")


def interview_feedback_template(user_id : str,final_score: str) -> str:
    return (f"The interview result for id -----{user_id} is ready!\n"
            f"{final_score}")