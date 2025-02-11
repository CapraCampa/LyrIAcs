import pandas as pd

# Function definition
def predict_genre(text, model, vectorizer, svd):
    # Ensure text is a valid string
    text = str(text) if not isinstance(text, str) else text

    if not text.strip():
        print("Input text is empty or invalid!")
        return ["Invalid or empty input"]
    
    # Predict the genre probabilities and get the top 3 predictions
    predicted_genre = model.predict_proba(svd.transform(vectorizer.transform([text])))
    top_three_indices = predicted_genre[0].argsort()[::-1][:3]
    predicted_genre = model.classes_[top_three_indices]
    predicted_genre = predicted_genre.tolist()
    return predicted_genre
