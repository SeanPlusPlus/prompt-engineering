import openai
import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

