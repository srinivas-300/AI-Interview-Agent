from datetime import datetime, timezone
import os
import logging
from pymongo import MongoClient
from urllib.parse import quote_plus
from dotenv import load_dotenv
from bson.objectid import ObjectId

load_dotenv()

log = logging.getLogger("db_mongo_service")
logging.basicConfig(level=logging.INFO)

# Load and encode credentials
MONGO_USERNAME = quote_plus(os.getenv("MONGO_USERNAME"))
MONGO_PASSWORD = quote_plus(os.getenv("MONGO_PASSWORD"))

# Build URI
MONGO_URI = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@llmcluster.tudpm.mongodb.net/llmdb?retryWrites=true&w=majority&appName=llmcluster"


client = MongoClient(MONGO_URI)
db = client['llmdb']


def store_conversation_history(history, role):
    if not history:
        log.info("No history to store.")
        return

    document = {
        "role": role,
        "history": history
    }

    try:
        result = db['chat'].insert_one(document)
        log.info(f"Conversation stored with ID: {result.inserted_id}")
    except Exception as e:
        log.error(f"Failed to store conversation: {e}")

def verify_user_id(user_id: str) -> bool:
    user_id = ObjectId(user_id)
    user = db['selection'].find_one({"_id": user_id})
    return user is not None


def get_user(user_id: str) -> dict:
    try:
        user_id = ObjectId(user_id)
        user = db['selection'].find_one({"_id": user_id})
        return user  # returns None if not found
    except Exception as e:
        log.error(f"Error verifying user ID: {e}")
        return None
    

def store_score_feedback(user_id: str, final_score: str, user_feedback: str) -> str:
    document = {
        "user_id": user_id,
        "final_score": final_score,
        "user_feedback": user_feedback,
        "timestamp": datetime.now(timezone.utc)
    }
    try:
        result = db["interview_result"].insert_one(document)
        return f"New interview result inserted with ID: {result.inserted_id}"
    except Exception as e:
        log.error(f"Error inserting interview_result \n{e}\n")
        return None
    

def get_interview_details() -> list:
    try:
        details_cursor = db['selection'].find({}, {"_id": 1, "name": 1, "role": 1 ,"timestamp" : 1 })
        details = []

        for doc in details_cursor:
            doc["_id"] = str(doc["_id"])
            details.append(doc)

        return details
    except Exception as e:
        log.error(f"Error fetching interview details: {e}")
        return []


    
def store_interview_setup_data(name: str,email: str,role: str ,jd: str, resume: str) -> str:
    document = {
        "name": name,
        "email": email,
        "role" :role,
        "jd" : jd,
        "resume" : resume,
        "timestamp": datetime.now(timezone.utc)
    }

    try:
        result = db['selection'].insert_one(document)
        log.info(f"Conversation stored with ID: {result.inserted_id}")
        return result.inserted_id
    except Exception as e:
        log.error(f"Failed to store conversation: {e}")
        return f"{e}"
    
def get_interview_result(result_id: str):
    try:
        result = db['interview_result'].find_one(
            {"user_id": result_id},
            {"_id": 0}  # Exclude the _id field
        )
        return result  # Still returns None if not found
    except Exception as e:
        log.error(f"Error fetching interview result: {e}")
        return None


