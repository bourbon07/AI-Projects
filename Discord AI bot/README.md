# High-Performance Discord AI Bot 🤖
[![Gemini 2.0](https://img.shields.io/badge/AI-Gemini%202.0-orange)](https://deepmind.google/technologies/gemini/)
[![Discord.py](https://img.shields.io/badge/Library-Discord.py-blue)](https://discordpy.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A versatile Discord bot powered by **Gemini 2.0 Flash** and **Tesseract OCR**, designed to enhance server interaction with AI intelligence and document processing capabilities.

![AI Chatting](./Screenshot/AI%20chatting.png)

## 🌟 Features
- **Intelligent Conversation**: Powered by Google's `Gemini 2.0 Flash` for ultra-fast and coherent chat interactions.
- **Deep Text Extraction (OCR)**: Extracts text from uploaded images (`.png`, `.jpg`) using Tesseract.
- **PDF Parsing**: Reads and summarizes documents using PyMuPDF (fitz).
- **Context Awareness**: Remembers the last few messages in a conversation for more natural AI replies.

## 🛠️ Usage
- `!ask [prompt]`: Start a conversation with the AI.
- `!read`: After uploading an image or PDF, use this command to extract its text.
- `!ping`: Check bot latency.

![Read Files](./Screenshot/Read%20files.png)

## ⚙️ Installation & Launch Guide
Follow these steps to get your Discord AI Bot up and running:

### 1. Environment Setup
Create a `.env` file in the bot's root directory and add your credentials:
```env
DISCORD_TOKEN=your_discord_token
GOOGLE_API_KEY=your_gemini_key
TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe
```

### 2. Prerequisites
- Ensure **Python 3.9+** is installed. Check using: `python --version`
- Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract/releases) if you plan on using the image-to-text features.

### 3. Launching the Bot
1. Open your terminal or CMD.
2. Navigate to the project folder.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the bot:
   ```bash
   python TGFR.py
   ```

### 4. Confirmation
If successful, you will see:
`✅ Logged in as YourBotName (ID: ...)`

Now go to your Discord server and type `!ask Hello!` to start chatting with your AI.

## 📦 Tech Stack
- **Framework**: Discord.py
- **AI Model**: Google Gemini 2.0 Flash
- **OCR Engine**: Tesseract
- **Document Processing**: PyMuPDF & Pillow

---
### 👤 Developer
**Fawaz Allan**  
AI & Flutter Developer  
[GitHub Profile](https://github.com/bourbon07)
