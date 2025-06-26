# ??????????????????????????????????????????????????????????????????????????????????
# s1.py - Intial tests with smolagents based on the docs
# ??????????????????????????????????????????????????????????????????????????????????

# --- Imports ---

import os

from dotenv import load_dotenv
from rich.pretty import pprint as ppr
from smolagents import (
    CodeAgent,
    GradioUI,
    InferenceClientModel,
    LiteLLMModel,
    LiteLLMRouterModel,
)

from .utz import header1

# --- Global Vars ---
load_dotenv("src/.ass")
NB_T = os.getenv("NBY")
SA_T = os.getenv("SAO")
os.environ['SAMBANOVA_API_KEY'] = SA_T

env_list = [NB_T, SA_T]


# --- mainFunc ---


def s1_main():
    # hf1()
    # hf2()
    # hf3()
    # hf4()
    # hf5_llm_ro()
    hf5_llm_ro_3g()


# --- SubFunc ---

# BrintaEnv
def brint_env():
    header1("BrintaEnv")
    ppr(env_list, expand_all=True)


# HF Example 1

def hf1():
    header1("HF Main Example1")

    model = InferenceClientModel(

    )
    agent = CodeAgent(
        tools=[],
        model=model,
    )

    result = agent.run("What is BootyDance?")
    ppr(result)

# Execute smolgens with litellm


def hf2():
    header1("HF LiteLLM Example")

    modelz = [
        "sambanova/Meta-Llama-3.2-3B-Instruct"
    ]

    model = LiteLLMModel(
        modelid=modelz[0],
        api_base="https://api.sambanova.ai/v1",
        apikey=SA_T,
        temperature=0.6,
        max_tokens=1000,
    )

    agent = CodeAgent(
        model=model,
        tools=[],
        add_base_tools=True
    )

    agent.run("What is BootyDance? and BootyCandy?")


def hf3():
    header1("HF LiteLLm Direct Example")

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "nWhat is BootyDance? and BootyCandy?"
                }
            ]
        }
    ]

    model = LiteLLMModel(
        modelid="sambanova/Meta-Llama-3.2-3B-Instruct",
        api_base="https://api.sambanova.ai/v1",
        apikey=SA_T,
        temperature=0.6,
        max_tokens=1000
    )

    # agent = CodeAgent(
    #     model=model,
    #     tools=[],
    #     add_base_tools=True
    # )

    # agent.run(messages)
    ppr(model(messages))

# ////////////////////////////////////  Normal API Call Testing //////////////////////


def hf4():

    # Set your SambaNova credentials
    os.environ["SAMBA_NOVA_API_KEY"] = SA_T

    # Wrap SambaNova model with LiteLLMModel
    model = LiteLLMModel(
        model_id="sambanova/Meta-Llama-3.2-3B-Instruct",
        api_base="https://api.sambanova.ai/v1",
        api_key=os.getenv("SAMBA_NOVA_API_KEY"),
        temperature=0.7,
        max_tokens=512
    )

    # Create a code-based agent
    agent = CodeAgent(
        tools=[],  # optionally add tools here
        model=model,
        stream_outputs=False
    )

    # Run the agent
    result = agent.run(
        "Explain the difference between BootyDance and BootyCandy.")
    print(result)

# Using the Litellm Router - this method works now next we will try it with agent


def hf5_llm_ro():
    header1("HF LiteLLM Router")

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "nWhat is BootyDance? and BootyCandy?"
                }
            ]
        }
    ]

    model = LiteLLMRouterModel(
        model_id="Meta-Llama-3.2-3B-Instruct",
        model_list=[
            {
                "model_name": "Meta-Llama-3.2-3B-Instruct",
                "litellm_params": {
                    "model": "sambanova/Meta-Llama-3.2-3B-Instruct",
                    "api_key": SA_T
                }
            }
        ]
    )

    ppr(model(messages))

# Tetsing it with an agent now


def hf5_llm_ro_2():
    header1("HF LiteLLM Router")

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "nWhat is BootyDance? and BootyCandy?"
                }
            ]
        }
    ]

    model = LiteLLMRouterModel(
        model_id="Meta-Llama-3.2-3B-Instruct",
        model_list=[
            {
                "model_name": "Meta-Llama-3.2-3B-Instruct",
                "litellm_params": {
                    "model": "sambanova/Meta-Llama-3.2-3B-Instruct",
                    "api_key": SA_T
                }
            }
        ]
    )

    agent = CodeAgent(
        model=model,
        tools=[],
        add_base_tools=True
    )

    agent.run(messages)

# --- Now testing with the Gradio UI


def hf5_llm_ro_3g():
    header1("HF LiteLLM Router")

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "nWhat is BootyDance? and BootyCandy?"
                }
            ]
        }
    ]

    model = LiteLLMRouterModel(
        model_id="Meta-Llama-3.2-3B-Instruct",
        model_list=[
            {
                "model_name": "Meta-Llama-3.2-3B-Instruct",
                "litellm_params": {
                    "model": "sambanova/Meta-Llama-3.2-3B-Instruct",
                    "api_key": SA_T
                }
            }
        ]
    )

    agent = CodeAgent(
        model=model,
        tools=[],
        add_base_tools=True
    )

    GradioUI(agent).launch()
