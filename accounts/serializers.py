from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User



class RegisterSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(
            max_length=30
            )
    number = serializers.IntegerField(
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    
    
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['number'])
        return user

    class Meta:
        model=User
        fields=('username','number')
        
       