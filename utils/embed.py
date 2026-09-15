import os

import dotenv
import numpy as np
import pandas as pd
import requests

# Load environment variables
dotenv.load_dotenv(dotenv.find_dotenv())
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = os.getenv("OPENROUTER_API_URL")


if not OPENROUTER_API_KEY:
    raise ValueError("Missing OPENROUTER_API_KEY in your .env file!")

headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
}


def get_embedding(text):
    data = {
        "model": "qwen/qwen3-embedding-4b",
        "input": text,
    }

    response = requests.post(
        OPENROUTER_API_URL,
        headers=headers,
        json=data,
    )

    response.raise_for_status()

    return response.json()["data"][0]["embedding"]


df = pd.read_csv("utils/quote.csv")

df["embedding"] = df["Quote"].apply(get_embedding)

df.to_csv("utils/quote.csv", index=False)
