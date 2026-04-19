''' this is a server file to created to analize the sebtiment.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    '''this will analyse the text and return the sentiment
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    text1 = "For the given statement, the system response is"
    text2 = f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
    text3 = f"'fear': {response['fear']}, 'joy': {response['joy']} "
    text4 = f"and 'sadness': {response['sadness']}."
    text5 = f"The dominant emotion is {response['dominant_emotion']}."
    return f"{text1} {text2} {text3} {text4} {text5}"

@app.route("/")
def render_index_page():
    '''this will return default index page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
