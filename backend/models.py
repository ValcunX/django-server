from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

LANGUAGE_CHOICES = (
    ('java', 'Java'),
    ('c', 'C'),
    ('py', 'Python'),
)
class USER(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 100, validators = [MinLengthValidator(6)])
    email = models.CharField(max_length = 40)

class PROJECT(models.Model):
    project_name = models.CharField(max_length = 20)
    volume_id = models.CharField(max_length = 100)

class LANGUAGE(models.Model):
    language = models.CharField(max_length = 4, choices=LANGUAGE_CHOICES)
    image_id = models.CharField(max_length = 100)