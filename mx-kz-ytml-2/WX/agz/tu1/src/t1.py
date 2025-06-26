# ?????????????????????????????????????????????????????????????????
# ty1- Tutorial 1 of smolagens
# ?????????????????????????????????????????????????????????????????

# --- Impors ---

import os

from dotenv import load_dotenv
from rich import print as rpr
from smolagents import (
    CodeAgent,
    DuckDuckGoSearchTool,
    GradioUI,
    HfApiModel,
    tool,
)

from .utz import header1

# --- Vars ---

load_dotenv("src/.azz")
GQ_T = os.getenv("GRQ")
HF_T = os.getenv("HF1")


# --- Main Function ---
def t1_main():
    # brint_env()
    # func1()
    func2()

# --- Sub Function---

# /// Brint env ///


def brint_env():
    header1("env brint")
    rpr(f"[green] GQ1: {GQ_T} [/green]")

# /// Fn1 ///


def func1():
    header1("F1 - Testing examples from docs")

    model = HfApiModel(
        model="meta-llama/Llama-3.1-8B-Instruct",
        provider="hf-inference",
        token=HF_T,
    )

    agent = CodeAgent(
        tools=[DuckDuckGoSearchTool()],
        model=model,
        add_base_tools=True,
    )

    agent.run("Compare and Contrast Booty Dancing and Booty Candy")

# /// Fn2 - Following the tutorial ///


def func2():

    header1("F2 - Following the tutorial")

    # Custom tool
    @tool
    def get_weather_date(city: str) -> dict:
        """
    Retrieves weather information for a given city and date.

    Args:
        city (str): The name of the city to get the weather for.

    Returns:
        dict: Weather data for the specified city and date.
    """

        # Sample Data
        sample_data = {
            "new york": {
                "temps": [20, 22, 21, 20, 19, 12, 15],
                "rain": [0, 0, 1, 0, 0, 1, 0],
                "humidity": [50, 55, 60, 65, 70, 75, 80],
                "unit": "Fahrenheit",
            },
            "london": {
                "temps": [15, 16, 14, 13, 12, 11, 10],
                "rain": [1, 0, 1, 0, 0, 1, 0],
                "humidity": [80, 85, 90, 95, 100, 105, 110],
                "unit": "Celsius",
            },
            "paris": {
                "temps": [18, 19, 20, 21, 22, 23, 24],
                "rain": [0, 0, 0, 1, 0, 0, 0],
                "humidity": [60, 65, 70, 75, 80, 85, 90],
                "unit": "Celsius",
            },
            "tokyo": {
                "temps": [25, 26, 27, 28, 29, 30, 31],
                "rain": [0, 0, 0, 0, 1, 0, 0],
                "humidity": [50, 55, 60, 65, 70, 75, 80],
                "unit": "Celsius",
            },
        }

        city_lower = city.lower()
        return sample_data.get(city_lower, {"error": f"No data for {city}"})

    model = HfApiModel(
        model="meta-llama/Llama-3.1-8B-Instruct",
        provider="hf-inference",
        token=HF_T,
    )

    agent = CodeAgent(
        tools=[get_weather_date],
        model=model,
        add_base_tools=True,
        additional_authorized_imports=['matplotlib'], verbosity_level=2,
    )

    # Printing the response
    rpr("Running Weather Analysis Agent...")
    # response = agent.run(
    #     """
    #     Get the weather data for New York, London, Paris, and Tokyo.
    #     1. Calculate the average temperature for each city.
    #     2. Determine which city has the highest humidity.
    #     3. Plot the temperature data for each city.
    #     4. Discuss the impact of weather on daily life in these cities.
    #     """
    # )

    GradioUI(agent).launch
