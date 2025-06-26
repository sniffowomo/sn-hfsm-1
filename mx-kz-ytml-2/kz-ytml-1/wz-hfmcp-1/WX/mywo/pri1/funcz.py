# //////////////////////////////////////
# Functions are called in app.py
# //////////////////////////////////////

import gradio as gr

# Name function


def name_func():

    intro_text = """
# Name Function
1. This is the name function
2. This gradio app is hidden and private
3. You are writting this app so that it can be private and you can later on release if needed
"""

    gr.Markdown(intro_text)
    inp = gr.Textbox(placeholder="What is your name Bastard Raper?")
    out = gr.Textbox()

    inp.change(fn=lambda x: f"Welcome, {x}!",
               inputs=inp,
               outputs=out)

    examples = gr.Examples(
        examples=[
            ["Alice"],
            ["Bob"],
            ["Charlie"],
        ],
        inputs=[inp],
    )

# INtro tab


def intro_tab():

    description = """
# Introduction Text
1. This is the intro text in this tab
2. This gradio app is hidden and private
3. You are writting this app so that it can be private and you can later on release if needed

# Second Section
1. Writing a section here

# Simple Table

| Column 1 | Column 2 |
|---------- | ----------|
| Cell 1 | Cell 2 |
| Cell 3 | Cell 4 |

"""

    gr.Markdown(description)
