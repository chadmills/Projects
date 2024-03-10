
# server.py



from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/EmotionDetector', methods=['POST'])
def emotion_detector_route():
    data = request.get_json()
    text = data.get('text', '')
    result = emotion_detector(text)
    
    response_text = f"For the given statement, the system response is "
    for emotion, score in result.items():
        if emotion != 'dominant_emotion':
            response_text += f"'{emotion}': {score}, "
    response_text += f"and the dominant emotion is {result['dominant_emotion']}."
    
    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(debug=True)
