from rest_framework import viewsets
from .serializers import DogSerializer, BreedSerializer
from dogs_core.models import Dog, Breed
# from dogs_core.api.filters import * # (optional)  change to only needed serializers

# viewset further simplifies API --
# provides higher-level access and
# automatically creates routes
class DogsViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

    # add filters here...
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = MyFirstModelFilter


class BreedsViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = MySecondModelFilter

