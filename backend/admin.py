from django.contrib import admin
from .models import USER, PROJECT, LANGUAGE

# Register your models here.
admin.site.register(USER)
admin.site.register(PROJECT)
admin.site.register(LANGUAGE)