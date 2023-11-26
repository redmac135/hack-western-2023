from django.db import models
from reflectors.models import Reflector
from gcloudapi.sentiment_analysis import SentimentProcessor
from gcloudapi.speech_to_text import SpeechProcessor


class EntryAudio(models.Model):
    audio = models.FileField(upload_to="audio/")

    def __str__(self):
        return str(self.audio)


class Entry(models.Model):
    reflector = models.ForeignKey(Reflector, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    sentiment = models.FloatField()  # -1~+1
    magnitude = models.FloatField()  # 0~+inf
    content = models.TextField()
    audio = models.ForeignKey(EntryAudio, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.reflector) + " " + str(self.created_at)

    @classmethod
    def create_entry(cls, reflector_uid: str, audio_pk):
        reflector = Reflector.objects.get(uid=reflector_uid)
        audio = EntryAudio.objects.get(pk=audio_pk).audio
        content = SpeechProcessor(audio).process()
        sentiment_analysis = SentimentProcessor(content).process()

        entry = cls.objects.create(
            reflector=reflector,
            audio=audio,
            content=content,
            sentiment=sentiment_analysis.score,
            magnitude=sentiment_analysis.magnitude,
        )
        return entry
