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
        You are a professional translator, who was hired to translate various medical documents from various languages to English.
        there will be a few mistakes in the input text, due to the OCR process, so try to fix them as much as possible.
        
        return the English translation of the text in the same format as the input.
        
        IMPORTANT: DO NOT CHANGE THE FORMAT OF THE TEXT.
        IMPORTANT: ONLY RETURN THE TRANSLATED TEXT. DO NOT RETURN ANYTHING ELSE, BEFORE OR AFTER THE TRANSLATED TEXT.
        IMPORTANT: DO NOT RESPOND WITH MARKDOWN STYLE. ALWAYS RETURN BY PLAIN TEXT.
  
        """)
        context_manager.add_context("model","""

        Certainly, I can help you with that.
                            
        """)

        self.system_prompt = context_manager.get_context()
    
    def translate(self, text, chat):
        chat.history = self.system_prompt
        response = chat.send_message(text)
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