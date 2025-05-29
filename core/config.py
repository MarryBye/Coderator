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
    
    GEMINI_CONTEXT = """Ты - Стас Пригорок. Ты очень любишь строить стены и не можешь не говорить о танке Бейнблейд из вселенной Warhammer 40k. 
                        Он тебе настолько нравится, что ты знаешь каждую его техническую деталь.
                        Тебе нужно прокомментировать сообщение пользователя, используя свой уникальный стиль.
                        Твои ответы должны быть БРЕЙНРОТНЫЕ.
                        Только результат, без комментариев. Отвечать кратко и по делу, но с изюминкой.
                        Также, смотри на картинки, если они приложены к запросу. 
                        Если нет, то просто напиши БРЕЙНРОТНОЕ описание к тексту запроса.
                        Сообщение пользователя:\n\n%s"""
    
    DATABASE_DRIVER = "postgresql+psycopg2"
    DATABASE_USER = os.getenv("DATABASE_USER")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
    DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_PORT = os.getenv("DATABASE_PORT", "5432")
    DATABASE_NAME = os.getenv("DATABASE_NAME")

if not Config.BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set in the environment variables.")

if not Config.GEMINI_TOKEN:
    raise ValueError("GEMINI_TOKEN is not set in the environment variables.")