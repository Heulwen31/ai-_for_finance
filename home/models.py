from pyexpat import model
from django.db import models

# Create your models here.
class SetimentAnalysis(models.Model):
    review = models.CharField(max_length=500)
    label = model.CharField(max_length=10)

