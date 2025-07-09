# ///////////////////////////////////
# 1st test of the module
# ///////////////////////////////////

# -- imports ---

import asyncio
import os

from browser_use import Agent, BrowserSession
from browser_use.llm import ChatOpenRouter
from dotenv import load_dotenv
from playwright.async_api import async_playwright
from rich import print as rpr

from .utz import he1

# --- Vars ---
load_dotenv("src/.azz")
# NOV_T = os.getenv("NOV")
# GRQ_T = os.getenv("GRQ")
OPR_T = os.getenv("OPR")

# -- Main Function ----


def b1_main():
    asyncio.run(b1())
    # asyncio.run(test_browser())


# ---sub functions ---

#  Brintaz envz

def brint():
    he1("Brintaz envz")
    rpr(OPR_T)


# Exmaple Function 1
load_dotenv()


async def b1():
    he1("b1 agent")

    browser_session = BrowserSession(
        headless=True,  # Required for video recording
        viewport={"width": 1280, "height": 720},
    )

    llm = ChatOpenRouter(
        model="deepseek/deepseek-r1-0528-qwen3-8b:free",
        api_key=OPR_T,  # Replace with your key
        temperature=0.7,
    )

    # Define the task
    agent = Agent(
        task=(
            "1. Go to google.com\n"
            "2. Search for 'price comparison of GPT-4o and DeepSeek-V3'\n"
            "3. Extract the top 3 results and summarize prices\n"
            "4. Take screenshots of the results\n"
            "5. (Video will auto-record due to BrowserSession config)"
        ),
        llm=llm,
        browser_session=browser_session,
        generate_gifs=True,  # Enable GIF generation
        use_vision=False

    )

    # Run the agent
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
