import google.generativeai as genai
from dotenv import load_dotenv
import os
from gemini_context_manager import GeminiContextManager

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

class TextParser:
    def __init__(self):
        
        context_manager = GeminiContextManager()
        
        # configure system prompt
        context_manager.add_context("user",
        """
        You are a text parser. Your job is to parse the input string to extract various medical information, and parse it so that our backend engineer can use it to store the information in our database.
        YOU MUST FOLLOW THE RESPONSE FORMAT EXACTLY.
        
        response format:
        { "notes": [{{ "note": "~doctor's note here~", "note_date": "~date in the format of YYYY-MM-DD if month or date is a single digit number, pad it with 0~"}}],
            "medicine": [{{ "med_name": "~medicine name here~", "med_dosage": "~medicine dosage here~", "med_frequency": "~medicine frequency here~", "med_date": "~medicine start date here~"}}, ...],
            "vaccine": [{{ "vac_name": "~vaccine name here~", "vaccine_date": "~vaccine start date here~"}}, ...],
            "lab_result": [{{ "lab_result": "~lab result here~", lab_date": "~lab date here~"}}],
            "surgeries": [{{ "surgery": "~surgery description here~", "surgery_date": "~surgery date here~"}}],
            "diagnosis": [{{ "diagnosis": "~diagnosis here~", "diagnosis_date": "~diagnosis date here~"}}],
            "symptoms": [{{ "symptom": "~symptom here~", "symptom_date": "~symptom date here~"}}, ...],
        }
        
        IMPORTANT: OBEY THE PROVIDED FORMAT.
        IMPORTANT: DO NOT INCLUDE ANY OTHER INFORMATION THAT IS NOT IN THE PROVIDED FORMAT.
        IMPORTANT: IF NO INFORMATION IS PROVIDED, PUT None INSTEAD.
        IMPORTANT: DO NOT RESPOND WITH MARKDOWN STYLE. ALWAYS RETURN BY PLAIN TEXT.
        IMPORTANT: ONLY RETURN THE DICTONARY. DO NOT RETURN ANYTHING ELSE, BEFORE OR AFTER THE DICTONARY.

        
        """)
        
        context_manager.add_context("model","Certainly, I can help you with that.")

        self.system_prompt = context_manager.get_context()
    
    def cut_off_until_bracket(self, text):
        bracket_index = text.find('{')
        if bracket_index != -1:
            return text[bracket_index:]
        else:
            return text
    
    def parse(self, text, chat):
        chat.history = self.system_prompt
        response = chat.send_message(text)
        print("is this?")
        print(response.text)
        return self.cut_off_until_bracket(response.text)

def main():
    parser = TextParser()
    response = parser.parse("""

    Patient ID: #123456
Name: John Doe
Date of Birth: 1990-05-15
Gender: Male
Height: 180 cm
Weight: 75 kg
Race: Caucasian
Ethnicity: Not specified

Prescription:

Medication: Ibuprofen
Dosage: 200 mg
Frequency: Twice daily
Start Date: 2024-02-10

notes:

Take Ibuprofen orally with a full glass of water after meals.
Do not exceed the recommended dosage of 400 mg per day.
In case of any adverse reactions, contact your healthcare provider immediately.
Doctor's Signature: Dr. Smith
    
    """)
    
    print(response)
    
if __name__ == "__main__":
    main()