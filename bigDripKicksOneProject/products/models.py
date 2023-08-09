from django.db import models

# Create your models here.

# Top Seller Product
class  TopSeller(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    # photo = models.ImageField(upload_to='images/')
# Latest arrival
class  LatestArrival(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    # photo = models.ImageField(upload_to='images/')
# Drip
class  Drip(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    # photo = models.ImageField(upload_to='images/')
# kicks
class  Kicks(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    # price = models.ImageField(upload_to='images/')
