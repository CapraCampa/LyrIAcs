import unittest
from unittest.mock import patch, MagicMock
import streamlit as st
import importlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src", "web")))
import feature_selection

class TestFeatureSelection(unittest.TestCase):

    @patch("streamlit.markdown")
    @patch("streamlit.warning")
    @patch("streamlit.write")
    @patch("streamlit.container")
    @patch("streamlit.columns")
    @patch("streamlit.switch_page")
    def test_feature_selection(self, mock_switch_page, mock_columns, mock_container, mock_write, mock_warning, mock_markdown):
        # Set the session state correctly before running the script
        st.session_state.user_lyrics = "sample lyrics"
        st.session_state.current_chunks = "sample lyrics"
        st.session_state.genres = ["Rock", "Pop", "Jazz"]
        st.session_state.emotions = ["Happy", "Sad", "Angry"]

        # Mock the container and columns to avoid UI interaction
        mock_container.return_value = MagicMock()
        mock_columns.return_value = [MagicMock() for _ in range(2)]

        # Reload the script after setting the session state
        importlib.reload(feature_selection)

        # Ensure the warning is not triggered
        mock_warning.assert_not_called()

        # Simulate the button click and ensure page switch
        mock_columns.return_value[-1].button.return_value = True
        importlib.reload(feature_selection)
        mock_switch_page.assert_called_with("generate_lyrics.py")

    @patch("streamlit.warning")
    def test_no_lyrics_warning(self, mock_warning):
        # Clear session state to simulate missing lyrics
        st.session_state.clear()
        st.session_state.genres = ["Rock", "Pop", "Jazz"]
        st.session_state.emotions = ["Happy", "Sad", "Angry"]


        # Reload the script to trigger the warning
        importlib.reload(feature_selection)

        # Ensure the warning is triggered for missing lyrics
        mock_warning.assert_called_with("No lyrics found. Please go back and input lyrics.")

    @patch("streamlit.warning")
    def test_no_genre_warning(self, mock_warning):
        # Clear session state to simulate missing lyrics
        st.session_state.clear()
        st.session_state.user_lyrics = "sample lyrics"

        # Reload the script to trigger the warning
        importlib.reload(feature_selection)

        # Ensure the warning is triggered for missing lyrics
        mock_warning.assert_called_with("An error occured with your predictions, please go back and input lyrics again.")
        

if __name__ == "__main__":
    unittest.main()