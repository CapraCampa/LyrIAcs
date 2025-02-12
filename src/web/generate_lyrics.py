import streamlit as st
from llama_connection.api_llama import ask_llama


# First LLM call
if "new_chunks" not in st.session_state:
    st.session_state.new_chunks = ask_llama(st.session_state.current_chunks, st.session_state.genre, st.session_state.emotion)

# Logo
cols = st.columns([1, 5, 1], gap="large", vertical_alignment="center")
cols[1].image("images/logo_black.png", width=450)

left, right = st.columns(2, gap="medium", vertical_alignment="center")


# Current chunks
left.markdown("""
    <p style='text-align: center;'>Your lyrics up to now</p>
""", unsafe_allow_html=True)

current_chunks_area = left.text_area(
    label="current_chunks",
    value=st.session_state.current_chunks,
    height=300,
    label_visibility="hidden",
    disabled=True
)

# New chunks
right.markdown("""
    <p style='text-align: center;'>New stanza</p>
""", unsafe_allow_html=True)

new_chunks_area = right.text_area(
    label="new_chunks",
    value=st.session_state.new_chunks,
    height=300,
    label_visibility="hidden",
)

buttons_left = left.columns(2, gap="medium", vertical_alignment="center")
buttons_right = right.columns(2, gap="medium", vertical_alignment="center")

# Back
if buttons_left[0].button("\u21A9 Back"):
    del st.session_state["new_chunks"]
    st.session_state.current_chunks = st.session_state.first_chunks
    st.switch_page("feature_selection.py")

# Add
if buttons_left[1].button("\uFF0B Add"):
    st.session_state.current_chunks =  st.session_state.current_chunks +  "\n\n" + new_chunks_area
    st.rerun()

# Re-generate
if buttons_right[0].button("\u21BB Re-generate"):
    st.session_state.new_chunks = ask_llama(st.session_state.current_chunks, st.session_state.genre, st.session_state.emotion)
    st.rerun()

# End generation
if buttons_right[1].button("Save \u2192"):
    st.switch_page("export_lyrics.py")


st.write(f"Genre: {st.session_state.genre}")
st.write(f"Emotion: {st.session_state.emotion}")
