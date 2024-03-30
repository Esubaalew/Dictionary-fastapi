from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dictionary.britannica import (
    get_entries,
    get_total_entries,
    get_word_of_the_day,
    get_parts,
    get_definitions
)

app = FastAPI()

# Allow requests from all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/britannica/entries/{word}")
async def britannica_entries(word: str):
    entries = get_entries(word)
    return {"entries": entries}


@app.get("/britannica/total_entries/{word}")
async def britannica_total_entries(word: str):
    total_entries = get_total_entries(word)
    return {"total_entries": total_entries}


@app.get("/britannica/word_of_the_day")
async def britannica_word_of_the_day():
    word_of_the_day = get_word_of_the_day()
    return {"word_of_the_day": word_of_the_day}


@app.get("/britannica/speeches/{word}")
async def britannica_parts(word: str):
    parts = get_parts(word)
    return {"parts_of_speech": parts}


@app.get("/britannica/definitions/{word}")
async def britannica_definitions(word: str):
    definitions = get_definitions(word)
    return {"definitions": definitions}


@app.get("/")
async def root():
    return {"message": "Hello World"}
