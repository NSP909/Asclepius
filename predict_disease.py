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
You are a neural network model that predicts diseases and its probability based on the various medical records provided below. Make sure to predict based on the latest medical records.
Provide 3 diseases and their probability in the following format, in decending order of probability.

medical record:
{input}

return format:
[{{"disease": "disease_name", "probability": "probability in percentage"}}, ...]

IMPORTANT: FOLLOW THE PROVIDED RETURN FORMAT EXACTLY.
IMPORTANT: USE THE ACTUAL DISEASE NAME.
"""

def predict_disease(input_data=None):
    
    chat = model.start_chat()
    response = chat.send_message(PROMPT.format(input=str(input_data)))
    print(response.text)
    return response.text

def main():
    predict_disease()

if __name__ == "__main__":
    main()