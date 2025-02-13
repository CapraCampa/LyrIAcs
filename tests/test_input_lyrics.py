import unittest
from unittest.mock import patch, MagicMock
import numpy as np

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src", "web")))
import input_lyrics

class TestInputLyrics(unittest.TestCase):

    @patch("input_lyrics.joblib.load")
    def test_load_models(self, mock_load):
        # Mock the models
        mock_genre_model = MagicMock()
        mock_emotion_model = MagicMock()
        mock_load.side_effect = [mock_genre_model, mock_emotion_model]

        # Call the function
        model_genre, model_emotion = input_lyrics.load_models()

        # Check if the models were loaded correctly
        mock_load.assert_any_call("artifacts/genre/model_genre.pkl")
        mock_load.assert_any_call("artifacts/emotion/model_emotion.pkl")
        self.assertEqual(model_genre, mock_genre_model)
        self.assertEqual(model_emotion, mock_emotion_model)

    @patch("joblib.load")
    def test_predict_genre(self, mock_load):
        # Mock the model
        mock_model_genre = MagicMock()
        mock_model_genre.predict_proba.return_value = np.array([[0.1, 0.7, 0.2]])
        mock_model_genre.classes_ = np.array(["Rock", "Pop", "Jazz"])

        # Call the function with the mock model
        result = input_lyrics.predict_genre("sample text", mock_model_genre)

        # Check the result
        self.assertEqual(result, ["Pop", "Jazz", "Rock"])

    @patch("joblib.load")
    def test_predict_emotion(self, mock_load):
        # Mock the model
        mock_model_emotion = MagicMock()
        mock_model_emotion.predict_proba.return_value = np.array([[0.3, 0.4, 0.2]])
        mock_model_emotion.classes_ = np.array(["Happy", "Sad", "Angry"])

        # Call the function with the mock model
        result = input_lyrics.predict_emotion("sample text", mock_model_emotion)

        # Check the result
        self.assertEqual(result, ["Sad", "Happy", "Angry"])

if __name__ == "__main__":
    unittest.main()