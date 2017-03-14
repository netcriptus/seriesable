from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=100)
    picture = models.URLField()
