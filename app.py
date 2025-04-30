import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
import chainlit as cl
from chainlit.prompt import Prompt
from chainlit.playground.providers import ChatOpenAI


load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_template = """You are a helpful assistant who always speak in a pleasant tone!
"""

user_template = """{input}
Think through your response step by step.
"""


@cl.on_chat_start
async def start():
  
  settings = {
    "model": "gpt-3.5-turbo",
    "temperature": 0,
    "max_tokens": 500,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
  }
  
  cl.user_session.set("settings", settings)


@cl.on_message
async def handle(message: cl.Message):
    prompt = Prompt(
        system_template=system_template,
        user_template=user_template,
    )


