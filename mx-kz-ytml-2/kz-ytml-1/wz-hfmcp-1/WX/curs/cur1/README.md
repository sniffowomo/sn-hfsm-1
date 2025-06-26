<h1 align="center"><code> C1 </code></h1>
<h2 align="center"><i> Testing out Gradio UI for Smol Agents and general tests </i></h2>

1. [c1](#c1)
2. [Filez](#filez)

# c1

1. This main python file is for learning various gradio related tasks

# Filez

1. Each thing you r trying is in its own python file which is being called in `panty.py` woman panty smell is good

|            File            |                                                                                                                                                                           What                                                                                                                                                                            |
| :------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|  [`hft.py`](./src/hft.py)  |                                                                                                                             Testing out calling HF models with the clients. The function write the output directly to stdout                                                                                                                              |
| [`gra1.py`](./src/grt1.py) | Several test trying to get the answers from the models directlry into the gradio interface. Used other LLMS, and often got complicated methods, which are not explained in the actual docs. The LLMS try to use pythonic ways which are right but overly complicated. The gradio docs try to make the process easier. You spend a day running these tests |
| [`gra2.py`](./src/gra2.py) |                                                                After reading [DOCS](https://www.gradio.app/guides/chatinterface-examples#hugging-face-transformers) - Used code from `gra1.py` and the inofrmation in the manual to finaly get the chat to work with streaming and history                                                                |
| [`grt1.py`](./src/grt1.py) |                                                                                                                                                  General tests which you might need to run in the future                                                                                                                                                  |
