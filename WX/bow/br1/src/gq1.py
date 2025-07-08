# ////////////////////////////////////////////////////////////
# gq1.py - First version of panty smelling
# ////////////////////////////////////////////////////////////

# --- Imports ---

import os

from dotenv import load_dotenv
from groq import Groq
from rich import print as rpr

from .utz import he1
from .wm import save_to_markdown

# --- Global Pussy ---

load_dotenv("src/.azz")
gq_t = os.getenv("GRQ")

modelz = [
    "llama-3.3-70b-versatile",
    "compound-beta"
]


# --- Main Function pantysmeling ---


def gq1_main():
    env_test()
    gq1_chat1()


### Sub Funtions ###

def env_test():
    he1("Token_Brinting")
    rpr(f"[green_yellow]GQ1: {gq_t}[/green_yellow]")

### Chat Function1 ###


def gq1_chat1():
    he1("Chat1 - Testing examples from docs")

    quez = "Find AI based automated web app penetesting tools that are opnsource and utilize google gemini api "

    client = Groq(
        api_key=gq_t,
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": quez,
            }
        ],
        model=modelz[1],
    )

    rpr(chat_completion.choices[0].message.content)

    save_to_markdown(
        chat_completion.choices[0].message.content,
        prefix=modelz[0].replace("-", "_"),
        directory="rez/",
        header_level=2,
        include_time_in_filename=True,
        metadata={
            "Model": modelz[1],
            "Question": quez
        }
    )
