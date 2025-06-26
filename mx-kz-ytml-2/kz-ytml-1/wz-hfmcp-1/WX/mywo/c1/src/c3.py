# /////////////////////////
#  HF Streaming Chatbot - Code generated with Mistral
#  Using deprecated patterns. Need to refactor.
# //////////////////////////

import os

import gradio as gr
import requests
import sseclient
from dotenv import load_dotenv


def header1(title):
    # Placeholder for your header function
    print(f"# {title}")


def hf_stream_bot():
    header1("Hugging Face Streaming Chatbot")

    # Load environment variables
    load_dotenv()

    default_model = "meta-llama/Llama-2-7b-chat-hf"
    default_api_key = os.getenv("HF", "")

    def build_prompt(history, message):
        """Construct prompt from chat history."""
        prompt = "".join(
            [f"User: {user_msg}\nAssistant: {assistant_msg}\n" for user_msg, assistant_msg in history])
        prompt += f"User: {message}\nAssistant:"
        return prompt

    def stream_response(api_key, model_name, prompt):
        """Handle the streaming response from Hugging Face API."""
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Accept": "text/event-stream",
            "Content-Type": "application/json"
        }

        payload = {
            "inputs": prompt,
            "parameters": {
                "do_sample": True,
                "max_new_tokens": 200,
                "return_full_text": False,
                "stream": True
            }
        }

        url = f"https://api-inference.huggingface.co/models/{model_name}"

        try:
            response = requests.post(
                url, headers=headers, json=payload, stream=True, timeout=30)
            response.raise_for_status()

            client = sseclient.SSEClient(response)
            for event in client:
                if event.data == "[DONE]":
                    break
                try:
                    token = eval(event.data)["token"]["text"]
                    yield token
                except (KeyError, SyntaxError):
                    continue
        except Exception as e:
            yield f"[Error] {str(e)}"

    def respond(message, history, api_key, model_name):
        """Process user message and stream the response."""
        if not api_key:
            yield "[Error] API key not found. Please provide the Hugging Face API key."
            return

        prompt = build_prompt(history, message)
        yield from stream_response(api_key, model_name or default_model, prompt)

    # Create and launch the Gradio interface
    demo = gr.ChatInterface(
        respond,
        title="Hugging Face Streaming Chatbot",
        description="Chat with a Hugging Face model using streaming responses.",
        examples=[["Hello! How are you doing?"]],
        additional_inputs=[
            gr.Textbox(value=default_api_key, label="Hugging Face API Key",
                       placeholder="Enter your Hugging Face API key", type="password"),
            gr.Textbox(value=default_model, label="Model Name",
                       placeholder="e.g., meta-llama/Llama-2-7b-chat-hf")
        ]
    )

    demo.launch()


# This would be in main.py
if __name__ == "__main__":
    hf_stream_bot()
