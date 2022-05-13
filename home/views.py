from django.shortcuts import redirect, render
from joblib import load

from home.models import SentimentAnalysis

# Create your views here.
# load model
model = load('model\model.joblib')

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