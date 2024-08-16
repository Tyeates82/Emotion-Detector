import unittest
from unittest.mock import patch
from emotion_detector import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    @patch('emotion_detector.requests.post')
    def test_emotion_detector_success(self, mock_post):
        # Sample response data
        mock_response_data = {
            "emotion": {
                "document": {
                    "emotion": {
                        "anger": 0.01,
                        "disgust": 0.01,
                        "fear": 0.02,
                        "joy": 0.9,
                        "sadness": 0.06
                    }
                }
            }
        }
        # Mocking the requests.post to return the sample response
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response_data
        
        # Call the function
        result = emotion_detector("I'm feeling great today!")
        
        # Expected result
        expected_result = {
            "anger": 0.01,
            "disgust": 0.01,
            "fear": 0.02,
            "joy": 0.9,
            "sadness": 0.06,
            "dominant_emotion": "joy"
        }
        
        # Assertions
        self.assertEqual(result, expected_result)

    @patch('emotion_detector.requests.post')
    def test_emotion_detector_failure(self, mock_post):
        # Mocking the requests.post to simulate an API error
        mock_post.return_value.status_code = 400
        mock_post.return_value.text = "Bad Request"
        
        # Call the function
        result = emotion_detector("I'm feeling great today!")
        
        # Assertions
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
