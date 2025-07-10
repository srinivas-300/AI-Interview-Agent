# import os
# import logging
# import google.generativeai as genai

# # Set up logging
# logging.basicConfig(level=logging.INFO)
# log = logging.getLogger("llm_service")

# # Configure Gemini
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# try:
#     chat_model = genai.GenerativeModel("gemini-1.5-flash")
#     chat_session = chat_model.start_chat()
#     log.info(" Gemini model initialized.")
# except Exception as e:
#     log.error("Error initializing Gemini model: %s", str(e))
#     chat_session = None

# def ask_llm(prompt: str) -> str:
#     log.info(" \n Prompt to Gemini: %s", prompt)
#     try:
#         if chat_session is None:
#             raise RuntimeError("Gemini model was not initialized.")
#         response = chat_session.send_message(prompt)
#         log.info("\n Gemini response: %s", response.text)
#         return response.text.strip()
#     except Exception as e:
#         log.error("Error from Gemini: %s", str(e))
#         return "Error getting response from the agent."


import os
import logging
import google.generativeai as genai

# Set up logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("llm_service")

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

try:
    chat_model = genai.GenerativeModel("gemini-1.5-flash")
    log.info("Gemini model initialized.")
except Exception as e:
    log.error("Error initializing Gemini model: %s", str(e))
    chat_model = None

def ask_llm(prompt: str) -> str:
    log.info("\nPrompt to Gemini:\n%s", prompt)
    try:
        if chat_model is None:
            raise RuntimeError("Gemini model was not initialized.")
        
        response = chat_model.generate_content(prompt)
        log.info("\nGemini response:\n%s", response.text)
        return response.text.strip()
    except Exception as e:
        log.error("Error from Gemini: %s", str(e))
        return "Error getting response from the agent."
