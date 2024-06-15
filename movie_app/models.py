from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    duration = models.DurationField()
    director = models.ForeignKey

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField(blank=True, null=True)
    movie = models.ForeignKey

    def __str__(self):
        return self.text

