from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField(null=False)
    name = models.CharField(max_length=128, null=False)
    password = models.CharField(max_length=32, null=False)
