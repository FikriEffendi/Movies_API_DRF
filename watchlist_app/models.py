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
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist',default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.rating) + " | " + self.watchlist.title
