from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-20250514"

from datetime import datetime, timedelta
from anthropic.types import Message
import requests
import json
import os
# ─────────────────────────────────────────
# TOOL FUNCTIONS
# ─────────────────────────────────────────

def get_current_datetime(date_format="%Y-%m-%d %H:%M:%S"):
    if not date_format:
        raise ValueError("date_format cannot be empty")
    return datetime.now().strftime(date_format)








def get_weather(city):
    API_KEY = ""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    temp = data["main"]["temp"]
    return f"Current temperature in {city} is {temp}°C"


# ─────────────────────────────────────────
# TOOL SCHEMAS
# ─────────────────────────────────────────

get_current_datetime_schema = {
    "name": "get_current_datetime",
    "description": "Returns the current date and time formatted according to the specified format string.",
    "input_schema": {
        "type": "object",
        "properties": {
            "date_format": {
                "type": "string",
                "description": "Format string using Python strftime codes. Default is '%Y-%m-%d %H:%M:%S'",
                "default": "%Y-%m-%d %H:%M:%S"
            }
        },
        "required": []  # no required fields, date_format has a default
    }
}

get_weather_schema = {
    "name": "get_weather",
    "description": "Get current temperature for a city",
    "input_schema": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "Name of the city e.g. Hyderabad, London"
            }
        },
        "required": ["city"]
    }
}

# all tools in one list
tools = [
    get_current_datetime_schema,
    
    get_weather_schema
]

# ─────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────

def add_user_message(messages, message):
    user_message = {
        "role": "user",
        "content": message.content if isinstance(message, Message) else message
    }
    messages.append(user_message)


def add_assistant_message(messages, message):
    assistant_message = {
        "role": "assistant",
        "content": message.content if isinstance(message, Message) else message
    }
    messages.append(assistant_message)


def chat(messages, system=None, temperature=1.0, stop_sequences=[], tools=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature,
        "stop_sequences": stop_sequences,
    }
    if tools:
        params["tools"] = tools
    if system:
        params["system"] = system

    message = client.messages.create(**params)
    return message                        # returns full message object


def text_from_message(message):
    return "\n".join(
        [block.text for block in message.content if block.type == "text"]
    )


# ─────────────────────────────────────────
# TOOL ROUTING
# ─────────────────────────────────────────

def run_tool(tool_name, tool_input):
    """Routes tool name to actual function and calls it"""
    if tool_name == "get_current_datetime":
        return get_current_datetime(**tool_input)
    elif tool_name == "get_weather":
        return get_weather(**tool_input)
    else:
        raise ValueError(f"Unknown tool: {tool_name}")


def run_tools(message):
    """Finds all tool requests in Claude's response and runs each one"""
    tool_requests = [
        block for block in message.content if block.type == "tool_use"
    ]

    tool_result_blocks = []

    for tool_request in tool_requests:
        print(f"  → Calling: {tool_request.name} with {tool_request.input}")
        try:
            tool_output = run_tool(tool_request.name, tool_request.input)
            print(f"  ← Result: {tool_output}")
            tool_result_blocks.append({
                "type": "tool_result",
                "tool_use_id": tool_request.id,
                "content": json.dumps(tool_output),
                "is_error": False
            })
        except Exception as e:
            tool_result_blocks.append({
                "type": "tool_result",
                "tool_use_id": tool_request.id,
                "content": f"Error: {e}",
                "is_error": True
            })

    return tool_result_blocks

# ─────────────────────────────────────────
# CONVERSATION LOOP
# ─────────────────────────────────────────

def run_conversation(user_message):
    messages = []
    add_user_message(messages, user_message)

    print(f"User: {user_message}\n")

    while True:
        response = chat(messages, tools=tools)      # send to Claude
        add_assistant_message(messages, response)   # save Claude's reply

        text = text_from_message(response)          # extract text
        if text:
            print(f"Claude: {text}")

        if response.stop_reason != "tool_use":      # no more tools needed?
            break                                    # exit loop

        tool_results = run_tools(response)          # call the tools
        add_user_message(messages, tool_results)    # send results back

    return response

# ─────────────────────────────────────────
# RUN IT
# ─────────────────────────────────────────

run_conversation("What is current time")