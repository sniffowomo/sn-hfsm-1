# ?????????????????????????????????????????
# nbg1.py - Running Neby wih gradio
# ?????????????????????????????????????????

# --- Imports Zone ---

import os

import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI
from rich import print as rpr

from .utz import header1

# --- Global Vars ---
load_dotenv("src/.ass")
NB_T = os.getenv("NBY")

modelz = [
    "meta-llama/Meta-Llama-3.1-8B-Instruct",
    "Qwen/Qwen2.5-Coder-7B"
]

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


def nbg1_main():
    # brint_env()
    # nb_test1()
    nb_hfgra_1()


# --- Sub functions ---

# Printaz Envuiaza
def brint_env():
    header1("Ass Stuff")
    rpr(NB_T)

# Gradio Test 1 - Taken from


def nb_hfgra_1():
    header1("Nebiioza Chat - Blocks Layout")

    intro_txt = """
# NebiuChatz with the gradioza
1. Tabbed interface 
2. Testing the gradio chat interfacez without dropdown
"""

    def intr_tab():
        gr.Markdown(intro_txt)

    def chat_func():
        client = OpenAI(
            base_url="https://api.studio.nebius.com/v1",
            api_key=NB_T
        )

        def predict(message, history):
            history.append({"role": "user", "content": message})
            stream = client.chat.completions.create(
                model=modelz[0],
                messages=history,
                stream=True
            )
            chunks = []
            for chunk in stream:
                chunks.append(chunk.choices[0].delta.content or "")
                yield "".join(chunks)

        panty = gr.ChatInterface(
            predict,
            title="Nebioza Chatbot",
            chatbot=gr.Chatbot(height=600),
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
