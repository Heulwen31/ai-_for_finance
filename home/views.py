from django.shortcuts import render
from joblib import load

from home.models import SentimentAnalysis

# Create your views here.

model = load('model\model.joblib')
def predictor(request):
    return render(request, 'main.html')

def form_infor(request):
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
    return render(request, 'result.html', {'review': result})