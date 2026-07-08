from config.settings import MODEL
from backend.rag import retrieve_context


def generate_flashcards():
    """
    Generates flashcards from uploaded notes.
    """

    context = retrieve_context(
        "Generate flashcards from uploaded notes",
        top_k=5
    )

    if not context.strip():
        return []

    prompt = f"""
You are Astra.

Using ONLY the uploaded notes, generate 10 flashcards.

Return ONLY in this format:

Q: Question
A: Answer

Q: Question
A: Answer

NOTES:

{context}
"""

    try:

        response = MODEL.generate_content(prompt)

        text = response.text

    except Exception:

        # Temporary sample data while Gemini quota is exhausted
        return [
            {
                "front": "What is Artificial Intelligence?",
                "back": "Artificial Intelligence is the simulation of human intelligence by machines."
            },
            {
                "front": "What is Machine Learning?",
                "back": "Machine Learning enables computers to learn from data."
            },
            {
                "front": "What is Deep Learning?",
                "back": "Deep Learning is a subset of Machine Learning using neural networks."
            }
        ]

    flashcards = []

    lines = text.split("\n")

    question = ""

    for line in lines:

        if line.startswith("Q:"):
            question = line.replace("Q:", "").strip()

        elif line.startswith("A:"):

            answer = line.replace("A:", "").strip()

            flashcards.append(
                {
                    "front": question,
                    "back": answer
                }
            )

    return flashcards