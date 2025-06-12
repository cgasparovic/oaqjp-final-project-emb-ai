''' 
Emotion Detection Server
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

# Define Default Route
@app.route("/")
def render_index_page():
    """
    Function to return the default index page
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_route():
    '''
    This function processes the text for emotion detection
    and returns the result in the specified format.
    '''
    # Get the text to be analyzed
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion detection function
    response = emotion_detector(text_to_analyze)

    # For status_code = 400, make the function return the
    # same dictionary, but with values for all keys being None.
    if response['dominant_emotion'] == 'None':
        return "Invalid text! Please try again."

    # Format the output as requested
    output_string = f"For the given statement, the system response is 'anger':\
    {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']},\
    'joy': {response['joy']} and 'sadness': {response['sadness']}.\
    The dominant emotion is <b>{response['dominant_emotion']}</b>."

    return output_string

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
