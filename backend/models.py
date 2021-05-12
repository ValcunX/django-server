from django.db import models
from django import forms
from django.utils import timezone

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} ({self.email})"


class Language(models.Model):
    name = models.CharField(max_length=255, default='Python')
    image_id = models.CharField(max_length=255, default='codercom/code-server')

    def __str__(self):
        return f"{self.name}"


class Project(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING)
    volume_id = models.CharField(max_length=100)
    last_mdate = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f"{self.name} by {self.user}"
