import streamlit as st
import random
import pickle
import pandas as pd

if "current_chunks" not in st.session_state:
    st.session_state.current_chunks = ""

# Logo
cols = st.columns([1, 5, 1], gap="large", vertical_alignment="center")
cols[1].image("src/web/images/logo_black.png", width=450)

# Title
st.markdown(f"""
    <p style='text-align: center;'>Select your preferences</p>
""", unsafe_allow_html=True)


if 'user_lyrics' in st.session_state:
    user_lyrics = st.session_state.user_lyrics
else:
    st.warning("No lyrics found. Please go back and input lyrics.")


if (not isinstance(st.session_state.get("genres"), list) or len(st.session_state.get("genres", [])) != 3 or
    not isinstance(st.session_state.get("emotions"), list) or len(st.session_state.get("emotions", [])) != 3):
     st.warning("An error occured with your predictions, please go back and input lyrics again.")
else:
    # Genre Selection (single selection only)
    with st.container(border=True):
        left, right= st.columns(2, vertical_alignment="center")
        genre = left.pills("Choose a **genre**:", st.session_state.genres + ["Random"], selection_mode="single",  key="genre_selection")


    # Emotions Selection (single selection only)
    with st.container(border=True):
        left, right= st.columns(2, vertical_alignment="center")
        emotion = left.pills("Choose a **emotion**:", st.session_state.emotions + ["Random"], selection_mode="single",  key="emotion_selection")

    # Continue
    cols = st.columns(5, vertical_alignment="center")
    if cols[-1].button("Continue \u2192"):
        if genre == "Random":
            st.session_state.genre = random.choice(['Rock', 'Metal', 'Pop', 'Indie', 'Folk', 'Electronic', 'R&B', 'Jazz', 'Hip-Hop', 'Country'])
        else:
            st.session_state.genre = genre
        if emotion == "Random":
            st.session_state.emotion = random.choice(['Fear', 'Sad', 'Love', 'Joy', 'Surprise', 'Anger'])
        else:
            st.session_state.emotion = emotion
        st.switch_page("generate_lyrics.py")

    # Back
    if cols[0].button("\u21A9 Back"):
        st.switch_page("input_lyrics.py")
