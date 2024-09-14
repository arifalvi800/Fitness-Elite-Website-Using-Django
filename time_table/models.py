from django.db import models

# Create your models here.
class Table(models.Model):
    day=models.CharField(max_length=15, default="")
    timing=models.TimeField(max_length=15, default="")
    duration=models.IntegerField(max_length=10,default="")
    room_no=models.IntegerField(max_length=10,default="")
    