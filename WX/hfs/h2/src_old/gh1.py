# /////////////////////////////////////////
# gh1.py - Testing out gh modelo
# /////////////////////////////////////////

# --- Imports Zone ---

import os

from dotenv import load_dotenv
from openai import OpenAI
from rich import inspect
from rich import print as rpr

from .utz import he1
from .wm import save_to_markdown

# --- Vars ---
load_dotenv("src/.azz")
GH_T = os.getenv("GHB")

# Models from github
modelz = [
    "openai/gpt-4.1",
]

# --- Main Function ---


def gh1_main():
    fn2()

# --- Sub Function ---

# Brintaz envaz


def fn1():
    he1("Function 1")
    rpr(f"[green] GHB: {GH_T} [/green]")

#
# Calling function from doco
# 1. Testing models that are compatible with open ai sdk


def fn2():

    quez = "What is the significant war happening in June 2025"
    endpoint = "https://models.github.ai/inference"
    client = OpenAI(
        base_url=endpoint,
        api_key=GH_T,
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": quez,
            }
        ],
        temperature=1.0,
        top_p=1.0,
        model=modelz[0]
    )

    answerz = response.choices[0].message.content
    inspect(answerz, methods=True)
    rpr(response.choices[0].message.content)

    save_to_markdown(
        answerz,
        prefix="openai_gpt-4.1",
        directory="rez/",
        header_level=2,
        include_time_in_filename=True,
        metadata={
            "Model": modelz[0],
            "Question": quez
        }
    )
