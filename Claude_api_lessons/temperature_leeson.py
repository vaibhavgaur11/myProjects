from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-0"



def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages, temperature, system=None):
    params = {
        "model": model,
        "max_tokens": 100,
        "messages": messages,
        "temperature": temperature
    }
    
    if system:
        params["system"] = system
    
    message = client.messages.create(**params)
    return message.content[0].text


messages = []

add_user_message(messages, "What is the best movie idea you can come up with?")
temperature = 1

answer = chat(messages, temperature=temperature)
print("Claude:", answer)