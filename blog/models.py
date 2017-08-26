from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=200)
	artist = models.CharField(max_length=200)
	body = models.TextField()
	album_cover = models.URLField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)