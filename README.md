# End-to-End AI Agent Chatbot

This project is an AI Agent Chatbot that allows users to interact with powerful LLMs (Groq LLaMA3, OpenAI GPT-4) via a web interface, with optional web search capabilities.

## Features
- Chat with LLMs (Groq, OpenAI)
- Optional web search tool (Tavily or Linkup)
- Streamlit frontend
- FastAPI backend

## Setup Instructions

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   (Run this command in the project root directory.)

2. **(Optional) Install Linkup Search Tool**
   If you want to use the Linkup search tool, install its package:
   ```bash
   pip install -U langchain-linkup
   ```

3. **Set up environment variables**
   - Create a `.env` file in the project root with your API keys:
     ```env
     GROQ_API_KEY=your_groq_api_key
     OPENAI_API_KEY=your_openai_api_key
     TAVILY_API_KEY=your_tavily_api_key
     LINKUP_API_KEY=your_linkup_api_key  # Required for Linkup search tool
     ```

   - The `LINKUP_API_KEY` is required if you want to use the Linkup search tool. You can get your API key from the Linkup provider.

## Running the Application

### 1. Start the FastAPI Backend
From the project root, run:
```bash
python -m uvicorn main:app --reload --port 8000
```
- The backend will be available at http://localhost:8000

### 2. Start the Streamlit Frontend
In a new terminal, from the project root, run:
```bash
streamlit run frontend/app.py
```
- The frontend will be available at http://localhost:8501

## Usage
- Use the Streamlit UI to select the model provider, model, system prompt, and enable/disable web search.
- You can now select which search tool to use: **Tavily** or **Linkup**.
- Enter your message and chat with the AI agent!

---

For any issues, ensure all dependencies are installed and API keys are set correctly.

