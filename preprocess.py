import google.generativeai as genai
from dotenv import load_dotenv
import os
from gemini_context_manager import GeminiContextManager
from translator import Translator
from text_parser import TextParser

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

class PreProcessor:
    def __init__(self):
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
        self.chat = model.start_chat()
        self.translator = Translator()
        self.parser = TextParser()
    
    def preprocess(self, text):
        response = self.translator.translate(text, self.chat)
        response = self.parser.parse(response, self.chat)
        return response