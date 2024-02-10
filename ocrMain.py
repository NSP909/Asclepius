import requests
import json
import base64
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from reportlab.pdfgen import canvas
from dotenv import load_dotenv
import os


VISION_GDCH_ENDPOINT = "vision.googleapis.com"

load_dotenv()

keyfile_path = os.getenv("VERTEX_VISION_PATH")


with open(keyfile_path, "r") as keyfile:
    credentials_info = json.load(keyfile)

credentials = service_account.Credentials.from_service_account_info(
    info=credentials_info,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)


credentials.refresh(Request())
access_token = credentials.token

def get_response(image_path, access_token):
    with open(image_path, "rb") as image_file:
        image_content = base64.b64encode(image_file.read()).decode("utf-8")


    annotate_image_request = {
        "requests": [
            {
                "image": {"content": image_content},
                "features": [
                    {"type": "TEXT_DETECTION"},
                ],
            }
        ]
    }


    json_data = json.dumps(annotate_image_request)

    url = f"https://{VISION_GDCH_ENDPOINT}/v1/images:annotate"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.post(url, data=json_data, headers=headers)
    return response

def get_text(response,line_height=40):
    if response.status_code == 200:
        
        result = response.json()


        text_annotations = result['responses'][0]['textAnnotations']

    
        sorted_words = sorted(text_annotations[1:], key=lambda x: (x['boundingPoly']['vertices'][0]['y']//line_height, x['boundingPoly']['vertices'][0]['x']))

        prev_line_y = sorted_words[0]['boundingPoly']['vertices'][0]['y']
        text = ""
        for word in sorted_words:
            word_text = word['description']
            text += word_text + " "
            word_y = word['boundingPoly']['vertices'][0]['y']

        
            if abs(word_y - prev_line_y) > line_height: 
                text += "\n"
                prev_line_y = word_y
        
        return text

    else:
        print(f"Error: {response.status_code}, {response.text}")

def main():
    image_path = "ocr\input\images3.jpg"
    response = get_response(image_path, access_token)
    print(get_text(response))

if __name__ == "__main__":
    main()
