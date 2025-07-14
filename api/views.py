from rest_framework import generics
from .serializers import *

# Buku GET all & POST
class PerpustakaanCreateView(generics.ListCreateAPIView):
    queryset = Perpustakaan.objects.all()
    serializer_class = PerpustakanSerializer

# Perpustakaan GET, PUT, & DELETE specific
class PerpustakaanRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Perpustakaan.objects.all()
    serializer_class = PerpustakanSerializer
    lookup_field = 'id'

# Buku GET all & POST
class BukuCreateView(generics.ListCreateAPIView):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer

# Buku GET, PUT, & DELETE specific
class BukuRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer
    lookup_field = 'id'

# Buku GET pada perpustakaan tertentu
class BukuInPerpustakaanView(generics.ListAPIView):
    serializer_class = BukuSerializer

    def get_queryset(self):
        return Buku.objects.all().filter(perpustakaan_id=self.kwargs['id'])

# Genre GET all & POST
class GenreCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

# Genre GET specific
class GenreRetrieve(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'id'

# Genre DELETE specific
class GenreDelete(generics.DestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'id'

# Buku GET dengan genre tertentu
class BukuWithGenreView(generics.ListAPIView):
    serializer_class = BukuSerializer

    def get_queryset(self):
        return Buku.objects.all().filter(genre_id=self.kwargs['id'])


