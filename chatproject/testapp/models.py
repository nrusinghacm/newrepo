from django.db import models

class Chat1(models.Model):
    text=models.CharField(max_length=255)

class Chat2(models.Model):
    text= models.CharField(max_length=255)
