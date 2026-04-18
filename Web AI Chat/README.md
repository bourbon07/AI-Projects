# Full-Stack Web AI Chatbot 🌐
[![Flask](https://img.shields.io/badge/Backend-Flask-green)](https://flask.palletsprojects.com/)
[![BlenderBot](https://img.shields.io/badge/Model-BlenderBot-blue)](https://huggingface.co/facebook/blenderbot-400M-distill)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A modern web-based chatbot application featuring a **Flask** backend and a robust NLP model based on Facebook's **BlenderBot**.

![Web Chat Screenshot](./Screenshots/Web%20Chat%20.png)

## ✨ Features
- **Natural Conversations**: Uses the `blenderbot-400M-distill` model for human-like dialogue.
- **RESTful API**: A Flask-based backend handles communication between the user and the language model.
- **Modern Interface**: A clean web UI for seamless chatting.
- **CORS Support**: Ready for integration with external frontends.

## 🛠️ Tech Stack
- **Backend**: Python (Flask)
- **AI Model**: Facebook BlenderBot (NLP Transformers)
- **Frontend**: HTML / JavaScript / Flask Templates
- **Data Exchange**: JSON

## 💻 Setup and Run
1. Install requirements:
   ```bash
   pip install flask flask-cors transformers torch
   ```
2. Start the Flask server:
   ```bash
   python "AI Chat.py"
   ```
3. Open your browser to `http://127.0.0.1:5000` to start chatting.

## 🔗 Endpoint Reference
The server exposes a `/chatbot` POST endpoint that accepts a JSON prompt:
```json
{
  "prompt": "Hello, how are you?"
}
```
Returns a string response from the BlenderBot model.

---
### 👤 Developer
**Fawaz Allan**  
Full-Stack & AI Developer  

📧 [Gmail](mailto:fwzallan@gmail.com) | 💼 [LinkedIn](https://www.linkedin.com/in/fawaz-allan-188717247/)
