from django.contrib import admin
from home.models import Contact
# Register your models here.
class ContactData(admin.ModelAdmin):
    list_display=('name','mobile','email')
admin.site.register(Contact,ContactData)    