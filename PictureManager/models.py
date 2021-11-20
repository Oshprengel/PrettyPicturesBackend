from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    continent = models.CharField(max_length=100)
    caption = models.CharField(max_length=200)

class Picture(models.Model):
    link = models.CharField(max_length=200)
    caption = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)


