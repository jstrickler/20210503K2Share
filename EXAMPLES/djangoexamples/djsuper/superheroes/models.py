"""
Models for the superheroes app.

Models include
    Superhero
    City
    Power
    Enemy

Note that these models will also be used in filters and
serializers, as well as *some* of our views.

The ``Superhero`` model is the main model of our app.
"""
from random import random
from django.db import models

class SuperheroManager(models.Manager):
    def get_fliers(self):
        return self.filter(powers__name__icontains="fly")

    def get_men(self):
        return self.filter(name__icontains="man")


class SuperHeroQuerySet(models.QuerySet):
    def fliers(self):
        return self.filter(powers__name__icontains="fly")

    def men(self):
        return self.filter(name__icontains="man")




class Power(models.Model):
    """
    Describes one power that a superhero might have.

    name - short name of the power
    description -- verbose description
    """
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return """City(name='{}')""".format(self.name)

class Enemy(models.Model):
    name = models.CharField(max_length=32, unique=True)
    powers = models.ManyToManyField(Power)

    def __str__(self):
        return self.name


def make_real_name():
    return "Bob"

def get_random():
    return random.random()

class Superhero(models.Model):
    name = models.CharField(max_length=32, unique=True)
    real_name = models.CharField(max_length=32, default=make_real_name)
    secret_identity = models.CharField(max_length=32)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    powers = models.ManyToManyField(Power)
    enemies = models.ManyToManyField(Enemy)
    magic1 = models.IntegerField(default=1)
    magic2 = models.IntegerField(default=2)
    thing = models.CharField(max_length=16, null=True)
    x = models.IntegerField(default=42)

    objects = SuperHeroQuerySet.as_manager()

    mgr = SuperheroManager()

    def __str__(self):
        return self.name


