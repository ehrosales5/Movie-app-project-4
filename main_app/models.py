from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    year = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={'movie_id': self.id})

    # def __str__(self):
    #     return self.title

class Comments(models.Model):
    comment = models.TextField()
    date = models.DateField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.movie.title}"

    class Meta:
        ordering = ['-date']
