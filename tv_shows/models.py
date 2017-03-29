from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models

from actors.models import Actor


class TvShow(models.Model):
    name = models.CharField(max_length=200)
    summary = models.TextField()
    actors = models.ManyToManyField(Actor)
    genres = JSONField()
    show_type = models.CharField(max_length=20)
    premiered = models.IntegerField()
    image = models.URLField()
    creators = ArrayField(models.CharField(max_length=100))
    tv_rage_id = models.IntegerField()
    language = models.CharField(max_length=20)
    networks = JSONField()
    tv_rage_rating = models.IntegerField()
    runtime = models.IntegerField()
    schedule = JSONField()
    status = models.CharField(max_length=20)

class Season(models.Model):
    tv_show = models.ForeignKey(TvShow, on_delete=models.CASCADE)
    number = models.IntegerField()
    year = models.IntegerField()
    image = models.URLField()


class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    number = models.IntegerField()
    synopsis = models.TextField()
    air_date = models.DateField()
    director = models.CharField(max_length=100)
