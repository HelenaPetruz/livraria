from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views 
from user import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('livraria.urls')),
    path('admin/', admin.site.urls),
    #path('registrar/', user_views.register, name='register'),
    #path('login/', user_views.login, name='login'),

]
