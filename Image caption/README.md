# BLIP-2 Image Captioning 🖼️
[![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow)](https://huggingface.co/docs/transformers/main/en/index)
[![Salesforce BLIP-2](https://img.shields.io/badge/Model-BLIP--2-blue)](https://huggingface.co/docs/transformers/main/en/model_doc/blip-2)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-red.svg)](https://opensource.org/licenses/Apache-2.0)

This project provides a professional-grade image captioning tool using the **BLIP-2 (OPT-2.7B)** architecture from Salesforce Research. It generates highly descriptive and accurate captions for any uploaded image.

![Captioning Screenshot](./.screenshots/image%20caption%20screenshot.png)

## 🚀 How it Works
The system leverages Salesforce's `blip2-opt-2.7b` model, which excels at understanding visual context and translating it into natural language. It utilizes **Beam Search** with 5 beams to ensure the generated sentences are diverse and high-quality.

## 🛠️ Tech Stack
- **Transformer Model**: BLIP-2 (Salesforce/blip2-opt-2.7b)
- **Framework**: PyTorch & Transformers (Hugging Face)
- **Interface**: Gradio for a seamless web UX

## 💻 Installation
1. Install the required libraries:
   ```bash
   pip install transformers torch pillow gradio numpy
   ```
2. (Recommended) Ensure CUDA is installed for GPU acceleration:
   ```python
   # The script will automatically detect and use GPU if available
   ```
3. Run the application:
   ```bash
   python "2- image caption code.py"
   ```

## 📈 Performance
By utilizing the OPT-2.7B backbone, the model provides a significant jump in accuracy compared to standard BLIP models, making it suitable for accessibility tools and automatic image tagging.

---
### 👤 Developer
**Fawaz Allan**  
AI Research & Development  

📧 [Gmail](mailto:fwzallan@gmail.com) | 💼 [LinkedIn](https://www.linkedin.com/in/fawaz-allan-188717247/)
