from backend.vectorstore import search_chunks


def retrieve_context(question, top_k=3):
    """
    Retrieves context and determines whether the retrieved chunks
    are relevant enough to answer from uploaded notes.
    """

    result = search_chunks(question, top_k)

    documents = result["documents"]
    distances = result["distances"]

    if not documents:

        return {
            "context": "",
            "sources": [],
            "found_relevant": False
        }

    context = "\n\n".join(documents)

    # Lower distance = more similar.
    # Adjust this threshold later if needed.
    THRESHOLD = 0.6

    found_relevant = any(
        distance <= THRESHOLD
        for distance in distances
    )

    return {
        "context": context,
        "sources": documents,
        "found_relevant": found_relevant
    }