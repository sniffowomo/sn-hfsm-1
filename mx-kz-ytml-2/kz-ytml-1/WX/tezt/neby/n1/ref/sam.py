# ??????????????????????????????????????????????
# sam.py - Samova Chatbot test following the docs
# ??????????????????????????????????????????????

# --- Imports ---
import os

import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI
from rich import print

from src.utz import header1

# --- Global Vars ---
load_dotenv("src/.ass")
SA_T = os.getenv("SAO")

themes = [
    gr.themes.Ocean(),
    gr.themes.Monochrome(),
    gr.themes.Citrus(),
    gr.themes.Glass(),
    gr.themes.Default(),
    gr.themes.Soft()
]
c_th = themes[5]

# Styling Css
czz = """ 
.gradio-container {background: url(https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTJ4b21tZ3hxdmQwYzVuejU1cnZ3dXZkc3hwYnJwdDhmcjlxbWY1MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7b8jdNUoFBdcoILjjv/giphy.gif); background-attachment: fixed; background-repeat: no-repeat; background-size: cover; background-position: center;} 
"""

# --- Main Function ---


def sam_main():
    # ass_print()
    # sam_chat1()
    sam_chat2()

# --- Sub Functions ---

# Print Ass


def ass_print():
    header1("Ass Stuff")
    print(SA_T)

# Actual Chat Test from example


def sam_chat1():
    header1("Sam Chat Test 1")

    client = OpenAI(
        base_url="https://api.sambanova.ai/v1",
        api_key=SA_T
    )

    def predict(message, history):
        history.append({"role": "user", "content": message})
        stream = client.chat.completions.create(
            model="Meta-Llama-3.2-1B-Instruct",
            messages=history,
            stream=True
        )
        chunks = []
        for chunk in stream:
            chunks.append(chunk.choices[0].delta.content or "")
            yield "".join(chunks)

    panty = gr.ChatInterface(
        predict,
        title="Samova Chatbot",
        description="Chat with Samova",
        type="messages",
        flagging_mode="manual",
    )

    panty.launch(
        show_error=True
    )


# Same chat as above but now with using blocks

def sam_chat2():
    header1("Samchat 2 - Blocks Layout")

    intro_txt = """
# Samnova Chat with 
1. Tabbed interface 
2. UI Styling 
3. BG Fixes
"""

    def intr_tab():
        gr.Markdown(intro_txt)

    def chat_func():
        client = OpenAI(
            base_url="https://api.sambanova.ai/v1",
            api_key=SA_T
        )

        def predict(message, history):
            history.append({"role": "user", "content": message})
            stream = client.chat.completions.create(
                model="Meta-Llama-3.2-1B-Instruct",
                messages=history,
                stream=True
            )
            chunks = []
            for chunk in stream:
                chunks.append(chunk.choices[0].delta.content or "")
                yield "".join(chunks)

        panty = gr.ChatInterface(
            predict,
            title="Samova Chatbot",
            chatbot=gr.Chatbot(height=700),
            textbox=gr.Textbox(
                placeholder="Bastard write something useful here !!! 🦧🦧🦧"),
            examples=[
                "Describe booty dancing",
                "Write rust script for testing API",
                "What is idiomatic panty"
            ],
            description="Chat with Samova",
            type="messages",
            flagging_mode="manual",
        )

    with gr.Blocks(
        theme=c_th,
        fill_height=True
    ) as pty:

        with gr.Tab("Intro Tab"):
            intr_tab()

        with gr.Tab("Chat"):
            chat_func()

    pty.launch(
        show_error=True
    )
