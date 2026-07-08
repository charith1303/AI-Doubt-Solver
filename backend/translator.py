from config.settings import MODEL


def translate_text(text, language):
    """
    Translates text into the selected language.
    """

    if not text.strip():
        return "No text available to translate."

    prompt = f"""
You are Astra AI.

Translate the following text into {language}.

Do not explain anything.
Return ONLY the translated text.

TEXT:

{text}
"""

    try:

        response = MODEL.generate_content(prompt)

        return response.text

    except Exception:

        # Temporary fallback while Gemini quota is exhausted
        return f"""🌍 Translation Preview

Target Language: {language}

-------------------------------------

{text}

-------------------------------------

(Translation unavailable because the Gemini API quota has been reached.)
"""