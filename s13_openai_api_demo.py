from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
messages = [
    {
        "role": "system",
        "content": "You are a python expert",
    }
]

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(model="gpt-5-nano", messages=messages)

    assistant_message = response.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_message})

    print(f"Assistant: {assistant_message}")
