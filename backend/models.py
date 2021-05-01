from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

LANGUAGE_CHOICES = (
    ('java', 'Java'),
    ('c', 'C'),
    ('py', 'Python'),
)

class User(models.Model):
    name = models.CharField(max_length = 255)
    password = models.CharField(max_length = 100, validators = [MinLengthValidator(6)])
    email = models.EmailField()

class Language(models.Model):
    language = models.CharField(max_length = 4, choices = LANGUAGE_CHOICES,default = 'py')
    image_id = models.CharField(max_length = 100)

class Project(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    language = models.ForeignKey(Language, on_delete = models.CASCADE, default = 'py')
    name = models.CharField(max_length = 255)
    volume_id = models.CharField(max_length = 100)