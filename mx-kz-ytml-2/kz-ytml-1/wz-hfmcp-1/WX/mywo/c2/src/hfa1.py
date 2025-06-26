# //////////////////////////////////////////////////
# Testing the HF API fromt he official docs
# https://huggingface.co/docs/inference-providers/providers/hf-inference
# //////////////////////////////////////////////////

import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from rich import print as rprint  # For rprinting

from src.utz import header1

# Extract the HF token from the .env file
load_dotenv("./src/.env")
hf_token = os.getenv("HF")
sn_token = os.getenv("SN")

# --- Main Entrpoint of the function ---


def hfa1_main():
    hf1()

# --- Testing out Inference API ---


def hf1():
    header1("Hugging Face Inference API Example")

    client = InferenceClient(
        provider="hf-inference",
        api_key=hf_token,
    )

    completion = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=[
            {"role": "user", "content": "Sing and dance for me "}
        ],
    )
    rprint(f"Response from {completion.model} model:")
    rprint(completion.choices[0].message.content)
