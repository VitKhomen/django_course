from django.urls import path, include
from rest_framework.routers import DefaultRouter
from lesson_9 import views

router = DefaultRouter()
router.register(r'games', views.GameViewSet)
router.register(r'gamers', views.GamerViewSet)
router.register(r'flower', views.FlowerViewSet)
router.register(r'client', views.ClientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    path('ping/', views.PongView.as_view(), name='ping')
]
