from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import (
    get_redoc_html, get_swagger_ui_html,
)
from fastapi.responses import RedirectResponse

from dictionary.britannica import (
    get_entries,
    get_total_entries,
    get_word_of_the_day,
    get_parts,
    get_definitions
)

app = FastAPI(
    title="Azeb's Dictionary API",
    description="API for accessing Britannica Dictionary data.",
    summary="Azeb's API: Explore the depths of the English language with comprehensive definitions, word of the "
            "day, and more.",
    contact={
        "name": "Esubalew Chekol",
        "url": "https://github.com/esubaalew",

    },

    version="1.0"
)

# Allow requests from all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/entries/{word}")
async def entries(word: str):
    """
    Retrieve entries for a given word from the Britannica Dictionary.

    Args:
        word (str): The word to retrieve entries for.

    Returns:
        dict: A dictionary containing entries for the given word.
    """
    entries = get_entries(word)
    return {"entries": entries}


@app.get("/total_entries/{word}")
async def total_entries(word: str):
    """
    Retrieve the total number of entries for a given word from the Britannica Dictionary.

    Args:
        word (str): The word to retrieve total entries for.

    Returns:
        dict: A dictionary containing the total number of entries for the given word.
    """
    total_entries = get_total_entries(word)
    return {"total_entries": total_entries}


@app.get("/word_of_the_day")
async def word_of_the_day():
    """
    Retrieve the word of the day from the Britannica Dictionary.

    Returns:
        dict: A dictionary containing the word of the day.
    """
    word_of_the_day = get_word_of_the_day()
    return {"word_of_the_day": word_of_the_day}


@app.get("/speeches/{word}")
async def parts(word: str):
    """
    Retrieve the parts of speech for a given word from the Britannica Dictionary.

    Args:
        word (str): The word to retrieve parts of speech for.

    Returns:
        dict: A dictionary containing the parts of speech for the given word.
    """
    parts = get_parts(word)
    return {"parts_of_speech": parts}


@app.get("/definitions/{word}")
async def  definitions(word: str):
    """
    Retrieve the definitions and examples for a given word from the Britannica Dictionary.

    Args:
        word (str): The word to retrieve definitions and examples for.

    Returns:
        dict: A dictionary containing the definitions and examples for the given word.
    """
    definitions = get_definitions(word)
    return {"definitions": definitions}


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url='/redoc')


@app.get("/redoc", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Azeb's Dictionary API    ")


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(openapi_url="/openapi.json", title="Azeb's Dictionary API")
