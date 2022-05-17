from django.shortcuts import redirect, render
from joblib import load

from home.models import SentimentAnalysis


import json 
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder

import colorama 
colorama.init()
from colorama import Fore, Style, Back

import random
import pickle

# chatbot model 
with open("intents.json") as file:
    data = json.load(file)




# Create your views here.
# load model
model = load('model\model.joblib')
conversation = []
# home page
def home(request):
    return render(request, 'home\home.html')


# save commit to database
def save_commit(request):
    review = request.GET['review']
    result = model.predict([review])
    if result == 0:
        result = 'Bad'  
    elif result == 1:
        result = 'Good'
    else:
        result = None
    sentiment = SentimentAnalysis(review=review, label=result)
    sentiment.save()
    return redirect('home')


def response_ans(request):
        # load trained model
    model = keras.models.load_model('chat_model')

    # load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 20

    inp = request.GET['question']

    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),
                                            truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])

    for i in data['intents']:
        if i['tag'] == tag:
            print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL , np.random.choice(i['responses']))
            conversation.append(inp)
            conversation.append(np.random.choice(i['responses']))
            print(conversation)
            return render(request, 'home\home.html', {'response': np.random.choice(i['responses'])})