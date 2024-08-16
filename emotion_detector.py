import requests
from requests.auth import HTTPBasicAuth
import json

def emotion_detector(text_to_analyze):
    # IBM Watson NLU API credentials and endpoint
    url = 'https://api.your-region.natural-language-understanding.watson.cloud.ibm.com/instances/your-instance-id/v1/analyze?version=2021-08-01'
    api_key = 'your_api_key_here'
    
    # Setting up the request headers and parameters
    headers = {"Content-Type": "application/json"}
    data = {
        "text": text_to_analyze,
        "features": {
            "emotion": {}
        }
    }

    # Making the POST request to the Watson NLU API
    response = requests.post(url, json=data, headers=headers, auth=HTTPBasicAuth('apikey', api_key))
    
    # Checking if the request was successful
    if response.status_code == 200:
        json_response = response.json()
        emotion_scores = json_response['emotion']['document']['emotion']
        
        # Determining the dominant emotion
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        emotion_scores['dominant_emotion'] = dominant_emotion
        
        return emotion_scores
    else:
        # Handle errors
        print(f"Error: {response.status_code}, {response.text}")
        return None

# Example usage:
text = "I'm feeling really happy today!"
result = emotion_detector(text)
if result:
    print(result)
