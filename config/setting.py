import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Check if API key exists
if GEMINI_API_KEY is None:
    raise ValueError("GEMINI_API_KEY not found. Please add it to your .env file.")

# Model configuration
MODEL_NAME = "gemini-2.5-flash"

# LLM generation defaults
MAX_TOKENS = 500
TEMPERATURE = 0.5
TOP_P = 0.1
TOP_K = None
REPETITION_PENALTY = None

# Chatbot personality / system prompt
SYSTEM_PROMPT = {
    "role": "system",
    "content": "You're a friendly and funny assistant who always adds a touch of humor when answering questions."
}

# Initial assistant greeting
INITIAL_ASSISTANT_PROMPT = {
    "role": "assistant",
    "content": "Hey there, fabulous! Ready to have some fun and get things done? How can this charming assistant help you today?"
}