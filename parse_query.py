import google.generativeai as genai
from dotenv import load_dotenv
import os
from gemini_context_manager import GeminiContextManager

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

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

cols = {
        "notes": ["note", "note_date"],
        "medicine": ["med_name", "med_dosage", "med_frequency", "med_date"],
        "vaccine": ["vac_name", "vac_date"],
        "lab_result": ["lab_result", "lab_date"],
        "surgeries": ["surgery", "surgery_date"],
        "emergencies": ["emergency_name", "emergency_date"],
        "vitals": ["vital_name", "vital_value", "vital_date"],
        "diagnosis": ["diagnosis", "diag_date"],
        "symptoms": ["symptom", "symptom_date"]
    }

context_manager = GeminiContextManager()
context_manager.add_context("user",f"""

This is a system prompt.
You are a natural language processor, that converts natural language to a structured SQL query.

below are the didctionary where key is the name of the table in teh database, and the value is the list of columns in the table.
{str(cols)}

IMPORTANT: ONLY RETURN THE QUERY STRING. DO NOT RETURN ANYTHING ELSE.

""")

context_manager.add_context("model","Certainly, I can help you with that.")

def parse_query(input_text):
    chat = model.start_chat(history=context_manager.get_context())
    response = chat.send_message(input_text)
    return response.text

def main():
    response = parse_query("I want all the medicine prescription")
    print(response)
    
if __name__ == "__main__":
    # TODO: actually testing this function
    # TODO: fix the text parser priniting extra lines in the beginning (sanitize)
    main()