# ?????????????????????????????????????????????????????????????????
# ty1- Tutorial 1 of smolagens
# ?????????????????????????????????????????????????????????????????

# --- Impors ---

import os

from dotenv import load_dotenv
from rich import print as rpr
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel, LiteLLMModel

from .utz import header1

# --- Vars ---

load_dotenv("src/.azz")
GQ_T = os.getenv("GRQ")
HF_T = os.getenv("HF1")


# --- Main Function ---
def t1_tez_main():
    # brint_env()
    func2()

# --- Sub Function---

# /// Brint env ///


def brint_env():
    header1("env brint")
    rpr(f"[green] GQ1: {GQ_T} [/green]")


# /// Fn1 ///
"""
This function will use hfapi , note that the token has to be explicity added as shown. Otehrwise is will search for .env in the root directory. For a token called - "hf_token"
"""


def func1():
    header1("F1 - Testing examples from docs")

    model = HfApiModel(
        token=HF_T,
    )

    agent = CodeAgent(
        tools=[DuckDuckGoSearchTool()],
        model=model,
        add_base_tools=True,
    )

    agent.run("Compare and Contrast Booty Dancing and Booty Candy")


# /// Fn2 ///
"""
This seems to be working but there is problem with the number of req/min,  smole agents sends out many requests, plus ur using uv which makes the number of requests being sent out even more per minute.
"""


def func2():
    header1("F2 - Testing agent run with Groq via litellm")

    model = LiteLLMModel(
        model_id="groq/llama-3.1-8b-instant",
        temperature=0.1,
        api_key=GQ_T,
    )

    agent = CodeAgent(
        tools=[DuckDuckGoSearchTool()],
        model=model,
        add_base_tools=True,
    )
    agent.run("Compare and Contrast Booty Dancing and Booty Candy")
