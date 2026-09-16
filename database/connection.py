import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_USER = quote_plus(os.getenv("DB_USER") or "")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD") or "")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
