from django.db import models

class Inventory(models.Model):
	id = models.AutoField(primary_key=True)
	description = models.CharField(default = "description for ID", max_length = 50)
