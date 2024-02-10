import google.generativeai as genai
from dotenv import load_dotenv
import os
from gemini_context_manager import GeminiContextManager

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)




# creating system prompt

context = GeminiContextManager()
context.add_context("user",
"""
This is a system prompt.
You are a doctor. give a response to the patient.   
""")
context.add_context("model","""

Certainly, I can help you with that.
                    
""")

# model config

safety_sttings = [
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

model = genai.GenerativeModel("gemini-pro",safety_settings=safety_sttings)
chat = model.start_chat(history=context.get_context())

response = chat.send_message("I have a headache")

print(response.text)