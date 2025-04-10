from django.urls import path, include
from rest_framework import routers
from lesson_10 import views

from django.contrib import admin

router = routers.SimpleRouter()
router.register(r'games', views.GameSetAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('function/', views.view_function, name='function_view'),
    path('class/', views.ClassAPIView.as_view(), name='class_view'),
    path('generic/', views.MyCreateAPIView.as_view(), name='generic'),
    path('retrieve/<int:pk>', views.MyRetrieveAPIView.as_view(), name='retrieve'),
    path('retrieve-update/<int:pk>',
         views.MyRetrieveUpdate.as_view(), name='retrieve_update'),
    path('api-login', views.user_login),
    path('create-user', views.CreateUser.as_view()),
    path('time/', views.GetTimeByCityAPIView.as_view(), name='time'),
]
