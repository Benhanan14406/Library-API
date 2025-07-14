from rest_framework import serializers
from .models import *

class PerpustakanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perpustakaan
        fields = ['id', 'nama_perpustakaan', 'alamat_perpustakaan']

class BukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buku
        fields = ['id', 'judul', 'pengarang', 'genre']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'nama_genre']