import streamlit as st

if "current_chunks" not in st.session_state:
    st.session_state.current_chunks = ""

if "new_chunks" not in st.session_state:
    st.session_state.new_chunks = "Arrivederci"

# Title
st.markdown("""
    <h1 style='text-align: center;'>LyrIAcs</h1>
""", unsafe_allow_html=True)

left, right = st.columns(2, gap="medium", vertical_alignment="center")


# Current chunks
left.markdown("""
    <p style='text-align: center;'>Your lyrics up to now</p>
""", unsafe_allow_html=True)

current_chunks = left.text_area(
    label="current_chunks",
    value=st.session_state.current_chunks,
    height=250,
    label_visibility="hidden",
    disabled=True
)

if left.button("Save"):
    pass

# New chunks
right.markdown("""
    <p style='text-align: center;'>New chunk</p>
""", unsafe_allow_html=True)

# Here it should be implemented the call to the LLM
st.session_state.new_chunks = "Arrivederci"

new_chunks = right.text_area(
    label="new_chunks",
    value=st.session_state.new_chunks,
    height=250,
    label_visibility="hidden",
    disabled=True
)

buttons = right.columns(2, gap="large", vertical_alignment="center")
if buttons[0].button("Re-generate"):
    pass
if buttons[1].button("Add"):
    st.session_state.current_chunks = st.session_state.current_chunks + "\n" + st.session_state.new_chunks
    st.rerun()