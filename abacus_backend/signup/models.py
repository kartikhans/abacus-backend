from django.db import models
import uuid


# Create your models here.

class User(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, null=False)
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=20, null=False)
    phone = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=500, null=True)
    is_deleted = models.BooleanField(null=True, default=True)
    is_admin = models.BooleanField(null=True, default=False)
