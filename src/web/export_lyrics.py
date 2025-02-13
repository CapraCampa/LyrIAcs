import streamlit as st
import pyperclip


# Logo
cols = st.columns([1, 5, 1], gap="large", vertical_alignment="center")
cols[1].image("src/web/images/logo_black.png", width=450)

# Title
st.markdown(f"""
    <p style='text-align: center;'>Enjoy your song!</p>
""", unsafe_allow_html=True)

left, right = st.columns(2, gap="medium", vertical_alignment="center")

# Final song
final_song= left.text_area(
    label="final_song",
    value=st.session_state.current_chunks,
    height=300,
    label_visibility="hidden",
    disabled=True
)

# Cliboard container
with right.container():
    left_col, right_col = st.columns(2, gap="medium", vertical_alignment="center")
    left_col.write("Copy to clipboard:")
    if right_col.button("Copy"):
        pyperclip.copy(st.session_state.current_chunks)


# Download container
with right.container():
    left_col, right_col = st.columns(2, gap="medium", vertical_alignment="center")
    left_col.write("Download file:")
    right_col.download_button(
        label=".txt",
        data=st.session_state.current_chunks,
        file_name="lyriacs.txt",
        mime="text/plain"
    )
     
# Back
if st.button("\u21A9 Back"):
    st.switch_page("generate_lyrics.py")


