import pandas as pd
from pinecone import Pinecone

import database.queries as db
from services.embedding import get_embeddings_list
from vector_db.connection import index, pc

MIN = db.get_min_id()[0]
MAX = db.get_max_id()[0]

BATCH_SIZE = 500

for i in range(MIN, MAX + 1, BATCH_SIZE):
    batch_end = min(i + BATCH_SIZE - 1, MAX)

    print(f"Processing batch {i}–{batch_end}")

    vectors = []
    quote_data = db.get_quote_data_by_range(i, batch_end)
    df = pd.DataFrame(quote_data)
    quotes_list = df["quote"].tolist()
    id_list = df["id"].tolist()
    embeddings = get_embeddings_list(quotes_list)
    for j in range(i, batch_end + 1):
        vectors.append(
            {
                "id": str(id_list[j - i]),
                "values": embeddings[j - i],
                "metadata": {"quote": quotes_list[j - i]},
            }
        )
    index.upsert(vectors=vectors)
    print(f"Upserted batch {i}-{batch_end}")

print("Done")
