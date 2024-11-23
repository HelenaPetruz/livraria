from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def str(self):
        return f'{self.user.username} Profile'


    def save(self):
        super().save()