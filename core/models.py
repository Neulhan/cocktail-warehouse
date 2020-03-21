from django.db import models

# Create your models here.


class ItemModel(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True
