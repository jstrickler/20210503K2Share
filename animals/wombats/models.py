from django.db import models

# Create your models here.

class Wombat(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
