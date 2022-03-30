from django.urls import path , include
from api import views
urlpatterns = [
    path('kisan/' , views.KisanList.as_view()) ,
    path('retailer/' , views.RetailerList.as_view()) ,
    path('schemes/' , views.GoverSchemeList.as_view()) ,
    path('crops/' , views.CropList.as_view()) ,
    path('farmtech/' , views.FarmTechList.as_view()) ,
    
]
