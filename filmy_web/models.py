from django.db import models


class AdditionalInfo(models.Model):
    GENRE = {
        (0, "Different"),
        (1, "Horror"),
        (2, "Comedy"),
        (3, "Drama"),
        (4, "Sci-fi"),
    }
    duration = models.PositiveSmallIntegerField(default=0)
    genre = models.PositiveSmallIntegerField(default=0, choices=GENRE, null=True, blank=True)


class Film(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    year = models.PositiveSmallIntegerField(default=2000)
    description = models.TextField(default="")
    premiere = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    poster = models.ImageField(upload_to="posters", null=True, blank=True)
    additional = models.OneToOneField(AdditionalInfo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.year})"


class Review(models.Model):
    review = models.TextField(default='', blank=True)
    stars = models.PositiveSmallIntegerField(default=5)
    movie = models.ForeignKey(Film, on_delete=models.CASCADE)


class Actor(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    films = models.ManyToManyField(Film)



