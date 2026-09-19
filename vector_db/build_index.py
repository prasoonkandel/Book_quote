from pinecone import Pinecone

import database.queries as db
from services.embedding import get_embeddings_list
from vector_db.connection import index, pc

MIN = db.get_min_id()[0]
MAX = db.get_max_id()[0]
BATCH_SIZE = 100

for i in range(MIN, MAX + 1, BATCH_SIZE):
    batch_end = min(i + BATCH_SIZE - 1, MAX)

    print(f"Processing batch {i}–{batch_end}")

    vectors = []
    quotes_list = db.get_quotes_list_by_range(i, batch_end)
    embeddings = get_embeddings_list(quotes_list)
    for j in range(i, batch_end + 1):
        vectors.append(
            {
                "id": str(j),
                "values": embeddings[j - i],
                "metadata": {"quote": quotes_list[j - i]},
            }
        )
    index.upsert(vectors=vectors)
    print(f"Upserted batch {i}-{batch_end}")

print("Done")
