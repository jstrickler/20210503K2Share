import uuid
from django.db import models

# define a model, which is the core of the Django app
# a model corresponds to a DB table
class Breed(models.Model):
    # specify model fields; these correspond to table columns
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, help_text="Unique ID of this artist")
    abbr = models.CharField(max_length=4, null=True, help_text="Abbreviation of breed name")

    name = models.CharField(max_length=64, help_text="Name of breed")

    # specify metadata for this model.
    class Meta:
        # set table name, otherwise defaults to
        #  APP_NAME_MODEL
        db_table = 'breeds'

    def __str__(self):
        return self.name

class DogManager(models.Manager):
    """
    Custom manager for the Dog model.

    This custom manager will add an aggregate function to
    return the dog with the shortest name
    """
    def __init__(self):
        super().__init__()

    def shortest_name(self):
        dogs = Dog.objects.all().order_by('name')
        return dogs.first()


class Dog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, help_text="Unique ID of this artist")
    name = models.CharField(max_length=64, help_text="Name of dog")
    sex = models.CharField(max_length=1, choices=[('f', 'Female'), ('m', 'Male')], help_text="Sex of dog (m or f)")
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name="breeds", help_text="Breed of dog")
    is_neutered = models.BooleanField(default=False, help_text="Whether dog is neutered")
    weight  = models.IntegerField(help_text="Approximate weight of dog in pounds")
    bites = models.BooleanField(default=False,
                                help_text="Whether dog bites")

    objects = DogManager()

    class Meta:
        db_table = 'dogs'
        # sort Dog objects by the 'name' field
        # on the related field 'breed'
        # if you just order by 'breed', it will order
        # by the breed ID, not the name
        ordering = ['breed__name', 'name']

    def __str__(self):
        return f"{self.name} ({self.breed})"

    def save(self, *args, **kwargs):
        print("Woof! Woof!")
        super().save(*args, **kwargs)



