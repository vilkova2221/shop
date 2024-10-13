from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/')
    brand = models.CharField(max_length=30)
    guarantee = models.CharField(max_length=30)
    discount = models.PositiveSmallIntegerField()
    material = models.CharField(max_length=30)
    rating = models.FloatField()
    stock = models.PositiveSmallIntegerField()
    