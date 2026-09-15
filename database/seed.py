import pandas as pd
from sqlalchemy import text

from database.connection import engine

df = pd.read_csv("data/quote.csv")
