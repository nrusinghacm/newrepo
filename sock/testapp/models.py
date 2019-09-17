from django.db import models

# Create your models here.
class Gpsdata(models.Model):
    latitude = models.CharField(max_length = 100)
    # longitude = models.CharField(max_length = 100)
    # speed = models.CharField(max_length = 100)
    # altitude = models.CharField(max_length = 100)
    # time = models.CharField(max_length = 100)
    #
    # class Meta:
    #     ordering=('speed',)
    #
    # def __str__(self):
    #     return self.speed
