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
    carImg = models.ImageField(upload_to='uploads/')
    carSdImg = models.ImageField(upload_to='uploads/')
    carFrImg = models.ImageField(upload_to='uploads/')
    carInImg = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.carName


class Message(models.Model):
    fname = models.CharField(max_length = 250)
    sname = models.CharField(max_length = 250)
    phone= models.CharField(max_length = 12)
    message = models.TextField()

    def __str__(self):
        return self.fname + ' ' + self.sname
