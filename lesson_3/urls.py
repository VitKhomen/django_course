from django.urls import path
from lesson_3 import views
from lesson_3 import post_view
from lesson_3 import homework_view


urlpatterns = [
    path('main/', views.main,),
    # path('main/text/', views.text, name='text'),
    # path('main/file/', views.file, name='file'),
    # path('main/redirect/', views.redirect, name='redirect'),
    # path('main/not-allowed/', views.not_allowed, name='not_allowed'),
    # path('main/json/', views.json, name='json'),

    path('class-view/', views.MyView.as_view(), name='class_view'),

    path('post/', post_view.MyTemplateView.as_view(), name='TemlateView'),

    path('', homework_view.HomeTemplateView.as_view(), name='home'),
    path('task-three/', homework_view.TaskThreeView.as_view(), name='task_three'),
    path('<str:name>/', homework_view.CharacterTemplateView.as_view(),
         name='character_page'),

    # path('post/', post_view.index_post, name='post'),
    path('post/<int:number>/', post_view.post_page, name='posts_list'),
]
