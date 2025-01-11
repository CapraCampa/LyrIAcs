from transformers import AutoModel
import torch

# Carica il modello pre-addestrato
model = AutoModel.from_pretrained(model_name)

# Converti il modello a precisione ridotta
model.half()

# Disattiva il calcolo dei gradienti per risparmiare memoria
with torch.no_grad():
    outputs = model(**inputs) # in inputs we have our tokenized lyrics

# Calcola la media degli embedding delle ultime hidden states
embeddings = outputs.last_hidden_state.mean(dim=1)  # Shape: (num_samples, hidden_size)

print(embeddings)
embe = pd.DataFrame(embeddings)
embe.to_csv("embe.csv")
