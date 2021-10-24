from django.db import models


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
    bio = models.TextField('', null=True, blank=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    cook_time = models.CharField(max_length=25)
    instructions = models.TextField(max_length=500)

    def __str__(self):
        return self.title
