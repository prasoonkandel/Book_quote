from pinecone import Pinecone

import database.queries as db
from services.embedding import get_embedding
from vector_db.connection import index, pc

MIN = db.get_min_id()[0]
MAX = db.get_max_id()[0]
BATCH_SIZE = 100

for i in range(MIN, MAX + 1, BATCH_SIZE):
    batch_end = min(i + BATCH_SIZE - 1, MAX)

    print(f"Processing batch {i}–{batch_end}")

    vectors = []

    for j in range(i, batch_end + 1):
        quote_data = db.get_quote_data(j)
        if quote_data:
            embedding = get_embedding(quote_data[1]).tolist()
            vectors.append(
                {
                    "id": str(quote_data[0]),
                    "values": embedding,
                    "metadata": {"quote": quote_data[1]},
                }
            )
    index.upsert(vectors=vectors)
    print(f"Upserted batch {i}")

print("Done")
