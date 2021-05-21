from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

# import models
from dogs_core.models import Dog, Breed

# import generic class-based views
from rest_framework import generics

# import custom serializers
from  .serializers import DogSerializerX, DogSerializer, BreedSerializer

# function-based view to respond to GET request on Dog resource
@api_view(['GET'])
def dogs(request):
     dogs = Dog.objects.all() # get all records
     serializer = DogSerializerX(dogs, many=True) # serialize the records
     dogs_json = JSONRenderer().render(serializer.data)  # create JSON version of data
     return Response(dogs_json, 200)  # return JSON to client


# class-based views (aka CBVs)

# handle GET or POST requests without PK
class DogsList(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

# handle GET, POST, PUT, PATCH, DELETE requests with PK
class DogsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class BreedsList(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

class BreedsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
