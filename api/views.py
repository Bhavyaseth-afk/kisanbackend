from rest_framework.response import Response
from .models import Crops, FarmingTech, GovernmentScheme, Kisan, Retailer
from .serializers import CropSerializer, FarmingTechSerializer, GovernmentSchemeSerializer, KisanSerializer, RetailerSerializer
from rest_framework.views import APIView
from rest_framework import status




class KisanList(APIView):
    
    def get(self,request,format=None):
        kisan = Kisan.objects.all()
        serializer= KisanSerializer(kisan, many= True)
        return Response(serializer.data,status=200)
    
    def post(self, request,format=None):
        serializer=KisanSerializer(data=request.data)
         
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status.HTTP_201_CREATED) 
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST) 
        
        
    
class RetailerList(APIView):
    queryset=Retailer.objects.all()
    serializer_class= RetailerSerializer

    def get(self,request,format=None):
        retailers=Retailer.objects.all()
        serializer= RetailerSerializer(retailers,many=True)
        return Response(serializer.data)
    
    def post(self, request,format=None):
        serializer=RetailerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status.HTTP_201_CREATED) 
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
          
        
class GoverSchemeList(APIView):
    def get(self,request,format=None):
        schemes = GovernmentScheme.objects.all()
        serializer=GovernmentSchemeSerializer(schemes, many=True)
        return Response(serializer.data)

class CropList(APIView):
    def get(self,request,format=None):
        cropname=Crops.objects.all()
        serializer=CropSerializer(cropname,many=True)
        return Response(serializer.data)

class FarmTechList(APIView):
    def get(self,request, format=None):
        techname=FarmingTech.objects.all()
        serializer= FarmingTechSerializer(techname,many=True)
        return Response(serializer.data)