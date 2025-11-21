from django.shortcuts import render
from .models import Video

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})

def video_play(request, video_id):
    video = Video.objects.get(id=video_id)
    return render(request, 'video_play.html', {'video': video})