from django.urls import path

from lesson_5 import views

urlpatterns = [
    path('create_flower/', views.create_flower, name='create_flower'),
    path('create_client/', views.create_client, name='create_client'),
    path('get_flower/', views.get_flower, name='get_flower'),
    path('flowers/', views.FlowerListViews.as_view(), name='all_flowers'),
    path('flowers/search/', views.SearchFlowerViews.as_view(), name='search_flower')
]
