from django.urls import path
from . import views

urlpatterns = [
    path('perpustakaan/', views.PerpustakaanCreateView.as_view(), name='perpustakaan_view_create'),
    path('perpustakaan/<id>', views.PerpustakaanRetrieveUpdateDestroy.as_view(), name='perpustakaan_retrieve_update_delete'),
    path('perpustakaan/<id>/buku', views.BukuInPerpustakaanView.as_view(), name='perpustakaan_daftar_buku'),
    path('buku/', views.BukuCreateView.as_view(), name='buku_view_create'),
    path('buku/<id>', views.BukuRetrieveUpdateDestroy.as_view(), name='buku_retrieve_update_delete'),
    path('genre/', views.GenreCreateView.as_view(), name='genre_view_create'),

]