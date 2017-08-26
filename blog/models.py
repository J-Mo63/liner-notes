from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return str(self.name)

class Post(models.Model):
	title = models.CharField(max_length=200)
	artist = models.CharField(max_length=200)
	genre = models.ForeignKey(Genre)
	release_date = models.DateField()
	reviewer = models.ForeignKey(User)
	body = models.TextField()
	album_cover = models.URLField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.title)
