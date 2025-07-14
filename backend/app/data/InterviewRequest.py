from pydantic import BaseModel

class InterviewRequest(BaseModel):
    name : str
    email : str
    role : str 
    jd :str
    resume : str