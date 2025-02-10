import streamlit as st


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
    value="Ciao",
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

current_chunks = right.text_area(
    label="current_chunks",
    value="Arrivederci",
    height=250,
    label_visibility="hidden",
)

buttons = right.columns(2, gap="large", vertical_alignment="center")
if buttons[0].button("Re-generate"):
    pass
if buttons[1].button("Add"):
    pass