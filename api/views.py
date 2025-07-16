from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

# Methods w/ api_view
# GET all, POST perpus
@api_view(['GET', 'POST'])
def get_post_perpustakaan(request):
    if request.method == 'GET':
        perpustakaan = Perpustakaan.objects.order_by('pk')
        serializer = PerpustakanSerializer(perpustakaan, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = PerpustakanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# GET, POST, DELETE specific perpus
@api_view(['GET', 'PUT', 'DELETE'])
def perpustakaan_detail(request, pk):
    try:
        perpustakaan = Perpustakaan.objects.get(pk=pk)
    except Perpustakaan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PerpustakanSerializer(perpustakaan)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PerpustakanSerializer(perpustakaan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        perpustakaan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# GET all, POST buku
@api_view(['GET', 'POST'])
def get_post_buku(request):
    if request.method == 'GET':
        buku = Buku.objects.order_by('pk')
        serializer = BukuSerializer(buku, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BukuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# GET, POST, DELETE specific buku
@api_view(['GET', 'PUT', 'DELETE'])
def buku_detail(request, pk):
    try:
        buku = Buku.objects.get(pk=pk)
    except Buku.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BukuSerializer(buku)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BukuSerializer(buku, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        buku.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# GET all buku in specific perpus
@api_view(['GET'])
def buku_in_perpustakaan(request, pk):
    perpustakaan = Perpustakaan.objects.get(pk=pk)
    if Perpustakaan.objects.filter(pk=pk).exists():
        serializer = BukuSerializer(perpustakaan.daftar_buku(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# GET all, POST genre
@api_view(['GET', 'POST'])
def get_post_genre(request):
    if request.method == 'GET':
        genre = Genre.objects.order_by('pk')
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# GET, POST, DELETE specific genre
@api_view(['GET', 'DELETE'])
def genre_detail(request, pk):
    try:
        genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GenreSerializer(genre)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# GET all buku w/ specific genre
@api_view(['GET'])
def buku_w_genre(request, pk):
    genre = Genre.objects.get(pk=pk)
    if Genre.objects.filter(pk=pk).exists():
        serializer = BukuSerializer(genre.daftar_buku(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# Methods w/ generics
# Buku GET all & POST
class PerpustakaanCreateView(generics.ListCreateAPIView):
    queryset = Perpustakaan.objects.order_by('pk')
    serializer_class = PerpustakanSerializer

# Perpustakaan GET, PUT, & DELETE specific
class PerpustakaanRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Perpustakaan.objects.order_by('pk')
    serializer_class = PerpustakanSerializer
    lookup_field = 'pk'

# Buku GET all & POST
class BukuCreateView(generics.ListCreateAPIView):
    queryset = Buku.objects.order_by('pk')
    serializer_class = BukuSerializer

# Buku GET, PUT, & DELETE specific
class BukuRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Buku.objects.order_by('pk')
    serializer_class = BukuSerializer
    lookup_field = 'pk'

# Buku GET pada perpustakaan tertentu
class BukuInPerpustakaanView(generics.ListAPIView):
    serializer_class = BukuSerializer

    def get_queryset(self):
        return Buku.objects.order_by('pk').filter(perpustakaan__id=self.kwargs['pk'])

# Genre GET all & POST
class GenreCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.order_by('pk')
    serializer_class = GenreSerializer

# Genre GET specific
class GenreRetrieveDelete(generics.RetrieveDestroyAPIView):
    queryset = Genre.objects.order_by('pk')
    serializer_class = GenreSerializer
    lookup_field = 'pk'

# Buku GET dengan genre tertentu
class BukuWithGenreView(generics.ListAPIView):
    serializer_class = BukuSerializer

    def get_queryset(self):
        return Buku.objects.order_by('pk').filter(genre__id=self.kwargs['pk'])


