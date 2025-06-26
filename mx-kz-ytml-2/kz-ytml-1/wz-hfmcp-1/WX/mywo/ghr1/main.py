import gradio as gr

themes = [
    gr.themes.Ocean(),
    gr.themes.Monochrome(),
    gr.themes.Citrus(),
    gr.themes.Glass(),
    gr.themes.Default(),
    gr.themes.Soft()
]
choose_theme = themes[5]

with gr.Blocks(theme=choose_theme) as demo:

    with gr.Tab("Intro"):
        gr.Markdown("# Booty Dance")

    with gr.Tab("Tab 1"):
        gr.Markdown("# Greetings from Gradio!")
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

if __name__ == "__main__":
    demo.launch()
