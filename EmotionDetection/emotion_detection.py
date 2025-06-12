'''
Emotion Detection Module
'''
import requests
from flask import json

def emotion_detector(text_to_analyze):
    '''
    Call the emotion detection service and return response
    '''
    # Define the URL for the emotion detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/' \
    'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }
    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    # Added a timeout for local testing and error handling
    try:
        # try request and set timeout
        response = requests.post(url, json=myobj, headers=header, timeout=2)
        # Parse the response from the API
        formatted_response = json.loads(response.text)

    except requests.exceptions.Timeout:
        # Handle Timeout Exception which may happen in local testing due
        # to permissions to IBM APIs

        print("\nRequest timed out...loading sample response...\n")

        # Use Sample Response due to local access to IBM NLM APIs
        sample_response_path = 'static/sample_responses/sample_response.txt'
        file_path = sample_response_path

        # Read sample response from file and set local response var
        with open(file_path, 'r', encoding="utf-8") as file:
            formatted_response = json.loads(file.read())

    except requests.exceptions.RequestException as e:
       # Handle General Request Exeptions and print exception details
        print(f"An error occurred: {e}")

    # Build Result JSON
    # Get Emotion scores
    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']

    # Determine the dominant emotion from response
    dominant_emotion = get_dominant_emotion_key(formatted_response)

   # Create the formatted output dictionary
    formatted_output = {
        'anger': emotion_scores.get('anger', 0.0),
        'disgust': emotion_scores.get('disgust', 0.0),
        'fear': emotion_scores.get('fear', 0.0),
        'joy': emotion_scores.get('joy', 0.0),
        'sadness': emotion_scores.get('sadness', 0.0),
        'dominant_emotion': dominant_emotion
    }

    return formatted_output

def get_dominant_emotion_key(data):
    """
    Find dominant emotion from response dict & return key
    """
    # Access the first dictionary in the "emotionPredictions" list
    first_prediction_dict = data["emotionPredictions"][0]

    # Access the "emotion" dictionary within the first dictionary
    emotion_data = first_prediction_dict["emotion"]

    # Find the key with the maximum value in the emotion dictionary
    max_emotion_key = max(emotion_data, key=emotion_data.get)

    return max_emotion_key
