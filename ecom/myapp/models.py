from django.db import models

# Create your models here.
class UserRegistration(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    Contactnum = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        self.name
class UserLogin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        self.username