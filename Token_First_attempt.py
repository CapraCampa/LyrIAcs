import pandas as pd
import numpy as np
import sys
from sklearn.cluster import KMeans
from tokenizers import Tokenizer
from tokenizers.models import WordPiece
from tokenizers.trainers import WordPieceTrainer
from tokenizers.normalizers import Lowercase
from tokenizers.pre_tokenizers import Whitespace
from transformers import AutoTokenizer

# Seleziona il modello appropriato per la lingua delle lyrics (ing per ora)
model_name = "bert-base-uncased" 

tokenizer = AutoTokenizer.from_pretrained(model_name)

db = pd.read_csv('lyr_ing_samp.csv')

lyrics = list(db["lyrics"])

# Applica la tokenizzazione
inputs = tokenizer(lyrics[:10], return_tensors="pt", padding=True, truncation=True, max_length=100)

print(inputs)

texts_ids = pd.DataFrame(inputs.input_ids)
texts_ids.to_csv("texts_ids.csv")
