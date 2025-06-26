# //////////////////////////////////////////////////////////
# GEneral Gradio tests in this section
# //////////////////////////////////////////////////////////


import os

import gradio as gr
from dotenv import load_dotenv

# from dotenv import load_dotenv
from src.utz import header1

# --- Getting the ENV Variables ---

load_dotenv("./src/.env")
hf_token = os.getenv("HF")

# --- Main Function ---


def grt1_main():
    """ Main Entry Function called in panty.py"""
    # grt1_f1()
    grt1_f2()

# --- Sub functions ----

# Trying to understand basic input and ouput here Testing the tabbed interfaces here


def grt1_f1():
    """Tabbed interface tests isolatin of into tabs"""
    header1("Gradio General Tests ")

    def greet(name):
        return name + "SmellFarts"

    def tab1():
        with gr.Tab("Smell Panty"):
            gr.Image("../../../wo/085.jpg")
            gr.Markdown("# Woman Si ltink Sniff")

    with gr.Blocks() as demo:
        tab1()
        tab1()
        tab1()

    demo.launch()

# --- I/O Tests ---


def grt1_f2():
    header1("Gradio I/O Tests ")

    # Function that executes
    def smellpanty(name):
        return name + "SmellFarts"

    # tabbed function intro tab
    def intro_msg():
        with gr.Tab("IntroTab"):
            message = """
    # Interface testing
    - Booty
    """
            gr.Markdown(message)

    # Input function
    def input_funtion():
        with gr.Tab("InputTab"):
            gr.Interface(
                fn=smellpanty,
                inputs=gr.Textbox(lines=2, label="Name"),
                outputs="text",
            )

    # Chat Interface

    # Tabbed Function
    with gr.Blocks() as demo:
        intro_msg()
        input_funtion()

    demo.launch()
