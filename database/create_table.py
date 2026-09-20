from sqlalchemy import text

from database.connection import engine

with engine.begin() as conn:
    conn.execute(
        text("""
            CREATE TABLE IF NOT EXISTS quotes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                quote TEXT NOT NULL,
                author TEXT,
                category TEXT
            );
        """)
    )
