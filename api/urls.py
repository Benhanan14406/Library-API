from django.urls import path
from . import views
from .views import PerpustakaanListCreate

urlpatterns = [
    path('perpustakaan/', views.PerpustakaanListCreate.as_view(), name='perpustakaan_view_create'),
    path('buku/', views.BukuListCreate.as_view(), name='buku_view_create'),
    path('genre/', views.GenreListCreate.as_view(), name='genre_view_create'),
]