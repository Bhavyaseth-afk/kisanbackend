from statistics import mode
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
    
class GovernmentScheme(models.Model):
    schemename=models.CharField(max_length=100)
    description= models.TextField()
    datereleased=models.DateField()
    helplineno=models.IntegerField(max_length=10)

class Crops(models.Model):
    cropname=models.CharField(max_length=20)
    description=models.TextField()
    season = models.CharField(max_length=40)
    price = models.IntegerField(max_length=10)
    

class FarmingTech(models.Model):
    techname=models.CharField(max_length=40)
    techdes = models.TextField()
    