from django.db import models
import uuid
from enum import Enum


# Create your models here.

# Create your models here.
class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def value_choices(cls):
        return [x.value for x in cls]


class TagsType(ChoiceEnum):
    BESTSELLER = "BESTSELLER"
    MUST_TRY = "MUST_TRY"
    NORMAL = "NORMAL"


class Product(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, null=False)
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)
    is_deleted = models.BooleanField(null=False, default=True)
    tag = models.CharField(choices=TagsType.choices(), null=False, default=TagsType.NORMAL.value, max_length=50)
    price = models.FloatField(null=False)
    category = models.CharField(max_length=25, null=True)
    description = models.CharField(max_length=10000, null=True)
