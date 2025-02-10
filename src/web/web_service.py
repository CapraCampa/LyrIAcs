import streamlit as st


# Page configuration
st.set_page_config(
    page_title="LyrIAcs",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Page navigation
pg = st.navigation([st.Page("input_lyrics.py"), st.Page("feature_selection.py"), st.Page("generate_lyrics.py")], position="hidden")

# CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("src/web/styles.css")


pg.run()
