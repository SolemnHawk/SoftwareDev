from django.db import models

# Create your models here.
class Score(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    score = models.IntegerField(default=0)
