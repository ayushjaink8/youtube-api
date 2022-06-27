from django.db import models

class YoutubeData(models.Model):
    """ 
    This model is used to serve the purpose of fetching video results from youtube.com
    based on the searched query.
    Primary Key: video_id - unique id of the particular video.
    """
    video_id = models.CharField(null=False, blank=False, max_length=200, primary_key=True)
    video_title = models.CharField(null=True, blank=True, max_length=200)
    description = models.CharField(null=True, blank=True, max_length=5100)
    channel_id = models.CharField(null=False, blank=False, max_length=500)
    channel_title = models.CharField(null=True, blank=True, max_length=500)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    published_datetime = models.DateTimeField()
    thumbnail_url = models.URLField()