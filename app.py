from fastapi import FastAPI
from pydantic import BaseModel
from pydantic.types import Json

app = FastAPI()


class Quote(BaseModel):
    query: str
    count: int


# dummy
def search(query: str, count: int):
    return list(range(1, count + 1))


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/quote")
def read_quote(quote: Quote):
    quotes = search(quote.query, int(quote.count))
    return {"quotes": quotes}
