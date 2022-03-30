from django.contrib import admin
from .models import *
@admin.register(Kisan)
class KisanAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'number']

admin.site.register(Retailer)
admin.site.register(GovernmentScheme)
admin.site.register(Crops)
admin.site.register(FarmingTech)
