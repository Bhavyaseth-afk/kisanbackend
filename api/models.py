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
    helplineno=models.IntegerField()

class Crops(models.Model):
    cropname=models.CharField(max_length=20)
    description=models.TextField()
    season = models.CharField(max_length=40)
    price = models.IntegerField()
    cropimg = models.TextField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.croptrust.org%2Fabout-us%2F&psig=AOvVaw1FZqITIQTLx14SxhLQIRDS&ust=1649005670360000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCIjl1Pvu9fYCFQAAAAAdAAAAABAD')
    

class FarmingTech(models.Model):
    techname=models.CharField(max_length=40)
    techdes = models.TextField()
    techimg= models.TextField(default="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.alimentarium.org%2Fen%2Ffact-sheet%2Farable-farming-techniques&psig=AOvVaw38P2DborETGsZ23i8otB8i&ust=1649005701555000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCKC0hYzv9fYCFQAAAAAdAAAAABAD")
    