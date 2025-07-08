# ///////////////////////////////////
# 1st test of the module
# ///////////////////////////////////

# -- imports ---

from browser_use.llm import ChatOpenAI
from browser_use import Agent
import asyncio
import os

from dotenv import load_dotenv
from rich import print as rpr

from .utz import he1

# --- Vars ---
load_dotenv("src/.azz")
NOV_T = os.getenv("NOV")


# -- Main Function ----


def b1_main():
    brint()


# ---sub functions ---

#  Brintaz envz

def brint():
    he1("Brintaz envz")
    rpr(NOV_T)


# Exmaple Function 1
load_dotenv()


async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=ChatOpenAI(model="o4-mini", temperature=1.0),
    )
    await agent.run()

asyncio.run(main())
