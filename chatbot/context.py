from multiprocessing import context
from typing import List, Dict
from .llm import generate_response

MAX_HISTORY = 10

def call_llm_with_context(prompt: str, context: List[Dict], role="user", **kwargs):

    context.append({"role": role, "content": prompt})

    response = generate_response(context, **kwargs)

    context.append(response)

    # keep system prompt always
    system = context[0]

    history = context[1:]

    if len(history) > MAX_HISTORY:
        history = history[-MAX_HISTORY:]

    context[:] = [system] + history
    print("Current context length:", len(context))
    print("First role:", context[0]["role"])

    return response