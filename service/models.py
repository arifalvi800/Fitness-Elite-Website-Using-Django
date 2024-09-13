from django.db import models

# Create your models here.
class Service(models.Model):
    service_des=models.TextField()

class Service_type(models.Model):
    service_type=models.CharField(max_length=100,default="")
    service_type_des=models.TextField()    