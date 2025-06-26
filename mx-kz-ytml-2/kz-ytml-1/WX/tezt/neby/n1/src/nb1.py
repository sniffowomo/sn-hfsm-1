# ?????????????????????????????????????????
# nb1.py - neby Test 1
# ?????????????????????????????????????????

# --- Imports Zone ---

import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from openai import OpenAI
from rich import print as rpr
from rich.pretty import pprint as ppr

from .utz import header1
from .wm import save_to_markdown

# --- Global Vars ---
load_dotenv("src/.ass")
NB_T = os.getenv("NBY")

modelz = [
    "meta-llama/Meta-Llama-3.1-8B-Instruct",
    "Qwen/Qwen2.5-Coder-7B"
]

# --- Main Function ---


def nb1_main():
    # brint_env()
    # nb_test1()
    nb_hf_1()


# --- Sub functions ---

# Printaz Envuiaza
def brint_env():
    header1("Ass Stuff")
    rpr(NB_T)

# API Tezta


def nb_test1():
    header1("NB1 Tezt")

    endpoint = "https://api.studio.nebius.com/v1"
    question = "Describe booty dancing"

    client = OpenAI(
        base_url=endpoint,
        api_key=NB_T
    )

    completion = client.chat.completions.create(
        model=modelz[1],
        messages=[
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0.5
    )

    ppr(completion.choices[0].message.content, expand_all=True)

    save_to_markdown(
        completion.choices[0].message.content,
        prefix="Qwen_Qwen2.5-Coder-7B",
        directory="rez/",
        header_level=2,
        include_time_in_filename=True,
        metadata={
            "Model": modelz[1],
            "Endpoint": endpoint,
            "Question": question
        }
    )


# Tsting with huggingface client
"""
Teting out the neby api with HF client. Since many models of HF , use the nb as inferencepanty
"""


def nb_hf_1():
    header1("Neby HF_1")

    use_model = modelz[0]
    quez = "Describe booty dancing"

    client = InferenceClient(
        provider="nebius",
        api_key=NB_T
    )

    messages = [
        {
            "role": "system",
            "content": "You talk like a drunk miedval knight"
        },
        {
            "role": "user",
            "content": quez
        }
    ]

    comp = client.chat.completions.create(
        model=use_model,
        messages=messages,
        max_tokens=1000
    )

    ppr(comp.choices[0].message.content, expand_all=True)

    save_to_markdown(
        comp.choices[0].message.content,
        prefix="HF_LAMA",
        directory="rez/",
        header_level=2,
        include_time_in_filename=True,
        metadata={
            "Model": modelz[1],
            "Endpoint": "huggingface_hub_inferenceClient",
            "Question": quez
        }
    )
