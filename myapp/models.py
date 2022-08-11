
from platform import mac_ver
from sys import maxsize
from django.db import models
# Create your models here.


class Account(models.Model):
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    date = models.DateField()
    def __str__(self):
        return self.email

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    country = models.CharField(max_length=122)
    date = models.DateField()
    def __str__(self):
        return self.name