from django.db import models
from django.contrib.auth.models import User
from mission.models import Mission

# Create your models here.
class Post(models.Model):
    writer = models.ForeignKey(User, related_name='writer', on_delete=models.CASCADE)
    mission_number = models.ForeignKey(Mission, related_name ='mission_num', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    content = models.TextField() # 이미지 필드 사용예정
    description = models.TextField()

    def __str__(self):
        return self.title

class PostVote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        auto_now_add=True,
    )	