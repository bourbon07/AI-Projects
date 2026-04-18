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

## ⚙️ Setup
1. **Prerequisites**:
   - Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract/releases) on your system.
   - A Discord Bot Token (via Developer Portal).
   - A Google AI (Gemini) API Key.
2. **Environment**: Create a `.env` file with:
   ```env
   DISCORD_TOKEN=your_discord_token
   GOOGLE_API_KEY=your_gemini_key
   TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe
   ```
3. **Run**:
   ```bash
   python TGFR.py
   ```

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
