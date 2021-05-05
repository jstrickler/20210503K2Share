from django.db import models

# Create your models here.

class Sandwich(models.Model):
    bread = models.CharField(max_length=32)
    filling = models.CharField(max_length=32)
    mayonnaise = models.BooleanField()
    mustard = models.BooleanField()
    horseradish = models.BooleanField(default=False)
    cheese = models.CharField(max_length=64)




