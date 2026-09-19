from pinecone import Pinecone

from services.embedding import get_embedding
from vector_db.connection import index


def search_top_k(query: list, top_k: int = 20):
    results = index.query(
        vector=query,
        top_k=top_k,
        include_metadata=True,
    )
    result_ids = []
    for match in results["matches"]:
        result_ids.append(match["id"])
    return result_ids
