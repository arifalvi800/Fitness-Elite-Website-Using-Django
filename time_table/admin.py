from django.contrib import admin
from time_table.models import Table
# Register your models here.
class TableData(admin.ModelAdmin):
    list_display=['day','timing','duration','room_no']
admin.site.register(Table,TableData)    