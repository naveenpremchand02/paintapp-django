from django.db import models

# Create your models here.
class Data(models.Model):
	name=models.CharField(max_length=60)
	wholedata=models.CharField(max_length=1000000)
