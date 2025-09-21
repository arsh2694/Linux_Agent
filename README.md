# MyAgent – LangChain + Google Generative AI Linux Assistant

This project is a simple command-line agent built with [LangChain](https://www.langchain.com/) and [Google Generative AI](https://ai.google.dev/).  
It allows you to interact with a Linux shell through natural language prompts, with responses logged to `output.log`.

---

## 🚀 Features
- Uses **Google Generative AI (Gemini model)** for natural language understanding.
- Executes **Linux shell commands** via `ShellTool`.
- Logs final outputs into `output.log`.

---

All dependencies are listed in [`requirements.txt`](requirements.txt).  
To install them:
```bash
pip install -r requirements.txt
```

## ⚠️ Important
The script currently contains a **hardcoded Google API Key**.  
For security, you **must** set it as an environment variable instead of storing it in the code.

```bash
export GOOGLE_API_KEY="your_api_key_here"

