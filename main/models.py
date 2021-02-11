from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    url = models.URLField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)