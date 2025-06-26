# /////////////////////////////////
# Agentt Calling from curso here - This was from the course which you are now abandoning
# /////////////////////////////////

from smolagents import CodeAgent, InferenceClientModel, WebSearchTool

from .utz import header1

# --- Main Function ---


def ag1_main():
    agent_fn1()

# --- Agent Function Test ---


def agent_fn1():
    header1("Agent Function Test - Examples from repository")
    model = InferenceClientModel(
        model_id="deepseek-ai/DeepSeek-R1",
        provider="together",
    )
    agent = CodeAgent(tools=[WebSearchTool()],
                      model=model, stream_outputs=True)
    agent.run(
        "How many seconds would it take for a leopard at full speed to run through Pont des Arts?")
