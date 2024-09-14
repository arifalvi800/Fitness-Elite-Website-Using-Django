from django.db import models

# Create your models here.
class Gallery(models.Model):
    gallery_img_1=models.FileField(upload_to='about/',max_length=250, default="", blank=True, null=True)
    gallery_img_2=models.FileField(upload_to='about/',max_length=250, default="", blank=True, null=True)
    