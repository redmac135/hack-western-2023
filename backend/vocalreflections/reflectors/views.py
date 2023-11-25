from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Reflector
from .serializers import ReflectorSerializer


# Create your views here.
class ReflectorDetailAPI(APIView):
    model_class = Reflector
    serializer_class = ReflectorSerializer

    def get(self, request):
        # TODO: implement user fetching by authentication class
        reflector = self.model_class.objects.all().first()
        serializer = self.serializer_class(reflector)
        return Response(serializer.data, status=status.HTTP_200_OK)
