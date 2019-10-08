from django.db import models


class Blog(models.Model):
    """Create a blog entry."""

    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    summary = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary_view(self):
        return self.summary[:100]

    def date_view(self):
        return self.date.strftime('%b %e %Y')
