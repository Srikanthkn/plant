from dataclasses import fields
from django.db import models

# Create your models here.
class userlogin(models.Model):
     firstname=models.CharField(max_length=50)
     lastname=models.CharField(max_length=50)
     mobilenumber=models.CharField(max_length=10)
     username = models.CharField(max_length=12)
     password = models.IntegerField()