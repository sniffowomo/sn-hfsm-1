# ///////////////////////////////////////////////////////////////
# App.py- This app is prepared fro uploading
# ///////////////////////////////////////////////////////////////

# --- Imports Zone ---

import time

import gradio as gr

from src.mkd import in_txt2, txt2

# --- Vars ---

# Theme choser
themes = [
    gr.themes.Ocean(),
    gr.themes.Monochrome(),
    gr.themes.Citrus(),
    gr.themes.Glass(),
    gr.themes.Default(),
    gr.themes.Soft()
]
c_th = themes[5]

czz = """ 
.gradio-container {background: url(https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTJ4b21tZ3hxdmQwYzVuejU1cnZ3dXZkc3hwYnJwdDhmcjlxbWY1MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7b8jdNUoFBdcoILjjv/giphy.gif); background-attachment: fixed; background-repeat: no-repeat; background-size: cover; background-position: center;} 
"""

# -- Sub Functions ---

# Chat Interface function


def ch_in():

    # Chat interface Function Call
    def slow_echo(message, history):
        for i in range(len(message)):
            time.sleep(0.05)
            yield "SmellPanty: " + message[:i + 1]

    # Chat Interface Description
    gr.Markdown(txt2)

    # Building chat interface
    gr.ChatInterface(
        slow_echo,
        type="messages",
        flagging_mode="manual",
        flagging_options=["Good", "Bad", "Shit"],
        save_history=True,
        examples=[
            ["Hi", "Hello"],
            ["How are you?", "Good"],
            ["What's your name?", "My name is SmellPanty"],
        ],
    )


# --- Main Function ---


def panty():
    with gr.Blocks(
        theme=c_th,
        css=czz
    ) as panty:

        with gr.Tab("Home"):
            gr.Markdown(in_txt2)

        with gr.Tab("ChatPanty"):
            ch_in()

    panty.launch(
        show_error=True
    )


if __name__ == "__main__":
    panty()
    print("BootySmells")
