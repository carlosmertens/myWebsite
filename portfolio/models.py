from django.db import models


class Portfolio(models.Model):
    """Create a portfolio entry."""

    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=350)
    gitHub = models.URLField(default='https://github.com/carlosmertens')

    def __str__(self):
        return self.description
