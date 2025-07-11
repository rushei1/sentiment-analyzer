import argparse
import json
import os
import random
import numpy as np
from datasets import load_dataset, Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from transformers import DataCollatorWithPadding
import torch

# Reproducibility
def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

set_seed(42)

# Parse CLI arguments
parser = argparse.ArgumentParser()
parser.add_argument("--data", type=str, required=True)
parser.add_argument("--epochs", type=int, default=3)
parser.add_argument("--lr", type=float, default=3e-5)
args = parser.parse_args()

# Load dataset
with open(args.data, "r", encoding="utf-8") as f:
    lines = [json.loads(line) for line in f]

dataset = Dataset.from_list(lines)
label_map = {"negative": 0, "positive": 1}
dataset = dataset.map(lambda e: {"label": label_map[e["label"]]})

# Load model & tokenizer
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

# Tokenize
def preprocess(example):
    return tokenizer(example["text"], truncation=True)

tokenized = dataset.map(preprocess, batched=True)
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

# Training setup
output_dir = os.path.join("..", "backend", "model")
training_args = TrainingArguments(
    output_dir=output_dir,
    per_device_train_batch_size=8,
    num_train_epochs=args.epochs,
    learning_rate=args.lr,
    logging_dir="./logs",
    seed=42,
    save_strategy="epoch"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized,
    tokenizer=tokenizer,
    data_collator=data_collator
)

trainer.train()
model.save_pretrained(output_dir)
tokenizer.save_pretrained(output_dir)

print(f"✅ Model saved to {output_dir}")
