from unsloth import FastLanguageModel
from transformers import AutoTokenizer

base_model = "mistralai/Mistral-7B-v0.1"  # or the base you fine-tuned on
adapter_path = "mistral-finetuned"

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = base_model,
    adapter_name = adapter_path,
)
