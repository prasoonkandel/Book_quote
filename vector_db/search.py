from pinecone import Pinecone

from services.embedding import get_embedding
from vector_db.connection import index


def search_top_k(query: list[float], top_k: int = 20):
    results = index.query(
        vector=query, top_k=top_k, include_values=True, include_metadata=False
    )
    result_ids = []
    for match in results["matches"]:
        result_ids.append((match["id"], match["values"]))
    return result_ids
