from django.db import models
from datetime import datetime
# Create your models here.


class Photo(models.Model):
    image = models.TextField()
    caption = models.CharField(max_length=32)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    post_date = models.DateField(default=datetime.today)