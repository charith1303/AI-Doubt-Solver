from config.settings import MODEL


def generate_related_topics(question, context=""):
    """
    Generate 5 related study topics for the given concept.
    """

    prompt = f"""
You are an educational AI assistant.

Given the topic below, suggest 5 closely related study topics.

Rules:
- Return ONLY the topic names.
- One topic per line.
- No numbering.
- No bullets.
- No explanation.
- Maximum 5 topics.

Topic:
{question}

Reference Notes:
{context}
"""

    try:

        response = MODEL.generate_content(prompt)

        topics = [
            line.strip()
            for line in response.text.split("\n")
            if line.strip()
        ]

        return topics

    except Exception:

        return []