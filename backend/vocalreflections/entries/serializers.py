from rest_framework import serializers
from .models import Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = "__all__"


class EntryAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = "__all__"
