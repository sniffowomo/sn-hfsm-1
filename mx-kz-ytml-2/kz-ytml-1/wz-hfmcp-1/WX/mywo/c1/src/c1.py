import random
import time

import gradio as gr

from .utz import header1

chatDescription = """
# Chat Interface Example
This example demonstrates a simple chat interface using Gradio.
"""


def chat_1():
    header1("Chat Interface Example")

    with gr.Blocks() as demo:
        gr.Markdown(chatDescription)
        chatbot = gr.Chatbot(type="messages")
        msg = gr.Textbox()
        clear = gr.ClearButton([msg, chatbot])

        def respond(message, chat_history):
            bot_message = random.choice(
                ["How are you?", "Today is a great day", "I'm very hungry"])
            chat_history.append({"role": "user", "content": message})
            chat_history.append({"role": "assistant", "content": bot_message})
            time.sleep(2)
            return "", chat_history

        msg.submit(respond, [msg, chatbot], [msg, chatbot])

    demo.launch()
