from django.db import models


class Portfolio(models.Model):
    # Create an image field
    image = models.ImageField(upload_to='images/')
    # Create the description field
    description = models.CharField(max_length=250)
