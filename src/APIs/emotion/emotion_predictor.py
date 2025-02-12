import pandas as pd

# Function definition
def predict_emotion(text, model):
    
    predicted_probs = model.predict_proba([text])
    top_three_indices = predicted_probs[0].argsort()[::-1][:3]
    predicted_emotions = model.classes_[top_three_indices]

    return predicted_emotions.tolist()
