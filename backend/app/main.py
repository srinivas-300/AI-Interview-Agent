from http.client import HTTPException
from fastapi import Request
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.data.ChatRequest import ChatRequest
from app.data.AuthRequest import AuthRequest
from app.data.InterviewRequest import InterviewRequest
from app.data.InterviewResultRequest import InterviewResultRequest

from app.utils.email_template import *
from app.services.email_service import *

from app.agents.interview_agent import InterviewAgent
from app.utils.email_template import *
from app.services.db_service import *

app = FastAPI()

load_dotenv()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global singleton instance and user ID
agent = None
user_id = None

@app.post("/authenticate")
async def authenticate_user(auth: AuthRequest):
    global user_id
    if verify_user_id(auth.user_id):
        user_id = auth.user_id
        return {"authenticated": True}
    return {"authenticated": False}

@app.get("/interview")
def redirect_to_chat():
    return RedirectResponse(url="/chat")

@app.post("/chat")
async def chat(request: Request):
    global agent, user_id

    if not user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")

    user = get_user(user_id)
    if agent is None:
        agent = InterviewAgent(user)

    data = await request.json()  
    message = data.get("message")
    if not message:
        return {"error": "No message provided"}

    response = agent.chat(message)
    return {"response": response}

@app.get("/chat")
def chat_home():
    return {"message": "Interview chat is ready. Send POST /chat with your message."}

@app.post("/end")
async def end_interview():
    global agent ,user_id
    if agent and agent.history:

        user_feedback , final_score = agent.get_finalscore_userfeedback()

        store_score_feedback(user_id , final_score , user_feedback)
        store_conversation_history(agent.history, agent.role)

        email_content = interview_feedback_template(user_id,final_score)

        send_email(f'{os.getenv("ADMIN_EMAIL")}' , email_content)

        agent = None  # Clear singleton and memory
        return user_feedback
    return {"message": "No active history to save."}



@app.post("/interview_setup")
async def interview_setup(request: InterviewRequest):

    id = store_interview_setup_data(request.name,request.email,request.role ,request.jd, request.resume)

    content = interview_id_template(id)

    send_email(request.email,content)

    return {"message" : "interview has been set up"}


@app.get("/interview_details")
def interview_details():

    interview_details = get_interview_details()
    return interview_details

@app.post("/interview_result")
def interview_result(request: InterviewResultRequest):

    result_id = request.id

    result = get_interview_result(result_id)

    return result
