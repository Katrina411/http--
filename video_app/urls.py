from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('play/<int:video_id>/', views.video_play, name='video_play'),
]