from django.db import models

# Create your models here.
class Bank(models.Model):
	ifsc = models.CharField(max_length=16)
	bank_id = models.IntegerField()
	branch = models.CharField(max_length=30)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=30)
	district = models.CharField(max_length=30)
	state = models.CharField(max_length=30)
	bank_name = models.CharField(max_length=200)