from django.db import models
from django.utils import timezone

# Create your models here.
class Tweet(models.Model):
    user = models.CharField(max_length=50)
    content = models.TextField()
    time = models.DateTimeField(default=timezone.now)
