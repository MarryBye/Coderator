from google.genai import Client, types
from core.config import Config

class Gemini(Client):
    def __init__(self, api_key: str):
        super().__init__(api_key=api_key)
        
        self.text_generator_settings = {
            "model": Config.GEMINI_TEXT_MODEL,
            "config": {
                "max_output_tokens": Config.GEMINI_MAX_OUTPUT_TOKENS,
                "safety_settings": Config.GEMINI_SAFETY_SETTINGS,
                "temperature": Config.GEMINI_TEMPERATURE,
                "top_k": Config.GEMINI_TOP_K,
                "top_p": Config.GEMINI_TOP_P
            }
        }
        
        self.image_generator_settings = {
            "model": Config.GEMINI_IMAGE_MODEL
        }

    def generate_text(self, prompt: str) -> types.Content:
        self.text_generator_settings["contents"] = {
            "role": "user",
            "parts": [
                {
                    "text": "Напиши 1 смешное описание к этому сообщению. Только результат, без комментариев:\n\n%s" % prompt
                }
            ]
        }
        response = self.models.generate_content(**self.text_generator_settings)

        return response.candidates[0].content if response.candidates else ""

    # def generate_image(self, prompt: str) -> types.Content:
    #     self.image_generator_settings["prompt"] = "Создай 1 картинку к этому сообщению. Только результат, без комментариев:\n\n%s" % prompt
    #     response = self.models.generate_images(**self.image_generator_settings)

    #     return response.candidates[0] if response.candidates else ""
    
gemini_client = Gemini(Config.GEMINI_TOKEN)