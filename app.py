from flask import Flask, request, render_template, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Initialize Flask app
app = Flask(__name__)

# Load Falcon model and tokenizer
# MODEL_PATH = "./falcon_model"
# tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
# model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, device_map="auto")

@app.route('/')
def index():
    return render_template('index.html')
'''
@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.json.get('text', '')
    if not user_input:
        return jsonify({'error': 'No input text provided'}), 400

    # Combine user input with the universal prompt
    prompt = f"Convert the following English text to LaTeX: {user_input}"

    # Generate model output
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_length=200)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return jsonify({'latex': response})

if __name__ == '__main__':
    app.run(debug=True)
'''
