from django.urls import path , include
from api import views
urlpatterns = [
    path('kisan/' , views.KisanList.as_view(), name='kisan') ,
    path('retailer/' , views.RetailerList.as_view(),name='retailer') ,
    path('schemes/' , views.GoverSchemeList.as_view(),name='schemes') ,
    path('crops/' , views.CropList.as_view(),name='crops') ,
    path('farmtech/' , views.FarmTechList.as_view(),name='farmtech') ,
    
]
