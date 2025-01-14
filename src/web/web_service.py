import streamlit as st


# Page configuration
st.set_page_config(
    page_title="LyrIAcs",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Page navigation
pg = st.navigation([st.Page("input_lyrics.py"), st.Page("feature_selection.py")], position="hidden")

# CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_css("styles.css")


pg.run()
