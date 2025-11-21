from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100, verbose_name="视频标题")
    file = models.FileField(upload_to='videos/', verbose_name="视频文件")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.title