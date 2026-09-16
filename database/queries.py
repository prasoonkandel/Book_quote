from sqlalchemy import text

from database.connection import engine


def get_all_quotes():
    with engine.begin() as conn:
        result = conn.execute(text("SELECT * FROM quotes"))
        return result.fetchall()
