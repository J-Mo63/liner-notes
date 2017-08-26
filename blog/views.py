from django.shortcuts import render
from django.http import Http404
from blog.models import Post

def home(request):
	try:
		post = Post.objects.last();
		last_post_id = post.get_previous_by_created_at().id
		next_post_id = 0
	except AttributeError:
		post = 0
		last_post_id = 0
		next_post_id = 0
	except Post.DoesNotExist:
		last_post_id = 0
		next_post_id = 0
	return render(request, 'blog/show.html', {
			'post': post,
			'last_post_id': last_post_id,
			'next_post_id': next_post_id,
		})

def show_post(request, id):
	try:
		post = Post.objects.get(id=id)
		try:
			last_post_id = post.get_previous_by_created_at().id
		except Post.DoesNotExist:
			last_post_id = 0
		try:
			next_post_id = post.get_next_by_created_at().id
		except Post.DoesNotExist:
			next_post_id = 0
	except Post.DoesNotExist:
		raise Http404('This post does not exist')
	return render(request, 'blog/show.html', {
			'post': post,
			'last_post_id': last_post_id,
			'next_post_id': next_post_id,
		})

def index_posts(request):
	posts = Post.objects.all()
	return render(request, 'blog/index.html', {
			'posts': posts,
		})