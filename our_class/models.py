from django.db import models

# Create your models here.
class Class(models.Model):
    img=models.FileField(upload_to='about/',max_length=250, default="", blank=True, null=True)
class Class_Type(models.Model):
    class_type=models.CharField(max_length=100,default="")
    class_price=models.CharField(max_length=100,default="")
    class_des=models.TextField()
    class_type_img=models.FileField(upload_to='about/',max_length=250, default="", blank=True, null=True)    