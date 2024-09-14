from django.db import models

# Create your models here.
class Training(models.Model):
    training_heading=models.CharField(max_length=100,default="")
    training_des=models.TextField()
    training_img=models.FileField(upload_to='about/',max_length=250, default="", blank=True, null=True) 