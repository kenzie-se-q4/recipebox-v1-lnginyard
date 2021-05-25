from django.db import models
from django.utils import timezone


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
    time_required = models.CharField(max_length=30)
    instructions = models.TextField()

    def __str__(self):
        return self.title

