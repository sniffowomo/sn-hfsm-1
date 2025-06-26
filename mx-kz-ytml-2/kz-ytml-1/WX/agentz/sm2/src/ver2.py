# ================================================
# s1.py -= version 1 of the work - following tutorial - Using HuggingFace Inference API
# ================================================

import os

from dotenv import load_dotenv
from rich import inspect
from rich import print as rprint
from smolagents import CodeAgent, GradioUI, InferenceClientModel

from .utz import header1

# === Get Env ===
load_dotenv("src/.env")
hf_t = os.getenv("HF")
or_t = os.getenv("OR")


# === Main File Entry Funvtion===


def ver1_main():
    # smol_1()
    # smol1_gradio()
    env_print()

# === Sun functions ===

# --- test print function of the env ---


def env_print():
    header1("Env Print")
    rprint(hf_t, or_t)

# --- Example 1 run ---


"""
This is a bare test of the model 
"""


def smol_1():

    header1("Smol 1")

    model_id = "meta-llama/Llama-3.3-70B-Instruct"
    query = "Is wokeism a type of cancer ?"

    # You can choose to not pass any model_id to InferenceClientModel to use a default model
    model = InferenceClientModel(
        model_id=model_id, token=hf_t)

    # you can also specify a particular provider e.g. provider="together" or provider="sambanova"
    agent = CodeAgent(tools=[], model=model, add_base_tools=True)

    result = agent.run(query)
    inspect(result, methods=True, all=True)

# -- Get the above function in a gradio ui ---


def smol1_gradio():
    header1("Smol 1 in gradio")

    model_id = "meta-llama/Llama-3.3-70B-Instruct"

    # You can choose to not pass any model_id to InferenceClientModel to use a default model
    model = InferenceClientModel(
        model_id=model_id, token=hf_t)

    # you can also specify a particular provider e.g. provider="together" or provider="sambanova"
    agent = CodeAgent(tools=[], model=model, add_base_tools=True)
    GradioUI(agent).launch()
