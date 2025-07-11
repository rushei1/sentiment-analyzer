from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import os

MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "model")

def load_model():
    if os.path.exists(os.path.join(MODEL_DIR, "config.json")):
        model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)
        tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
    else:
        model_name = "distilbert-base-uncased-finetuned-sst-2-english"
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    return pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
