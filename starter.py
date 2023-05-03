import openai
import os
from dotenv import load_dotenv
from IPython.display import display, HTML

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

prompt = f"""
Your task is to list the ten largest cities in the world by population.

The output should be in an HTML table format.

The table columns should be "City Name", "Country", "Population".

Give the table the title "Largest Citites in the World".

Place the table and the title in a <div> element.
"""

response = get_completion(prompt)
display(HTML(response))