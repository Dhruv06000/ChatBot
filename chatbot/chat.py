from .context import call_llm_with_context
from .utils import print_response
from config.setting import HF_API_TOKEN, MODEL_NAME, SYSTEM_PROMPT, INITIAL_ASSISTANT_PROMPT

# Initialize   Conversation context
context = [SYSTEM_PROMPT, INITIAL_ASSISTANT_PROMPT]


def chat(temperature=None, top_k=None, top_p=None, repetition_penalty=None):
    # Print initial assistant message
    print_response(context[-1])

    while True:
        prompt = input("You: ")
        if prompt.strip().upper() == "STOP":
            print("Chat ended.")
            break

        # Generate LLM response and update context
        response = call_llm_with_context(
            prompt=prompt,
            context=context,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            repetition_penalty=repetition_penalty
        )

        # Print user + assistant
        # print_response(context[-2])  # user
        print_response(context[-1])  # assistant


# Run the chat if this file is executed directly
if __name__ == "__main__":
    chat()