from django.shortcuts import render
from rest_framework import generics
from .serializers import PhotoSerializer
from .models import Photo
# Create your views here.

class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all().order_by('-id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = PhotoSerializer # tell django what serializer to use

class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all().order_by('-id')
    serializer_class = PhotoSerializer