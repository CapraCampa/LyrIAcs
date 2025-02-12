import streamlit as st

import pickle
import pandas as pd



# Title
st.markdown("""
    <h1 style='text-align: center;'>LyrIAcs</h1>
    <p style='text-align: center;'>Select your preferences</p>
""", unsafe_allow_html=True)


if 'user_lyrics' in st.session_state:
    user_lyrics = st.session_state.user_lyrics
else:
    st.warning("No lyrics found. Please go back and input lyrics.")

st.write(f"Input: {st.session_state.current_chunks}")

# Genre Selection (single selection only)
with st.container(border=True):
    left, right = st.columns(2, vertical_alignment="center")
    options = st.session_state.genres
    genres = left.pills("Choose a **genre**:", options, selection_mode="multi",  key="genre_selection")
    genres_random = right.pills("", ["Random "], selection_mode="single",  key="genre_random")


# Emotions Selection (single selection only)
with st.container(border=True):
    left, right = st.columns(2, vertical_alignment="center")
    options = st.session_state.emotions
    emotions = left.pills("Choose a **emotion**:", options, selection_mode="multi",  key="emotion_selection")
    emotions_random = right.pills("", ["Random "], selection_mode="single",  key="emotion_random")

cols = st.columns(6, vertical_alignment="center")
if cols[-1].button("Continue"):
    st.switch_page("generate_lyrics.py")
