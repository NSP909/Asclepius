import google.generativeai as genai
from dotenv import load_dotenv
import os
from gemini_context_manager import GeminiContextManager

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

class Translator:
    def __init__(self):
        context_manager = GeminiContextManager()
        # configure system prompt

        context_manager.add_context("user",
        """
        This is a system prompt.
        You are a professional translator, who was hired to translate various medicala documents from varrious languages to English.
        
        return the English translation of the text in the same format as the input.
        IMPORTANT: DO NOT CHANGE THE FORMAT OF THE TEXT.  
        """)
        context_manager.add_context("model","""

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

        self.system_prompt = context_manager.get_context()
        model = genai.GenerativeModel("gemini-pro",safety_settings=safety_sttings)
        self.chat = model.start_chat(history=self.system_prompt)
    
    def translate(self, text):
        self.chat.history = self.system_prompt
        response = self.chat.send_message(text)
        return response.text
    
    def print_history(self):
        for message in self.chat.history:
            print(f"Role: {message.role}, Text: {message.parts[0].text}")


def main():
    translator = Translator()
    response = translator.translate("通院履歴:なし, アレルギー:[杉花粉]")
    response = translator.translate("通院履歴:あり, アレルギー:[猫]")
    translator.print_history()
    print(response)

if __name__ == "__main__":
    main()