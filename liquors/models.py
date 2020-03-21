from django.db import models
from core.models import ItemModel

# Create your models here.

# 분류(럼, 보드카, 리큐르...)


class Category(ItemModel):
    pass


class Ingridient(ItemModel):
    pass


#


class liquor(models.Model):
    price = models.IntegerField()
    name = models.CharField(max_length=255)
    strength = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
