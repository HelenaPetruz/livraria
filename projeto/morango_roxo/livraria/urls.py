from django.urls import path
from . import views

urlpatterns = [
    path('livraria/', views.home, name='home'),
]