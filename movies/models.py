from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    year = models.IntegerField()
    rating = models.FloatField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    poster = models.ImageField(upload_to="posters/%Y/%m/", blank=True)
    genre = models.CharField(max_length=50, blank=True)



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs= {'post_id': self.pk})