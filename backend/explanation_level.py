def get_level_prompt(level):
    """
    Returns the instruction for the selected explanation level.
    """

    level = level.lower()

    if level == "beginner":

        return """
Explain in very simple language.

Use short sentences.

Avoid technical jargon.

Use real-life examples.

Assume the student has no prior knowledge.
"""

    elif level == "intermediate":

        return """
Explain clearly using moderate technical terms.

Give examples where appropriate.

Suitable for undergraduate students.
"""

    elif level == "advanced":

        return """
Provide a detailed technical explanation.

Use proper terminology.

Include important concepts and technical details.

Suitable for engineering students.
"""

    else:

        return """
Explain clearly and concisely.
"""