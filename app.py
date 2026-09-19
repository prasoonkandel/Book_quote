from fastapi import FastAPI
from pydantic import BaseModel
from pydantic.types import Json

app = FastAPI()


class Quote(BaseModel):
    query: str
    count: int


@app.get("/")
def read_root():
    return {"message": "Welcome to Book Quote"}


@app.post("/get-quotes")
def get_quotes(quote: Quote):
    try:
        top_quotes = get_top_quotes(quote.query, quote.count)
        return {"quotes": top_quotes}, 200
    except Exception as e:
        return {"error": str(e)}, 500
