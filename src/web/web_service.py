import streamlit as st


# CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("styles.css")


# Page configuration
pg = st.navigation([st.Page("input_lyrics.py"), st.Page("feature_selection.py")])
pg.run()
