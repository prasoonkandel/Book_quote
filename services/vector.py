import numpy as np
import pandas as pd


def normalize_vector(vector):
    return vector / np.linalg.norm(vector)


def cosine_similarity(A, B):
    return np.dot(A, B)


def similarity_rank(query: np.ndarray, results: pd.DataFrame):
    def similarity_with_query(x):
        return cosine_similarity(query, x)

    results["similarity"] = results["vector"].apply(similarity_with_query)

    return results.sort_values("similarity", ascending=False)
