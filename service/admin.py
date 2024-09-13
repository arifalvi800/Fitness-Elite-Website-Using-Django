from django.contrib import admin
from service.models import Service
from service.models import Service_type
# Register your models here.
admin.site.register(Service)

class ServiceType(admin.ModelAdmin):
    list_display=['service_type',]
admin.site.register(Service_type,ServiceType)    
    