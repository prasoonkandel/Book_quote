from sqlalchemy import text

from database.connection import engine


def get_all_quotes():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT quote FROM quotes"))
        return result.fetchall()


def get_all_quotes_data():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM quotes"))
        return result.fetchall()


def get_quote_data(quote_id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM quotes WHERE id = :quote_id"), {"quote_id": quote_id}
        )
        return result.fetchone()


def get_max_id():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT MAX(id) FROM quotes"))
        return result.fetchone()


def get_min_id():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT MIN(id) FROM quotes"))
        return result.fetchone()
