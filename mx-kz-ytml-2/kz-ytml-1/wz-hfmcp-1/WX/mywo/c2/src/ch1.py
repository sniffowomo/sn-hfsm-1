# //////////////////////////////////////////////////
# Testing of chatbot behavior in this
# //////////////////////////////////////////////////

import os

import gradio as gr
import sambanova_gradio as sg
from dotenv import load_dotenv

from .utz import header1

# -- Get tokens ---
load_dotenv("./src/.env")
hf_token = os.getenv("HF")
sn_token = os.getenv("SN")

# --- Main Function caller ---


def ch1_mf():
    # chatbot1_sambanova()
    c2_sn_tabs()


# -- Chatbt test 1

def chatbot1_sambanova():

    header1("Chatbot 1 - Llama-4-Maverick-17B-128E-Instruct")

    def main_chat_fn():
        gr.load("Llama-4-Maverick-17B-128E-Instruct",
                src=sg.registry,
                accept_token=True,
                multimodal=True,
                token=sn_token,
                ).launch()

# --- Chat Modal Test with tabs


def c2_sn_tabs():
    header1("Chatbot 1 - Llama-4-Maverick-17B-128E-Instruct")

    with gr.Blocks(title="Llama-4-Maverick Chatbot - Sambanova") as app:
        with gr.Tabs():
            # Description Tab
            with gr.Tab("Description"):
                gr.Markdown("""
                ## 🦙 Llama-4-Maverick-17B-128E-Instruct
                
                **Model Specifications:**
                - Parameters: 17 Billion
                - Context Length: 128K tokens
                - Architecture: Transformer-based
                - Capabilities: Text and Multimodal
                
                **Usage Guidelines:**
                1. Be specific with your prompts  
                2. For coding questions, specify the language  
                3. Use clear instructions for best results  
                
                **Example Prompts:**
                - "Explain quantum entanglement to a 5th grader"  
                - "Write a Python function to calculate Fibonacci sequence"  
                - "Compare CNN and RNN architectures"  
                """)

            # Chat Tab
            with gr.Tab("Chat"):
                gr.load(
                    "Llama-4-Maverick-17B-128E-Instruct",
                    src=sg.registry,
                    token=sn_token,
                    accept_token=True,
                    multimodal=True
                )

    app.launch()
