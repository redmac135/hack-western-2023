from rest_framework import serializers
from .models import Entry


class EntrySerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Entry
        fields = "__all__"


class EntryAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ["audio"]
