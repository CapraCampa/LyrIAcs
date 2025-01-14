import streamlit as st
import requests

# Title
st.markdown("""
    <h1 style='text-align: center;'>LyrIAcs</h1>
    <p style='text-align: center;'>Input your lyrics</p>
""", unsafe_allow_html=True)

# Text area
#TODO: max_chars
user_lyrics = st.text_area(
    label="input_lyrics",
    height=200,
    placeholder="Never gonna give you up, never gonna let you down...",
    label_visibility="hidden"
)

# Submit button
if st.button("Submit"):

    # Error management
    if not user_lyrics:
        st.warning("Please enter some text before submitting.")

    else:
        if user_lyrics.strip():

            # Save input
            st.session_state.first_chunks = user_lyrics

            # Call the API for sentiment analysis
            response = requests.post(
                "http://127.0.0.1:8080/predict_emotion_endpoint", 
                json={"text": user_lyrics}
            )

            # Display the prediction
            if response.status_code == 200:
                result = response.json()
                st.session_state.emotions = result['prediction']

            # Error
            else:
                st.error("Sentiment analyzer not reached.")


            # Call the API for genre predictor
            response = requests.post(
                "http://127.0.0.1:8080/predict_genre_endpoint", 
                json={"text": user_lyrics}
            )

            # Display the prediction
            if response.status_code == 200:
                result = response.json()
                st.session_state.genres = result['prediction']
                st.write(f"Prediction: {result['prediction']}")

            # Error
            else:
                st.error("Genre predictor not reached.")

        st.switch_page("feature_selection.py")