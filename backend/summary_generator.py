from config.settings import MODEL
from backend.rag import retrieve_context


def generate_summary(summary_type="Short"):
    """
    Generates a study summary from uploaded notes.
    """

    context = retrieve_context(
        "Summarize the uploaded notes",
        top_k=5
    )

    if not context.strip():
        return "❌ No uploaded notes found."

    prompt = f"""
You are Astra, an AI Learning Assistant.

Create a {summary_type} study summary using ONLY the uploaded notes.

Structure your response like this:

📌 Key Concepts

🧠 Important Definitions

⭐ Exam Tips

📖 Revision Notes

------------------------

NOTES

{context}

------------------------
"""

    try:

        response = MODEL.generate_content(prompt)

        return response.text

    except Exception as e:

        if "429" in str(e):

            return f"""
## ⚠ Gemini API quota reached

The uploaded notes were retrieved successfully.

### Retrieved Notes

{context}

Gemini is temporarily unavailable because the API quota has been exceeded.
"""

        return f"Error: {e}"