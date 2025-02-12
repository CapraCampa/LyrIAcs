import streamlit as st
import asyncio
import httpx

# Asynchronous function to call the genre predictor
async def call_genre_predictor(api_url: str, text: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(api_url, json={"text": text})
            response.raise_for_status()  # Raise exception for non-2xx responses
            return response.json()
        except httpx.RequestError as exc:
            return {"error": f"An error occurred while requesting: {exc}"}
        except httpx.HTTPStatusError as exc:
            return {"error": f"Non-success status code {exc.response.status_code}: {exc.response.text}"}

# Asynchronous function to call the sentiment analyzer
async def call_sentiment_analyzer(api_url: str, text: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(api_url, json={"text": text})
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as exc:
            return {"error": f"An error occurred while requesting: {exc}"}
        except httpx.HTTPStatusError as exc:
            return {"error": f"Non-success status code {exc.response.status_code}: {exc.response.text}"}


# Main function to handle parallel API calls
async def get_predictions(text: str):
    # Define model API endpoints
    genre_predictor_url = "http://localhost:8080/predict_genre_endpoint"  # Replace with actual URL
    sentiment_analyzer_url = "http://localhost:8081/predict_emotion_endpoint"  # Replace with actual URL

    # Send requests in parallel
    results = await asyncio.gather(
        call_genre_predictor(genre_predictor_url, text),
        call_sentiment_analyzer(sentiment_analyzer_url, text),
    )

    # Unpack results
    genres, emotions = results
    return genres, emotions



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

    # Error management
    if not user_lyrics:
        st.warning("Please enter some text before submitting.")

    else:
        if user_lyrics.strip():

            # Save input
            st.session_state.first_chunks = user_lyrics

            # Run the predictions asynchronously
            with st.spinner("Processing..."):
                genres, emotions = asyncio.run(get_predictions(user_lyrics))
            
            # Check for errors in API responses
            if "error" in genres:
                st.error(f"Genre Predictor Error: {genres['error']}")
            else:
                st.session_state.genres = genres.get('prediction', "No prediction available")

            if "error" in emotions:
                st.error(f"Emotion Analyzer Error: {emotions['error']}")
            else:
                st.session_state.emotions = emotions.get('prediction', "No prediction available")

            st.switch_page("feature_selection.py")

        else:
            st.warning("Please enter text for prediction.")
