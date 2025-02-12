import streamlit as st
import joblib
import numpy as np

# Cache model loading to improve efficiency
@st.cache_resource
def load_models():
    genre_model_path = "artifacts/genre/model_genre.pkl"
    emotion_model_path = "artifacts/emotion/model_emotion.pkl"
    
    model_genre = joblib.load(genre_model_path)
    model_emotion = joblib.load(emotion_model_path)
    return model_genre, model_emotion


def predict_genre(text):
    predicted_probs = model_genre.predict_proba([text])
    top_three_indices = predicted_probs[0].argsort()[::-1][:3]
    predicted_genres = model_genre.classes_[top_three_indices]
    return predicted_genres.tolist()

def predict_emotion(text):
    predicted_probs = model_emotion.predict_proba([text])
    top_three_indices = predicted_probs[0].argsort()[::-1][:3]
    predicted_emotions = model_emotion.classes_[top_three_indices]
    return predicted_emotions.tolist()

# Title
st.markdown("""
    <h1 style='text-align: center;'>LyrIAcs</h1>
    <p style='text-align: center;'>Input your lyrics</p>
""", unsafe_allow_html=True)

# Text area
user_lyrics = st.text_area(
    label="input_lyrics",
    height=200,
    placeholder="Never gonna give you up, never gonna let you down...",
    label_visibility="hidden"
)

if user_lyrics:
    st.session_state.user_lyrics = user_lyrics

# Submit button
if st.button("Submit"):
    if not user_lyrics.strip():
        st.warning("Please enter some text before submitting.")
    else:
        st.session_state.current_chunks = user_lyrics
        with st.spinner("Processing..."):
            # Load models only once
            model_genre, model_emotion = load_models()
            st.session_state.genres = predict_genre(user_lyrics)
            st.session_state.emotions = predict_emotion(user_lyrics)
        
        st.switch_page("feature_selection.py")
