from pyexpat import model
from attr import field, fields
from rest_framework import serializers
from .models  import *

class KisanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Kisan
        fields=['id','name','number']
        
        
class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Retailer
        fields=['retname', 'address','phnumber','list_items']
    
class GovernmentSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model=GovernmentScheme
        fields='__all__'
        
class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crops
        fields='__all__'
        
class FarmingTechSerializer(serializers.ModelSerializer):
    class Meta:
        model= FarmingTech
        fields='__all__'