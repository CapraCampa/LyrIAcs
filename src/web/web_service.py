import streamlit as st
import argparse

# Page configuration
st.set_page_config(
    page_title="LyrIAcs",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Page navigation
pg = st.navigation([st.Page("input_lyrics.py"), st.Page("feature_selection.py"), st.Page("generate_lyrics.py"), st.Page("export_lyrics.py"), st.Page("health.py")], position="hidden")

# Model location
parser = argparse.ArgumentParser()
parser.add_argument("--genre", type=str, default="http://127.0.0.1:8080/predict_genre_endpoint")
parser.add_argument("--emotion", type=str, default="http://127.0.0.1:8081/predict_emotion_endpoint")
parser.add_argument("--key", type=str, default=None)
args = parser.parse_args()
st.session_state.genre_path = args.genre
st.session_state.emotion_path = args.emotion
st.session_state.key = args.key
st.session_state.args = 4

# CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("styles.css")


pg.run()
