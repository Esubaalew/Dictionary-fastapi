from fastapi import FastAPI, Query

from dictionary.britannica import (
    get_entries,
    get_total_entries,
    get_word_of_the_day,
    get_parts,
    get_definitions
)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/britannica/entries/{word}")
async def britannica_entries(word: str):
    entries = get_entries(word)
    return {"entries": entries}


@app.get("/britannica/total_entries/{word}")
async def britannica_total_entries(word: str):
    total_entries = get_total_entries(word)
    return {"total_entries": total_entries}
