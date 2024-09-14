from django.contrib import admin
from our_class.models import Class
from our_class.models import Class_Type
# Register your models here.
class ClassTypeData(admin.ModelAdmin):
    list_display=['class_type','class_price',]
admin.site.register(Class_Type,ClassTypeData)    
admin.site.register(Class)