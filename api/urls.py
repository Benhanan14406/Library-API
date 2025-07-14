from django.urls import path
from . import views
from .views import PerpustakaanListCreate

urlpatterns = [
    path('perpustakaan/', views.PerpustakaanListCreate.as_view(), name='perpustakaan_view_create'),
]