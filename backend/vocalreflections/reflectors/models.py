from django.db import models


# Create your models here.
class Reflector(models.Model):
    uid = models.CharField(max_length=255, primary_key=True, unique=True)
    display_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.display_name)
