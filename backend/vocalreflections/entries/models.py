from django.db import models
from reflectors.models import Reflector


# Create your models here.
class Entry(models.Model):
    reflector = models.ForeignKey(Reflector, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    audio = models.FileField(upload_to="audio/")

    def __str__(self):
        return str(self.reflector) + " " + str(self.created_at)
