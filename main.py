import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

messages = []

while True:
    user_input = input("User：")
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages = messages,
        stream = False
    )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    print(reply)