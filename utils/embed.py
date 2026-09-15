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

url = OPENROUTER_API_URL
headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
}
data = {
    "model": "qwen/qwen3-embedding-4b",
    "input": "The quick brown fox jumps over the lazy dog",
}
response = requests.post(url, headers=headers, json=data)

response.raise_for_status()

response_json = response.json()

embedding = response_json["data"][0]["embedding"]
print(embedding)

# Read your CSV file
df = pd.read_csv("utils/quote.csv")
