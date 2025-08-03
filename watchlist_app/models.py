from django.db import models

class StreamPlatform(models.Model):
    name=models.CharField(max_length=100)
    about=models.CharField(max_length=150)
    website=models.URLField(max_length=100)
    
    def __str__(self):
        return self.name

class WatchList(models.Model):
    title = models.CharField(max_length=100)
    story_line = models.TextField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
