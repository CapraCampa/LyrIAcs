import streamlit as st


# Title
st.markdown("""
    <h1 style='text-align: center;'>LyrIAcs</h1>
    <p style='text-align: center;'>Select your preferences</p>
""", unsafe_allow_html=True)

# Genre Selection (single selection only)
with st.container(border=True):
    left, right = st.columns(2, vertical_alignment="center")
    options = ["Pop", "Rock", "Country", "Heavy metal"]
    genres = left.pills("Choose a **genre**:", options, selection_mode="single")
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
