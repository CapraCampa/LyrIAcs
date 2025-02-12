import streamlit as st
from llama_connection.api_llama import ask_llama


# First LLM call
if "new_chunks" not in st.session_state:
    st.session_state.new_chunks = ask_llama(st.session_state.current_chunks, st.session_state.genre, st.session_state.emotion)

    
# Title
st.markdown("""
    <h1 style='text-align: center;'>LyrIAcs</h1>
""", unsafe_allow_html=True)

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

# End generation
if left.button("Save"):
    st.switch_page("export_lyrics.py")

# New chunks
right.markdown("""
    <p style='text-align: center;'>New chunk</p>
""", unsafe_allow_html=True)

new_chunks_area = right.text_area(
    label="new_chunks",
    value=st.session_state.new_chunks,
    height=300,
    label_visibility="hidden",
)

buttons = right.columns(2, gap="large", vertical_alignment="center")

if buttons[0].button("Re-generate"):
    st.session_state.new_chunks = ask_llama(st.session_state.current_chunks, st.session_state.genre, st.session_state.emotion)
    st.rerun()

if buttons[1].button("Add"):
    st.session_state.current_chunks =  st.session_state.current_chunks +  "\n\n" + new_chunks_area
    st.rerun()
