import numpy as np
import pandas as pd

import database.queries as db
from services.embedding import get_embedding
from services.vector import similarity_rank
from vector_db.search import search_top_k


def get_full_quote_data(quote_ids):
    quote_data_list = db.get_quote_data_list_by_ids(quote_ids)
    return pd.DataFrame(quote_data_list, columns=["id", "quote", "author"])


def merge_quote_data(a, b):
    df = a["quote", "author"].merge(b, on="id")
    return df


def get_top_quotes(query: str, k: int = 20):
    try:
        query_embedding = get_embedding(query)
        top_k = search_top_k(query_embedding, k)
        df = pd.DataFrame(top_k, columns=["id", "vector"])
        df = merge_quote_data(df, get_full_quote_data(df["id"]))
        df = similarity_rank(query_embedding, df)
        df = df[["quote", "author", "similarity"]]
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}
