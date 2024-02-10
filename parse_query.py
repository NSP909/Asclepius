import google.generativeai as genai
from dotenv import load_dotenv
import os
from gemini_context_manager import GeminiContextManager

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

context_manager = GeminiContextManager()
context_manager.add_context("user","""

This is a system prompt.
You are a natural language processor, that converts natural language to a structured SQL query.

""")

def parse_query(input_text):
    pass
