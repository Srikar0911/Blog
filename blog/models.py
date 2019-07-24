from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    pen_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    rating = models.CharField(max_length=1)
    # published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        # self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title	

class Comment(models.Model):
    pen_name = models.CharField(max_length=200)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    key = models.IntegerField()

    def publish(self):
        # self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title   