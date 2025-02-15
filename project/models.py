from django.db import models

# Create your models here.
class Details(models.Model):
    NAME=models.CharField(max_length=20)
    PHONE=models.IntegerField()
    EMAIL=models.CharField(max_length=20)
    USERNAME=models.CharField(max_length=20)
    PASSWORD=models.CharField(max_length=20)