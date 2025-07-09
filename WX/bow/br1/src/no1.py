# //////////////////////////
# Novita AI Testing
# //////////////////////////

# --- Imports ---

import os

from dotenv import load_dotenv
from openai import OpenAI
from rich import print as rpr
from rich.console import Console
from rich.rule import Rule

from .utz import he1
from .wm import save_to_markdown

console = Console()

# --- Global Pussy ---

load_dotenv("src/.azz")
NOV_T = os.getenv("NOV")

modelz = [
    "baidu/ernie-4.5-vl-28b-a3b",
]


# --- Main Function pantysmeling ---


def n1_main():
    env_test()
    nov1()


### Sub Funtions ###

def env_test():
    he1("Token_Brinting")
    rpr(f"[green_yellow]GQ1: {NOV_T}[/green_yellow]")

### Chat Function1 ###


def nov1():

    he1("Novita AI Chat Example")

    base_url = "https://api.novita.ai/v3/openai"
    api_key = NOV_T
    model = modelz[0]
    quez = "What is buta ?"

    client = OpenAI(
        base_url=base_url,
        api_key=api_key,
    )

    stream = True  # or False
    max_tokens = 1000

    response_format = {"type": "text"}

    chat_completion_res = client.chat.completions.create(
        model=model,
        messages=[

            {
                "role": "user",
                "content": quez,
            }
        ],
        stream=stream,
        extra_body={
        }
    )

    if stream:
        console.print(Rule("[bold green]STARTSTREAM[/]", style="green"))

        for chunk in chat_completion_res:
            rpr(chunk.choices[0].delta.content or "", end=""),

        console.print(Rule("[red]ENDSTREAM[/]", style="red"))
    else:
        rpr(chat_completion_res.choices[0].message.content)

    save_to_markdown(
        chunk.choices[0].delta.content,
        prefix="baidu_ernie-4.5-vl-28b-a3b",
        directory="rez/",
        header_level=2,
        include_time_in_filename=True,
        metadata={
            "Model": modelz[0],
            "Question": quez
        })
