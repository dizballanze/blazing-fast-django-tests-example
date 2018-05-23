from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):

    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Author(User):

    bio = models.TextField()
    articles_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username


class Article(models.Model):

    title = models.CharField(max_length=64)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, related_name='articles', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    comments_on = models.BooleanField(default=True)

    def __str__(self):
        return self.title
