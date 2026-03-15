from .context import call_llm_with_context
from .utils import print_response
from config.setting import  SYSTEM_PROMPT, INITIAL_ASSISTANT_PROMPT

# Initialize   Conversation context
context = [SYSTEM_PROMPT, INITIAL_ASSISTANT_PROMPT]


def chat(temperature = None, 
         top_k = None, 
         top_p = None,
         repetition_penalty = None):
    """
    Runs an interactive chat session between the user and an AI assistant.

    The chat continues in a loop until the user types 'STOP'. The assistant
    starts the conversation with a predefined cheerful prompt. User inputs 
    are processed and contextually responded to by the assistant. Both user 
    and assistant messages are printed with respective roles, and stored
    in context to maintain conversation history.

    Usage:
        Run the function and type your prompts. Type 'STOP' to end the chat.
    """
    # Start by printing the initial assistant prompt
    print_response(context[-1])
    
    # Continues until the user types 'STOP'
    while True:
        prompt = input("User: ")
        if prompt.upper() == 'STOP':
            break

        # Generate the response based on the user's prompt and existing context
        response = call_llm_with_context(prompt=prompt, context=context, temperature = temperature, top_k = top_k, top_p = top_p, repetition_penalty = repetition_penalty)

        # Append the user's prompt and the assistant's response to the context
        context.append({"role": "user", "content": prompt})
        context.append(response)

        # Print the most recent user output, followed by the assistant response
        
        print_response(context[-1])


# Run the chat if this file is executed directly
if __name__ == "__main__":
    chat()