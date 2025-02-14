import requests
import unittest

class TestAppHealth(unittest.TestCase):

    def health_check(self, url):
        try:
            response = requests.get(url)
            self.assertEqual(response.status_code, 200, f"Health check failed for {url} with status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.fail(f"Error during health check for {url}: {e}")

    def test_streamlit_health(self):
        url = "https://lyriacs-web.onrender.com"
        self.health_check(url)

    def test_emotion_api(self):
        api_url_emotion = "https://lyriacs-api-emotion.onrender.com/health"
        data = {"text": "I am feeling great!"}
        try:
            response = requests.get(api_url_emotion, json=data)
            self.assertEqual(response.status_code, 200, f"Emotion API failed with status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.fail(f"Error during emotion API test: {e}")

    def test_genre_api(self):
        api_url_genre = "https://lyriacs-api-genre.onrender.com/health"
        data = {"text": "Some song lyrics"}
        try:
            response = requests.get(api_url_genre, json=data)
            self.assertEqual(response.status_code, 200, f"Genre API failed with status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.fail(f"Error during genre API test: {e}")

if __name__ == "__main__":
    unittest.main()