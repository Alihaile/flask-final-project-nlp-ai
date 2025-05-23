import requests,json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }    
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=myobj, headers=header)
    formated_response = json.loads(response.text)

    dominant_name = None

    if response.status_code == 200:
        anger_score = formated_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formated_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formated_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formated_response['emotionPredictions'][0]['emotion']['joy']
        sadnes_score = formated_response['emotionPredictions'][0]['emotion']['sadness']

        scores_list = [anger_score, disgust_score, fear_score, joy_score, sadnes_score]
        score_names =  {anger_score: 'anger', disgust_score: 'disgust_score', fear_score: 'fear', joy_score: 'joy', 
                    sadnes_score: 'sadness'}
        dominant_emotion = max(scores_list)
        dominant_name = score_names[dominant_emotion]
    
    if response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadnes_score = None

    return {
        'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score,
        'sadness': sadnes_score,'dominant_emotion': dominant_name
        }
    
