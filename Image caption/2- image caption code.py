import gradio as gr
import numpy as np
from PIL import Image
from transformers import AutoProcessor, Blip2ForConditionalGeneration
import torch

# Use GPU if available for better performance
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the BLIP-2 processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip2-opt-2.7b")
model = Blip2ForConditionalGeneration.from_pretrained(
    "Salesforce/blip2-opt-2.7b",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
)
model.to(device)

# Image captioning function
def caption_image(input_image: np.ndarray):
    # Convert image to PIL and ensure RGB
    raw_image = Image.fromarray(input_image).convert('RGB')

    # Process the image using the BLIP-2 processor
    inputs = processor(images=raw_image, return_tensors="pt").to(device, torch.float16 if torch.cuda.is_available() else torch.float32)

    # Generate caption using beam search for higher quality
    output = model.generate(
        **inputs,
        max_new_tokens=50,
        num_beams=5,               # Use beam search
        early_stopping=True,
        no_repeat_ngram_size=2     # Avoid repeated phrases
    )

    # Decode the output token IDs to text
    caption = processor.tokenizer.decode(output[0], skip_special_tokens=True)
    return caption

# Create the Gradio interface
iface = gr.Interface(
    fn=caption_image,
    inputs=gr.Image(type="numpy"),
    outputs="text",
    title="High-Accuracy Image Captioning",
    description="Upload an image to generate an accurate caption using BLIP-2 (OPT-2.7B). Optimized for quality using beam search.",
)

iface.launch()

