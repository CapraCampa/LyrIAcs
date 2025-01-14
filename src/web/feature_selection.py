import streamlit as st

st.write(f"Input: {st.session_state.first_chunks}")
st.write(f"Emotions: {st.session_state.emotions}")
st.write(f"Genres: {st.session_state.genres}")

if st.button("Go to Main Page"):
    st.switch_page("input_lyrics.py")
    