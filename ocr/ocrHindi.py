import requests
import json
import base64
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from dotenv import load_dotenv
import os

# Set your Google Cloud Vision API endpoint
VISION_GDCH_ENDPOINT = "vision.googleapis.com"

# Load environment variables
load_dotenv()

# Set the path to your service account key file
keyfile_path = r"C:\Users\sange\Downloads\favorable-mix-413908-a57969b30ec9.json"

with open(keyfile_path, "r") as keyfile:
    credentials_info = json.load(keyfile)

credentials = service_account.Credentials.from_service_account_info(
    info=credentials_info,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

# Refresh the credentials to obtain a valid access token
credentials.refresh(Request())

# Obtain the access token from the refreshed credentials
access_token = credentials.token

# Read the image file
image_path = r"C:\Users\sange\Downloads\Text-block-of-Devanagari-Script.png"

with open(image_path, "rb") as image_file:
    image_content = base64.b64encode(image_file.read()).decode("utf-8")

# Set your image annotation requests
annotate_image_request = {
    "requests": [
        {
            "image": {"content": image_content},
            "features": [
                {"type": "TEXT_DETECTION"},
            ],
            "imageContext": {
                "languageHints": ["hi"]
            }
        }
    ]
}

# Convert the request payload to JSON
json_data = json.dumps(annotate_image_request)

# Make the HTTP POST request
url = f"https://{VISION_GDCH_ENDPOINT}/v1/images:annotate"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}",
}

response = requests.post(url, data=json_data, headers=headers)

# Check the response
if response.status_code == 200:
    # Successful response
    result = response.json()

    # Extract text and bounding box information
    text_annotations = result['responses'][0]['textAnnotations']

    # Extract words and sort them by y and then x
    sorted_words = sorted(text_annotations[1:], key=lambda x: (x['boundingPoly']['vertices'][0]['y'], x['boundingPoly']['vertices'][0]['x']))

    # Register the custom font for Hindi
    pdfmetrics.registerFont(TTFont('Tiro Devanagari Hindi', r"C:\Users\sange\Downloads\Tiro_Devanagari_Hindi\TiroDevanagariHindi-Regular.ttf"))

    # Create a PDF with the registered font
    pdf_output_path = 'Asclepius\ocr\output\de.pdf'
    c = canvas.Canvas(pdf_output_path, pagesize=letter)
    c.setFont("Tiro Devanagari Hindi", 12)

    # Your PDF content goes here
    page_width = 600
    y_position = 500
    prev_line_y = sorted_words[0]['boundingPoly']['vertices'][0]['y']
    horizontal_spacing = 1
    for word in sorted_words:
        word_text = word['description']
        word_x, word_y = word['boundingPoly']['vertices'][0]['x'], word['boundingPoly']['vertices'][0]['y']

        # Check for a new line (vertical spacing)
        if abs(word_y - prev_line_y) > 20:
            y_position -= 20
            prev_line_y = word_y

        # Check for horizontal spacing
        word_width = c.stringWidth(word_text, "Tiro Devanagari Hindi", 12)
        if word_x + word_width > page_width:
            y_position -= 20
            prev_line_y = word_y
            word_x = 10

        # Draw the word with adjusted horizontal spacing
        word_x += word_width+ horizontal_spacing
        c.drawString(word_x, y_position, word_text)

    c.save()

    print(f"PDF created successfully: {pdf_output_path}")

else:
    # Handle errors
    print(f"Error: {response.status_code}, {response.text}")
