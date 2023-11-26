from django.db import models
from reflectors.models import Reflector
from gcloudapi.sentiment_analysis import SentimentProcessor
from gcloudapi.speech_to_text import SpeechProcessor
from django.core.files.uploadedfile import InMemoryUploadedFile


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
    def create_entry(cls, reflector_uid: str, audio: InMemoryUploadedFile):
        # Get or Create method used due to forntend use of tmp useruid
        reflector = Reflector.objects.get_or_create(
            uid=reflector_uid, display_name="tmp", email="fakeemail@fake.mail"
        )[0]
        audio_class = EntryAudio.objects.create(audio=audio)
        content = SpeechProcessor(audio_class.audio.path).process()
        sentiment_analysis = SentimentProcessor(content).process()

        entry = cls.objects.create(
            reflector=reflector,
            audio=audio_class,
            content=content,
            sentiment=sentiment_analysis["score"],
            magnitude=sentiment_analysis["magnitude"],
        )
        return entry
