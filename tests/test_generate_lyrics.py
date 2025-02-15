import unittest
from unittest.mock import MagicMock, patch

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'web')))

def mock_streamlit_module(mock_columns, mock_text_area, mock_warning, mock_button, mock_switch_page):
    # Mock session state as an object (not a dict)
        mock_st = MagicMock()
        mock_st.session_state = MagicMock()
        mock_st.session_state.__len__.return_value = 5
        mock_st.session_state.genres = MagicMock()
        mock_st.session_state.emotions = MagicMock()
        mock_st.session_state.new_chunks = MagicMock()
        mock_st.session_state.current_chunks = MagicMock()
        mock_st.session_state.song_chars = 100

        columns_1 = [MagicMock(), MagicMock(), MagicMock()]  # First call returns 3 columns
        columns_2 = [MagicMock(), MagicMock()]  # Second call returns 2 columns
        columns_3 = [MagicMock(), MagicMock(), MagicMock(), MagicMock()]  # Third call returns 2 columns
        
        columns_2[0].text_area = mock_text_area
        columns_2[1].text_area = mock_text_area
        columns_3[0].button = mock_button
        columns_3[1].button = mock_button
        columns_3[2].button = mock_button
        columns_3[3].button = mock_button

        mock_columns.side_effect = [
            columns_1,  # First call returns 3 columns
            columns_2,  # Second call returns 2 columns
            columns_3,  # Third call returns 4 columns
        ]

        mock_st.columns = mock_columns
        mock_st.text_area = mock_text_area
        mock_st.warning = mock_warning
        mock_st.switch_page = mock_switch_page
        return mock_st

class TestFeatureSelection(unittest.TestCase):
    
    @patch("streamlit.switch_page")
    @patch("streamlit.columns")
    @patch("streamlit.text_area", side_effect=[["Rock"], ["Happy"]]) 
    @patch("streamlit.warning")
    @patch("streamlit.button", side_effect=[True, False, False, False]) 
    def test_back_button(self, mock_button, mock_warning, mock_text_area, mock_columns, mock_switch_page):
        mock_button.side_effect = [True, False, False, False]
        mock_st = mock_streamlit_module(mock_columns, mock_text_area, mock_warning, mock_button, mock_switch_page)
        
        # Patch sys.modules to inject our mock streamlit
        with patch.dict("sys.modules", {"streamlit": mock_st}), patch("llama_connection.api_llama.ask_llama", return_value="Mocked response"):
            # Simulate the button behavior and the feature selection process
            import generate_lyrics  # Import after patching streamlit

        # Assert that switch_page is called once with the expected page name
        mock_switch_page.assert_called_once_with("feature_selection.py")



    @patch("streamlit.switch_page")
    @patch("streamlit.columns")
    @patch("streamlit.text_area",side_effect = [["First"], ["Second"]]) 
    @patch("streamlit.warning")
    @patch("streamlit.button", side_effect=[False, False, False, True]) 
    def test_save_button(self, mock_button, mock_warning, mock_text_area, mock_columns, mock_switch_page):
        mock_button.side_effect = [False, False, False, True]
        # Mock session state as an object (not a dict)
        mock_st = mock_streamlit_module(mock_columns, mock_text_area, mock_warning, mock_button, mock_switch_page)

        # Patch sys.modules to inject our mock streamlit
        with patch.dict("sys.modules", {"streamlit": mock_st}),patch("llama_connection.api_llama.ask_llama", return_value="Mocked response"):
            # Simulate the button behavior and the feature selection process
            import generate_lyrics  # Import after patching streamlit
        
        # Test warning when emotion is not selected
        mock_switch_page.assert_called_once_with("export_lyrics.py")

    @patch("streamlit.rerun")
    @patch("streamlit.switch_page")
    @patch("streamlit.columns")
    @patch("streamlit.text_area",side_effect = [["First"], ["Second"]]) 
    @patch("streamlit.warning")
    @patch("streamlit.button", side_effect=[False, False, True, False]) 
    def test_generate_new_chunks(self, mock_button, mock_warning, mock_text_area, mock_columns, mock_switch_page, mock_rerun):
        mock_st = mock_streamlit_module(mock_columns, mock_text_area, mock_warning, mock_button, mock_switch_page)
        mock_st.rerun = mock_rerun

        # Patch sys.modules to inject our mock streamlit
        with patch.dict("sys.modules", {"streamlit": mock_st}),patch("llama_connection.api_llama.ask_llama", return_value="Mocked response"):
            # Simulate the button behavior and the feature selection process
            import generate_lyrics  # Import after patching streamlit

        # Test warning when emotion is not selected
        mock_rerun.assert_called_once()


    @patch("streamlit.switch_page")
    @patch("streamlit.columns")
    @patch("streamlit.text_area",side_effect = [["First"], ["Second"]]) 
    @patch("streamlit.warning")
    @patch("streamlit.button", side_effect=[False, False, False, False]) 
    def test_empty_state(self, mock_button, mock_warning, mock_text_area, mock_columns, mock_switch_page):
        mock_st = mock_streamlit_module(mock_columns, mock_text_area, mock_warning, mock_button, mock_switch_page)
        mock_st.session_state.__len__.return_value = 0

        # Patch sys.modules to inject our mock streamlit
        with patch.dict("sys.modules", {"streamlit": mock_st}),patch("llama_connection.api_llama.ask_llama", return_value="Mocked response"):
            # Simulate the button behavior and the feature selection process
            import generate_lyrics  # Import after patching streamlit

        # Test switching when session state empty
        mock_switch_page.assert_called_once_with("input_lyrics.py")

    @patch("streamlit.rerun")
    @patch("streamlit.switch_page")
    @patch("streamlit.columns")
    @patch("streamlit.text_area",side_effect = [["First"], ["Second"]]) 
    @patch("streamlit.warning")
    @patch("streamlit.button", side_effect=[False, True, False, False]) 
    def test_add_button(self, mock_button, mock_warning, mock_text_area, mock_columns, mock_switch_page,mock_rerun):
        mock_st = mock_streamlit_module(mock_columns, mock_text_area, mock_warning, mock_button, mock_switch_page)
        mock_st.rerun = mock_rerun

        # Patch sys.modules to inject our mock streamlit
        with patch.dict("sys.modules", {"streamlit": mock_st}),patch("llama_connection.api_llama.ask_llama", return_value="Mocked response"):
            # Simulate the button behavior and the feature selection process
            import generate_lyrics  # Import after patching streamlit

        # Test warning when emotion is not selected
        mock_rerun.assert_called_once()

if __name__ == "__main__":
    unittest.main()
