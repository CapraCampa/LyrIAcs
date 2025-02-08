import streamlit as st

# Title
st.markdown("""
    <h1 style='text-align: center;'>LyrIAcs</h1>
    <p style='text-align: center;'>Input your lyrics</p>
""", unsafe_allow_html=True)

# Text area
#TODO: max_chars
user_lyrics = st.text_area(
    label="input_lyrics",
    height=200,
    placeholder="Never gonna give you up, never gonna let you down...",
    label_visibility="hidden"
)

if user_lyrics:
    st.session_state.user_lyrics = user_lyrics

# Submit button
if st.button("Submit"):

    # Error management
    if not user_lyrics:
        st.warning("Please enter some text before submitting.")

    else:
        st.switch_page("feature_selection.py")