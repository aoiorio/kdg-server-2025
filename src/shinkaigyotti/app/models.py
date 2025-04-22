from django.db import models


class Post(models.Model):
    photo = models.URLField()

    def __str__(self):
        return self.name


class ImageModel(models.Model):
    image = models.ImageField(upload_to="media")
    matched_fish_url = models.URLField()
