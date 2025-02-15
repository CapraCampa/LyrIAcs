import unittest
from unittest.mock import MagicMock, patch

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'web')))

def mock_streamlit_module(mock_columns, mock_pills, mock_warning, mock_button, mock_switch_page):
    # Mock session state as an object (not a dict)
        mock_st = MagicMock()
        mock_st.session_state = MagicMock()
        mock_st.session_state.__len__.return_value = 5
        mock_st.session_state.genres = MagicMock()
        mock_st.session_state.emotions = MagicMock()

        columns_1 = [MagicMock(), MagicMock(), MagicMock()]  # First call returns 3 columns
        columns_2 = [MagicMock(), MagicMock()]  # Second call returns 2 columns
        columns_3 = [MagicMock(), MagicMock()]  # Third call returns 2 columns
        columns_4 = [MagicMock(), MagicMock(), MagicMock(), MagicMock(), MagicMock()]  # Last call returns 5 columns

        columns_2[0].pills = mock_pills
        columns_3[0].pills = mock_pills
        columns_4[0].button = mock_button
        columns_4[-1].button = mock_button

        mock_columns.side_effect = [
            columns_1,  # First call returns 3 columns
            columns_2,  # Second call returns 2 columns
            columns_3,  # Third call returns 2 columns
            columns_4   # Fourth call returns 5 columns, with mock_button in the last column
        ]

        mock_st.columns = mock_columns
        mock_st.pills = mock_pills
        mock_st.warning = mock_warning
        mock_st.switch_page = mock_switch_page
        return mock_st

class TestFeatureSelection(unittest.TestCase):
    
    @patch("streamlit.switch_page")
    @patch("streamlit.columns")
    @patch("streamlit.pills", side_effect=[["Rock"], ["Happy"]]) 
    @patch("streamlit.warning")
    @patch("streamlit.button", side_effect=[True, False]) 
    def test_feature_selection(self, mock_button, mock_warning, mock_pills, mock_columns, mock_switch_page):
        
        mock_st = mock_streamlit_module(mock_columns, mock_pills, mock_warning, mock_button, mock_switch_page)

        # Patch sys.modules to inject our mock streamlit
        with patch.dict("sys.modules", {"streamlit": mock_st}):
            # Simulate the button behavior and the feature selection process
            import feature_selection  # Import after patching streamlit

        # Assert that switch_page is called once with the expected page name
        mock_switch_page.assert_called_once_with("generate_lyrics.py")



    @patch("streamlit.switch_page")
    @patch("streamlit.columns")
    @patch("streamlit.pills",side_effect = [None, ["Happy"]]) 
    @patch("streamlit.warning")
    @patch("streamlit.button", side_effect=[True, False]) 
    def test_missing_genre(self, mock_button, mock_warning, mock_pills, mock_columns, mock_switch_page):
        # Mock session state as an object (not a dict)
        mock_st = mock_streamlit_module(mock_columns, mock_pills, mock_warning, mock_button, mock_switch_page)

        # Patch sys.modules to inject our mock streamlit
        with patch.dict("sys.modules", {"streamlit": mock_st}):
            # Simulate the button behavior and the feature selection process
            import feature_selection  # Import after patching streamlit
        
        # Test warning when emotion is not selected
        mock_warning.assert_called_with("Select a genre.")


    @patch("streamlit.switch_page")
    @patch("streamlit.columns")
    @patch("streamlit.pills",side_effect = [["Rock"], None]) 
    @patch("streamlit.warning")
    @patch("streamlit.button", side_effect=[True, False]) 
    def test_missing_emotion(self, mock_button, mock_warning, mock_pills, mock_columns, mock_switch_page):
        mock_st = mock_streamlit_module(mock_columns, mock_pills, mock_warning, mock_button, mock_switch_page)

        # Patch sys.modules to inject our mock streamlit
        with patch.dict("sys.modules", {"streamlit": mock_st}):
            # Simulate the button behavior and the feature selection process
            import feature_selection  # Import after patching streamlit

        # Test warning when emotion is not selected
        mock_warning.assert_called_with("Select an emotion.")


    @patch("streamlit.switch_page")
    @patch("streamlit.columns")
    @patch("streamlit.pills",side_effect = [["Rock"], None]) 
    @patch("streamlit.warning")
    @patch("streamlit.button", side_effect=[True, False]) 
    def test_empty_state(self, mock_button, mock_warning, mock_pills, mock_columns, mock_switch_page):
        mock_st = mock_streamlit_module(mock_columns, mock_pills, mock_warning, mock_button, mock_switch_page)
        mock_st.session_state.__len__.return_value = 0

        # Patch sys.modules to inject our mock streamlit
        with patch.dict("sys.modules", {"streamlit": mock_st}):
            # Simulate the button behavior and the feature selection process
            import feature_selection  # Import after patching streamlit

        # Test switching when session state empty
        mock_switch_page.assert_called_once_with("input_lyrics.py")

    @patch("streamlit.switch_page")
    @patch("streamlit.columns")
    @patch("streamlit.pills",side_effect = [["Rock"], None]) 
    @patch("streamlit.warning")
    @patch("streamlit.button", side_effect=[False, True]) 
    def test_back_button(self, mock_button, mock_warning, mock_pills, mock_columns, mock_switch_page):
        mock_st = mock_streamlit_module(mock_columns, mock_pills, mock_warning, mock_button, mock_switch_page)

        # Patch sys.modules to inject our mock streamlit
        with patch.dict("sys.modules", {"streamlit": mock_st}):
            # Simulate the button behavior and the feature selection process
            import feature_selection  # Import after patching streamlit

        # Test switching when session state empty
        mock_switch_page.assert_called_once_with("input_lyrics.py")

if __name__ == "__main__":
    unittest.main()
