# ///////////////////////////////////
# Testing Gradio chat interface with apis from their manual
# ///////////////////////////////////

# --- imports ---

import os

import gradio as gr
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

from .utz import header1

# --- Getting th api keys ---
load_dotenv("./src/.env")
hf_token = os.getenv("HF")

# --- Main Entry Function


def gra2_main():
    gra2_chat1()

# //// Sun Functions /////


modelz = [
    "meta-llama/Llama-3.1-8B-Instruct",
    "mistralai/Mistral-7B-Instruct-v0.3"
]

# This code work with the minimal examples for calling the cat interface


def gra2_chat1():
    header1("Testing HF API and Models")

    client = InferenceClient(
        provider="hf-inference",
        api_key=hf_token,
    )

    def predict(message, history):
        history.append({"role": "user", "content": message})

        stream = client.chat.completions.create(
            messages=history, model=modelz[0], stream=True)
        chunks = []

        for chunk in stream:
            chunks.append(chunk.choices[0].delta.content or "")
            yield "".join(chunks)

    demo = gr.ChatInterface(predict, type="messages", save_history=True,
                            title="Chat with " + modelz[0])

    demo.launch()
