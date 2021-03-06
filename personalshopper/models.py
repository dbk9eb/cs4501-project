from django.db import models

class User(models.Model):
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    username = models.CharField(max_length=30)
    def __str__(self):
        return str(self.username) + " (" + str(self.email) + ")"

class PersonalShopper(models.Model):
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    username = models.CharField(max_length=30)
    def __str__(self):
        return str(self.username) + " (" + str(self.email) + ")"

class Item(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    country = models.CharField(max_length=100, default="US")
    def __str__(self):
        desc = self.description if (self.description != "") else "No description provided."
        return str(self.name) + ": " + desc
