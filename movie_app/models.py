from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    duration = models.DurationField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

@property
def movie_title(self):
    if self.title_id:
        return self.title.name
    return None


class Review(models.Model):
    text = models.TextField(blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)

    def __str__(self):
        return self.text
