from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Language(models.Model):
    name = models.CharField(max_length=255, default='Python')
    image_id = models.CharField(max_length=255, default='codercom/code-server')

    def __str__(self):
        return f"{self.name}"


class Project(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING)
    volume_id = models.CharField(max_length=100)
    last_mdate = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f"{self.name} by {self.user}"
