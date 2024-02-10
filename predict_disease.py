from gemini_context_manager import GeminiContextManager
from dotenv import load_dotenv
import google.generativeai as genai
import os
from flask import get_all_data

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE"
            }
        ]
        
model = genai.GenerativeModel("gemini-pro",safety_settings=safety_settings)

message = """
You are a neural network model that predicts diseases and its probability based on the medical record provided below.
Provide 3 diseases and their probability in the following format, in decending order of probability.

medical record:
{input}

return format:
{{ [{{"disease": "disease_name", "probability": "~probability~"}}, ...]}}

IMPORTANT: FOLLOW THE PROVIDED RETURN FORMAT EXACTLY.
"""

def predict_disease(user_id):
    if type(user_id) != str:
        user_id = str(user_id)
    info_list = get_all_data(user_id)
    
    """chat = model.start_chat()
    response = chat.send_message()"""

def main():
    name = "1"
    predict_disease()

if __name__ == "__main__":
    main()