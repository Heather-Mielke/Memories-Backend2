from django.db import models

# Create your models here.


class Photo(models.Model):
    image = models.TextField()
    caption = models.CharField(max_length=32)
    description = models.TextField()
