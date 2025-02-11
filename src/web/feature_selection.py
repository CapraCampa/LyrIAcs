import streamlit as st

import joblib
import pickle
import gzip
import pandas as pd
import os
import shutil
from azure.storage.blob import BlobServiceClient

connection_string = st.secrets.get("AZURE_CONNECTION_STRING")
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Specifica il nome del contenitore e del blob
container_client = blob_service_client.get_container_client("ml-models")
blob_client = container_client.get_blob_client("model_genre.pkl")

# Scarica il file del modello
with open("model_genre_azure.pkl", "wb") as f:
    f.write(blob_client.download_blob().readall())

with open("model_genre_azure.pkl", "rb") as f:
    model_genre = pickle.load(f)

#model_genre = joblib.load('artifacts/model_compressed.pkl')
#with gzip.open('artifacts/model_genre_compressed.pkl.gz', 'rb') as f:
#    model_genre = joblib.load(f)
#with open('artifacts/model_genre.pkl', 'rb') as file:
#    model_genre = pickle.load(file)
with open('artifacts/vectorizer_genre.pkl', 'rb') as file:
    tfidf_vectorizer = pickle.load(file)
with open('artifacts/svd_genre.pkl', 'rb') as file:
    svd = pickle.load(file)
# Function definition
def predict_genre(text):
    # Ensure text is a valid string
    text = str(text) if not isinstance(text, str) else text

    if not text.strip():
        print("Input text is empty or invalid!")
        return ["Invalid or empty input"]
    # Predict the genre probabilities and get the top 3 predictions
    predicted_genre = model_genre.predict_proba(svd.transform(tfidf_vectorizer.transform([text])))
    top_three_indices = predicted_genre[0].argsort()[::-1][:3]
    predicted_genre = model_genre.classes_[top_three_indices]
    return predicted_genre
    


st.write(f"Input: {st.session_state.first_chunks}")
st.write(f"Emotions: {st.session_state.emotions}")
st.write(f"Genres: {st.session_state.genres}")


# Title
st.markdown("""
    <h1 style='text-align: center;'>LyrIAcs</h1>
    <p style='text-align: center;'>Select your preferences</p>
""", unsafe_allow_html=True)


if 'user_lyrics' in st.session_state:
    user_lyrics = st.session_state.user_lyrics
else:
    st.warning("No lyrics found. Please go back and input lyrics.")


with st.spinner('Predicting genre...'):
    result = predict_genre(user_lyrics)
    st.success('Prediction complete!')

with st.container(border=True):
    left, right = st.columns(2, vertical_alignment="center")
    options = result
    genres = left.pills("Choose a **genre**:", options, selection_mode="multi")
    genres_random = right.pills("", ["Random "], selection_mode="single")

# Genre Selection (single selection only)
with st.container(border=True):
    left, right = st.columns(2, vertical_alignment="center")
    options = ["Pop", "Rock", "Country", "Heavy metal"]
    genres = left.pills("Choose a **genre**:", options, selection_mode="single")
    genres_random = right.pills("", ["Random"], selection_mode="single")



# Emotions Selection (single selection only)
with st.container(border=True):
    left, right = st.columns(2, vertical_alignment="center")
    options = ["Love", "Sadness", "Rage", "Happiness"]
    emotions = left.pills("Choose a **emotion**:", options, selection_mode="multi")
    emotions_random = right.pills("", ["Random "], selection_mode="single")

cols = st.columns(6, vertical_alignment="center")
if cols[-1].button("Continue"):
    st.switch_page("generate_lyrics.py")
