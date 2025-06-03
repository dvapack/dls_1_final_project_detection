from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    

class VideoModel(models.Model):
    videoID = models.AutoField(primary_key=True)
    initialVideoFile = models.FileField(upload_to='videos/initial/')
    resultVideoFile = models.FileField(
        upload_to='videos/result/', 
        null=True,
        blank=True
    )
    


class UsageHistory(models.Model):
    operationID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    videoID = models.ForeignKey(VideoModel, on_delete=models.SET_NULL, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Ожидает обработки'),
            ('processing', 'В процессе'),
            ('completed', 'Завершено'),
            ('failed', 'Ошибка')
        ],
        default='pending'
    )
    detectionModel = models.CharField(max_length=20)
    trackingModel = models.CharField(max_length=20)
    analysisModel = models.CharField(max_length=20)