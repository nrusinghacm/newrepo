from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    res_id=models.IntegerField()
    #name = models.CharField(max_length=500)
    address=models.CharField(max_length=500)
    locality=models.CharField(max_length=500)
    city=models.CharField(max_length=500)

    def __str__(self):
        return self.city
