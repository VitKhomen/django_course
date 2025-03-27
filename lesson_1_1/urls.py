from django.urls import path
from lesson_1_1.views import index

urlpatterns = [
    path('', index, name='index'),
]
