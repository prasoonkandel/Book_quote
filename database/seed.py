import pandas as pd
from sqlalchemy import text

from database.connection import engine

df = pd.read_csv("data/quotes.csv")

df = df[["quote", "author"]]

df = df.dropna(subset=["quote", "author"])

df.to_sql(name="quotes", con=engine, if_exists="append", index=False, chunksize=5000)
