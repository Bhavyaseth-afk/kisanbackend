from django.urls import path , include
from api import views
urlpatterns = [
    path('kisan/' , views.KisanList.as_view()) ,
    path('retailer/' , views.RetailerList.as_view()) ,
    
]
