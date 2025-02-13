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


def predict_genre(text, model_genre):
    predicted_probs = model_genre.predict_proba([text])
    top_three_indices = predicted_probs[0].argsort()[::-1][:3]
    predicted_genres = model_genre.classes_[top_three_indices]
    return predicted_genres.tolist()

def predict_emotion(text, model_emotion):
    predicted_probs = model_emotion.predict_proba([text])
    top_three_indices = predicted_probs[0].argsort()[::-1][:3]
    predicted_emotions = model_emotion.classes_[top_three_indices]
    return predicted_emotions.tolist()


# Logo
cols = st.columns([1, 5, 1], gap="large", vertical_alignment="center")
cols[1].image("src/web/images/logo_black.png", width=450)

# Title
st.markdown(f"""
    <p style='text-align: center;'>Input your lyrics</p>
""", unsafe_allow_html=True)

# Text area
user_lyrics = st.text_area(
    label="input_lyrics_area",
    height=200,
    placeholder="Never gonna give you up, never gonna let you down...",
    label_visibility="hidden"
)

if user_lyrics:
    st.session_state.user_lyrics = user_lyrics


# Submit button
cols = st.columns(5, vertical_alignment="center")
if cols[-1].button("Submit \u2192"):

    # Error management
    if not user_lyrics:
        st.warning("Please enter some text before submitting.")
        
    else:
        if user_lyrics.strip():

            # Save input
            st.session_state.first_chunks = user_lyrics

            # Run the predictions
            with st.spinner("Processing..."):
                model_genre, model_emotion = load_models()
                genres = predict_genre(user_lyrics,model_genre)
                emotions = predict_emotion(user_lyrics,model_emotion)
            
            # Check for errors in model predictions
            if "error" in genres:
                st.error(f"Genre Predictor Error")
            else:
                st.session_state.genres = genres

            if "error" in emotions:
                st.error(f"Emotion Analyzer Error")
            else:
                st.session_state.emotions = emotions

            st.session_state.current_chunks = user_lyrics
            st.switch_page("feature_selection.py")

        else:
            st.warning("Please enter text for prediction.")

