from django.db import models

# Create your models here.
class SentimentAnalysis(models.Model):
    review = models.CharField(max_length=500)
    label = models.CharField(max_length=10)

