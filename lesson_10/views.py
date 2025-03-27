from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.utils.timezone import now

from rest_framework.generics import CreateAPIView, RetrieveAPIView, \
    RetrieveUpdateAPIView

from rest_framework import viewsets
from rest_framework.views import APIView

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from lesson_8.models import GameModel, GamerModel
from lesson_9.serializers import GameSerializer, GamerSerializer
from lesson_10.serializers import UserSerializer

from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

import pytz
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim


class GetTimeByCityAPIView(APIView):
    permission_classes = [AllowAny,]

    def get(self, request):
        city = request.GET.get('city', None)

        if not city:
            return Response({'error': 'City parameter is required'},
                            status=HTTP_400_BAD_REQUEST)

        geolocator = Nominatim(user_agent='timezone_api')
        location = geolocator.geocode(city)

        if not location:
            return Response({'error': 'City not found'}, status=HTTP_400_BAD_REQUEST)

        tf = TimezoneFinder()
        timezone_str = tf.timezone_at(
            lng=location.longitude, lat=location.latitude)

        if not timezone_str:
            return Response({'error': 'Could not determine timezone'}, status=HTTP_400_BAD_REQUEST)

        tz = pytz.timezone(timezone_str)
        current_time = now().astimezone(tz).strftime('%Y-%m-%d %H:%M:%S')

        return Response({
            'city': city,
            'timezone': timezone_str,
            'current_time': current_time
        })


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if not all([username, password]):
        return Response({'error': 'please enter username and password'})
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid data'})
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'Token': token.key}, status=HTTP_200_OK)


class CreateUser(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
def view_function(request):
    print(request.data)
    return Response({'function': 'some_data'})


class ClassAPIView(APIView):
    def get(self, request):
        return Response({'class': 'some_class_data'})

    def post(self, request):
        print(request.data)
        return Response({'class': 'some_class_data'})


class GameSetAPIView(viewsets.ViewSet):
    queryset = GameModel.objects.filter(id__lt=50)

    def list(self, request):
        serializer = GameSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = GameSerializer(user)
        return Response(serializer.data)


class MyCreateAPIView(CreateAPIView):
    serializer_class = GamerSerializer


class MyRetrieveAPIView(RetrieveAPIView):
    permission_classes = (IsAdminUser,)
    queryset = GamerModel.objects.all()
    serializer_class = GamerSerializer


class MyRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = GamerModel.objects.all()
    serializer_class = GamerSerializer
