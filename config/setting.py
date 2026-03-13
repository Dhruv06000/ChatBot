import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

HF_API_TOKEN = os.getenv("HF_API_TOKEN")

# Check if API key exists
if HF_API_TOKEN is None:
    raise ValueError("HF_API_TOKEN not found. Please add it to your .env file.")

# Model configuration
MODEL_NAME = "meta-llama/Meta-Llama-3-8B-Instruct"

# LLM generation defaults
MAX_TOKENS = 500
TEMPERATURE = 0.7
TOP_P = 0.9
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