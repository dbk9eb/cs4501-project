from django.db import models

class User(models.Model):
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    username = models.CharField(max_length=30)

class PersonalShopper(models.Model):
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    username = models.CharField(max_length=30)    

class Item(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    country = models.CharField(max_length=100, default="US")

class Address(models.Model):
    user = models.ForeignKey(User)
    street = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField()
