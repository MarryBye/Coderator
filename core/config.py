import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    GEMINI_TOKEN = os.getenv("GEMINI_TOKEN")

if not Config.BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set in the environment variables.")

if not Config.GEMINI_TOKEN:
    raise ValueError("GEMINI_TOKEN is not set in the environment variables.")