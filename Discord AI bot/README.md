# High-Performance Discord AI Bot 🤖
[![Gemini 2.0](https://img.shields.io/badge/AI-Gemini%202.0-orange)](https://deepmind.google/technologies/gemini/)
[![Discord.py](https://img.shields.io/badge/Library-Discord.py-blue)](https://discordpy.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A versatile Discord bot powered by **Gemini 2.0 Flash** and **Tesseract OCR**, designed to enhance server interaction with AI intelligence and document processing capabilities.

![AI Chatting](./Screenshot%20dis/AI%20chatting.png)

## 🌟 Features
- **Intelligent Conversation**: Powered by Google's `Gemini 2.0 Flash` for ultra-fast and coherent chat interactions.
- **Deep Text Extraction (OCR)**: Extracts text from uploaded images (`.png`, `.jpg`) using Tesseract.
- **PDF Parsing**: Reads and summarizes documents using PyMuPDF (fitz).
- **Context Awareness**: Remembers the last few messages in a conversation for more natural AI replies.

## 🛠️ Usage
- `!ask [prompt]`: Start a conversation with the AI.
- `!read`: After uploading an image or PDF, use this command to extract its text.
- `!ping`: Check bot latency.

![Read Files](./Screenshot%20dis/Read%20files.png)

## ⚙️ Setup & Launch Guide

### Step 1: Python Installation
- Press `Windows + R`, type `cmd`, and press Enter.
- Type `python --version` to check if Python is installed.
- If not found, download it from [python.org](https://www.python.org/downloads/).

### Step 2: Prerequisites
- **Install Tesseract OCR**: Download the Windows installer (`.exe`) from [Tesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki).
- **Obtain API Keys**: Get a **Discord Bot Token** and a **Google AI (Gemini) API Key**.
- **Configure the .env file**:
   ```env
   DISCORD_TOKEN=your_discord_token
   GOOGLE_API_KEY=your_gemini_key
   TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe
   ```

### Step 3: Launching the Bot
1. Navigate to the bot's folder:
   ```bash
   cd "path\to\your\bot"
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the bot:
   ```bash
   python TGFR.py
   ```

### Step 4: Confirmation
If successful, you will see:
`✅ Logged in as YourBotName (ID: 1234567890)`

Now you can head to Discord and use `!ask <prompt>` or `!read` to interact with your AI!

## 📦 Tech Stack
- **Framework**: Discord.py
- **AI Model**: Google Gemini 2.0 Flash
- **OCR Engine**: Tesseract
- **Document Processing**: PyMuPDF & Pillow

---
### 👤 Developer
**Fawaz Allan**  
AI & Flutter Developer  

📧 [Gmail](mailto:fwzallan@gmail.com) | 💼 [LinkedIn](https://www.linkedin.com/in/fawaz-allan-188717247/)
