from django.urls import path, include
from . import views

urlpatterns = [
    path('livraria/', views.home, name='home'),
]