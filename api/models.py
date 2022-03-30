from django.db import models

# Create your models here.
class Kisan(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField(max_length=10)
    
class Retailer(models.Model):
    retname=models.CharField(max_length=50)
    address=models.TextField()
    phnumber=models.IntegerField(max_length=10)
    list_items=models.TextField()
    