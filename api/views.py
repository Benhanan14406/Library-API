from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

class PerpustakaanListCreate(generics.ListCreateAPIView):
    queryset = Perpustakaan.objects.all()
    serializer_class = PerpustakanSerializer

class BukuListCreate(generics.ListCreateAPIView):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer

class GenreListCreate(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer