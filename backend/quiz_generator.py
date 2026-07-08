from config.settings import MODEL
from backend.rag import retrieve_context


def generate_quiz(num_questions=5, difficulty="Easy"):
    """
    Generates an AI quiz from uploaded notes.
    """

    context = retrieve_context(
        "Generate quiz from uploaded notes",
        top_k=5
    )

    if not context.strip():

        return "No uploaded notes found."

    prompt = f"""
You are Astra, an AI Learning Assistant.

Using ONLY the notes below, create {num_questions} multiple-choice questions.

Difficulty: {difficulty}

Requirements:

- Four options (A, B, C, D)
- Mention the correct answer after each question
- Keep questions clear and student-friendly.

-----------------------
NOTES
-----------------------

{context}

-----------------------
QUIZ
-----------------------
"""

    try:

        response = MODEL.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"Error: {e}"