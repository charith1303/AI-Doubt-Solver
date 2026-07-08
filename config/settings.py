import os
from dotenv import load_dotenv

try:
    import google.generativeai as genai
except ImportError as exc:
    raise ImportError(
        "google.generativeai package not found."
    ) from exc

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "Gemini API Key not found."
    )

genai.configure(api_key=GEMINI_API_KEY)

MODEL_NAME = "gemini-2.5-flash"

_model = None


def get_model():
    """
    Loads Gemini model only once.
    """

    global _model

    if _model is None:

        print("Loading Gemini Model...")

        _model = genai.GenerativeModel(MODEL_NAME)

    return _model