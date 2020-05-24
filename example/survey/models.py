from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30)
    email  = models.EmailField()
    linkedin  = models.URLField()
    github = models.URLField()
    favorite_sport  = models.CharField(max_length=30)

