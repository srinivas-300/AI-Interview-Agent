from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.data.ChatRequest import ChatRequest
from app.data.AuthRequest import AuthRequest
from app.agents.interview_agent import InterviewAgent
from app.services.db_service import store_conversation_history , verify_user_id

app = FastAPI()

# Allow CORS for frontend access (adjust origin if deployed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Redirect /interview to /chat
@app.get("/interview")
def redirect_to_chat():
    return RedirectResponse(url="/chat")


agent = InterviewAgent(role="Data Scientist")

@app.post("/authenticate")
async def authenticate_user(auth: AuthRequest):
    if verify_user_id(auth.user_id):
        return {"authenticated": True}
    return {"authenticated": False}

@app.post("/chat")
def chat(request: ChatRequest):
    response = agent.ask_question(request.message)
    return {"response": response}


@app.get("/chat")
def chat_home():
    return {"message": "Interview chat is ready. Send POST /chat with your message."}

@app.post("/end")
async def end_interview():
    if agent and agent.history:
        store_conversation_history(agent.history,agent.role)
        agent.role = None
        agent.history = []
        return {"message": "Interview history saved and agent state reset."}
    return {"message": "No active history to save."}


# Resume parser stub
@app.get("/resume-parser")
def resume_parser():
    return {"message": "Resume Parser backend is working!"}
