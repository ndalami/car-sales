from django.db import models

# Create your models here.
class Car (models.Model):
    carName = models.CharField(max_length=20)
    carPrice = models.CharField(max_length=20)
    carEngine =models.CharField(max_length=20)
    fuel = models.CharField(max_length=10)
    transmission = models.CharField(max_length=15)
    color = models.CharField(max_length=20, blank=True)
    doors = models.IntegerField()
    carImg = models.ImageField()

    def __str__(self):
        return self.carName


class Message(models.Model):
    name = models.CharField(max_length = 250)
    email= models.EmailField()
    subject = models.CharField(max_length = 250)
    message = models.TextField()

    def __str__(self):
        return self.name
