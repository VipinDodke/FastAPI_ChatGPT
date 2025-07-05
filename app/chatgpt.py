import openai
from dotenv import load_dotenv
import os

load_dotenv()  

openai.api_key = os.getenv("OPENAI_API_KEY") 

def ask_gpt(resume_text: str, question: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Act like an interviewer"},
            {"role": "user", "content": f"My resume:\n{resume_text}"},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content
