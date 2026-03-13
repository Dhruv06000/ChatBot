from huggingface_hub import InferenceClient
from typing import List, Dict
from config.setting import HF_API_TOKEN, MODEL_NAME, MAX_TOKENS, TEMPERATURE, TOP_P

# Initialize Hugging Face client
client = InferenceClient(token=HF_API_TOKEN)


def generate_response(messages, temperature=None, top_p=None, **kwargs):

    params = {
        "model": MODEL_NAME,
        "messages": messages
    }

    if temperature is not None:
        params["temperature"] = temperature

    if top_p is not None:
        params["top_p"] = top_p

    response = client.chat_completion(**params)

    return {
        "role": "assistant",
        "content": response.choices[0].message.content
    }