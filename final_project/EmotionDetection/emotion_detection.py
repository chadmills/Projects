# emotion_detection.py
import json

def emotion_detector(text_to_analyze):
    # This function runs emotion detection using the appropriate Emotion Detection function
    import requests

    # Define URL, headers, and input json format
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    # Send a POST request to the Emotion Detection function
    response = requests.post(url, json=input_json, headers=headers)

    # Check if 'emotionPredictions' key is present in the response JSON
    response_json = response.json()
    if 'emotionPredictions' in response_json:
        # Extract required emotions and their scores
        emotions = {}
        for prediction in response_json['emotionPredictions']:
            emotion = prediction.get('emotion', {})
            emotions.update(emotion)

        # Find the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        
        # Return the formatted output
        output = {
            'anger': emotions.get('anger', 0),
            'disgust': emotions.get('disgust', 0),
            'fear': emotions.get('fear', 0),
            'joy': emotions.get('joy', 0),
            'sadness': emotions.get('sadness', 0),
            'dominant_emotion': dominant_emotion
        }
        return output
        
    return "No emotion prediction found or couldn't determine the emotion."
