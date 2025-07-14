from django.db import models

class Perpustakaan(models.Model):
    nama_perpustakaan = models.CharField(max_length=100, editable=True)
    alamat_perpustakaan = models.CharField(max_length=1000, editable=True)

    def __str__(self):
        return self.nama_perpustakaan

class Genre(models.Model):
    nama_genre = models.CharField(max_length=1000, editable=True)
    daftar_buku = []

    def __str__(self):
        return self.nama_genre

class Buku(models.Model):
    judul = models.CharField(max_length=1000, editable=True)
    pengarang = models.CharField(max_length=1000, editable=True)
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)

    def __str__(self):
        return self.judul