from config.settings import MODEL


def generate_diagram(question, context=""):
    """
    Generate a Mermaid flowchart for the given concept.
    """

    prompt = f"""
You are an educational AI assistant.

Your task is to create a Mermaid flowchart that explains the topic.

Rules:
- Return ONLY Mermaid code.
- Do NOT explain anything.
- Do NOT use Markdown.
- Start directly with:

graph TD

Question:
{question}

Reference Notes:
{context}
"""

    try:

        response = MODEL.generate_content(prompt)

        return response.text.strip()

    except Exception:

        return "graph TD\nA[Unable to generate diagram]"