from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from lesson_8.models import GameModel, GamerModel, GamerLibraryModel
from lesson_5.models import Flower, Client, Bouquet
from lesson_9 import serializers


class GameViewSet(viewsets.ModelViewSet):
    queryset = GameModel.objects.all().order_by('-year')
    serializer_class = serializers.GameSerializer


class GamerViewSet(viewsets.ModelViewSet):
    queryset = GamerModel.objects.all()
    serializer_class = serializers.GamerSerializer


class FlowerViewSet(viewsets.ModelViewSet):
    queryset = Flower.objects.all()
    serializer_class = serializers.FlowerSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = serializers.ClientSerializer


class PongView(APIView):
    def get(self, request):
        return Response({'message': 'PONG'})
