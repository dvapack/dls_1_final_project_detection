from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    

class VideoModel(models.Model):
    videoID = models.AutoField(primary_key=True)
    video_file = models.FileField(upload_to='videos/')


class UsageHistory(models.Model):
    operationID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    imageID = models.ForeignKey(VideoModel, on_delete=models.SET_NULL, null=True)