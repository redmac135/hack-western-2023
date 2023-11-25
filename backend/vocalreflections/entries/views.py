from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Entry
from .serializers import EntrySerializer


# Create your views here.
class EntryListAPI(APIView):
    model_class = Entry
    serializer_class = EntrySerializer

    def get(self, request):
        # TODO: filter by reflector
        entries = self.model_class.objects.all()
        serializer = self.serializer_class(entries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EntryAudioAPI(APIView):
    model_class = Entry
    serializer_class = EntrySerializer

    def get(self, request, pk):
        audio = self.model_class.objects.get(pk=pk)
        serializer = self.serializer_class(audio)
        return Response(serializer.data, status=status.HTTP_200_OK)