import chromadb


def get_vectorstore(docs):
    """
    Expects `docs` as returned by load_policies:
      [{"id":..., "text":..., "source":...}, ...]
    Persists to `.chromadb/`, creates / reuses collection "hr-policies".
    """
    client = chromadb.PersistentClient(path=".chromadb")
    col = client.get_or_create_collection("hr-policies")

    # add each chunk
    col.add(
        ids=[d["id"] for d in docs],
        documents=[d["text"] for d in docs],
        metadatas=[{"source": d["source"]} for d in docs]
    )
    return col