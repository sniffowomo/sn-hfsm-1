# //////////////////////////////////////////////////
# Side by side with tabs
# //////////////////////////////////////////////////

import gradio as gr

from .utz import header1


# --- Main Function caller ---
def c2_mf():
    # c2()
    c2t1()

# -- c2 with tabs and examples --


def c2():
    header1("Chat 1")

    def greet(name, emoji):
        return f"Hello {name} {emoji}"

    def tab_desc():
        gr.Markdown("## Chat 1")
        gr.Markdown("This is a simple greeting app using Gradio.")

    def mainui():
        with gr.Row():
            with gr.Column():
                name = gr.Textbox(label="Name", placeholder="Enter your name")
                emoji = gr.Textbox(label="Emoji", placeholder="Enter an emoji")
                greet_button = gr.Button("Greet")
            with gr.Column():
                output = gr.Textbox(label="Output")
                greet_button.click(greet, inputs=[name, emoji], outputs=output)

        examples = gr.Examples(
            examples=[
                ["Alice", "😊"],
                ["Bob", "😄"],
                ["Charlie", "👍"],
            ],
            inputs=[name, emoji],
        )

    def tab_intro():
        main_intro_text = """
# Chat 1 - Gradio Example
This is a simple Gradio app that allows users to greet others with emojis.

1. The main application is in the second tab.
2. This app is just testing entering variable and and having them displayed.
3. Goal is to find out ho gradio is manipulating variables
"""
        gr.Markdown(main_intro_text)

    # Create the Gradio interface with tabs
    with gr.Blocks() as demo:
        with gr.Tabs():
            with gr.TabItem("🫣 Ui Intro"):
                tab_intro()
            with gr.TabItem("⚙️ Chat 2"):
                tab_desc()
                mainui()

    demo.launch()

# ////////////////////////////////////////////////////////////////////////////////////

# -- c2 with themes testing


def c2t1():
    header1("Chat 1 - with Themes")

    themes = [
        gr.themes.Ocean(),
        gr.themes.Monochrome(),
        gr.themes.Citrus(),
        gr.themes.Glass(),
        gr.themes.Default(),
    ]
    themez = themes[4]

    def greet(name, emoji):
        return f"Hello {name} {emoji}"

    def tab_desc():
        gr.Markdown("## Chat 1")
        gr.Markdown("This is a simple greeting app using Gradio.")

    def mainui():
        with gr.Row():
            with gr.Column():
                name = gr.Textbox(label="Name", placeholder="Enter your name")
                emoji = gr.Textbox(label="Emoji", placeholder="Enter an emoji")
                greet_button = gr.Button("Greet")
            with gr.Column():
                output = gr.Textbox(label="Output")
                greet_button.click(greet, inputs=[name, emoji], outputs=output)

        examples = gr.Examples(
            examples=[
                ["Alice", "😊"],
                ["Bob", "😄"],
                ["Charlie", "👍"],
            ],
            inputs=[name, emoji],
        )

    def tab_intro():
        main_intro_text = """
# Chat 1 - Gradio Example
This is a simple Gradio app that allows users to greet others with emojis.

1. The main application is in the second tab.
2. This app is just testing entering variable and and having them displayed.
3. Goal is to find out ho gradio is manipulating variables
"""
        gr.Markdown(main_intro_text)

    # Create the Gradio interface with tabs
    with gr.Blocks(theme=themez) as demo:
        with gr.Tabs():
            with gr.TabItem("🫣 Ui Intro"):
                tab_intro()
            with gr.TabItem("⚙️ Chat 2"):
                tab_desc()
                mainui()

    demo.launch()
