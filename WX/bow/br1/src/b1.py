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

WEBZ = "https://www.femscat.com/"


async def test_browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        # Use your existing folder — plain string works fine!
        context = await browser.new_context(
            record_video_dir="ss",
            record_video_size={"width": 1280, "height": 720}
        )

        page = await context.new_page()

        await page.goto(WEBZ)
        print(await page.title())

        await page.wait_for_timeout(1000)

        await page.click("a:has-text('ENTER')")
        print("Clicked the ENTER link!")

        await page.wait_for_timeout(1000)

        await page.screenshot(path="ss/fs.png")
        print("Screenshot saved as example_after_enter.png")

        await context.close()
        await browser.close()

        rpr("Video saved in your videos/ folder!")
