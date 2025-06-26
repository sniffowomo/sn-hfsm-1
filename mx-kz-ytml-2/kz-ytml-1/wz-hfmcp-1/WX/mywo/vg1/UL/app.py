# ////////////////////////////////////////////////////////////////
# Testkng gradio video
# ////////////////////////////////////////////////////////////////
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


def intro_tab():

    description = """
# Introduction Text
1. This is the intro text in this tab
2. This gradio app is hidden and private
3. You are writting this app so that it can be private and you can later on release if needed


"""

    gr.Markdown(description)


def video_tab():
    gr.HTML(
        """
            <div style="text-align:center;">
                <iframe width="560" height="315" 
                        src="https://www.youtube.com/embed/h556kOzFKXk?si=djDkJmDLi1wSBrDo" 
                        title="YouTube video player" 
                        frameborder="0" 
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                        referrerpolicy="strict-origin-when-cross-origin" 
                        allowfullscreen>
                </iframe>
            </div>
            """
    )


def video_tab2():
    gr.HTML(
        """
                <div style="text-align:center;">
                    <iframe width="560" height="315" 
                            src="https://www.youtube.com/embed/ea6Mp8RzGqo?si=CnzlCFdUdIYYpYDi" 
                            title="YouTube video player" 
                            frameborder="0" 
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                            referrerpolicy="strict-origin-when-cross-origin" 
                            allowfullscreen>
                    </iframe>
                </div>
                """
    )


with gr.Blocks(theme=choose_theme) as demo:

    with gr.Tab("Intro"):
        intro_tab()

    with gr.Tab("Name Function"):
        intro_tab()

        with gr.Row():
            with gr.Column(scale=1):
                video_tab()
            with gr.Column(scale=1):
                video_tab2()


if __name__ == "__main__":
    demo.launch()
