import requests
import json

def emotion_detector(text_to_analyze):
    myobj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, headers = headers, json = myobj)

    dic = json.loads(response.text)

    anger = dic["emotionPredictions"][0]["emotion"]["anger"]
    disgust = dic["emotionPredictions"][0]["emotion"]["disgust"]
    fear = dic["emotionPredictions"][0]["emotion"]["fear"]
    joy = dic["emotionPredictions"][0]["emotion"]["joy"]
    sadness = dic["emotionPredictions"][0]["emotion"]["sadness"]

    emotion_scores = {
    "anger": anger,
    "disgust": disgust,
    "fear": fear,
    "joy": joy,
    "sadness": sadness
    }

    dominant_emotion = max(emotion_scores, key = emotion_scores.get)

    return_dict = {
    "anger": anger,
    "disgust": disgust,
    "fear": fear,
    "joy": joy,
    "sadness": sadness,
    "dominant_emotion": dominant_emotion
    }

    return return_dict





