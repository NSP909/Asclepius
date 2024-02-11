from dotenv import load_dotenv
import google.generativeai as genai
import os
from io import BytesIO
from PIL import Image

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-pro-vision")

PROMPT = f"""
You are a image processor that recognize the content of the image and extract information from it.
Your job is to extract information and provide texts in a structured format so that it can be easily processed by the next module.

valid tags:
{str({
        "notes": ["note", "note_date"],
        "medicine": ["med_name", "med_dosage", "med_frequency", "med_date"],
        "vaccine": ["vac_name", "vac_date"],
        "lab_result": ["lab_result", "lab_date"],
        "surgeries": ["surgery", "surgery_date"],
        "emergencies": ["emergency_name", "emergency_date"],
        "vitals": ["vital_name", "vital_value", "vital_date"],
        "diagnosis": ["diagnosis", "diag_date"],
        "symptoms": ["symptom", "symptom_date"]
})}
here, the key is the name of the table in the database, and the value is the list of columns in the table.
"""