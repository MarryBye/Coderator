import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    GEMINI_TOKEN = os.getenv("GEMINI_TOKEN")
    
    GEMINI_TEXT_MODEL = "models/gemini-2.0-flash"
    GEMINI_IMAGE_MODEL = "models/imagen-3.0-generate-002"
    GEMINI_MAX_OUTPUT_TOKENS = 128
    GEMINI_MEDIA_RESOLUTION = "MEDIA_RESOLUTION_LOW"
    GEMINI_TEMPERATURE = 1.5
    GEMINI_TOP_K = 40
    GEMINI_TOP_P = 0.95

    GEMINI_SAFETY_SETTINGS = [
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE"
        }
    ]

if not Config.BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set in the environment variables.")

if not Config.GEMINI_TOKEN:
    raise ValueError("GEMINI_TOKEN is not set in the environment variables.")