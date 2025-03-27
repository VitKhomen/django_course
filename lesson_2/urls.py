from django.urls import path
from lesson_2 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bio/<username>/', views.bio, name='bio'),
    path('articles/<int:year>/', views.year_archive),
    path('home/', views.home, name='home-view'),
    path(f'book/<int:title>/', views.book, name='book'),
]
