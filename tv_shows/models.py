from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models

from actors.models import Actor

class TvShow(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    actors = models.ManyToManyField(Actor)
    genres = JSONField()
    year = models.IntegerField()
    poster = models.URLField()
    creators = ArrayField(models.CharField(max_length=100))


class Season(models.Model):
    tv_show = models.ForeignKey(TvShow, on_delete=models.CASCADE)
    number = models.IntegerField()
    year = models.IntegerField()
    poster = models.URLField()

class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    number = models.IntegerField()
    synopsis = models.TextField()
    air_date = models.DateField()
    director = models.CharField(max_length=100)
