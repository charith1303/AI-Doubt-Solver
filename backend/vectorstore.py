import chromadb
import uuid

from backend.embeddings import get_embeddings

# ----------------------------------------
# Persistent Chroma Client
# ----------------------------------------

client = chromadb.PersistentClient(
    path="database/chroma_db"
)

collection = client.get_or_create_collection(
    name="astra_notes"
)


def clear_vector_database():
    """
    Clears all stored vectors.
    """

    global collection

    try:

        client.delete_collection("astra_notes")

    except Exception:
        pass

    collection = client.get_or_create_collection(
        name="astra_notes"
    )


def add_chunks(chunks):
    """
    Stores text chunks inside ChromaDB.
    """

    if not chunks:

        print("❌ No chunks received!")

        return

    embeddings = get_embeddings(chunks)

    ids = [

        str(uuid.uuid4())

        for _ in chunks

    ]

    collection.add(

        ids=ids,

        documents=chunks,

        embeddings=embeddings

    )

    print("✅ Chunks stored successfully!")


def search_chunks(query, top_k=3):
    """
    Searches similar chunks.
    Returns both documents and similarity distances.
    """

    query_embedding = get_embeddings([query])[0]

    results = collection.query(

        query_embeddings=[query_embedding],

        n_results=top_k,

        include=["documents", "distances"]

    )

    documents = []

    distances = []

    if "documents" in results and len(results["documents"]) > 0:

        documents = results["documents"][0]

    if "distances" in results and len(results["distances"]) > 0:

        distances = results["distances"][0]

    print("=" * 60)
    print("SEARCH QUERY:")
    print(query)
    print("=" * 60)

    print(results)

    return {

        "documents": documents,

        "distances": distances

    }