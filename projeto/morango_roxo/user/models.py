from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Adicione campos personalizados aqui (opcional)
    nickname = models.CharField(max_length=15, blank=True, null=True)

