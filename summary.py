from gemini_context_manager import GeminiContextManager
from dotenv import load_dotenv
import google.generativeai as genai
import os

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

PROMPT = """
You are a natural Language Processing model that summarizes the medical records to help the doctors to understand the patient's condition.
If there are any alerting signs, the model will highlight them.

medical record:
{input}
"""

def summarize(input_data=None):
    
    chat = model.start_chat()
    response = chat.send_message(PROMPT.format(input=str(input_data)))
    print(response.text)
    return response.text

def main():
    summarize()

if __name__ == "__main__":
    main()