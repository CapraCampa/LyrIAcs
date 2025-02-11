#import joblib
import pickle
import gzip
import pandas as pd
import os
import shutil
#from azure.storage.blob import BlobServiceClient

#connection_string = st.secrets.get("AZURE_CONNECTION_STRING")
#blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Specifica il nome del contenitore e del blob
#container_client = blob_service_client.get_container_client("ml-models")
#blob_client = container_client.get_blob_client("model_genre.pkl")

# Scarica il file del modello
#with open("model_genre_azure.pkl", "wb") as f:
#    f.write(blob_client.download_blob().readall())

#with open("model_genre_azure.pkl", "rb") as f:
#    model_genre = pickle.load(f)

#model_genre = joblib.load('artifacts/model_compressed.pkl')
#with gzip.open('artifacts/model_genre_compressed.pkl.gz', 'rb') as f:
#    model_genre = joblib.load(f)


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
