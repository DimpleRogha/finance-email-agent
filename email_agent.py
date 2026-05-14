from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

def generate_email(prompt):

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You generate finance follow-up emails."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        extra_headers={
            "HTTP-Referer": "http://localhost:8501",
            "X-Title": "finance-email-agent"
        }
    )

    return response.choices[0].message.content