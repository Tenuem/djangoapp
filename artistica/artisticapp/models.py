from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms

class CustomUser(AbstractUser):
    is_editor = models.BooleanField(default=False)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    widgets = {
            'content': forms.Textarea(attrs={'class': 'comment-content', 'placeholder': 'Dodaj komentarz...'}),
        }