# /////////////////////////////////////////
# Tavily testing here
# /////////////////////////////////////////

import datetime
import os
from datetime import datetime

from dotenv import load_dotenv
from rich import print as rprint
from tavily import TavilyClient

from .utz import header1

# Get the envs
load_dotenv()
T_V = os.getenv("TA")

# --- Main entry point of function ---


def main_tv():
    header1("Tavily Testing")
    tv_search_2()


# -- Testing functions below ---

def tv_search_1():

    header1("Tavily Testing 1 ")

    search_query = "What is cosmology"

    try:
        tavily_client = TavilyClient(api_key=T_V)
        response = tavily_client.search(search_query)
        rprint(response)
    except Exception as e:
        rprint(f"[bold red]Error:[/bold red] {e}")

# -- TV Search2 write to python file ---


def tv_search_2():
    header1("Tavily Testing 1")

    search_query = "What is cosmology"

    try:
        tavily_client = TavilyClient(api_key=T_V)
        response = tavily_client.search(search_query)
        rprint(response)

        # Save results to Markdown inside rez/
        if response and "results" in response:
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

            # Create rez directory if it doesn't exist
            os.makedirs("rez", exist_ok=True)
            filename = f"rez/tavily_results_{timestamp}.md"

            md = [
                "# Tavily Search Results",
                f"**Query**: {response['query']}",
                f"**Generated At**: {now.strftime('%Y-%m-%d %H:%M:%S')}",
                "\n---"
            ]

            for i, result in enumerate(response["results"], 1):
                md.append(f"\n### {i}. {result.get('title', 'No Title')}")
                md.append(
                    f"[{result.get('url', '')}]({result.get('url', '')})")
                md.append(result.get('content', 'No content available.'))
                md.append("---")

            with open(filename, "w", encoding="utf-8") as f:
                f.write("\n".join(md))

            rprint(f"[green]Results saved to:[/green] {filename}")

    except Exception as e:
        rprint(f"[bold red]Error:[/bold red] {e}")
