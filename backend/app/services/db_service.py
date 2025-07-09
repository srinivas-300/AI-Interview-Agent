import os
import logging
from pymongo import MongoClient
from urllib.parse import quote_plus
from dotenv import load_dotenv
from bson.objectid import ObjectId

load_dotenv()

log = logging.getLogger("mongo_service")
logging.basicConfig(level=logging.INFO)

# Load and encode credentials
MONGO_USERNAME = quote_plus(os.getenv("MONGO_USERNAME"))
MONGO_PASSWORD = quote_plus(os.getenv("MONGO_PASSWORD"))

# Build URI
MONGO_URI = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@llmcluster.tudpm.mongodb.net/llmdb?retryWrites=true&w=majority&appName=llmcluster"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client['llmdb']
collection = db['chat']

def store_conversation_history(history, role):
    if not history:
        log.info("No history to store.")
        return

    document = {
        "role": role,
        "history": history
    }

    try:
        result = collection.insert_one(document)
        log.info(f"Conversation stored with ID: {result.inserted_id}")
    except Exception as e:
        log.error(f"Failed to store conversation: {e}")

def verify_user_id(user_id: str) -> bool:
    user_id = ObjectId(user_id)
    user = db['selection'].find_one({"_id": user_id})
    return user is not None

