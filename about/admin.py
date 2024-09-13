from django.contrib import admin
from about.models import About
# Register your models here.
class AboutData(admin.ModelAdmin):
    list_display=['about_heading']
admin.site.register(About,AboutData)    