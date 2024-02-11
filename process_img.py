#TODO: get the image and if it is a xray or mri image, skip to data extraction. Otherwise, check the language and pass the image to OCR.
from dotenv import load_dotenv
import google.generativeai as genai
import os
from io import BytesIO
from PIL import Image

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-pro-vision")

PROMPT = """
You are a image processor that recognize the content of the image and extract information from it.
You look at the image and take one of two actions provided below.

1. If the image is a X-ray or MRI image:
respnose format: {{ "type": "xray/mri", "data": "~If there is any alarming information in the image, provide it here, otherwise None" }}

2. If the image is not a X-ray or MRI image:
response format: {{ "type": "document", "data": "~Language of the text~" }}
"""

def convert_to_pil(imgbase64):
    img = BytesIO(imgbase64)
    img = Image.open(img)
    return img

def process_img(imgbase64):
    img = convert_to_pil(imgbase64)
    response = model.generate_content([PROMPT, img])
    print(response.text)

def main():
    with open(r"ocr\input\images2.png","rb") as img:
        imgbase64 = img.read()
    process_img(imgbase64)

if __name__ == "__main__":
    main()