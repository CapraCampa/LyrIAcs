import streamlit as st


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
    genres = left.pills("Choose a **genre**:", st.session_state.genres, selection_mode="single",  key="genre_selection")
    genres_random = right.pills("random_genre_pill", ["Random"], selection_mode="single",  key="genre_random", label_visibility="hidden")


# Emotions Selection (single selection only)
with st.container(border=True):
    left, right = st.columns(2, vertical_alignment="center")
    emotion = left.pills("Choose a **emotion**:", st.session_state.emotions, selection_mode="single",  key="emotion_selection")
    emotion_random = right.pills("random_emotion_pill", ["Random "], selection_mode="single",  key="emotion_random", label_visibility="hidden")


# Continue
cols = st.columns(5, vertical_alignment="center")
if cols[-1].button("Continue \u2192"):
    st.session_state.genre = genres
    st.session_state.emotion = emotion
    st.switch_page("generate_lyrics.py")

# Back
if cols[0].button("\u21A9 Back"):
    st.switch_page("input_lyrics.py")
