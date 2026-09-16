import pandas as pd
from sqlalchemy import text

from database.connection import engine

df = pd.read_csv("data/quotes.csv")

df = df[["quote", "author"]]

df = df.dropna(subset=["quote", "author"])

with engine.begin() as conn:
    conn.execute(
        text("""
            CREATE TABLE IF NOT EXISTS quotes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                quote TEXT NOT NULL,
                author TEXT
            );
        """)
    )

print("Table created successfully!")

df.to_sql(name="quotes", con=engine, if_exists="append", index=False, chunksize=5000)

print("Data seeded successfully!")
