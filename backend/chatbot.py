from config.settings import MODEL
from backend.rag import retrieve_context
from backend.explanation_level import get_level_prompt


def get_ai_response(user_question, level="Intermediate"):
    """
    Astra intelligently decides whether to use:
    1. Uploaded Notes (RAG)
    2. Gemini General Knowledge
    """

    try:

        rag_data = retrieve_context(user_question)

        context = rag_data["context"]
        sources = rag_data["sources"]
        found_relevant = rag_data["found_relevant"]

        level_instruction = get_level_prompt(level)

        # ======================================================
        # CASE 1 : Relevant Notes Found
        # ======================================================

        if found_relevant:

            prompt = f"""
You are Astra, an AI Study Assistant.

{level_instruction}

Answer ONLY using the uploaded notes below.

If the uploaded notes do not contain the answer,
say that clearly.

-----------------------
UPLOADED NOTES
-----------------------

{context}

-----------------------
QUESTION
-----------------------

{user_question}

-----------------------
ANSWER
-----------------------
"""

            response = MODEL.generate_content(prompt)

            return {
                "answer": response.text,
                "sources": sources
            }

        # ======================================================
        # CASE 2 : No Relevant Notes
        # ======================================================

        prompt = f"""
You are Astra, an AI Study Assistant.

{level_instruction}

The uploaded notes do NOT contain the answer.

Please answer using your own knowledge.

Begin your response with:

"I couldn't find this information in the uploaded notes.
Here's a general explanation:"

QUESTION

{user_question}
"""

        response = MODEL.generate_content(prompt)

        return {
            "answer": response.text,
            "sources": []
        }

    except Exception as e:

        error = str(e)

        if "429" in error:

            return {
                "answer": "⚠ Gemini API quota exceeded. Please try again later.",
                "sources": []
            }

        return {
            "answer": f"Error: {error}",
            "sources": []
        }