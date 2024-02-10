import google.generativeai as genai
from dotenv import load_dotenv
import os
from translator import Translator
from text_parser import TextParser
import time
import ast

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

class PreProcessor:
    def __init__(self):
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
        self.chat = model.start_chat()
        self.translator = Translator()
        self.parser = TextParser()
    
    def to_dict(self, text):
        return ast.literal_eval(text)
    
    def preprocess(self, text):
        response = self.translator.translate(text, self.chat)
        response = self.parser.parse(response, self.chat)
        response = self.to_dict(response)
        
        # dictionary
        return response

def main():
    preprocessor = PreProcessor()
    response = preprocessor.preprocess("""
                                       
患者番号: #123456
名前: ジョン・ドウ
生年月日: 1990-05-15
性別: 男性
身長: 180 cm
体重: 75 kg
人種: 白人
民族: 指定なし

処方箋:
- 薬: パロキセチン
- 用量: 20 mg
- 頻度: 1回/日
- 開始日: 2022-01-01

ワクチン:
- 名前: コロナワクチン
- 開始日: 2022-01-01

検査結果:
- 結果: 陰性
- 日付: 2022-01-01

手術履歴:
- 手術: なし
- 日付: なし

注意事項:
- 注意事項: 食事の後に服用してください
- 日付: 2022-01-01

医師の署名:
- 署名: Dr. Smith                                       
                                       """)
    
    
    
    print(response)
    print(type(response))
    
    
if __name__ == "__main__":
    t1 = time.time()
    main()
    t2 = time.time()
    print(f"Time taken: {t2-t1} seconds")