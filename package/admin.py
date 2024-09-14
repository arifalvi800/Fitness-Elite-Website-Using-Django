from django.contrib import admin
from package.models import Package
# Register your models here.
class PackageData(admin.ModelAdmin):
    list_display=['package_type','package_price',]
admin.site.register(Package,PackageData)    