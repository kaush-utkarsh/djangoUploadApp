from django.db import models

# Create your models here.

class User_Details(models.Model):
    userid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512,null=True,blank=True)
    email = models.CharField(max_length=512,null=True,blank=True)
    username = models.CharField(max_length=512,null=True,blank=True)
    password = models.CharField(max_length=512,null=True,blank=True)
