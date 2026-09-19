from sqlalchemy import text

from database.connection import engine


def get_all_quotes_list():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT quote FROM quotes"))
        return result.fetchall()


def get_all_quote_data():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM quotes"))
        return result.fetchall()


def get_quote_data_by_id(quote_id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM quotes WHERE id = :quote_id"), {"quote_id": quote_id}
        )
        return result.fetchone()


def get_quote_data_by_range(start_id, end_id):
    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT * FROM quotes
                WHERE id BETWEEN :start_id AND :end_id
            """),
            {"start_id": start_id, "end_id": end_id},
        )
        return result.fetchall()


def get_quotes_list_by_range(start_id, end_id):
    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT quote FROM quotes
                WHERE id BETWEEN :start_id AND :end_id
            """),
            {"start_id": start_id, "end_id": end_id},
        )
        quotes = []
        for row in result:
            quotes.append(row[0])
    return quotes


def get_max_id():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT MAX(id) FROM quotes"))
        return result.fetchone()


def get_min_id():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT MIN(id) FROM quotes"))
        return result.fetchone()
