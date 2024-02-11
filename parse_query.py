import google.generativeai as genai
from dotenv import load_dotenv
import os
from gemini_context_manager import GeminiContextManager
import re

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
        "usertable": ["user_id"],
        "userinfo": ["fullname", "date_of_birth"],
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
You are a natural language processor. Your job is to generate valid SQL queries based on the user's input. The user will provide a dictionary of tables and columns. If the query wants to get all patients with certain condition, the query returned should be something like this: SELECT userinfo.fullname FROM userinfo JOIN (necessary table name) ON userinfo.user_id = (necessary table name).user_id WHERE (necessary table name).(something) = 'something required';
Below are the didctionary where key is the name of the table in the database, and the value is the list of columns in the table. Only use values in this dictionary to generate the SQL query.

Dictionary:
{str(cols)}

return format:
["~SQL query here~"]

example:
["SELECT * FROM usertable"]
["SELECT surgery from surgeries"]

IMPORTANT: FOLLOW THE PROVIDED FORMAT EXACTLY.
IMPORTANT: ONLY RETURN THE QUERY STRING. DO NOT RETURN ANYTHING ELSE.
IMPORTANT: DO NOT INCLUDE BACK QUOTES OR STRING UNRELATED TO THE QUERY.
IMPORTANT: DO NOT INCLUDE COLUMNS THAT ARE NOT IN THE DICTIONARY ABOVE.
""")

context_manager.add_context("model","Certainly, I can help with creating the SQL quey.")

def sanitize(text):
    text = text.replace("\n"," ")
    text = text.replace("`","")
    text = text.replace("sql","")
    #text = text.replace("*"," * ")
    #text = re.sub("\W+", " ", text)
    return text

def parse_query(input_text):
    chat = model.start_chat(history=context_manager.get_context())
    response = chat.send_message(input_text)
    response = sanitize(response.text)
    return response

def main():
    response = parse_query("I want all the medicine prescription")
    
if __name__ == "__main__":
    main()