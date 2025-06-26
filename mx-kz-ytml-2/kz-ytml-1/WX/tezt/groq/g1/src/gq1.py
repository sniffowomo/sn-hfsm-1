# ////////////////////////////////////////////////////////////
# gq1.py - First version of panty smelling
# ////////////////////////////////////////////////////////////

# --- Imports ---

import os

from dotenv import load_dotenv
from groq import Groq
from rich import inspect as rich_inspect
from rich import print as rpr

from .outz import save_output_to_markdown
from .utz import header1

# --- Global Pussy ---

load_dotenv("src/.env")
gq_t = os.getenv("GQ")


# --- Main Function pantysmeling ---


def gq1_main():
    # env_test()
    gq1_chat1()


### Sub Funtions ###

def env_test():
    header1("Token_Brinting")
    rpr(f"[green_yellow]GQ1: {gq_t}[/green_yellow]")

### Chat Function1 ###


def gq1_chat1():
    header1("Chat1 - Testing examples from docs")

    client = Groq(
        api_key=os.environ.get("GQ"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Is wokeism a type of cancer ?",
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    printrez = chat_completion.choices[0].message.content
    save_output_to_markdown(printrez, directory="rez", label="chat_response")

    rich_inspect(chat_completion, methods=True, all=True)
