from typing import List, Dict
from .llm import generate_response

MAX_HISTORY = 10

def call_llm_with_context(prompt: str, context: List[Dict], role="user", **kwargs):

    if not context:
        raise ValueError("Context must start with a system message")

    # add user message
    context.append({"role": role, "content": prompt})

    # get model response
    response = generate_response(context, **kwargs)

    # add assistant reply
    context.append(response)

    # keep system prompt
    system = context[0]
    history = context[1:]

    # trim history
    if len(history) > MAX_HISTORY:
        history = history[-MAX_HISTORY:]

    context[:] = [system] + history

    
    print("First role:", context[0]["role"])

    return response