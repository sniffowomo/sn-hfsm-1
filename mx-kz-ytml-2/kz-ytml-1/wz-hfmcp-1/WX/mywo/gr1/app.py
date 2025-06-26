import gradio as gr


# Main greeter function
def greet(name, intensity):
    return "Fuckoff " + name + "! Intensity: " + str(intensity)


# Setting up the Gradio interface with blocks and tabs
with gr.Blocks(title="RapezAppmomm") as demo:
    with gr.Tabs():

        # Intro tab with a welcome message
        with gr.Tab("Intro"):
            gr.Markdown("# 👋 Welcome to the Greeting App!")
            gr.Markdown("""
            This app generates a humorous greeting with your name and a chosen intensity.

            - Use the **Greeting** tab to input your name.
            - Slide the intensity meter to dial up or down the 'energy'.
            - It's all in good fun — enjoy!
            """)

        # Greeting tab with input fields and a button
        with gr.Tab("GreetingPanty"):
            gr.Markdown("## Customize Your Greeting")

            with gr.Row():
                # First column - Input controls
                with gr.Column():
                    name = gr.Textbox(
                        label="Name", placeholder="Enter your name")
                    intensity = gr.Slider(
                        value=2,
                        minimum=0,
                        maximum=100,
                        label="Intensity",
                        step=1
                    )
                    greet_btn = gr.Button("Greet", variant="primary")
                    output = gr.Textbox(label="Greeting", lines=3)
                    greet_btn.click(fn=greet, inputs=[
                                    name, intensity], outputs=output)

                # Second column - Examples
                with gr.Column():
                    gr.Markdown("### Try these examples:")
                    gr.Examples(
                        examples=[["Alice", 10], ["Bob", 20], ["Charlie", 30]],
                        inputs=[name, intensity],
                        label="Click any example to apply",
                        examples_per_page=3
                    )

if __name__ == "__main__":
    demo.launch()
