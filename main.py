import os
import gradio as gr
from mistralai import Mistral, UserMessage
from dotenv import load_dotenv, find_dotenv


def chat_bot(user_input):
    load_dotenv(find_dotenv())
    miss_api_key = os.environ["MISTRAL_API"]
    model = "mistral-small-latest"

    client = Mistral(api_key=miss_api_key)

    message = [{
        "role": "user",
        "content": user_input,
    }, ]

    chat_response = client.chat.complete(
        model=model,
        messages=message,
    )
    # response = client.create_chat_completion()
    return chat_response.choices[0].message.content

    # for chunk in client.chat.stream(model=model, messages=message):
    # if "delta" in chunk.data.choices[0]:
    #   if chunk.data.choices[0].delta.content:
    #      print(chunk.data.choices[0].delta.content, end="")


iface = gr.Interface(
    fn=chat_bot,
    inputs="text",
    outputs="text",
    description="Guides the website usage",
    examples=[["How can you help me?"]],
    title="Website Guide"
)
iface.launch()
