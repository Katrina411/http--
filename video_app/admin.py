from django.contrib import admin
from .models import Video  # 导入视频模型

admin.site.register(Video)  # 将视频模型注册到后台