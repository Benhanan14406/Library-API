from rest_framework import serializers
from .models import *

class PerpustakanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perpustakaan
        fields = '__all__'

class BukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buku
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'