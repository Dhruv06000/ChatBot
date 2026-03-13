# AI ChatBot 🤖

A modular **CLI-based AI chatbot built in Python** that integrates with Hugging Face Large Language Models (LLMs).
The project demonstrates core concepts used in modern AI systems such as **conversation memory, system prompts, context management, and configurable model parameters**.

This chatbot maintains conversational context, applies personality instructions through a system prompt, and provides an interactive terminal chat experience.

---

# 🚀 Features

- **LLM Integration**
  - Uses Hugging Face inference API to communicate with a large language model.

- **Conversation Memory**
  - Maintains conversation history to allow multi-turn dialogue.

- **Context Window Management**
  - Implements a sliding context window using `MAX_HISTORY` to prevent context overflow.

- **System Prompt Personality**
  - The chatbot is initialized with a predefined personality prompt.

- **Environment Configuration**
  - Secure API key management using `.env`.

- **Modular Architecture**
  - Clean project structure separating chat logic, LLM communication, utilities, and configuration.

- **CLI Chat Interface**
  - Simple terminal-based chat experience with colored responses.

- **Persistent Chat History (Planned Feature)**
  - Future update will allow saving and resuming conversations using JSON storage.

---

# 🧠 How It Works

The chatbot works through the following pipeline:

User Input
↓
Context Manager
↓
LLM API Call
↓
Assistant Response
↓
Updated Conversation Context

The conversation history is maintained and trimmed to prevent exceeding the LLM context window.

---

# 📂 Project Structure

```
ai_ChatBot/
│
├── chatbot/
│   ├── __init__.py
│   ├── chat.py          # CLI chat interface
│   ├── context.py       # Conversation context management
│   ├── llm.py           # Hugging Face LLM API interaction
│   ├── utils.py         # Utility functions (response formatting)
│
├── config/
│   └── setting.py       # Configuration and model settings
│
├── .env                 # Environment variables
└── app.py               # Placeholder for future web interface
```

---

# ⚙️ Installation

### 1 Clone the Repository

```bash
git clone https://github.com/yourusername/ai_ChatBot.git
cd ai_ChatBot
```

---

### 2 Create Virtual Environment

```bash
python -m venv .chatbot
```

Activate it:

**Windows**

```bash
.chatbot\Scripts\activate
```

---

### 3 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root:

```
HF_API_TOKEN=your_huggingface_api_key
```

You can get a token from:

https://huggingface.co/settings/tokens

---

# ▶️ Running the Chatbot

Start the chatbot using:

```bash
python -m chatbot.chat
```

Example session:

```
Assistant: Hey there, fabulous! Ready to have some fun?

You: tell me a joke
Assistant: Why do programmers prefer dark mode?
Because light attracts bugs.

You: STOP
Chat ended.
```

---

# ⚙️ Configuration

Model and generation settings can be modified in:

```
config/setting.py
```

Example settings:

```
MODEL_NAME = "meta-llama/Meta-Llama-3-8B-Instruct"
MAX_TOKENS = 500
TEMPERATURE = 0.7
TOP_P = 0.9
```

You can adjust these parameters to change the chatbot's behavior.

---

# 🧩 Context Management

To avoid exceeding the model's context window, the chatbot maintains a sliding history window:

```
MAX_HISTORY = 10
```

This ensures:

- The **system prompt is always preserved**
- Only the **most recent conversation messages are sent to the model**

This approach is commonly used in production LLM applications.

---

# 🔮 Planned Improvements

Future enhancements for this project include:

- Persistent conversation history using JSON storage
- Resume previous conversations
- Web interface using Flask
- Streaming responses (typing effect)
- Retrieval-Augmented Generation (RAG) support

---

# 🎯 Learning Objectives

This project demonstrates practical concepts used in real AI systems:

- LLM API integration
- Prompt engineering
- Conversation context management
- Sliding context windows
- Modular Python project design
- Environment configuration
- CLI application development

---

# 🛠 Technologies Used

- Python
- Hugging Face Inference API
- Meta LLaMA Model
- dotenv
- Virtual Environments

---

# 📜 License

This project is open-source and available under the MIT License.

---

# 👨‍💻 Author

Ricky Raj Sahani
Computer Science Student | AI/ML Enthusiast
