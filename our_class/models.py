from django.db import models

# Create your models here.
class Class(models.Model):
    img=models.FileField(upload_to='about/',max_length=250, default="", blank=True, null=True)