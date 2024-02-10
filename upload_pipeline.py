from preprocess import PreProcessor
from ocrMain import get_text
import json
import time

def upload_pipeline(image_path):
    text = get_text(image_path)
    preprocessor = PreProcessor()
    response = preprocessor.preprocess(text)
    return json.dumps(response)

def main():
    image_path = "ocr\input\images2.png"
    t1 = time.time()
    print(upload_pipeline(image_path))
    t2 = time.time()
    print(t2-t1)

if __name__ == "__main__":
    main()