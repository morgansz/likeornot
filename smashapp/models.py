from django.db import models

class Picture(models.Model):
    image = models.ImageField(upload_to='original_images/')
    processed_image = models.ImageField(upload_to='processed_images/', null=True, blank=True)
    likes = models.IntegerField(default=0)  # 添加这一行
    dislikes = models.IntegerField(default=0)  # 新增这个字段来存储"不喜欢"的数量



class UserPreference(models.Model):
    session_id = models.CharField(max_length=256)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    liked = models.BooleanField()
