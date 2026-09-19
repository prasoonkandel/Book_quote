import numpy as np
import pandas as pd


def normalize_vector(vector):
    return vector / np.linalg.norm(vector)


def cosine_similarity(A, B):
    return np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))
