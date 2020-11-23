from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    instructions = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name
