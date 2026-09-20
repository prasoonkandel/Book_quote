from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pydantic.types import Json
from pydantic_core.core_schema import ErrorType

from services.quote_service import get_top_quotes

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
        if "error" in top_quotes:
            return top_quotes, 500
        return {"quotes": top_quotes}, 200
    except Exception as e:
        return {"error": str(e)}, 500
