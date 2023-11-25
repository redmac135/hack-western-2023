from django.db import models
from reflectors.models import Reflector


class EntryAudio(models.Model):
    audio = models.FileField(upload_to="audio/")

    def __str__(self):
        return str(self.audio)


class Entry(models.Model):
    reflector = models.ForeignKey(Reflector, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    audio = models.ForeignKey(EntryAudio, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.reflector) + " " + str(self.created_at)
