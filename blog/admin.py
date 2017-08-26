from django.contrib import admin
from django import forms
from .models import Post
from .models import Genre

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'artist']

class GenreAdmin(admin.ModelAdmin):
	list_display = ['name']

admin.site.register(Post, PostAdmin)
admin.site.register(Genre, GenreAdmin)