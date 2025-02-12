import streamlit as st


# Title
st.markdown("""
    <h1 style='text-align: center;'>LyrIAcs</h1>
    <p style='text-align: center;'>Select your preferences</p>
""", unsafe_allow_html=True)


# Genre Selection (single selection only)
with st.container(border=True):
    left, right = st.columns(2, vertical_alignment="center")
    genres = left.pills("Choose a **genre**:", st.session_state.genres, selection_mode="single",  key="genre_selection")
    genres_random = right.pills("", ["Random"], selection_mode="single",  key="genre_random")


# Emotions Selection (single selection only)
with st.container(border=True):
    left, right = st.columns(2, vertical_alignment="center")
    emotions = left.pills("Choose a **emotion**:", st.session_state.emotions, selection_mode="single",  key="emotion_selection")
    emotions_random = right.pills("", ["Random "], selection_mode="single",  key="emotion_random")


cols = st.columns(6, vertical_alignment="center")
if cols[-1].button("Continue"):
    st.switch_page("generate_lyrics.py")
