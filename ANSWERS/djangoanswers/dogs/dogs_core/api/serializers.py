from rest_framework import serializers
from dogs_core.models import Dog, Breed

# these are named with a trailing 'X' so they don't
# conflict with the ones based on ModelSerializer

class BreedSerializerX(serializers.Serializer):
    """
    Custom serializer for Breed model.
    """
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=32)
    abbr = serializers.CharField(max_length=8)

class DogSerializerX(serializers.Serializer):
    """
    Custom serializer for Dog model.
    """
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=32)
    weight = serializers.IntegerField()
    sex = serializers.CharField(max_length=2)
    breed = BreedSerializerX()
    is_neutered = serializers.BooleanField()


class BreedSerializer(serializers.ModelSerializer):
    """
    "Shortcut" serializer for Breed model using
    ModelSerializer, which handles the details.

    This serializer does everything that the above
    custom serializer BreedSerializerX does, but with
    less boilerplate.

    the *model* and *fields* attributes of the Meta class
    are required.
    """
    class Meta:
        model = Breed
        fields = ('id', 'name', 'abbr')

class DogSerializer(serializers.ModelSerializer):
    """
    Serializer for Dog model using
    ModelSerializer, which handles the details.

    This serializer does everything that the above
    custom serializer DogSerializerX does, but with
    less boilerplate.

    the *model* and *fields* attributes of the Meta class
    are required.

    *fields* selects which fields of the model will be
    exposed via the API.
    """

    breed = serializers.HyperlinkedRelatedField(view_name='dogs_core:api:breeds-detail-cbv', read_only=True)

    class Meta:
        model = Dog
        fields = ('id', 'name', 'breed', 'weight', 'sex', 'is_neutered')

