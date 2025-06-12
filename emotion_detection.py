'''
Task 2: Create an emotion detection application using Watson NLP library
'''
import requests

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
        # try request with and handle timeouts
        response = requests.post(url, json=myobj, headers=header, timeout=1).text

    except requests.exceptions.Timeout:
        print("\nRequest timed out...loading sample response...\n")

        # Use Sample Response due to local access to IBM NLM APIs
        sample_response_path = 'static/sample_responses/sample_response.txt'
        file_path = sample_response_path

        # Read sample response from file and set local response var
        with open(file_path, 'r', encoding="utf-8") as file:
            response = file.read()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    return response
