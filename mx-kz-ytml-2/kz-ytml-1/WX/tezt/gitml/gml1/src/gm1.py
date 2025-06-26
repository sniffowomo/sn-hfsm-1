# ????????????????????????????????????????????????????????????
# gm1 - GithubMl Test1
# ????????????????????????????????????????????????????????????

# --- Imports Zone ---
import os

from dotenv import load_dotenv
from openai import OpenAI
from rich.pretty import pprint as ppr

from .utz import header1
from .wm import save_to_markdown

# -- Globsl Vars

# --- Load the envpussy --
load_dotenv("src/.pussy")
GH_T = os.getenv("GHT")

# --- Models List ---
model_ids = [
    "openai/gpt-4.1",
    "openai/gpt-4.1-mini",
    "openai/gpt-4.1-nano",
    "openai/gpt-4o",
    "openai/gpt-4o-mini",
    "openai/o1",
    "openai/o1-mini",
    "openai/o1-preview",
    "openai/o3",
    "openai/o3-mini",
    "openai/o4-mini",
    "openai/text-embedding-3-large",
    "openai/text-embedding-3-small",
    "ai21-labs/ai21-jamba-1.5-large",
    "ai21-labs/ai21-jamba-1.5-mini",
    "cohere/cohere-command-a",
    "cohere/cohere-command-r",
    "cohere/cohere-command-r-08-2024",
    "cohere/cohere-command-r-plus",
    "cohere/cohere-command-r-plus-08-2024",
    "cohere/cohere-embed-v3-english",
    "cohere/cohere-embed-v3-multilingual",
    "core42/jais-30b-chat",
    "deepseek/deepseek-r1",
    "deepseek/deepseek-r1-0528",
    "deepseek/deepseek-v3-0324",
    "meta/llama-3.2-11b-vision-instruct",
    "meta/llama-3.2-90b-vision-instruct",
    "meta/llama-3.3-70b-instruct",
    "meta/llama-4-maverick-17b-128e-instruct-fp8",
    "meta/llama-4-scout-17b-16e-instruct",
    "meta/meta-llama-3.1-405b-instruct",
    "meta/meta-llama-3.1-70b-instruct",
    "meta/meta-llama-3.1-8b-instruct",
    "meta/meta-llama-3-70b-instruct",
    "meta/meta-llama-3-8b-instruct",
    "mistral-ai/codestral-2501",
    "mistral-ai/ministral-3b",
    "mistral-ai/mistral-large-2411",
    "mistral-ai/mistral-medium-2505",
    "mistral-ai/mistral-nemo",
    "mistral-ai/mistral-small-2503",
    "xai/grok-3",
    "xai/grok-3-mini",
    "microsoft/mai-ds-r1",
    "microsoft/phi-3.5-mini-instruct",
    "microsoft/phi-3.5-moe-instruct",
    "microsoft/phi-3.5-vision-instruct",
    "microsoft/phi-3-medium-128k-instruct",
    "microsoft/phi-3-medium-4k-instruct",
    "microsoft/phi-3-mini-128k-instruct",
    "microsoft/phi-3-mini-4k-instruct",
    "microsoft/phi-3-small-128k-instruct",
    "microsoft/phi-3-small-8k-instruct",
    "microsoft/phi-4",
    "microsoft/phi-4-mini-instruct",
    "microsoft/phi-4-mini-reasoning",
    "microsoft/phi-4-multimodal-instruct",
    "microsoft/phi-4-reasoning"
]


# -- Main Function Call --


def gm1_main():
    # print_env()  # Testing env access
    gm1_1()  # Run the official example test

# --- SubFunc---

# Test ENV Access


def print_env():
    header1("Brint ENV")
    ppr(f"GiGaand = {GH_T}")

# Official Example Test


def gm1_1():

    header1("Official Example Test")

    endpoint = "https://models.github.ai/inference"
    model = model_ids[58]

    client = OpenAI(
        base_url=endpoint,
        api_key=GH_T,
    )

    question = "What is smellpanty algoritm ?"

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant, who talks like in rhyming slang",
            },
            {
                "role": "user",
                "content": question,
            }
        ],
        temperature=1.0,
        top_p=1.0,
        model=model
    )

    # Print Console Output
    ppr(response.choices[0].message.content)

    # Save to Markdown
    save_to_markdown(
        response.choices[0].message.content,
        prefix="microsoft_phi-4-reasoning",
        directory="rez/",
        header_level=2,
        include_time_in_filename=True,
        metadata={
            "Model": model,
            "Endpoint": endpoint,
            "Question": question
        }
    )
