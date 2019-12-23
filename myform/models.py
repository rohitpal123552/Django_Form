from django.db import models

# Create your models here.

class Person(models.Model):
	first_name=models.CharField(max_length=20)
	last_name=models.CharField(max_length=20)
	mobile=models.IntegerField()
	email=models.EmailField(max_length=200)
	bio=models.CharField(max_length=500)
