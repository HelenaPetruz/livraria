from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    sinopse = models.TextField(max_length=1000)

    def __str__(self):
        return self.titulo
