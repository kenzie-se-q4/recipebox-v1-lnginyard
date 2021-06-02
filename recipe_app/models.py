from django.db import models
from django.utils import timezone
from django.contrib.auth import authenticate

# Create your models here.
"""
Author:
- name
- byline (optional)


Recipe:
- Body
- Author??
- post_created
- Title
"""


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    cook_time = models.DateTimeField(default=timezone.now)
    instructions = models.TextField()

    def __str__(self):
        return self.title

