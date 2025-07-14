from django.db import models

class Perpustakaan(models.Model):
    nama_perpustakaan = models.CharField(max_length=100)
    alamat_perpustakaan = models.TextField()

    def __str__(self):
        return self.nama_perpustakaan

    # Method untuk mengambil seluruh buku dalam suatu perpustakaan
    def daftar_buku(self):
        return self.buku_perpustakaan.all()

class Genre(models.Model):
    nama_genre = models.CharField(max_length=1000, editable=True)

    def __str__(self):
        return self.nama_genre

    # Method untuk mengambil seluruh buku dengan genre tertentu
    def daftar_buku(self):
        return self.buku_genre.all()

class Buku(models.Model):
    judul = models.CharField(max_length=1000)
    pengarang = models.CharField(max_length=1000)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='buku_genre')
    # Asumsi: Terdapat field 'perpustakaan' agar semua buku dalam suatu perpustakaan bisa diambil
    perpustakaan = models.ForeignKey(Perpustakaan, on_delete=models.SET_NULL, null=True, related_name='buku_perpustakaan')

    def __str__(self):
        return self.judul