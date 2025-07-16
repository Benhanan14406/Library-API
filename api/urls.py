from django.urls import path
from . import views

urlpatterns = [
    # URLS using api_view
    path('perpustakaan/', views.get_post_perpustakaan, name='get_post_perpustakaan'),
    path('perpustakaan/<pk>', views.perpustakaan_detail, name='get_put_del_perpustakaan'),
    path('perpustakaan/<pk>/buku', views.buku_in_perpustakaan, name='get_buku_in_perpustakaan'),
    path('buku/', views.get_post_buku, name='get_post_buku'),
    path('buku/<pk>', views.buku_detail, name='get_put_del_buku'),
    path('genre/', views.get_post_genre, name='get_post_genre'),
    path('genre/<pk>', views.genre_detail, name='get_del_genre'),
    path('genre/<pk>/buku', views.buku_w_genre, name='get_buku_w_genre'),

    # URLS using the generics methods
    # path('perpustakaan/', views.PerpustakaanCreateView.as_view(), name='perpustakaan_view_create'),
    # path('perpustakaan/<id>', views.PerpustakaanRetrieveUpdateDestroy.as_view(), name='perpustakaan_retrieve_update_delete'),
    # path('perpustakaan/<id>/buku', views.BukuInPerpustakaanView.as_view(), name='perpustakaan_daftar_buku'),
    # path('buku/', views.BukuCreateView.as_view(), name='buku_view_create'),
    # path('buku/<id>', views.BukuRetrieveUpdateDestroy.as_view(), name='buku_retrieve_update_delete'),
    # path('genre/', views.GenreCreateView.as_view(), name='genre_view_create'),
    # path('genre/<id>', views.GenreRetrieve.as_view(), name='genre_retrieve_delete'),
    # path('genre/<id>/buku', views.BukuWithGenreView.as_view(), name='genre_daftar_buku'),

]