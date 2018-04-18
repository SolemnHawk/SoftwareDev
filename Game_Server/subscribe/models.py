from django.db import models

class Subscribe(models.Model):
	id = models.CharField(primary_key=True, max_length = 15)
	level = models.IntegerField(default = 0)
	