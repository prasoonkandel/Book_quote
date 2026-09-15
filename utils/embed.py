import os
from errno import EMEDIUMTYPE

import fastembed
import numpy as np
import pandas as pd

model = fastembed.TextEmbedding()
df = pd.read_csv("utils/quote.csv")

os.system("clear")

df["embedding"] = list(model.embed(df["Quote"]))


if __name__ == "__main__":
    query = input("Search for a quote: ")
    query_embedding = list(model.embed(query))[0]
    similarities = []
    for id, quote, author, book, embedding in zip(
        df["id"], df["Quote"], df["Author"], df["Book"], df["embedding"]
    ):
        similarity = (
            np.dot(embedding, query_embedding)
            / np.linalg.norm(embedding)
            * np.linalg.norm(query_embedding)
        )
        if similarity > 0.6:
            similarities.append((similarity, id, quote, author, book))

    similarities.sort(reverse=True)
    similarities = similarities[:5]
    for similarity, id, quote, author, book in similarities:
        print(f"{quote} \n- {author} ({book})\n (similarity: {similarity})\n")
