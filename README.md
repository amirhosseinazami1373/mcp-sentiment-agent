# 🧠 MCP Sentiment Agent

A **fully local AI agent** powered by `smolagents`, running a local LLM (DeepSeek-R1 via Ollama), and calling Python tools through the [Machine-Centric Protocol (MCP)](https://huggingface.co/learn/mcp-course/en/). This agent analyzes sentiment from natural language inputs and returns structured results, all with zero cloud dependencies.

---

## 🚀 Features

- 🤖 **LLM-powered agent** using `ToolCallingAgent` from [smolagents](https://github.com/huggingface/smolagents)
- 📊 **Sentiment analysis tool** exposed through Gradio with MCP server
- 💬 **TextBlob** for analyzing polarity and subjectivity
- ⚡ **DeepSeek-R1 8B** running locally via [Ollama](https://ollama.com)
- 🔌 **Fully local**: no OpenAI, no external API calls
- 🛠️ **Modular design**: easily add new tools to your agent

---

## 📁 Project Structure

```
mcp-sentiment-agent/
├── app.py              # Gradio MCP tool server exposing `sentiment()`
├── tiny_agent.py       # Tool-calling agent using local DeepSeek-R1
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── .venv/              # (Optional) Python virtual environment
```

---

## 🧪 How It Works

### 🧾 User prompt:

> "Analyze the sentiment of: 'I love this project!'"

### 🧠 Reasoning steps:

1. The agent sends the prompt to the LLM.
2. The LLM decides to use the `sentiment()` tool.
3. `smolagents` calls the MCP tool server running in `app.py`.
4. `TextBlob` analyzes polarity and subjectivity.
5. The agent returns a final, summarized response.

---

## ⚙️ How to Run This Project Locally

### 🔧 1. Clone the repo

```bash
git clone https://github.com/amirhosseinazami1373/mcp-sentiment-agent.git
cd mcp-sentiment-agent
```

### 🐍 2. Set up Python environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 📦 3. Install NLTK corpora for TextBlob (first time only)

```bash
python -m textblob.download_corpora
```

---

### 🧠 4. Start Ollama and pull the model

If not already done:

```bash
ollama pull deepseek-r1:8b
```

Start the model:

```bash
ollama run deepseek-r1:8b
```

### 🌐 5. Start the tool server (in another terminal)

```bash
python app.py
```

This exposes your tool at:  
`http://localhost:7860/gradio_api/mcp/schema`

### 🔁 6. Run the agent

```bash
python tiny_agent.py
```

---

## 🧩 Output Example

```
Calling tool: 'sentiment' with arguments: {'text': "'I love this!'"}
Observations: Sentiment(polarity=0.625, subjectivity=0.6)

Final answer: The sentiment of the text is positive with a polarity score of 0.625 and a high degree of subjectivity.
```

---

## 🧠 Technologies Used

| Component         | Description                                     |
|------------------|-------------------------------------------------|
| `smolagents`      | Lightweight multi-step tool-calling framework   |
| `TextBlob`        | Sentiment analysis tool                         |
| `Gradio` + `MCP`  | Exposes Python functions as structured tools    |
| `Ollama`          | Runs local LLMs (e.g., DeepSeek-R1, LLaMA3)     |
| `LiteLLM`         | Unified LLM client used by smolagents           |

---

## 🔄 Extend the Agent

Want to build more powerful agents?

- Add tools to `app.py` (e.g., math, web search, summarizer)
- Use different local models (e.g., `llama3`, `mistral`)
- Deploy the tool server on Hugging Face Spaces
- Create an interactive chat UI with Gradio

---

## 📚 References

- [Hugging Face MCP Course](https://huggingface.co/learn/mcp-course/en/)
- [smolagents GitHub](https://github.com/huggingface/smolagents)
- [Ollama](https://ollama.com/)
- [TextBlob Documentation](https://textblob.readthedocs.io/en/dev/)

---
