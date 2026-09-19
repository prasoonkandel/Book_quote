from sqlalchemy import text

from database.connection import engine


def get_all_quotes():
    with engine.begin() as conn:
        result = conn.execute(text("SELECT quote FROM quotes"))
        return result.fetchall()


def get_all_quotes_data():
    with engine.begin() as conn:
        result = conn.execute(text("SELECT * FROM quotes"))
        return result.fetchall()


def get_quote_data(quote_id):
    with engine.begin() as conn:
        result = conn.execute(text(f"SELECT * FROM quotes WHERE id = {quote_id}"))
        return result.fetchone()
