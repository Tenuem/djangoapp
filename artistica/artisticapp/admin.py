from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CustomUser, Post, Comment

admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(Comment)