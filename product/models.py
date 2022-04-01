from django.db import models
from django.forms import CharField

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory_quantity = models.IntegerField()