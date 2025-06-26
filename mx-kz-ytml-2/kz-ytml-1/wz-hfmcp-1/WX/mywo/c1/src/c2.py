import random
import time

import gradio as gr

chatDescription = "This is a simple chatbot interface. Type a message and get a random response."


def chat_2():
    with gr.Blocks(title="Chat Interface Panty") as demo:
        with gr.Tabs():
            # Intro Tab
            with gr.Tab("Intro"):
                gr.Markdown("# 🤖 Welcome to the Chatbot Interface")
                gr.Markdown("""
                This app demonstrates a basic chatbot using Gradio.

                - Head over to the **Chat** tab to start chatting.
                - The bot will reply with random responses.
                - This is for demonstration purposes only.
                """)

            # Chat Tab
            with gr.Tab("Chat"):
                gr.Markdown("## Chat Interface Example")
                gr.Markdown(chatDescription)

                chatbot = gr.Chatbot(type="messages")
                msg = gr.Textbox(
                    placeholder="Type a message...", show_label=False)
                clear = gr.ClearButton([msg, chatbot])

                def respond(message, chat_history):
                    bot_message = random.choice([
                        "How are you?",
                        "Today is a great day.",
                        "I'm very hungry."
                    ])
                    chat_history.append({"role": "user", "content": message})
                    chat_history.append(
                        {"role": "assistant", "content": bot_message})
                    time.sleep(2)
                    return "", chat_history

                msg.submit(respond, [msg, chatbot], [msg, chatbot])

    demo.launch()
