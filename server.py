""" Emotion Detector Module """
from flask import Flask, request,render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def emotion_analyzer():
    """ emotion analyzer page """

    text_to_analyse = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyse)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    result_formated = f"For the given statement, the system response is 'anger': \
    {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, \
    'joy': {result['joy']} and 'sadness': {result['sadness']}. The dominant emotion \
    is {result['dominant_emotion']}."

    return result_formated

@app.route("/")
def render_index_page():
    """ index page """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
