from django.db import models

class Subscribe(models.Model):
	id = models.IntegerField(primary_key=True)
	level = models.IntegerField(default = 0)
	