import streamlit as st
import random


# Logo
cols = st.columns([1, 5, 1], gap="large", vertical_alignment="center")
cols[1].image("images/logo_black.png", width=450)

# Title
st.markdown(f"""
    <p style='text-align: center;'>Select your preferences</p>
""", unsafe_allow_html=True)


# Genre Selection (single selection only)
with st.container(border=True):
    left, right = st.columns(2, vertical_alignment="center")
    genre = left.pills("Choose a **genre**:", st.session_state.genres + ["Random"], selection_mode="single",  key="genre_selection")


# Emotions Selection (single selection only)
with st.container(border=True):
    left, right = st.columns(2, vertical_alignment="center")
    emotion = left.pills("Choose a **emotion**:", st.session_state.emotions + ["Random"], selection_mode="single",  key="emotion_selection")


# Continue
cols = st.columns(5, vertical_alignment="center")
if cols[-1].button("Continue \u2192"):
    if genre == None:
        st.warning("Select a genre.")
    elif emotion == None:
        st.warning("Select an emotion.")
    else:
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

