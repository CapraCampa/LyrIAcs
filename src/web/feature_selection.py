import streamlit as st

import pickle
import pandas as pd

if "current_chunks" not in st.session_state:
    st.session_state.current_chunks = ""

# Title
st.markdown("""
    <h1 style='text-align: center;'>LyrIAcs</h1>
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
        left, right = st.columns(2, vertical_alignment="center")
        options = st.session_state.genres
        genres = left.pills("Choose a **genre**:", options, selection_mode="single",  key="genre_selection")
        genres_random = right.pills("", ["Random "], selection_mode="single",  key="genre_random")


    # Emotions Selection (single selection only)
    with st.container(border=True):
        left, right = st.columns(2, vertical_alignment="center")
        options = st.session_state.emotions
        emotions = left.pills("Choose an **emotion**:", options, selection_mode="single",  key="emotion_selection")
        emotions_random = right.pills("", ["Random "], selection_mode="single",  key="emotion_random")

    cols = st.columns(6, vertical_alignment="center")
    if cols[-1].button("Continue"):
        st.switch_page("generate_lyrics.py")
