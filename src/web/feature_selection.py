import streamlit as st

st.write(f"Input: {st.session_state.first_chunks}")
st.write(f"Emotions: {st.session_state.emotions}")
st.write(f"Genres: {st.session_state.genres}")


# Title
st.markdown("""
    <h1 style='text-align: center;'>LyrIAcs</h1>
    <p style='text-align: center;'>Select your preferences</p>
""", unsafe_allow_html=True)


# Genre Selection (single selection only)
with st.container(border=True):
    left, right = st.columns(2, vertical_alignment="center")
    genres = left.pills("Choose a **genre**:", st.session_state.genres, selection_mode="single")
    genres_random = right.pills("", ["Random"], selection_mode="single")


# Emotions Selection (single selection only)
with st.container(border=True):
    left, right = st.columns(2, vertical_alignment="center")
    options = ["Love", "Sadness", "Rage", "Happiness"]
    emotions = left.pills("Choose a **emotion**:", options, selection_mode="multi")
    emotions_random = right.pills("", ["Random "], selection_mode="single")


cols = st.columns(6, vertical_alignment="center")
if cols[-1].button("Continue"):
    st.switch_page("generate_lyrics.py")
