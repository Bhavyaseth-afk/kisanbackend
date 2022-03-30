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
    