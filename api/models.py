from django.db import models

class Perpustakaan(models.Model):
    nama_perpustakaan = models.CharField(max_length=100)
    alamat_perpustakaan = models.TextField()

    def __str__(self):
        return self.nama_perpustakaan

class Genre(models.Model):
    nama_genre = models.CharField(max_length=1000, editable=True)

    def __str__(self):
        return self.nama_genre

    def daftar_buku(self):
        return self.buku_set.all()

class Buku(models.Model):
    judul = models.CharField(max_length=1000)
    pengarang = models.CharField(max_length=1000)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.judul