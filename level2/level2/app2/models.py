from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=125)
    lastName = models.CharField(max_length=125)
    email = models.EmailField(max_length=125,unique=True)


    
