import google.generativeai as genai
from dotenv import load_dotenv
import os
from gemini_context_manager import GeminiContextManager

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

return format:
["~SQL query here~"]

IMPORTANT: FOLLOW THE PROVIDED FORMAT EXACTLY.
IMPORTANT: ONLY RETURN THE QUERY STRING. DO NOT RETURN ANYTHING ELSE.
IMPORTANT: DO NOT INCLUDE BACK QUOTES OR STRING UNRELATED TO THE QUERY.
""")

context_manager.add_context("model","Certainly, I can help with creating the SQL quey. and I will NOT add any texxts unreltaed to the query")

def sanitize(text):
    text.replace("\n","")
    text.replace("`","")
    text.replace("sql","")
    
    return text

def parse_query(input_text):
    chat = model.start_chat(history=context_manager.get_context())
    response = chat.send_message(input_text)
    response = sanitize(response.text)
    return response

def main():
    response = parse_query("I want all the medicine prescription")
    print(response)
    
if __name__ == "__main__":
    main()