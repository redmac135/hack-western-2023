from rest_framework import serializers
from .models import Reflector


class ReflectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reflector
        fields = "__all__"
