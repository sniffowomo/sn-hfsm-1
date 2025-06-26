# ///////////////////////////////////////////////////////////////
# c4.py - Truying to write a streaming chatbot from scratch with Hugging Face API
#
# ////////////////////////////////////////////////////////////////

import time

import gradio as gr


def main():
    # Intro Message
    intro_message = """
# Streaming Chatbot Example
1. Testing making blocks and stream 
"""

    def slow_echo(message, history):
        for i in range(len(message)):
            time.sleep(0.05)
            yield "You typed: " + message[: i + 1]

    def chat_box():
        gr.ChatInterface(
            slow_echo,
            type="messages",
            save_history=True,
        )

    # Defining the main block
    with gr.Blocks() as demo:
        # Defining the intro block
        with gr.Tab("Intro"):
            gr.Markdown(intro_message)

        # Actual Chat Interface Here
        with gr.Tab("Chat", scale=1):
            chat_box()

    demo.launch()


if __name__ == "__main__":
    main()
