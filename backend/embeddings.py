from sentence_transformers import SentenceTransformer

# ----------------------------------------
# Global Embedding Model
# ----------------------------------------

_embedding_model = None


def get_embedding_model():
    """
    Loads the embedding model only when required.
    The model is cached after the first load.
    """

    global _embedding_model

    if _embedding_model is None:

        print("Loading embedding model...")

        _embedding_model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        print("Embedding model loaded.")

    return _embedding_model


def get_embedding(text):
    """
    Converts a single text into an embedding.
    """

    model = get_embedding_model()

    return model.encode(text).tolist()


def get_embeddings(text_chunks):
    """
    Converts multiple text chunks into embeddings.
    """

    model = get_embedding_model()

    return model.encode(text_chunks).tolist()