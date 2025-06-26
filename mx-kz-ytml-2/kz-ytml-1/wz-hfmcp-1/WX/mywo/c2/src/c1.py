# //////////////////////////////////////////////////
# Testing basic input and output in gradio
# //////////////////////////////////////////////////

import gradio as gr

from .utz import header1


def c1_main_func():
    c1()


def c1():
    header1("Chat 1")

    def greet(name, emoji):
        return f"Hello {name} {emoji}"

    with gr.Blocks() as demo:

        gr.Markdown("## Chat 1")
        gr.Markdown("This is a simple greeting app using Gradio.")

        with gr.Row():

            with gr.Column():

                name = gr.Textbox(label="Name", placeholder="Enter your name")
                emoji = gr.Textbox(label="Emoji", placeholder="Enter an emoji")
                greet_button = gr.Button("Greet")

            with gr.Column():
                output = gr.Textbox(label="Output")
                greet_button.click(greet, inputs=[name, emoji], outputs=output)

    demo.launch()
