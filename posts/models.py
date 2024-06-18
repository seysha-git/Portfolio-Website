from typing import Any
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=75, default="SOME STRING")
    body = models.TextField(default="some string")
    slug = models.SlugField(default="some string")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title