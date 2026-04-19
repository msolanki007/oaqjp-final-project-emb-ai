import requests, json

def emotion_detector(text_to_analyze):
    '''This method is developend for emotion detection.
    '''
    #URL for emotion analysys.
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    #Setting up headers
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    #creating dictionary with the text to detect the emotion
    myobj = { "raw_document": { "text": text_to_analyze } } 

    response = requests.post(url, json=myobj, headers=header)
    
    if response.status_code == 200:

        formatted_response = json.loads(response.text)
        emotion_dict = formatted_response['emotionPredictions'][0]['emotion']
        first_val = list(emotion_dict.values())[0]
        dominant_emotion = ''
        for value in emotion_dict.values():
            if value > first_val:
                first_val = value
        for key in emotion_dict:
            if emotion_dict[key] == first_val:
                dominant_emotion = key
        emotion_dict.update({'dominant_emotion': dominant_emotion })
        return emotion_dict
    
    elif response.status_code == 400:
        emotion_dict = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
        return emotion_dict
    else:
        return None

        