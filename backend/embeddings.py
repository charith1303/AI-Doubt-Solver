from sentence_transformers import SentenceTransformer

_embedding_model = None


def get_model():
    """
    Load the embedding model only when needed.
    """

    global _embedding_model

    if _embedding_model is None:

        print("Loading embedding model...")

        _embedding_model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    return _embedding_model


def get_embedding(text):

    model = get_model()

    return model.encode(text).tolist()


def get_embeddings(texts):

    model = get_model()

    return model.encode(texts).tolist()