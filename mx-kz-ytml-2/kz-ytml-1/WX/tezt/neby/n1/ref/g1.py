# ???????????????????????????????????????????????????????????????????
# g1.py - Gradio test 1
# ???????????????????????????????????????????????????????????????????

# --- Imports ---

import time

import gradio as gr

from .mkd import in_txt, in_txt2, txt2
from .utz import header1

# --- GLobal Vars ---

# Choosing the themes
themes = [
    gr.themes.Ocean(),
    gr.themes.Monochrome(),
    gr.themes.Citrus(),
    gr.themes.Glass(),
    gr.themes.Default(),
    gr.themes.Soft()
]
c_th = themes[5]


# --- Main Function ---


def g1_main():
    # g1_1()
    # g1_2()
    g1_3()


# --- Sub Function ---

# General tab testing here
def g1_1():
    header1("Gradio Test 1.1")

    # Introduction section
    def intro_section():
        gr.Markdown(in_txt)

    # Main Interface
    with gr.Blocks(
        theme=c_th
    ) as g1_ui:

        with gr.Tab("Gradio Test 1.1"):
            intro_section()

    g1_ui.launch(
        show_error=True,
    )

# Tsting out the chat interfac tests here


def g1_2():
    header1("Gradio Test - Chat Interface Testing")

    # Intro tab
    def intro_section():
        gr.Markdown(in_txt2)

    # Chat Interface function
    def ch_in():

        def slow_echo(message, history):
            for i in range(len(message)):
                time.sleep(0.05)
                yield "SmellPanty: " + message[:i + 1]

        gr.ChatInterface(
            slow_echo,
            title="Booty Sniffing Chat Interface",
            description="Chat with SmellPanty",
            textbox=gr.Textbox(
                placeholder="Bastard write something useful here !!! 🦧🦧🦧",
            ),
            type="messages",
            flagging_mode="manual",
            flagging_options=["Good", "Bad", "Shit"],
            examples=[
                ["Hi", "Hello"],
                ["How are you?", "Good"],
                ["What's your name?", "My name is SmellPanty"],
            ],
            save_history=True,
        )

    # Main UI
    with gr.Blocks(
        theme=c_th
    ) as g1_ui:

        with gr.Tab("Gradio Test 1.2"):
            intro_section()

        with gr.Tab("Demo Chat Interaface Example"):
            gr.Markdown(txt2)
            ch_in()

    g1_ui.launch(
        show_error=True,
    )

# Testing basic I/O


def g1_3():
    header1("Gradio Test 1.3")

    def welcome(name):
        return f"u typed {name}"

    czz = " .gradio-container {background: url(https://i.giphy.com/U3qYN8S0j3bpK.webp)} "

    # Main ui
    with gr.Blocks(
        theme=c_th,
        css=czz
    ) as g3_ui:

        with gr.Tab("Intro Text"):
            gr.Markdown("#Simple Input output test")

        with gr.Tab("Actual Functions"):
            inp = gr.Textbox(
                placeholder="Fuck OFf bastard",
                type="password"
            )
            out = gr.Textbox()
            rape_btn = gr.Button("Rape")
            rape_btn.click(welcome, inputs=inp, outputs=out)

    g3_ui.launch(
        show_error=True
    )
