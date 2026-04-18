# Importing tokenizer and model for seq2seq language modeling
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Choosing the pre-trained BlenderBot model (distilled version for speed)
model_name = "facebook/blenderbot-1B-distill"

# Load model and tokenizer (downloads them if not cached)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Initialize an empty conversation history
conversation_history = []

# Convert conversation history into a single string (initially empty)
history_string = "\n".join(conversation_history)

# Input message to start the conversation
input_text = "hello, how are you doing?"

# Tokenize both the history and current input together
inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")
print(inputs)  # Debug: view tokenized input structure

# Generate a response from the model
outputs = model.generate(**inputs)
print(outputs)  # Debug: raw model output tokens

# Decode the model output into readable text
response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
print(response)  # Print bot's reply

# Save both the user input and bot response to conversation history
conversation_history.append(input_text)
conversation_history.append(response)
print(conversation_history)  # Debug: view conversation history

# Start interactive loop for chatting
while True:
    history_string = "\n".join(conversation_history)  # Update history string
    input_text = input("> ")  # Get user input

    # Tokenize history and input
    inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")

    # Generate model response
    outputs = model.generate(**inputs)

    # Decode output
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    print(response)

    # Update conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)






!pip install flask-cors

from flask import Flask, request, render_template
from flask_cors import CORS
import json
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = Flask(__name__)
CORS(app)

model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
conversation_history = []

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/chatbot', methods=['POST'])
def handle_prompt():
    data = request.get_data(as_text=True)
    data = json.loads(data)
    print(data) # DEBUG
    input_text = data['prompt']
    
    # Create conversation history string
    history = "\n".join(conversation_history)

    # Tokenize the input text and history
    inputs = tokenizer.encode_plus(history, input_text, return_tensors="pt")

    # Generate the response from the model
    outputs = model.generate(**inputs)

    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # Add interaction to conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)

    return response

if __name__ == '__main__':
    app.run()