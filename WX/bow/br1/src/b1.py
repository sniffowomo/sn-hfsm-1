# ///////////////////////////////////
# 1st test of the module
# ///////////////////////////////////

# -- imports ---

import asyncio
import os

from browser_use import Agent
from browser_use.llm import ChatOpenAI
from dotenv import load_dotenv
from playwright.async_api import async_playwright
from rich import print as rpr

from .utz import he1

# --- Vars ---
load_dotenv("src/.azz")
NOV_T = os.getenv("NOV")


# -- Main Function ----


def b1_main():
    # asyncio.run(b1())
    asyncio.run(test_browser())


# ---sub functions ---

#  Brintaz envz

def brint():
    he1("Brintaz envz")
    rpr(NOV_T)


# Exmaple Function 1
load_dotenv()


async def b1():
    he1("b1 agent")
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=ChatOpenAI(model="o4-mini", temperature=1.0),
    )
    await agent.run()


# /// Playqright Testing ///


async def test_browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto("https://www.femscat.com/")
        print(await page.title())

        # Wait 1 second (1000 milliseconds)
        await page.wait_for_timeout(1000)

        # Click the "Enter" button
        # Use a selector that matches your site's button.
        # For example, if it's <button>Enter</button>:
        await page.click("text=Enter")

        # Take a screenshot after clicking
        await page.screenshot(path="ss/example_after_click.png")
        rpr("Screenshot saved as example_after_click.png")

        await browser.close()
