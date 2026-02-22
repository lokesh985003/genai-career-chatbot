import google.generativeai as genai
from config.settings import settings
from prompts.system_prompt import get_system_prompt
from utils.logger import get_logger

logger = get_logger()

# Limit how many previous messages are sent to avoid token overflow
MAX_CONTEXT_MESSAGES = 4


class GeminiService:

    def __init__(self):
        if not settings.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY missing in .env")

        # Configure API key
        genai.configure(api_key=settings.GEMINI_API_KEY)

        # Initialize model
        self.model = genai.GenerativeModel(
            model_name=settings.MODEL_NAME,
            system_instruction=get_system_prompt()
        )

    def generate_response(self, chat_history):
        try:
            if not chat_history:
                return "Please ask a question."

            # Keep only recent messages (sliding window memory)
            trimmed_history = chat_history[-MAX_CONTEXT_MESSAGES:]

            # Convert chat history to Gemini format
            formatted_history = []

            for msg in trimmed_history[:-1]:
                role = "user" if msg["role"] == "user" else "model"

                formatted_history.append({
                    "role": role,
                    "parts": [msg["content"]]
                })

            # Latest user message
            latest_user_message = trimmed_history[-1]["content"]

            # Start chat session
            chat = self.model.start_chat(history=formatted_history)

            # Send latest message
            response = chat.send_message(latest_user_message)

            return response.text

        except Exception as e:
            error_message = str(e)

            # Quota exceeded
            if "429" in error_message:
                logger.error(f"Quota exceeded: {error_message}")
                return "🚫 API quota exceeded. Please try again later."

            # Invalid API key
            if "API key not valid" in error_message:
                logger.error(f"Invalid API Key: {error_message}")
                return "🔑 Invalid API key. Please check your configuration."

            # Invalid role format
            if "valid role" in error_message:
                logger.error(f"Role formatting error: {error_message}")
                return "⚠️ Chat formatting error. Please restart the app."

            # Model not found
            if "not found" in error_message:
                logger.error(f"Model error: {error_message}")
                return "⚠️ Model not available. Check MODEL_NAME in settings."

            logger.error(f"Gemini API Error: {error_message}")
            return "⚠️ Error generating response. Check logs."