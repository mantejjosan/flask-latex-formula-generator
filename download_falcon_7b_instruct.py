from transformers import AutoModelForCausalLM, AutoTokenizer

# Replace "tiiuae/falcon-7b-instruct" with your chosen model
model_name = "tiiuae/falcon-7b-instruct"

# Download tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

# Save locally if desired
tokenizer.save_pretrained("./falcon_model")
model.save_pretrained("./falcon_model")

