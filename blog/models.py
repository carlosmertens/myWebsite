from django.db import models


class Blog(models.Model):
    """Create a blog entry."""

    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    summary = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
