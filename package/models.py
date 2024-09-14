from django.db import models

# Create your models here.
class Package(models.Model):
    package_type=models.CharField(max_length=100,default="")
    package_price=models.CharField(max_length=100,default="")
    package_facility_1=models.CharField(max_length=100,default="")
    package_facility_2=models.CharField(max_length=100,default="")
    package_facility_3=models.CharField(max_length=100,default="")
    package_facility_4=models.CharField(max_length=100,default="")
    package_facility_5=models.CharField(max_length=100,default="")
    package_img=models.FileField(upload_to='about/',max_length=250, default="", blank=True, null=True)