from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Reflector(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username
