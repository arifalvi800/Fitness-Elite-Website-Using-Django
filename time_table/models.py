from django.db import models

# Create your models here.
class Table(models.Model):
    day=models.CharField(max_length=15, default="")
    timing=models.TimeField()
    duration=models.IntegerField()
    room_no=models.IntegerField()
    