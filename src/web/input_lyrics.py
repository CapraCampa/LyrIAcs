import streamlit as st
import asyncio
import httpx


MAX_CHARS = 12000

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
    genre_predictor_url = st.session_state.genre_path
    sentiment_analyzer_url = st.session_state.emotion_path

    # Send requests in parallel
    results = await asyncio.gather(
        call_genre_predictor(genre_predictor_url, text),
        call_sentiment_analyzer(sentiment_analyzer_url, text),
    )

    # Unpack results
    genres, emotions = results
    return genres, emotions


def contains_non_utf8(text):
    try:
        text.encode('utf-8')
        return False
    except UnicodeEncodeError:
        return True 
    

# Logo
cols = st.columns([1, 5, 1], gap="large", vertical_alignment="center")
cols[1].image("images/logo_black.png", width=450)

# Title
st.markdown(f"""
    <div style='text-align: center; max-width: 500px; margin: 0 auto; '>
        Can't find new verses for your original song?<br> 
        No worries, input what you have thought until now, and we'll help you continue the lyrics!
    </div>
""", unsafe_allow_html=True)

# Text area
user_lyrics = st.text_area(
    label="input_lyrics_area",
    height=200,
    placeholder="Never gonna give you up, never gonna let you down...",
    label_visibility="hidden"
)


# Submit button
cols = st.columns(5, vertical_alignment="center")
if cols[-1].button("Submit \u2192"):
    # Error management
    if not user_lyrics or not user_lyrics.strip():
        st.warning("Please enter some text before submitting.")

    elif len(user_lyrics) > MAX_CHARS:
        st.warning(f"Song too long. The maximum amount of characters is {MAX_CHARS}.")

    elif contains_non_utf8(user_lyrics):
        st.warning("Only UTF-8 characters are supported.")

    else:
        # Save input
        st.session_state.first_chunks = user_lyrics
        st.session_state.song_chars = len(user_lyrics)

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

        st.session_state.current_chunks = user_lyrics
        st.switch_page("feature_selection.py")


