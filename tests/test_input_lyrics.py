import unittest
from unittest.mock import MagicMock, AsyncMock, patch
import asyncio
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'web')))

def mock_streamlit_module(mock_button, mock_warning, mock_text_area, mock_columns, mock_switch_page):
     # Mock session state as an object (not a dict)
        mock_st = MagicMock()

        columns_1 = [MagicMock(), MagicMock(), MagicMock()]  
        columns_2 = [MagicMock(), MagicMock(), MagicMock(), MagicMock(), MagicMock()] 
        columns_2[-1].button = mock_button

        mock_columns.side_effect = [
            columns_1,  
            columns_2 
        ]

        mock_st.columns = mock_columns
        mock_st.text_area = mock_text_area
        mock_st.warning = mock_warning
        mock_st.switch_page = mock_switch_page
        return mock_st

class TestInputLyrics(unittest.TestCase):
    
    
    @patch("streamlit.switch_page")
    @patch("streamlit.columns")
    @patch("streamlit.text_area", side_effect=["Hello, world!"]) 
    @patch("streamlit.warning")
    @patch("streamlit.button", side_effect=[True, False]) 
    def test_valid(self, mock_button, mock_warning, mock_text_area, mock_columns, mock_switch_page):

        mock_st = mock_streamlit_module(mock_button, mock_warning, mock_text_area, mock_columns, mock_switch_page)
        

        # Patch sys.modules to inject our mock streamlit
        with patch.dict("sys.modules", {"streamlit": mock_st}):
            # Simulate the button behavior and the feature selection process
            import input_lyrics  # Import after patching streamlit
        
        mock_switch_page.assert_called_once_with("feature_selection.py")
    
    @patch("streamlit.switch_page")
    @patch("streamlit.columns")
    @patch("streamlit.text_area", side_effect=["Hello, world! \udc80"]) 
    @patch("streamlit.warning")
    @patch("streamlit.button", side_effect=[True, False]) 
    def test_contains_non_utf8(self, mock_button, mock_warning, mock_text_area, mock_columns, mock_switch_page):

        mock_st = mock_streamlit_module(mock_button, mock_warning, mock_text_area, mock_columns, mock_switch_page)


        # Patch sys.modules to inject our mock streamlit
        with patch.dict("sys.modules", {"streamlit": mock_st}):
            # Simulate the button behavior and the feature selection process
            import input_lyrics  # Import after patching streamlit
        
        mock_warning.assert_called_with("Only UTF-8 characters are supported.")
    

    @patch("streamlit.switch_page")
    @patch("streamlit.columns")
    @patch("streamlit.text_area", side_effect=["c"*13000]) 
    @patch("streamlit.warning")
    @patch("streamlit.button", side_effect=[True, False]) 
    def test_max_char_limit(self, mock_button, mock_warning, mock_text_area, mock_columns, mock_switch_page):

        mock_st = mock_streamlit_module(mock_button, mock_warning, mock_text_area, mock_columns, mock_switch_page)

        # Patch sys.modules to inject our mock streamlit
        with patch.dict("sys.modules", {"streamlit": mock_st}):
            # Simulate the button behavior and the feature selection process
            import input_lyrics  # Import after patching streamlit
            from input_lyrics import MAX_CHARS
        
        mock_warning.assert_called_with(f"Song too long. The maximum amount of characters is {MAX_CHARS}.")
    

if __name__ == "__main__":
    unittest.main()
