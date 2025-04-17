import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 200:
        result = response.json()
        emotion_scores = result['emotionPredictions'][0]['emotion']
        
        # Find the dominant emotion
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        return {
            "anger": emotion_scores["anger"],
            "disgust": emotion_scores["disgust"],
            "fear": emotion_scores["fear"],
            "joy": emotion_scores["joy"],
            "sadness": emotion_scores["sadness"],
            "dominant_emotion": dominant_emotion
        }
    else:
        return {"error": "API request failed with status code " + str(response.status_code)}
