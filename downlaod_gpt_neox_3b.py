from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "EleutherAI/gpt-neox-3b"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",  # Automatically maps layers to GPU/CPU
    torch_dtype="auto"  # Use FP16 if available
)

