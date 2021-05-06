from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    year = models.IntegerField()

    def __str__(self):
        return "{}/{}".format(self.make, self.model)

